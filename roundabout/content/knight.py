"""
The Redcrosse Knight, Town Square — Quest 54, Fight the Knight.

Design: npcs.md (The Redcrosse Knight), quests.md (Quest 54), mechanics.md
(Skill Progression; Combat).

- Mages and Rogues only: Warriors already have melee (skill_melee) and are
  waved off. Level 3 minimum to fight; at 1 heart he won't start.
- FIGHT / CHALLENGE / KILL KNIGHT starts the trial (he draws); each further
  attack is one round. He rolls 2d8 and has 4 hearts. Hearts the player loses
  are real. The trial ends when either side is down to 1 heart; if he gets
  there he yields, even on a tie that drops the player there too.
- Leaving the square mid-trial abandons it; the next one starts fresh.
- Won: PAY KNIGHT (3 Zenni) teaches melee and completes Quest 54 (8 XP, no
  Zenni — the skill is the reward).

State: KNIGHT-FOUGHT, KNIGHT-FIGHTING, KNIGHT-HEARTS, KNIGHT-WON, skill_melee
"""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.world import World

KNIGHT_HEARTS = 4
KNIGHT_DICE = (2, 8)
MIN_LEVEL = 3
TRAINING_COST = 3

PRESENCE = ("The Redcrosse Knight, Knight of Faith, stands at ease near the fountain, "
            "watching the town go about its business.")
EXAMINE = ("A tall man in plain, well-kept armour, a red cross faded on the breast. He "
           "wears his sword like a tool he respects. His eyes are calm, and they miss "
           "very little.")

_FIRST = (
    "The Knight stands at ease in the square, watching the town go about its business. "
    "When he notices you, he turns fully to face you — unhurried, attentive. \"You're "
    "looking at me like someone who wants to learn something,\" he says. \"I teach one "
    "thing. Come find me when you're ready to show me what you already know.\""
)
_WARRIOR = (
    "The Knight turns to face you, unhurried, and takes in the way you stand before "
    "anything else. \"You already know what I teach,\" he says. \"You've nothing to prove "
    "to me. Go and use it.\""
)
_WARRIOR_FIGHT = "He doesn't reach for his sword. \"You don't need me for that,\" he says."
_TOO_LOW = "He looks you over once. \"Not yet,\" he says, not unkindly. \"Come back when you've got more behind you.\""
_ONE_HEART = "He looks you over. \"Not like that. Rest first, then come back.\""
_DRAWS = "He draws his weapon."
_ROUND_WON = "You get inside his guard and land a clean blow. He gives ground, nodding."
_ROUND_LOST = "He turns your strike aside and catches you with the flat of his blade."
_ROUND_TIE = "You trade blows, and both of you land one."
_LOST = (
    "He steps back and lowers his weapon. \"You fought well enough to keep your feet. "
    "That's not nothing.\" He studies you for a moment. \"Come back. I'll be here.\""
)
_NOT_THAT = "\"Not that,\" he says. \"Steel. That's what I teach.\""
_SHORT = "\"Three Zenni,\" he says. \"Come back when you have it.\""
_TRAINED = (
    "He walks you through it twice, slowly, then once at speed: your footing, your "
    "guard, where your weight goes when you swing. By the end your arms ache, and "
    "something has settled into them that wasn't there before."
)
_SHAMUS = "\"Shamus, at the inn, keeps weapons in the back. Tell him I sent you.\""


def _name(w: World) -> str:
    return w.globals.get("player_name", "") or "Adventurer"


def _start_line(w: World) -> str:
    return (f"\"I'm {_name(w)}, and I'm ready.\"\n\nHe looks at you. Something in his "
            f"posture shifts — just slightly. \"Then let's see what you know.\" He draws "
            f"his weapon.")


def _won_line(w: World) -> str:
    return (f"He holds still for a moment after you land the deciding blow. Then "
            f"something in his posture shifts — subtle, but real. \"Good, {_name(w)},\" he "
            f"says. Just that. He sheathes his weapon and nods toward an open space in "
            f"the square. \"Again — this time I'll show you what you did right.\"")


def fighting(w: World) -> bool:
    knight = w.objects.get("KNIGHT")
    return bool(w.get_global("KNIGHT-FIGHTING")) and knight is not None \
        and knight.location is w.here


def talk(w: World) -> None:
    from content import quests
    from content.experience import get_level
    if w.globals.get("player_class") == "warrior":
        print(_WARRIOR)
    elif w.globals.get("skill_melee"):
        print(f"\"{_name(w)}.\" He nods, once. \"Keep your guard up.\"")
    elif w.get_global("KNIGHT-WON"):
        print(f"\"Three Zenni, {_name(w)}, and I'll show you what you did right.\"")
    elif w.get_global("KNIGHT-FOUGHT"):
        print(f"\"{_name(w)},\" he says. \"Ready to try again?\"")
    else:
        print(_FIRST)
        if get_level(w) >= MIN_LEVEL:
            quests.discover(w, "54")


