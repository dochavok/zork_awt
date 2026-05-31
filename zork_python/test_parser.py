"""Smoke tests for engine/parser.py."""

from engine.world import (
    World, Room, GameObject,
    TAKEBIT, CONTBIT, OPENBIT, ONBIT, ACTORBIT, TRANSBIT,
)
from engine.parser import (
    Parser, Vocabulary, SyntaxRule, ObjectSpec, ParseResult,
    LOC_HELD, LOC_CARRIED, LOC_ON_GROUND, LOC_IN_ROOM, LOC_HAVE,
    LOC_MANY, LOC_TAKE,
)


# ---------------------------------------------------------------------------
# Shared fixture helpers
# ---------------------------------------------------------------------------

def make_vocab() -> Vocabulary:
    v = Vocabulary()

    # Directions
    v.add_direction("north", "n")
    v.add_direction("south", "s")
    v.add_direction("east",  "e")
    v.add_direction("west",  "w")
    v.add_direction("up",    "u")
    v.add_direction("down",  "d")

    # Buzzwords
    v.add_buzz("a", "an", "the", "is", "and", "of", "some", "my")

    # Prepositions
    v.add_preposition("with",  "using", "through", "thru")
    v.add_preposition("in",    "inside", "into")
    v.add_preposition("on",    "onto")
    v.add_preposition("at")
    v.add_preposition("from")
    v.add_preposition("to")

    # Verbs (canonical + synonyms)
    v.add_verb("take",    "get", "grab", "pick", "carry")
    v.add_verb("drop",    "put", "leave")
    v.add_verb("examine", "x", "look", "l", "describe")
    v.add_verb("inventory", "i")
    v.add_verb("wait",    "z")
    v.add_verb("attack",  "kill", "hit", "fight")

    return v


def make_rules() -> list[SyntaxRule]:
    return [
        # inventory / wait  (no objects)
        SyntaxRule(verb="inventory", action="V-INVENTORY"),
        SyntaxRule(verb="wait",      action="V-WAIT"),

        # examine OBJECT
        SyntaxRule(
            verb="examine", action="V-EXAMINE",
            obj1=ObjectSpec(locations=frozenset({LOC_HAVE})),
        ),

        # take OBJECT (FIND TAKEBIT) (ON-GROUND IN-ROOM MANY)
        SyntaxRule(
            verb="take", action="V-TAKE", preaction="PRE-TAKE",
            obj1=ObjectSpec(
                find_flag=TAKEBIT,
                locations=frozenset({LOC_ON_GROUND, LOC_IN_ROOM, LOC_MANY}),
            ),
        ),

        # drop OBJECT (HELD)
        SyntaxRule(
            verb="drop", action="V-DROP", preaction="PRE-DROP",
            obj1=ObjectSpec(locations=frozenset({LOC_HELD, LOC_MANY})),
        ),

        # drop OBJECT in OBJECT  (put something in a container)
        SyntaxRule(
            verb="drop", action="V-PUT", preaction="PRE-PUT",
            obj1=ObjectSpec(locations=frozenset({LOC_HELD})),
            prep="in",
            obj2=ObjectSpec(locations=frozenset({LOC_HAVE})),
        ),

        # attack OBJECT (FIND ACTORBIT) with OBJECT
        SyntaxRule(
            verb="attack", action="V-ATTACK",
            obj1=ObjectSpec(
                find_flag=ACTORBIT,
                locations=frozenset({LOC_ON_GROUND, LOC_IN_ROOM}),
            ),
            prep="with",
            obj2=ObjectSpec(locations=frozenset({LOC_HELD})),
        ),

        # attack OBJECT (FIND ACTORBIT) — no weapon
        SyntaxRule(
            verb="attack", action="V-ATTACK",
            obj1=ObjectSpec(
                find_flag=ACTORBIT,
                locations=frozenset({LOC_ON_GROUND, LOC_IN_ROOM}),
            ),
        ),
    ]


