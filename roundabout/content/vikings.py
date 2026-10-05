"""
Archery Range & Viking Encampment — Quest 57, The Viking Trust Trials.

Text is from AWT_story_line/locations.md (Archery Range & Viking Encampment)
and npcs.md (Raznak, Ivanaar, Haalvar, Unnamed Child, Aylora). The Pale Blade
forging scene is from ring-rituals.md (Artifact 1, Step 3).

State (story flags):
    RIDDLE-DONE      Trial 1 (Haalvar's riddle) complete
    CIRCLE-DONE      Trial 2 (Ritual Circle) complete
                     Trials 1 and 2 may be done in either order; Aylora
                     (Trial 3) won't start the contest until both are done.
    RITUAL-PROGRESS  stones lit so far in the Ritual Circle (0–5)
    AYLORA-OUT       Aylora lost the drinking contest
    AYLORA-DRAGGED   player is dragging Aylora back to the encampment
    VIKING-TRUST     runed metal handed over; arrow hazard disabled

Quest 42: GIVE STONES TO IVANAAR (all three rune stones) → Ivanaar's Tunic.
"""

from __future__ import annotations
import random
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_ENTER, M_END

if TYPE_CHECKING:
    from engine.world import World


def _first_two_done(w: World) -> bool:
    return bool(w.get_global("RIDDLE-DONE") and w.get_global("CIRCLE-DONE"))


def _arrived(w: World, msg: int, room: str) -> bool:
    """M_ENTER marks arrival; the following M_END (after the room is described) consumes it."""
    key = f"ARRIVED-{room}"
    if msg == M_ENTER:
        w.set_global(key, True)
        return False
    if msg == M_END and w.get_global(key):
        w.set_global(key, False)
        return True
    return False


# ---------------------------------------------------------------------------
# Archery Range — arrow hazard (Agility, Easy 5, no class bonus)
# ---------------------------------------------------------------------------

_ARROW_DODGE = "An arrow hisses past, close enough to hear the fletching."
_ARROW_HIT = (
    "An arrow from the far end of the range catches you. Someone shouts an "
    "apology in a language you don't speak."
)


def archery_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if _arrived(w, msg, "ARCHERY-RANGE") and not w.get_global("VIKING-TRUST"):
        from content.player import roll_class_bonus
        from content.perception import EASY
        if roll_class_bonus(w, "agility") >= EASY:
            print(_ARROW_DODGE)
        else:
            print(_ARROW_HIT)
            from content.combat import _take_damage
            _take_damage(w, 1)
    return M_NOT_HANDLED


# ---------------------------------------------------------------------------
# Viking Encampment — Ivanaar
# ---------------------------------------------------------------------------

_IVANAAR_STATES = {
    0: (
        '"You want something from us. They always want something. Prove '
        'yourself. Talk to Haalvar — north. If you can satisfy him, come back."'
    ),
    1: '"Haalvar speaks well of you. That\'s not nothing. The circle is south."',
    2: '"Two down. The fire pit is west. Don\'t embarrass yourself."',
}

_HANDOFF = (
    "Ivanaar looks at Aylora, then at you, then at Aylora again. He says "
    "nothing for a long moment.\n"
    '"...Thornbrew?" he finally asks.\n'
    "You nod. He laughs — once, short, like it surprised him too. Then he "
    "straightens, and the laugh is gone, and something older takes its place.\n"
    '"Will Passion sent you. He asked me to build something that would tell '
    "him whether you were worth trusting with what comes next. He didn't tell "
    'me what comes next."\n'
    "He moves to the longhouse and returns holding a length of dark metal — "
    "dense, rune-carved, warm to the touch even in the open air. He holds it "
    "with both hands.\n"
    '"This is Brotherhood metal. It has been kept since before this '
    "encampment. It would make a fine blade in the right hands — a blacksmith "
    'who knows what he is looking at could tell you more."\n'
    'He places it in your hands. "I hope Will is right about you."\n'
    '"One more thing. There are three stones out in the world — Brotherhood '
    "metal, rune-carved. They've been scattered a long time. If you come "
    'across them, bring them to me."\n'
    'He glances back once. "I\'ll make it worth your time."\n'
    "Ivanaar returns to his fire.\n"
    "[Runed Metal added to inventory.]"
)