def attack(w: World) -> None:
    """FIGHT / CHALLENGE / KILL KNIGHT — start the trial, or one round of it."""
    from content.experience import get_level
    from content import quests
    if fighting(w):
        _round(w)
        return
    if w.globals.get("player_class") == "warrior":
        print(_WARRIOR_FIGHT)
        return
    if w.globals.get("skill_melee"):
        print(f"\"We're done with that, {_name(w)},\" he says.")
        return
    if w.get_global("KNIGHT-WON"):
        talk(w)
        return
    if get_level(w) < MIN_LEVEL:
        print(_TOO_LOW)
        return
    if w.globals.get("hearts", 1) <= 1:
        print(_ONE_HEART)
        return
    quests.discover(w, "54")
    print(_DRAWS if w.get_global("KNIGHT-FOUGHT") else _start_line(w))
    w.set_global("KNIGHT-FOUGHT", True)
    w.set_global("KNIGHT-FIGHTING", True)
    w.globals["KNIGHT-HEARTS"] = KNIGHT_HEARTS


def _round(w: World) -> None:
    """One round (content/combat.py)."""
    from content import combat
    hearts = int(w.globals.get("KNIGHT-HEARTS", KNIGHT_HEARTS))
    hearts -= combat.fight_round(w, KNIGHT_DICE, _ROUND_WON, _ROUND_LOST, _ROUND_TIE,
                                 finishing=False)          # a trial, not a kill
    w.globals["KNIGHT-HEARTS"] = hearts
    if hearts <= 1:
        w.set_global("KNIGHT-FIGHTING", False)
        w.set_global("KNIGHT-WON", True)
        print(_won_line(w))
    elif w.globals.get("hearts", 1) <= 1:
        w.set_global("KNIGHT-FIGHTING", False)
        print(_LOST)


def not_that(w: World) -> bool:
    """CAST FIREBALL during the trial. True if handled."""
    if not fighting(w):
        return False
    print(_NOT_THAT)
    return True


def pay(w: World) -> None:
    """PAY KNIGHT / GIVE KNIGHT THREE ZENNI — melee training (Quest 54)."""
    from content import quests
    if not w.get_global("KNIGHT-WON") or w.globals.get("skill_melee") \
            or w.globals.get("player_class") == "warrior":
        talk(w)
        return
    zenni = w.globals.get("zenni", 0)
    if zenni < TRAINING_COST:
        print(_SHORT)
        return
    w.globals["zenni"] = zenni - TRAINING_COST
    w.globals["skill_melee"] = True
    print(_TRAINED)
    print(_SHAMUS)
    quests.complete(w, "54")     # 8 XP, no Zenni


def give_zenni_input_hook(w: World, text: str) -> bool:
    """GIVE KNIGHT THREE ZENNI / GIVE 3 ZENNI TO KNIGHT — Zenni isn't an object."""
    words = [x for x in text.lower().split() if x != "the"]
    if not words or words[0] not in ("give", "hand", "pay") or "zenni" not in words:
        return False
    if "knight" not in words and "redcrosse" not in words:
        return False
    knight = w.objects.get("KNIGHT")
    if knight is None or knight.location is not w.here:
        return False
    from content import ink
    if not ink.refuse(w, "KNIGHT"):
        pay(w)
    return True


BOW_REFUSED = (
    "He steps inside your draw and pushes the bow aside with the flat of his "
    'blade. "Steel," he says. "That\'s what you came to learn."'
)


def shoot_input_hook(w: World, text: str):
    """SHOOT KNIGHT / KILL KNIGHT WITH BOW, bow in hand: he won't have it — no
    turn used (npcs.md)."""
    words = text.lower().split()
    if not words or not ({"knight", "redcrosse"} & set(words)):
        return False
    shot = words[0] == "shoot" or ("with" in words and "bow" in words)
    knight = w.objects.get("KNIGHT")
    if not shot or knight is None or knight.location is not w.here \
            or w.objects["BOW"] not in w.player.contents:
        return False
    from content import ink
    if ink.refuse(w, "KNIGHT"):
        return True                      # inked: a refusal, and a turn like any other
    from engine.game import HOOK_NO_TURN
    print(BOW_REFUSED)
    return HOOK_NO_TURN


def on_enter(w: World, room) -> None:
    """Enter hook: leaving the square abandons a trial in progress."""
    if room.name != "TOWN-SQUARE":
        w.set_global("KNIGHT-FIGHTING", False)
