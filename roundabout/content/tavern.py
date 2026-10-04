"""
Tale and Ale — May at the Bar.

Design: npcs.md (May). First visit to the Bar fires her introduction once.
Quest 51's reward (one free drink, 1 heart) is served on TALK TO MAY.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_NOT_HANDLED, M_END

if TYPE_CHECKING:
    from engine.world import World

_MAY_FIRST_VISIT = (
    "A woman behind the bar glances up as you come in — shoulder-length red "
    "hair, appraisal done in about a second, apparently satisfactory.\n"
    '"New face," she says, not unkindly. "I\'m May. Drinks are two Zenni, '
    "food's the same — keeps you on your feet longer than you'd think. Rooms "
    'are upstairs if you need to sleep it off properly."\n'
    "She sets a glass down and leans one hand on the bar.\n"
    '"If you get stuck on something and want a nudge in the right direction, '
    "money talks. Shamus is in the kitchen if you need supplies — he keeps "
    'more than recipes back there."\n'
    "She picks the glass back up and goes back to work. The conversation is "
    "over when she decides it is."
)
_MAY_BUSY = (
    "She picks the glass back up and goes back to work. The conversation is "
    "over when she decides it is."
)
_MAY_MUGGER_REWARD = (
    'May glances up. "Heard the back alley\'s gone quiet." She sets a glass '
    'on the bar. "That one\'s on the house."'
)


def bar_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_END and not w.get_global("MAY-MET"):
        w.set_global("MAY-MET", True)
        print(_MAY_FIRST_VISIT)
    return M_NOT_HANDLED


def talk_may(w: World) -> None:
    g = w.globals
    if w.get_global("FREE-DRINK-PENDING"):
        print(_MAY_MUGGER_REWARD)
        w.set_global("FREE-DRINK-PENDING", False)
        g["hearts"] = min(g.get("max_hearts", g.get("hearts", 1)), g.get("hearts", 1) + 1)
        return
    from content import cellar
    if not cellar.talk_may(w):
        print(_MAY_BUSY)