def make_world() -> tuple[World, dict]:
    """
    Build a small test world:
      CELLAR (dark) contains: troll (actor), sword (weapon, takeable)
      LIVING-ROOM (lit) contains: lantern (lit, takeable), bottle (container)
      BOTTLE contains: water (takeable)
      PLAYER is in LIVING-ROOM, carrying: coin
    """
    w = World()

    cellar = Room("CELLAR", "Cellar")
    living = Room("LIVING-ROOM", "Living Room", flags={ONBIT})
    w.register_room(cellar)
    w.register_room(living)

    troll  = GameObject("TROLL",   synonyms=["troll"],   desc="nasty troll",
                        flags={ACTORBIT})
    sword  = GameObject("SWORD",   synonyms=["sword"],   desc="elvish sword",
                        adjectives=["elvish", "short"],  flags={TAKEBIT})
    lantern= GameObject("LANTERN", synonyms=["lantern", "lamp"],
                        adjectives=["brass", "old"],      desc="brass lantern",
                        flags={TAKEBIT, ONBIT})
    bottle = GameObject("BOTTLE",  synonyms=["bottle"],  desc="glass bottle",
                        adjectives=["glass"],
                        flags={CONTBIT, OPENBIT, TAKEBIT}, capacity=20)
    water  = GameObject("WATER",   synonyms=["water"],   desc="quantity of water",
                        flags={TAKEBIT}, size=4)
    coin   = GameObject("COIN",    synonyms=["coin"],    desc="gold coin",
                        adjectives=["gold"],              flags={TAKEBIT})

    player = GameObject("PLAYER",  synonyms=["me", "myself"], desc="yourself",
                        flags={CONTBIT, OPENBIT}, capacity=100)

    for obj in [troll, sword, lantern, bottle, coin, player, water]:
        w.register_object(obj)

    w.move_object(troll,   cellar)
    w.move_object(sword,   cellar)
    w.move_object(lantern, living)
    w.move_object(bottle,  living)
    w.move_object(water,   bottle)
    w.move_object(player,  living)
    w.move_object(coin,    player)

    w.player = player
    w.winner = player
    w.here   = living

    return w, {
        "troll": troll, "sword": sword, "lantern": lantern,
        "bottle": bottle, "water": water, "coin": coin, "player": player,
        "cellar": cellar, "living": living,
    }


def make_parser() -> Parser:
    return Parser(make_vocab(), make_rules())


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_empty_input(capsys=None):
    p = make_parser()
    w, _ = make_world()
    result = p.parse("", w)
    assert result is None
    print("PASS: empty input -> None")


def test_direction_bare():
    p = make_parser()
    w, _ = make_world()
    result = p.parse("north", w)
    assert result is not None
    assert result.action == "V-WALK"
    assert result.direction == "north"
    assert result.prso == []
    print("PASS: bare direction")


def test_direction_abbreviated():
    p = make_parser()
    w, _ = make_world()
    result = p.parse("n", w)
    assert result is not None
    assert result.direction == "north"
    print("PASS: abbreviated direction")


def test_direction_go_prefix():
    p = make_parser()
    w, _ = make_world()
    result = p.parse("go south", w)
    assert result is not None
    assert result.direction == "south"
    print("PASS: 'go <direction>' command")


def test_no_object_verb():
    p = make_parser()
    w, _ = make_world()
    result = p.parse("inventory", w)
    assert result is not None
    assert result.action == "V-INVENTORY"
    assert result.prso == []
    assert result.prsi == []
    print("PASS: no-object verb (inventory)")


def test_no_object_verb_synonym():
    p = make_parser()
    w, _ = make_world()
    result = p.parse("i", w)
    assert result is not None
    assert result.action == "V-INVENTORY"
    print("PASS: verb synonym ('i' -> inventory)")


def test_take_object():
    p = make_parser()
    w, objs = make_world()
    result = p.parse("take lantern", w)
    assert result is not None
    assert result.action == "V-TAKE"
    assert objs["lantern"] in result.prso
    print("PASS: take object by noun")


def test_take_object_with_article():
    p = make_parser()
    w, objs = make_world()
    result = p.parse("take the lantern", w)
    assert result is not None
    assert objs["lantern"] in result.prso
    print("PASS: take object with article (buzzword stripped)")


def test_take_object_with_adjective():
    p = make_parser()
    w, objs = make_world()
    result = p.parse("take brass lantern", w)
    assert result is not None
    assert objs["lantern"] in result.prso
    print("PASS: take object with adjective ('brass lantern')")