def encampment_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if not _arrived(w, msg, "VIKING-ENCAMPMENT"):
        return M_NOT_HANDLED

    from content import quests
    if w.get_global("AYLORA-DRAGGED"):
        _runed_metal_handoff(w)
    elif not quests.is_discovered(w, "57"):
        # Quest 57 discovery: Ivanaar greets the player on first entry
        quests.discover(w, "57")
        print(_IVANAAR_STATES[0])
    return M_NOT_HANDLED


def _runed_metal_handoff(w: World) -> None:
    from content import quests
    w.set_global("AYLORA-DRAGGED", False)
    w.move_object(w.objects["AYLORA"], w.rooms["VIKING-ENCAMPMENT"])
    print(_HANDOFF)
    w.move_object(w.objects["RUNED-METAL"], w.player)
    w.set_global("VIKING-TRUST", True)   # arrow hazard silently disabled
    quests.complete(w, "57")
    quests.discover(w, "42")             # Ivanaar's "three stones" request

def talk_ivanaar(w: World) -> None:
    if w.get_global("VIKING-TRUST"):
        print("Ivanaar returns to his fire.")
    else:
        print(_IVANAAR_STATES[_ivanaar_state(w)])


def _ivanaar_state(w: World) -> int:
    """
    0: nothing done, or only the circle ("Talk to Haalvar — north").
    1: riddle done, circle not ("The circle is south").
    2: both done ("The fire pit is west").
    """
    if _first_two_done(w):
        return 2
    return 1 if w.get_global("RIDDLE-DONE") else 0


# ---------------------------------------------------------------------------
# Trial 1 — Haalvar's Hut, the Riddle Stone (answer: SEA)
# ---------------------------------------------------------------------------

_RIDDLE = (
    'Haalvar says: "I have no legs but travel far. I have no mouth but '
    "swallow ships. I have no hands but I will take everything you own if "
    'you let me. What am I?"'
)
_KEVRY_WHISPER = 'Kevry\'s voice, faint and amused, somewhere behind your ear: "Sea."'
_RIDDLE_SOLVED = (
    'The stone glows. Haalvar: "The stone is satisfied. I am also satisfied, '
    'which happens less often. '
)
_HAALVAR_TO_CIRCLE = 'Go south — there is a circle there that will want your attention next."'
_HAALVAR_TO_AYLORA = (
    "The circle has already had its look at you, I hear — so that leaves "
    'Aylora, at the fire pit. Try not to drown."'
)
_RIDDLE_WRONG = '"Impressive. Wrong, but impressive in its wrongness."'


def _riddle_open(w: World) -> bool:
    return not w.get_global("RIDDLE-DONE")


def _ask_riddle(w: World) -> None:
    print(_RIDDLE)
    if w.globals.get("actually_enchanted_glasses_worn"):
        print(_KEVRY_WHISPER)


def hut_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if _arrived(w, msg, "HAALVARS-HUT") and _riddle_open(w):
        _ask_riddle(w)
    return M_NOT_HANDLED


def talk_haalvar(w: World) -> None:
    if _riddle_open(w):
        _ask_riddle(w)
    else:
        print('"' + _haalvar_next(w))


def _haalvar_next(w: World) -> str:
    """Where Haalvar sends the player: the circle, or Aylora if it's done."""
    return _HAALVAR_TO_AYLORA if w.get_global("CIRCLE-DONE") else _HAALVAR_TO_CIRCLE


def riddle_input_hook(w: World, text: str) -> bool:
    """
    Free-text riddle answers in Haalvar's Hut: a bare word (SEA), or
    ANSWER <words> / SAY <words>. Directions and verbs pass through.
    """
    if w.here is None or w.here.name != "HAALVARS-HUT" or not _riddle_open(w):
        return False

    words = text.strip().lower().replace('"', " ").split()
    if not words:
        return False

    if words[0] in ("answer", "reply", "say") and len(words) > 1:
        answer = words[1:]
    elif len(words) == 1:
        vocab = w.game.parser._vocab
        if vocab.canonical_direction(words[0]) or vocab.canonical_verb(words[0]):
            return False
        answer = words
    else:
        return False

    if [a for a in answer if a not in ("the", "a")] == ["sea"]:
        print(_RIDDLE_SOLVED + _haalvar_next(w))
        w.set_global("RIDDLE-DONE", True)
    else:
        print(_RIDDLE_WRONG)
    return True


