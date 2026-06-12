"""
Natural language parser.

Mirrors the ZIL GPARSER module (gparser.zil) and GSYNTAX conventions.

Pipeline (matching ZIL SYNTAX-CHECK then SNARF-OBJECTS):
  1. tokenize
  2. AGAIN / empty-input short-circuit
  3. direction shortcut (bare direction or "go <dir>")
  4. find verb
  5. structural match: find a SyntaxRule whose particle + prep + noun-clause
     count fits the input  (no object resolution yet — mirrors SYNTAX-CHECK)
  6. object resolution for the winning rule (mirrors SNARF-OBJECTS / GET-OBJECT)
  7. return ParseResult

Content modules populate Vocabulary and supply SyntaxRule lists.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Callable, Optional

if TYPE_CHECKING:
    from engine.world import World, GameObject

# ---------------------------------------------------------------------------
# Location / search-scope constants
# Mirror ZIL bit constants (SH=128 SC=64 SOG=16 SIR=32 STAKE=8 SMANY=4)
# ---------------------------------------------------------------------------

LOC_HELD      = "HELD"       # directly in player's hands (first level only)
LOC_CARRIED   = "CARRIED"    # anywhere in player inventory (recursive)
LOC_ON_GROUND = "ON-GROUND"  # directly on room floor (not inside containers)
LOC_IN_ROOM   = "IN-ROOM"    # in room including contents of open containers
LOC_HAVE      = "HAVE"       # player inventory OR current room (most common)
LOC_MANY      = "MANY"       # "all" keyword allowed for multiple objects
LOC_TAKE      = "TAKE"       # auto-take if not already held


# ---------------------------------------------------------------------------
# ObjectSpec
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class ObjectSpec:
    """
    Constraints for one object slot (PRSO or PRSI) in a SyntaxRule.

    Mirrors ZIL SYNTAX OBJECT (FIND flag) (location-bits).

    find_flag -- if set, candidate must have this engine flag (e.g. TAKEBIT)
    locations -- frozenset of LOC_* constants controlling where to search
    """
    find_flag: Optional[str] = None
    locations: frozenset = field(default_factory=frozenset)

    @property
    def many_allowed(self) -> bool:
        return LOC_MANY in self.locations

    @property
    def auto_take(self) -> bool:
        return LOC_TAKE in self.locations


# ---------------------------------------------------------------------------
# SyntaxRule
# ---------------------------------------------------------------------------

@dataclass
class SyntaxRule:
    """
    One complete sentence pattern from gsyntax.zil, e.g.:

      TAKE OBJECT (FIND TAKEBIT) (ON-GROUND IN-ROOM MANY) = V-TAKE PRE-TAKE
      PUT  OBJECT (HELD MANY)    IN OBJECT                = V-PUT  PRE-PUT
      TURN ON OBJECT (FIND LIGHTBIT) (HELD IN-ROOM)       = V-LAMP-ON

    verb      -- canonical verb string (e.g. "take", "put", "turn")
    particle  -- optional post-verb word ("on", "off", "up", "down"…)
    action    -- handler name stored as PRSA (e.g. "V-TAKE")
    preaction -- pre-handler called first (e.g. "PRE-TAKE"), or None
    obj1      -- direct object (PRSO) spec, None if no direct object
    prep      -- canonical preposition between obj1 and obj2 ("with", "in"…)
    obj2      -- indirect object (PRSI) spec, None if no indirect object
    """
    verb: str
    action: str
    preaction: Optional[str] = None
    particle: Optional[str] = None
    obj1: Optional[ObjectSpec] = None
    prep: Optional[str] = None
    obj2: Optional[ObjectSpec] = None


# ---------------------------------------------------------------------------
# ParseResult
# ---------------------------------------------------------------------------

@dataclass
class ParseResult:
    """
    Output of a successful parse; equivalent to ZIL PRSA/PRSO/PRSI globals.

    action    -- verb handler name (PRSA)
    preaction -- optional pre-handler name
    prso      -- list of direct objects (usually 1, more with "all")
    prsi      -- list of indirect objects (usually 0 or 1)
    direction -- canonical direction string if this is a movement command
    syntax    -- the matched SyntaxRule (needed by game loop for flag checks)
    words     -- tokenized input (stored for AGAIN replay)
    """
    action: str
    preaction: Optional[str]
    prso: list   # list[GameObject]
    prsi: list   # list[GameObject]
    direction: Optional[str]
    syntax: Optional[SyntaxRule]
    words: list[str]


# ---------------------------------------------------------------------------
# Vocabulary
# ---------------------------------------------------------------------------

class Vocabulary:
    """
    Registry of all known words and their types / canonical forms.

    Content modules call the add_* methods during init.  The parser uses
    this to classify tokens (direction, buzzword, verb, preposition) without
    knowing anything about specific game objects.
    """

    def __init__(self) -> None:
        # word → canonical direction name ("n" → "north")
        self._directions: dict[str, str] = {}
        # words silently consumed during parsing
        self._buzzwords: set[str] = set()
        # word → canonical verb ("get" → "take")
        self._verbs: dict[str, str] = {}
        # word → canonical preposition ("using" → "with")
        self._preps: dict[str, str] = {}

    # ---- registration ------------------------------------------------------

    def add_direction(self, canonical: str, *aliases: str) -> None:
        self._directions[canonical.lower()] = canonical.lower()
        for a in aliases:
            self._directions[a.lower()] = canonical.lower()

    def add_buzz(self, *words: str) -> None:
        for w in words:
            self._buzzwords.add(w.lower())

    def add_verb(self, canonical: str, *aliases: str) -> None:
        """Register a verb and all its synonyms (all map to canonical)."""
        self._verbs[canonical.lower()] = canonical.lower()
        for a in aliases:
            self._verbs[a.lower()] = canonical.lower()

    def add_preposition(self, canonical: str, *aliases: str) -> None:
        self._preps[canonical.lower()] = canonical.lower()
        for a in aliases:
            self._preps[a.lower()] = canonical.lower()

    # ---- classification ----------------------------------------------------

    def canonical_direction(self, word: str) -> Optional[str]:
        return self._directions.get(word.lower())

    def is_buzz(self, word: str) -> bool:
        return word.lower() in self._buzzwords

    def canonical_verb(self, word: str) -> Optional[str]:
        return self._verbs.get(word.lower())

    def canonical_prep(self, word: str) -> Optional[str]:
        return self._preps.get(word.lower())

    def is_known(self, word: str) -> bool:
        w = word.lower()
        return (w in self._directions or w in self._buzzwords
                or w in self._verbs or w in self._preps)


# ---------------------------------------------------------------------------
# Internal sentinel for "error already printed, stop trying rules"
# ---------------------------------------------------------------------------

class _ParseError(Exception):
    """Raised internally when an error message was already shown to the player."""


# ---------------------------------------------------------------------------
# Parser
# ---------------------------------------------------------------------------

_PUNCT_RE = re.compile(r"[.,;:!?\"'`]+")

_WALK_VERBS = {"go", "walk", "run", "proceed", "step"}
_ALL_WORDS  = {"all", "everything", "every"}
_BUT_WORDS  = {"but", "except"}


class Parser:
    """
    The game's natural language parser.

    Constructed once with a Vocabulary and list of SyntaxRules (supplied by
    the content module).  Call parse() once per player turn.
    """

    def __init__(self, vocab: Vocabulary, rules: list[SyntaxRule]) -> None:
        self._vocab = vocab
        self._rules = rules

        # Index rules by canonical verb for fast lookup.
        self._by_verb: dict[str, list[SyntaxRule]] = {}
        for rule in rules:
            self._by_verb.setdefault(rule.verb, []).append(rule)

        # AGAIN buffer — stores words from last successful parse.
        self._again_words: list[str] = []

    # ------------------------------------------------------------------ #
    # Public API                                                           #
    # ------------------------------------------------------------------ #

    def parse(self, input_text: str, world: World) -> Optional[ParseResult]:
        """
        Parse one line of player input.

        Returns a ParseResult on success.  On failure, prints an error message
        and returns None.
        """
        words = self._tokenize(input_text)

        if not words:
            print("I beg your pardon?")
            return None

        # AGAIN / G: replay last successful command.
        if words[0] in ("again", "g"):
            if not self._again_words:
                print("You haven't done anything yet!")
                return None
            words = list(self._again_words)

        # Direction shortcut (bare direction or "go <dir>").
        direction = self._resolve_direction(words)
        if direction is not None:
            result = ParseResult(
                action="V-WALK",
                preaction=None,
                prso=[],
                prsi=[],
                direction=direction,
                syntax=None,
                words=words,
            )
            self._again_words = words
            return result

        # Find the first verb token.
        verb_pos, canonical_verb = self._find_verb(words)
        if canonical_verb is None:
            unknown = self._first_unknown(words)
            if unknown:
                print(f"I don't know the word \"{unknown}\".")
            else:
                print("There was no verb in that sentence!")
            return None

        # Tokens after the verb.
        rest = words[verb_pos + 1:]

        # Structural match then object resolution.
        try:
            result = self._match_and_resolve(canonical_verb, rest, world, words)
        except _ParseError:
            return None

        if result is not None:
            self._again_words = words
        return result

    # ------------------------------------------------------------------ #
    # Tokenization                                                         #
    # ------------------------------------------------------------------ #

    @staticmethod
    def _tokenize(text: str) -> list[str]:
        text = _PUNCT_RE.sub(" ", text.strip().lower())
        return [w for w in text.split() if w]

    # ------------------------------------------------------------------ #
    # Direction resolution                                                 #
    # ------------------------------------------------------------------ #

    def _resolve_direction(self, words: list[str]) -> Optional[str]:
        if not words:
            return None
        if len(words) == 1:
            return self._vocab.canonical_direction(words[0])
        # "go north", "walk south", etc.
        if words[0] in _WALK_VERBS and len(words) == 2:
            return self._vocab.canonical_direction(words[1])
        return None

    # ------------------------------------------------------------------ #
    # Verb identification                                                  #
    # ------------------------------------------------------------------ #

    def _find_verb(self, words: list[str]) -> tuple[int, Optional[str]]:
        for i, word in enumerate(words):
            canon = self._vocab.canonical_verb(word)
            if canon is not None:
                return i, canon
        return -1, None

    def _first_unknown(self, words: list[str]) -> Optional[str]:
        for w in words:
            if not (self._vocab.is_buzz(w) or self._vocab.is_known(w)):
                return w
        return None

    # ------------------------------------------------------------------ #
    # Structural match then object resolution (mirrors SYNTAX-CHECK +    #
    # SNARF-OBJECTS).  Three-phase pipeline:                             #
    #   1. Detect and consume verb particle ("turn ON", "blow UP")       #
    #   2. Split remainder into noun clauses around the first preposition #
    #   3. Pick the rule whose (particle, prep, nc-count) fits exactly   #
    #   4. Resolve objects for the winning rule                          #
    # ------------------------------------------------------------------ #

    def _match_and_resolve(
        self,
        verb: str,
        rest: list[str],
        world: World,
        original_words: list[str],
    ) -> Optional[ParseResult]:
        rules = self._by_verb.get(verb, [])
        if not rules:
            print(f"That's not something I know how to {verb}.")
            return None

        # Phase 1 — particle detection.
        particle, rest_after = self._detect_particle(rest, rules)
        particle_rules = [r for r in rules if r.particle == particle]
        if not particle_rules:
            print("That sentence isn't one I recognize.")
            return None

        # Phase 2 — split into noun clauses.
        # Parse the first preposition in rest_after to split nc1 / nc2.
        nc1_raw, prep, nc2_raw = self._extract_noun_clauses(rest_after)

        # Phase 3 — pick the best structurally-matching rule.
        rule = self._pick_rule(particle_rules, nc1_raw, prep, nc2_raw)
        if rule is None:
            print("That sentence isn't one I recognize.")
            return None

        # Phase 4 — object resolution.
        try:
            return self._resolve_rule(rule, nc1_raw, nc2_raw, world, original_words)
        except _ParseError:
            return None

    # ------------------------------------------------------------------ #
    # Phase 1: particle detection                                         #
    # ------------------------------------------------------------------ #

    def _detect_particle(
        self, rest: list[str], rules: list[SyntaxRule]
    ) -> tuple[Optional[str], list[str]]:
        """
        If the first token of `rest` is a particle in any candidate rule,
        consume it and return (particle, remaining).
        Also checks canonical preposition form so e.g. "inside" resolves
        to particle "in" in rules that use particle="in".
        """
        particles = {r.particle for r in rules if r.particle is not None}
        if rest:
            word = rest[0]
            if word in particles:
                return word, rest[1:]
            # Allow canonical preposition form to serve as a particle
            canon = self._vocab.canonical_prep(word)
            if canon is not None and canon in particles:
                return canon, rest[1:]
        return None, rest

    # ------------------------------------------------------------------ #
    # Phase 2: noun-clause extraction                                     #
    # ------------------------------------------------------------------ #

    def _extract_noun_clauses(
        self, tokens: list[str]
    ) -> tuple[list[str], Optional[str], list[str]]:
        """
        Split tokens into (nc1, canonical_prep, nc2) at the first preposition.

        Mirrors ZIL CLAUSE: the parser scans left-to-right for a preposition
        that divides the input into two noun clauses.  Buzzwords are NOT
        stripped here — that happens later when matching object names.
        """
        for i, token in enumerate(tokens):
            canon = self._vocab.canonical_prep(token)
            if canon is not None:
                return tokens[:i], canon, tokens[i + 1:]
        return tokens, None, []

    # ------------------------------------------------------------------ #
    # Phase 3: rule selection (mirrors SYNTAX-CHECK)                      #
    # ------------------------------------------------------------------ #

    def _pick_rule(
        self,
        rules: list[SyntaxRule],
        nc1_raw: list[str],
        prep: Optional[str],
        nc2_raw: list[str],
    ) -> Optional[SyntaxRule]:
        """
        Choose the first rule whose (prep, obj1-required, obj2-required)
        matches the parsed noun-clause structure.

        Mirrors ZIL SYNTAX-CHECK which selects based on P-NCN (noun-clause
        count) and preposition match — before any object resolution.
        """
        # Noun-clause presence after buzzword removal.
        nc1_words = [t for t in nc1_raw if not self._vocab.is_buzz(t)]
        nc2_words = [t for t in nc2_raw if not self._vocab.is_buzz(t)]
        has_nc1 = bool(nc1_words) or (nc1_raw and nc1_raw[0] in _ALL_WORDS)
        has_nc2 = bool(nc2_words)

        for rule in rules:
            needs_obj1 = rule.obj1 is not None
            needs_obj2 = rule.obj2 is not None
            rule_prep  = rule.prep

            # Rule needs obj1 but we have none (unless obj1 allows "all").
            if needs_obj1 and not has_nc1:
                if rule.obj1 and not rule.obj1.many_allowed:
                    continue

            # Rule has no prep/obj2 but input carries a prep+nc2 — too specific
            # for this rule, skip so a more specific rule can be tried first.
            if not needs_obj1 and not needs_obj2 and (has_nc1 or has_nc2):
                continue

            if not needs_obj2 and has_nc2 and rule_prep is None:
                # Input has a preposition+nc2 that this rule can't absorb.
                continue

            # Rule requires a preposition that doesn't match what was parsed.
            if rule_prep is not None and rule_prep != prep:
                continue

            # Rule requires obj2 but we have none.
            if needs_obj2 and not has_nc2:
                continue

            return rule   # first match wins

        return None

    # ------------------------------------------------------------------ #
    # Phase 4: object resolution (mirrors SNARF-OBJECTS)                 #
    # ------------------------------------------------------------------ #

    def _resolve_rule(
        self,
        rule: SyntaxRule,
        nc1_raw: list[str],
        nc2_raw: list[str],
        world: World,
        original_words: list[str],
    ) -> Optional[ParseResult]:
        """Resolve the actual game objects for a structurally-matched rule."""
        nc1_words = [t for t in nc1_raw if not self._vocab.is_buzz(t)]
        nc2_words = [t for t in nc2_raw if not self._vocab.is_buzz(t)]

        prso: list = []
        prsi: list = []

        if rule.obj1 is not None:
            # Check for "all [qualifier] but/except [items]" BEFORE buzzword
            # stripping, since "all", "but", and "except" are buzzwords in the
            # real game vocabulary and would otherwise be invisible here.
            all_but = (self._extract_all_but(nc1_raw)
                       if rule.obj1.many_allowed else None)
            if all_but is not None:
                qualifier, exclusion_groups = all_but
                prso = self._resolve_all_but(qualifier, exclusion_groups,
                                             rule.obj1, world)
            elif nc1_words or rule.obj1.many_allowed:
                prso = self._resolve_phrase(nc1_words, rule.obj1, world)

        if rule.obj2 is not None and nc2_words:
            prsi = self._resolve_phrase(nc2_words, rule.obj2, world)

        return ParseResult(
            action=rule.action,
            preaction=rule.preaction,
            prso=prso,
            prsi=prsi,
            direction=None,
            syntax=rule,
            words=original_words,
        )

    # ------------------------------------------------------------------ #
    # "all but / all except" helpers                                      #
    # ------------------------------------------------------------------ #

    def _extract_all_but(
        self, words: list[str]
    ) -> Optional[tuple[list[str], list[list[str]]]]:
        """
        Detect 'all [qualifier] but/except [items]' in raw (unstripped) words.

        Returns (qualifier_words, exclusion_groups) where qualifier_words are
        the buzzword-stripped tokens between 'all' and 'but' (e.g. ["treasure"]
        in "all treasure but sceptre"), and exclusion_groups is a list of
        word-lists split on 'and'/',' (one per excluded item noun phrase).

        Returns None when the pattern is absent.
        """
        all_idx: Optional[int] = None
        for i, w in enumerate(words):
            if w in _ALL_WORDS:
                all_idx = i
                break
        if all_idx is None:
            return None

        but_idx: Optional[int] = None
        for i in range(all_idx + 1, len(words)):
            if words[i] in _BUT_WORDS:
                but_idx = i
                break
        if but_idx is None:
            return None

        qualifier = [w for w in words[all_idx + 1 : but_idx]
                     if not self._vocab.is_buzz(w)]
        exclusion_groups = self._split_on_and(words[but_idx + 1 :])
        return qualifier, exclusion_groups

    def _split_on_and(self, words: list[str]) -> list[list[str]]:
        """Split raw words on 'and' / ',' into buzzword-stripped sub-lists."""
        groups: list[list[str]] = []
        current: list[str] = []
        for w in words:
            if w == "and" or w == ",":
                stripped = [x for x in current if not self._vocab.is_buzz(x)]
                if stripped:
                    groups.append(stripped)
                current = []
            else:
                current.append(w)
        if current:
            stripped = [x for x in current if not self._vocab.is_buzz(x)]
            if stripped:
                groups.append(stripped)
        return groups

    def _resolve_all_but(
        self,
        qualifier: list[str],
        exclusion_groups: list[list[str]],
        spec: ObjectSpec,
        world: "World",
    ) -> list:
        """Resolve 'all [qualifier] but [exclusions]' to a filtered object list."""
        candidates = self._scope_objects(spec, world)

        if qualifier:
            candidates = [o for o in candidates
                          if self._matches_phrase(o, qualifier)]

        excluded_ids: set[int] = set()
        for exc_words in exclusion_groups:
            if exc_words:
                for o in candidates:
                    if self._matches_phrase(o, exc_words):
                        excluded_ids.add(id(o))

        return [o for o in candidates if id(o) not in excluded_ids]

    # ------------------------------------------------------------------ #
    # Object resolution (mirrors GET-OBJECT / THIS-IT? / SEARCH-LIST)    #
    # ------------------------------------------------------------------ #

    def _resolve_phrase(
        self,
        words: list[str],
        spec: ObjectSpec,
        world: World,
    ) -> list:
        """
        Find game objects matching a noun phrase under the given ObjectSpec.

        Returns a list of matching GameObjects.
        Raises _ParseError (after printing) when nothing is found.

        Handles:
          "all"          → all accessible objects
          "all but lamp" → all except the named object
          "brass lantern"→ object whose synonyms include "lantern" and
                          adjectives include "brass"
        """
        # "ALL" / "EVERYTHING" → return everything in scope.
        # Also fires when words is empty and spec allows many (happens when
        # "all" was stripped as a buzzword — plain "drop all").
        # "all but X" is handled upstream in _resolve_rule before buzzword
        # stripping, so it never reaches here.
        if (not words and spec.many_allowed) or (words and words[0] in _ALL_WORDS):
            if not spec.many_allowed:
                pass  # fall through to normal single-object matching
            else:
                return self._scope_objects(spec, world)

        # Normal noun phrase.
        candidates = self._scope_objects(spec, world)
        matched = [o for o in candidates if self._matches_phrase(o, words)]

        if not matched:
            noun = words[-1] if words else "object"
            if world.is_lit():
                print(f"You can't see any {noun} here!")
            else:
                print("It's too dark to see!")
            raise _ParseError()

        if len(matched) > 1:
            noun = words[-1] if words else "object"
            options = ", ".join(f"the {o.desc}" for o in matched[:-1])
            options += f", or the {matched[-1].desc}"
            print(f"Which {noun} do you mean, {options}?")
            raise _ParseError()

        return matched

    # ------------------------------------------------------------------ #
    # Scope: which objects are candidates for a given ObjectSpec          #
    # ------------------------------------------------------------------ #

    def _scope_objects(self, spec: ObjectSpec, world: World) -> list:
        """
        Build the list of candidate objects based on spec.locations.

        Mirrors ZIL DO-SL (DO-Search-List) and SEARCH-LIST.
        """
        locs = spec.locations
        candidates: list = []
        seen: set = set()

        def add(obj) -> None:
            if id(obj) not in seen and not obj.has_flag("INVISIBLE"):
                seen.add(id(obj))
                candidates.append(obj)

        # Determine which search passes are needed.
        no_locs = not locs or locs.issubset({LOC_MANY, LOC_TAKE})

        search_inv_top  = no_locs or LOC_HELD     in locs or LOC_HAVE in locs
        search_inv_deep = no_locs or LOC_CARRIED  in locs or LOC_HAVE in locs
        search_room_top = no_locs or LOC_ON_GROUND in locs or LOC_HAVE in locs
        search_room_deep= no_locs or LOC_IN_ROOM  in locs or LOC_HAVE in locs

        # Player inventory.
        if world.player and (search_inv_top or search_inv_deep):
            for obj in world.player.contents:
                add(obj)
                if search_inv_deep:
                    self._collect_deep(obj, add)

        # Current room contents.
        if world.here and (search_room_top or search_room_deep):
            for obj in world.here.contents:
                if search_room_top:
                    add(obj)
                if search_room_deep:
                    self._collect_deep(obj, add)

        # Room global objects.
        for obj in world.global_objects_for():
            add(obj)

        # Apply find_flag filter.
        # RMUNGBIT is a ZIL parser special case meaning "any object in scope" — no filter.
        if spec.find_flag and spec.find_flag != "RMUNGBIT":
            candidates = [o for o in candidates if o.has_flag(spec.find_flag)]

        return candidates

    def _collect_deep(self, container, add_fn: Callable) -> None:
        """Recursively add objects from inside open/transparent/searchable containers."""
        if not container.has_flag("CONTBIT"):
            return
        # SEARCHBIT: ZIL parser searches inside even when closed (e.g. the jeweled egg)
        if not (container.has_flag("OPENBIT") or container.has_flag("TRANSBIT")
                or container.has_flag("SEARCHBIT")):
            return
        for obj in container.contents:
            add_fn(obj)
            self._collect_deep(obj, add_fn)

    # ------------------------------------------------------------------ #
    # Object ↔ noun-phrase matching (mirrors ZIL THIS-IT?)               #
    # ------------------------------------------------------------------ #

    def _matches_phrase(self, obj, words: list[str]) -> bool:
        """
        Return True if the object matches all words in the noun phrase.

        Rules (mirroring ZIL THIS-IT?):
          - The last word is the head noun; it must appear in obj.synonyms.
          - All preceding words are adjectives; each must appear in
            obj.adjectives (or also in obj.synonyms for flexible matching).
          - If there is only one word it is treated as both noun and adjective
            candidate (so "lantern" matches even if "lantern" is an adjective).
        """
        if not words:
            return True

        head = words[-1]
        adj_words = words[:-1]

        # Head noun must be in synonyms.
        if head not in obj.synonyms:
            # Allow head to be an adjective if it's the only word
            # (e.g. "take brass" when "brass" is an adjective on an object
            # whose only synonym is "lantern").  ZIL handles this via P-ADJ
            # fallback.
            if len(words) == 1 and head in obj.adjectives:
                return True
            return False

        # All adjective words must appear in obj.adjectives.
        for adj in adj_words:
            if adj not in obj.adjectives and adj not in obj.synonyms:
                return False

        return True