def test_take_not_in_room():
    p = make_parser()
    w, objs = make_world()
    # Troll is in CELLAR, we're in LIVING-ROOM; also troll lacks TAKEBIT
    result = p.parse("take troll", w)
    assert result is None  # error printed + _ParseError raised
    print("PASS: take object not in scope -> None")


def test_take_without_takebit():
    p = make_parser()
    w, objs = make_world()
    # bottle has TAKEBIT so it can be taken — remove it to test FIND filter
    objs["bottle"].flags.discard(TAKEBIT)
    result = p.parse("take bottle", w)
    # Bottle has no TAKEBIT, so it won't appear in scope for this rule
    assert result is None
    print("PASS: take object without TAKEBIT -> None")


def test_two_object_command():
    p = make_parser()
    w, objs = make_world()
    # Put coin (held) in bottle (in room)
    result = p.parse("drop coin in bottle", w)
    assert result is not None
    assert result.action == "V-PUT"
    assert objs["coin"] in result.prso
    assert objs["bottle"] in result.prsi
    print("PASS: two-object command with preposition")


def test_examine_object_in_container():
    p = make_parser()
    w, objs = make_world()
    # Water is inside the open bottle — should be accessible via LOC_HAVE
    result = p.parse("examine water", w)
    assert result is not None
    assert result.action == "V-EXAMINE"
    assert objs["water"] in result.prso
    print("PASS: examine object inside open container")


def test_examine_carried_object():
    p = make_parser()
    w, objs = make_world()
    result = p.parse("examine coin", w)
    assert result is not None
    assert objs["coin"] in result.prso
    print("PASS: examine carried object")


def test_take_all():
    p = make_parser()
    w, objs = make_world()
    result = p.parse("take all", w)
    assert result is not None
    assert result.action == "V-TAKE"
    # Should include lantern and bottle (both TAKEBIT, in room)
    assert objs["lantern"] in result.prso
    assert objs["bottle"]  in result.prso
    # Coin is already carried — also in scope
    print("PASS: 'take all' returns multiple objects")


def test_attack_with_weapon():
    p = make_parser()
    w, objs = make_world()
    # Move player to cellar; carry lantern (light) and sword (weapon)
    w.move_object(objs["lantern"], objs["player"])
    w.move_object(objs["sword"],   objs["player"])
    w.here = objs["cellar"]
    result = p.parse("attack troll with sword", w)
    assert result is not None
    assert result.action == "V-ATTACK"
    assert objs["troll"] in result.prso
    assert objs["sword"] in result.prsi
    print("PASS: two-object attack with weapon")


def test_again():
    p = make_parser()
    w, objs = make_world()
    r1 = p.parse("take lantern", w)
    assert r1 is not None
    # Simulate player taking the lantern
    w.move_object(objs["lantern"], objs["player"])
    # Move lantern back to room so AGAIN can take it
    w.move_object(objs["lantern"], w.here)
    r2 = p.parse("again", w)
    assert r2 is not None
    assert r2.action == "V-TAKE"
    assert objs["lantern"] in r2.prso
    print("PASS: AGAIN replays last command")


def test_again_shorthand_g():
    p = make_parser()
    w, objs = make_world()
    p.parse("take lantern", w)
    # Move lantern back
    w.move_object(objs["lantern"], objs["player"])
    w.move_object(objs["lantern"], w.here)
    result = p.parse("g", w)
    assert result is not None
    assert result.action == "V-TAKE"
    print("PASS: 'g' works as AGAIN shorthand")


def test_unknown_word():
    p = make_parser()
    w, _ = make_world()
    result = p.parse("frobnicate lamp", w)
    assert result is None  # unknown verb
    print("PASS: unknown verb -> None")


def test_words_stored_in_result():
    p = make_parser()
    w, _ = make_world()
    result = p.parse("take the brass lantern", w)
    assert result is not None
    assert result.words == ["take", "the", "brass", "lantern"]
    print("PASS: original words stored in ParseResult")


def test_preaction_stored():
    p = make_parser()
    w, _ = make_world()
    result = p.parse("take lantern", w)
    assert result is not None
    assert result.preaction == "PRE-TAKE"
    print("PASS: preaction stored in ParseResult")


