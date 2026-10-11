"""
CURSE, and Will's fine for cursing in his tower — the Notorious penalty.

Design: mechanics.md (Cursing and Notorious), npcs.md (Will Passion — Cursing
in his presence).

- CURSE anywhere else: the guild-hall line; at a person or a thing, its own line.
- CURSE with Will in the room and Zenni in the purse: Will fines half of it,
  rounded up — [pay/refuse]. Refusing gets one last chance ("Are you SURE…?"):
  yes makes the player Notorious, anything else pays after all.
- With an empty purse there's nothing to fine: Will writes in his ledger.
- Notorious is permanent. Side quests still play out, but pay no XP and no
  Zenni (content/quests.py complete(); Will's Teaching XP in content/will.py).
  The One Ring path isn't a quest in that table, so it's never touched.

State: NOTORIOUS
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.world import ACTORBIT

if TYPE_CHECKING:
    from engine.world import World

_CURSE = (
    "Such language in a high-class establishment like this! Why, you're lucky "
    "that you weren't within 10 feet of the guild hall. You know what happens then!"
)
_CURSE_PERSON = "Insults of this nature won't help you."
_CURSE_THING = "What a loony!"

_FINE = (
    "Will sets down his pen. Very slowly, he removes his spectacles. \"In my "
    "tower,\" he says. It isn't a question. \"There is a fine for that. Half of "
    "what you carry — {n} Zenni. Or I make sure every guild in Roundabout knows "
    "your name, and not fondly.\""
)
FINE_PROMPT = "[pay/refuse] "
SURE_PROMPT = "\"Are you SURE you want to do that?\" (yes/no) "
_PAID = (
    "Will holds out a hand until the coins are in it. \"Thank you.\" He replaces "
    "his spectacles and picks up his pen. It is as though nothing happened, "
    "except that you are poorer."
)
_NOTORIOUS = (
    "\"As you wish.\" Will doesn't raise his voice. He doesn't need to. \"You "
    "are Notorious. Go on, then. See who still wants your help.\""
)
_LEDGER = (
    "Will sets down his pen. Very slowly, he removes his spectacles. \"In my "
    "tower,\" he says. His eyes go to your empty purse and stay there a moment. "
    "\"Nothing to fine. How convenient for you.\" He opens a small black ledger, "
    "writes one line in it, and closes it again. He doesn't explain."
)


# SCORE and READ JOURNAL show this while Notorious
STANDING = "You are Notorious. Quests pay you nothing."


def is_notorious(w: World) -> bool:
    return bool(w.get_global("NOTORIOUS"))


def curse(w: World) -> None:
    from content.will import _will_present
    if _will_present(w):
        _fine(w)
    elif w.prso is None:
        print(_CURSE)
    elif w.prso.has_flag(ACTORBIT):
        print(_CURSE_PERSON)
    else:
        print(_CURSE_THING)


def _ask(prompt: str) -> str | None:
    """One answer, lowercased; None if input is closed."""
    try:
        return input(prompt).strip().lower()
    except (EOFError, KeyboardInterrupt):
        print()
        return None


def _fine(w: World) -> None:
    zenni = w.globals.get("zenni", 0)
    if zenni <= 0:
        print(_LEDGER)
        return
    fine = (zenni + 1) // 2
    print(_FINE.format(n=fine))
    answer = _ask(FINE_PROMPT)
    while answer not in (None, "pay", "p", "refuse", "r"):
        answer = _ask(FINE_PROMPT)
    if answer in ("refuse", "r") and _ask(SURE_PROMPT) in ("yes", "y"):
        w.set_global("NOTORIOUS", True)
        print(_NOTORIOUS)
        return
    w.globals["zenni"] = zenni - fine       # paid — or "no" at the last chance
    print(_PAID)
