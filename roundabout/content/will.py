"""
Will Passion — spell teaching and the glasses fail state.

Design sources:
  mechanics.md — Warrior/Rogue scroll resistance; Spell training (Quest 56):
                 3 Zenni per spell, Warriors and Rogues only
  npcs.md      — Will Passion: Spell teaching / Teaching dialogue
  items.md     — Enchanted Glasses: wearing them in Will's presence is an
                 instant fail state (Will attacks, no recovery)
"""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.world import World


# Spell scroll object name -> spell flag (player stat)
SPELL_SCROLLS = {
    "SCROLL-UNBIND-UNDEAD": "spell_unbind_undead",
    "SCROLL-LIGHT": "spell_light",
    "FIREBALL-SCROLL": "spell_fireball",
}

TEACHING_COST = 3

_RESISTANCE = (
    "The words are legible. The meaning is not. Whatever is written here was "
    "meant for someone with a different kind of mind — or a different kind of "
    "training. Will Passion, in his tower, has been known to translate this "
    "sort of thing for people like you."
)

_TEACHING = (
    "Will glances at the scroll, then at you. He takes it without ceremony "
    "and unrolls it, reading silently for a moment. Then he reads it aloud — "
    "not to you, exactly, more as if the words need to be heard in the right "
    "kind of room. When he finishes, you understand it. You're not sure how. "
    '"Keep that," he says, nodding at the space where the scroll was. It\'s '
    'gone. "The knowing, I mean."'
)

_MAGE_READS = (
    "You read the scroll through once, and the words settle into you as if "
    "they had always meant to. The scroll crumbles to dust in your hands."
)

_CANT_PAY = (
    '"Three Zenni," Will says, without looking up. "I don\'t make the rules. '
    'Well. I do. Come back when you have it."'
)

_GLASSES_FAIL = (
    "Will looks up from his desk. His eyes go to the glasses on your face and "
    "stay there. For a moment nothing in the room moves. Then he is out of his "
    "chair, and whatever happens next, you don't see it coming.\n\n"
    "*** GAME OVER ***"
)

# mechanics.md — Shovel & Dig Mechanic: 1-in-20 after any successful DIG
DIG_NOTE = (
    "Will Passion materializes in your thoughts, uninvited. \"Do you know how "
    "long it takes to dig a six-foot hole?\" You suspect he does. You suspect he "
    "has timed it."
)


def _will_present(w: World) -> bool:
    will = w.objects.get("WILL")
    return will is not None and w.here is not None and will.location is w.here


def read_scroll(w: World, scroll) -> bool:
    """READ <spell scroll>. Returns True if `scroll` is a spell scroll."""
    if scroll.name not in SPELL_SCROLLS:
        return False
    if w.globals.get("player_class") == "mage":
        print(_MAGE_READS)
        _learn(w, scroll)
    elif _will_present(w):
        teach(w, scroll)
    else:
        print(_RESISTANCE)   # scroll not consumed
    return True


def teach(w: World, scroll) -> None:
    """Will teaches a spell scroll (READ SCROLL in his presence, or GIVE SCROLL TO WILL)."""
    zenni = w.globals.get("zenni", 0)
    if zenni < TEACHING_COST:
        print(_CANT_PAY)
        return
    w.globals["zenni"] = zenni - TEACHING_COST
    print(_TEACHING)
    _learn(w, scroll)
    from content.experience import award_xp
    award_xp(w, 4)   # Quest 56 — Will's Teaching: 4 XP per spell (experience.md)


def _learn(w: World, scroll) -> None:
    w.globals[SPELL_SCROLLS[scroll.name]] = True
    w.move_object(scroll, None)   # consumed


def glasses_seen(w: World) -> bool:
    """
    Fail state: the glasses are being worn where Will can see them. Checked at
    the end of every turn in the tower (arriving wearing them, or putting them
    on there). Returns True if the game ended.
    """
    from engine.world import WEARBIT
    glasses = w.objects.get("ENCHANTED-GLASSES")
    if glasses is None or not glasses.has_flag(WEARBIT) or not _will_present(w):
        return False
    print(_GLASSES_FAIL)
    w.set_global("GAME-OVER", True)
    w.game.quit()
    return True