# ---------------------------------------------------------------------------
# "all but / all except" tests
# Both variants of the vocabulary need covering:
#   (a) "all" and "but" are NOT buzzwords → existing _resolve_phrase "all" path
#   (b) "all" and "but" ARE buzzwords      → new _resolve_rule pre-strip path
# ---------------------------------------------------------------------------

def _make_buzz_vocab() -> Vocabulary:
    """Vocabulary where 'all', 'but', 'except', 'and' are buzzwords (real game)."""
    v = make_vocab()
    v.add_buzz("all", "but", "except", "every", "everything")
    return v


def test_drop_all_but_single():
    """'drop all but lantern' excludes the lantern from the dropped set."""
    p = Parser(_make_buzz_vocab(), make_rules())
    w, objs = make_world()
    # Give player the lantern and coin (both already in scope)
    w.move_object(objs["lantern"], objs["player"])

    result = p.parse("drop all but lantern", w)
    assert result is not None, "Should parse successfully"
    assert result.action == "V-DROP"
    assert objs["lantern"] not in result.prso, "Lantern must be excluded"
    assert objs["coin"] in result.prso, "Coin must be included"
    print("PASS: 'drop all but lantern' excludes lantern")


def test_drop_all_but_multiple():
    """'drop all but lantern and coin' excludes both named items."""
    p = Parser(_make_buzz_vocab(), make_rules())
    w, objs = make_world()
    w.move_object(objs["lantern"], objs["player"])
    w.move_object(objs["bottle"], objs["player"])

    result = p.parse("drop all but lantern and coin", w)
    assert result is not None
    assert objs["lantern"] not in result.prso, "Lantern must be excluded"
    assert objs["coin"]    not in result.prso, "Coin must be excluded"
    assert objs["bottle"]  in result.prso,     "Bottle must be included"
    print("PASS: 'drop all but lantern and coin' excludes both")


def test_drop_all_except():
    """'except' is an alias for 'but' in all-but phrases."""
    p = Parser(_make_buzz_vocab(), make_rules())
    w, objs = make_world()
    w.move_object(objs["lantern"], objs["player"])

    result = p.parse("drop all except lantern", w)
    assert result is not None
    assert objs["lantern"] not in result.prso, "Lantern must be excluded with 'except'"
    assert objs["coin"] in result.prso
    print("PASS: 'drop all except lantern' works as alias for 'but'")


def test_all_but_with_non_buzz_vocab():
    """When 'all' and 'but' are not buzzwords, all-but still works via _resolve_rule."""
    p = make_parser()   # default vocab: "all" and "but" NOT buzzwords
    w, objs = make_world()
    w.move_object(objs["lantern"], objs["player"])

    result = p.parse("drop all but lantern", w)
    assert result is not None
    assert objs["lantern"] not in result.prso, "Lantern must be excluded"
    assert objs["coin"] in result.prso
    print("PASS: all-but works when 'all'/'but' are not buzzwords")


def test_drop_all_still_works():
    """Plain 'drop all' (no exclusion) is unaffected by the all-but changes."""
    p = Parser(_make_buzz_vocab(), make_rules())
    w, objs = make_world()
    w.move_object(objs["lantern"], objs["player"])

    result = p.parse("drop all", w)
    assert result is not None
    assert objs["lantern"] in result.prso
    assert objs["coin"]    in result.prso
    print("PASS: plain 'drop all' still drops everything")


if __name__ == "__main__":
    test_empty_input()
    test_direction_bare()
    test_direction_abbreviated()
    test_direction_go_prefix()
    test_no_object_verb()
    test_no_object_verb_synonym()
    test_take_object()
    test_take_object_with_article()
    test_take_object_with_adjective()
    test_take_not_in_room()
    test_take_without_takebit()
    test_two_object_command()
    test_examine_object_in_container()
    test_examine_carried_object()
    test_take_all()
    test_attack_with_weapon()
    test_again()
    test_again_shorthand_g()
    test_unknown_word()
    test_words_stored_in_result()
    test_preaction_stored()
    test_drop_all_but_single()
    test_drop_all_but_multiple()
    test_drop_all_except()
    test_all_but_with_non_buzz_vocab()
    test_drop_all_still_works()
    print("\nAll tests passed.")