# ---------------------------------------------------------------------------
# Trial 2 — The Ritual Circle (Earth → Air → Fire → Water → Heart)
# ---------------------------------------------------------------------------

_STONE_ORDER = ["EARTH-STONE", "AIR-STONE", "FIRE-STONE", "WATER-STONE", "HEART-STONE"]
_CIRCLE_DONE = (
    "The fifth stone lights, and all five hum together for a moment. The "
    "child looks at you, then points back toward the encampment."
)


def activate_stone(w: World, stone) -> bool:
    """Returns True if `stone` is a Ritual Circle stone (handled)."""
    if stone.name not in _STONE_ORDER:
        return False

    if w.get_global("CIRCLE-DONE"):
        print("The stones are quiet. The trial is done.")
        return True

    progress = int(w.get_global("RITUAL-PROGRESS") or 0)
    if _STONE_ORDER[progress] != stone.name:
        print('"The child looks disappointed in you."')
        w.set_global("RITUAL-PROGRESS", 0)
        return True

    name = stone.name.split("-")[0].capitalize()
    print(f"The {name} stone hums and lights from within.")
    progress += 1
    w.set_global("RITUAL-PROGRESS", progress)
    if progress == len(_STONE_ORDER):
        print(_CIRCLE_DONE)
        w.set_global("CIRCLE-DONE", True)
    return True


# ---------------------------------------------------------------------------
# Trial 3 — The Fire Pit, Thornbrew drinking contest
# Best of five, contested: player strength roll vs Aylora 1d6 + 2; ties to
# Aylora; first to 3 wins. Resolves on one DRINK.
# ---------------------------------------------------------------------------

_AYLORA_OFFER = (
    "Aylora sets two cups on the bench and fills them from the barrel. "
    '"Thornbrew," she says. "Five cups. Last one standing." She pushes one '
    "toward you."
)
_ROUND_WON = "You drain the cup. Aylora matches you, but slower."
_ROUND_LOST = "Aylora drains hers without blinking. Yours fights back."
_CONTEST_WON = (
    "Aylora sets down her cup with great care, looks at it, and slides gently "
    "off the bench. Aylora passes out."
)
_AYLORA_SNORING = "Aylora is slumped on the bench, snoring."
_CONTEST_LOST_VIKING = (
    'A nearby Viking: "Ha! Aylora strikes again. Don\'t feel bad — she\'s been '
    'doing this since she could reach the cup."'
)
_DRAG = "You get her under the arms and start to drag."
# Aylora refuses until Trials 1 and 2 are done (approved 2026-10-03)
_AYLORA_NOT_YET = (
    "Aylora looks you over and doesn't reach for the barrel. \"Haalvar's "
    "stone and the circle first,\" she says. \"I don't waste Thornbrew on "
    "strangers.\""
)


def talk_aylora(w: World) -> None:
    if w.get_global("AYLORA-OUT"):
        print(_AYLORA_SNORING)
    elif not _first_two_done(w):
        print(_AYLORA_NOT_YET)
    else:
        print(_AYLORA_OFFER)


def drink_contest(w: World) -> bool:
    """DRINK at the Fire Pit. Returns True if handled."""
    if w.here is None or w.here.name != "FIRE-PIT":
        return False
    if w.get_global("AYLORA-OUT"):
        print(_AYLORA_SNORING)
        return True
    if not _first_two_done(w):
        print(_AYLORA_NOT_YET)
        return True

    from content.player import roll_class_bonus
    mine = hers = 0
    while mine < 3 and hers < 3:
        if roll_class_bonus(w, "strength") > random.randint(1, 6) + 2:
            mine += 1
            print(_ROUND_WON)
        else:
            hers += 1
            print(_ROUND_LOST)

    if mine == 3:
        print(_CONTEST_WON)
        from content.combat import award_combat_xp
        award_combat_xp(w, "aylora", kill=False)   # 2 XP; she passes out — not a kill
        w.set_global("AYLORA-OUT", True)
        aylora = w.objects["AYLORA"]
        aylora.fdesc = aylora.ldesc = _AYLORA_SNORING
    else:
        # Player passes out; wakes in the encampment two turns later
        print("You pass out.")
        w.game.clock.tick(w, command_parsed=True)
        w.game.clock.tick(w, command_parsed=True)
        w.game.enter_room(w.rooms["VIKING-ENCAMPMENT"])
        print(_CONTEST_LOST_VIKING)
    return True


def take_aylora(w: World) -> None:
    if not w.get_global("AYLORA-OUT") or w.get_global("VIKING-TRUST"):
        print("You can't take Aylora.")
        return
    print(_DRAG)
    w.set_global("AYLORA-DRAGGED", True)


# ---------------------------------------------------------------------------
# Raznak — State 1 only so far (trust states are Quest 55, full-score path)
# ---------------------------------------------------------------------------

_RAZNAK_NOT_READY = (
    "Raznak eyes you the way he'd eye an arrow with a bad fletching — not "
    "hostile, just certain you're not ready.\n"
    '"You want something from me, go talk to the encampment first. West '
    'of here. When they know you, come back."\n'
    "He turns away. The conversation is over."
)
_RAZNAK_ROGUE = (
    "Raznak watches you cross the range. He doesn't say anything for a moment. "
    "His eyes go to your hands. Then your stance. Then back to your hands.\n"
    '"You\'ve done this before."\n'
    "It isn't a question. He disappears into the longhouse and returns with a "
    "bow — plain, well-maintained, strung and ready.\n"
    '"Don\'t embarrass it," he says, and hands it over.\n'
    "[Bow added to inventory.]"
)
_RAZNAK_OFFER = (
    "Raznak looks at you differently now — not warm exactly, but the suspicion "
    'is gone. "You want to learn the bow," he says. It isn\'t a question either. '
    '"Three Zenni. We start now if you have it."'
)
_RAZNAK_SHORT = '"Come back when you do."'
_RAZNAK_TRAINED = (
    "Raznak watches you complete the final drill. He is quiet for a moment in "
    "the way of someone making a decision they've already made.\n"
    '"You\'re not a natural," he says. "You worked for it. That\'s better."\n'
    "He takes a bow from the rack — slightly better than the practice ones, "
    "strung tight, balanced.\n"
    '"This one\'s yours. It\'ll tell you when you\'re doing it wrong."\n'
    "He pauses.\n"
    '"Most bows don\'t. This one does. Pay attention to it."\n'
    "[Bow added to inventory.]"
)
TRAINING_COST = 3


def _raznak_greeting(w: World) -> str:
    name = w.globals.get("player_name", "")
    return (f'Raznak looks up when you enter the range. "{name}," he says, with a '
            "nod. He goes back to his work. That's the entire greeting, and "
            "somehow it's enough.")


def talk_raznak(w: World) -> None:
    from content import quests
    if not w.get_global("VIKING-TRUST"):
        print(_RAZNAK_NOT_READY)
        return
    if w.globals.get("skill_bow"):
        if w.globals.get("player_class") == "rogue" and not w.get_global("RAZNAK-BOW-GIVEN"):
            print(_RAZNAK_ROGUE)          # State 2A — no training, no Zenni
            w.set_global("RAZNAK-BOW-GIVEN", True)
            w.move_object(w.objects["BOW"], w.player)
        else:
            print(_raznak_greeting(w))    # State 3 — later visits
        return
    print(_RAZNAK_OFFER)                   # State 2B — Warrior or Mage
    quests.discover(w, "55")


def pay_raznak(w: World) -> None:
    """PAY RAZNAK / GIVE RAZNAK THREE ZENNI — archery training (Quest 55)."""
    from content import quests
    if not w.get_global("VIKING-TRUST"):
        print(_RAZNAK_NOT_READY)
        return
    if w.globals.get("skill_bow"):
        talk_raznak(w)
        return
    zenni = w.globals.get("zenni", 0)
    if zenni < TRAINING_COST:
        print(_RAZNAK_SHORT)
        return
    w.globals["zenni"] = zenni - TRAINING_COST
    w.globals["skill_bow"] = True
    w.set_global("RAZNAK-BOW-GIVEN", True)
    print(_RAZNAK_TRAINED)
    w.move_object(w.objects["BOW"], w.player)
    quests.discover(w, "55")
    quests.complete(w, "55")


def give_zenni_input_hook(w: World, text: str) -> bool:
    """GIVE RAZNAK THREE ZENNI / GIVE 3 ZENNI TO RAZNAK — Zenni isn't an object."""
    words = [x for x in text.lower().split() if x != "the"]
    if not words or words[0] not in ("give", "hand", "pay") or "zenni" not in words:
        return False
    if "raznak" not in words:
        return False
    raznak = w.objects.get("RAZNAK")
    if raznak is None or raznak.location is not w.here:
        return False
    pay_raznak(w)
    return True


# ---------------------------------------------------------------------------
# Pale Blade — Pyronicus forges the runed metal (ring-rituals.md, Artifact 1)
# ---------------------------------------------------------------------------

_FORGING = (
    "Pyronicus turns the metal over in his hands without speaking. He runs a "
    "thumb along the runes. Then he sets it on the forge.\n"
    '"Brotherhood metal," he says. "I haven\'t seen this in some time." He '
    'picks up his hammer. "You know what it\'s for."\n'
    "He doesn't phrase it as a question.\n"
    "The forge does the rest quickly — the metal accepts the heat the way it "
    "has been waiting to, and Pyronicus works it with the focused economy of "
    "someone who has done this before and expects to do it again. When he's "
    "done, he holds it up. The blade is pale, almost white, and thin in the "
    "way of something that doesn't need to be heavy to do what it does.\n"
    "He holds it out, pommel first.\n"
    '"It will go willingly," he says. "When the time comes."\n'
    "He goes back to his work.\n"
    "[Runed Metal removed from inventory. The Pale Blade added to inventory.]"
)


def forge_pale_blade(w: World) -> None:
    w.move_object(w.objects["RUNED-METAL"], None)   # consumed by the forge
    print(_FORGING)
    w.move_object(w.objects["PALE-BLADE"], w.player)
    w.set_global("PALE-BLADE-FORGED", True)


# ---------------------------------------------------------------------------
# Quest 42 — The Brotherhood Stones (locations.md — Viking Encampment, Stone return)
# ---------------------------------------------------------------------------

RUNE_STONES = ("OLD-OAK-RUNE-STONE", "BOG-RUNE-STONE", "DUNGEON-RUNE-STONE")

_NOT_ALL_STONES = (
    "Ivanaar turns the stone over once and hands it back. \"Three,\" he says, and "
    "returns to his fire."
)


def _stones_returned(w: World) -> str:
    name = w.globals.get("player_name", "")
    return (
        "Ivanaar turns the stones over in his hands, one by one. He doesn't speak for "
        "a long moment.\n"
        "When he looks up, something has settled in his expression that wasn't there "
        "before.\n"
        f"\"{name}.\"\n"
        "He says it the way you'd say the name of someone you've decided to trust. He "
        "sets the stones down and disappears into the longhouse.\n"
        "He returns with a folded tunic — Brotherhood weave, the runes along the hem "
        "faintly lit now.\n"
        "\"Wear it,\" he says, and hands it over.\n"
        "He returns to his fire.\n"
        "[Ivanaar's Tunic added to inventory.]"
    )


def give_stones(w: World) -> None:
    """GIVE STONE(S) TO IVANAAR — all three, or he hands it back."""
    from content import quests
    stones = [w.objects[n] for n in RUNE_STONES]
    if not all(s in w.player.contents for s in stones):
        print(_NOT_ALL_STONES)
        return
    for s in stones:
        w.move_object(s, None)
    print(_stones_returned(w))
    w.move_object(w.objects["IVANAAR-TUNIC"], w.player)
    quests.complete(w, "42")     # 5 Zenni, paid silently
