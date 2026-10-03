"""
The Back Alley — Quest 51, The Back Alley Mugger.

Design: locations.md (The Back Alley), quests.md (Quest 51), mechanics.md
(Combat; enemy stats: mugger 1d6, 2 hearts), experience.md (mugger 5 XP).

- Medium perception check on every visit until the mugger is spotted.
  Fail: mugged — 1 heart, 2–3 Zenni stolen (none if broke), wake a turn later.
  Pass: the mugger is visible; fight with KILL MUGGER, one round per command.
- Losing the fight is not death: wake with 1 heart; the mugger's hearts reset.
- Leaving mid-fight (fleeing) resets the mugger to full hearts.
- Winning: mugger slain permanently, lockpicks drop, Quest 51 completes
  (6 XP, 3 Zenni) and May's free drink waits at the Bar.

State: MUGGER-SPOTTED, MUGGER-DEAD, MUGGER-HEARTS, FREE-DRINK-PENDING
"""

from __future__ import annotations
import random
from typing import TYPE_CHECKING

from engine.game import M_NOT_HANDLED, M_ENTER, M_END

if TYPE_CHECKING:
    from engine.world import World

MUGGER_HEARTS = 2
MUGGER_DICE = (1, 6)

MUGGER_PRESENCE = (
    "A figure waits in the shadow of the crates, very still, weight on the "
    "balls of their feet. They've seen you see them."
)
_MUGGED = "Something hits you from behind. The alley tilts, then goes away."
_MUGGED_WAKE = "You come to in the Back Alley, lighter in the pocket and sore in the head."
_ROUND_WON = "You land a solid blow. The mugger staggers."
_ROUND_LOST = "The mugger gets through your guard. You take a hit."
_ROUND_TIE = "You trade blows. Both of you feel it."
_MUGGER_DOWN = (
    "The mugger goes down and doesn't get up. Something clatters to the "
    "cobbles beside them — a roll of lockpicks."
)
_FIGHT_LOST = (
    "You come to on the cobbles. The mugger is gone, and so is most of your "
    "strength. The inn has beds."
)


def back_alley_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if w.get_global("MUGGER-DEAD"):
        return M_NOT_HANDLED

    if msg == M_ENTER:
        # Fleeing resets the fight; a fresh visit starts at full hearts
        w.set_global("MUGGER-HEARTS", MUGGER_HEARTS)
        if not w.get_global("MUGGER-SPOTTED"):
            from content.player import check_perception
            from content.perception import MEDIUM
            if check_perception(w, MEDIUM):
                w.set_global("MUGGER-SPOTTED", True)
                w.objects["MUGGER"].clear_flag("INVISIBLE")
            else:
                w.set_global("MUGGER-PENDING", True)   # mugged after the description
        return M_NOT_HANDLED

    if msg == M_END and w.get_global("MUGGER-PENDING"):
        w.set_global("MUGGER-PENDING", False)
        _mugged(w)
    return M_NOT_HANDLED


def _mugged(w: World) -> None:
    g = w.globals
    print(_MUGGED)
    # Not death: being mugged knocks the player out, never below 1 heart
    g["hearts"] = max(1, g.get("hearts", 1) - 1)
    zenni = g.get("zenni", 0)
    g["zenni"] = max(0, zenni - random.randint(2, 3))
    w.game.clock.tick(w, command_parsed=True)   # wakes one turn later
    print(_MUGGED_WAKE)


def fight_round(w: World) -> None:
    """KILL MUGGER — one round. Higher roll hits for 1 heart; ties hit both."""
    from content.player import roll
    g = w.globals
    mine = roll(w)
    his = sum(random.randint(1, MUGGER_DICE[1]) for _ in range(MUGGER_DICE[0]))
    mugger_hearts = int(g.get("MUGGER-HEARTS", MUGGER_HEARTS))

    if mine > his:
        print(_ROUND_WON)
        mugger_hearts -= 1
    elif his > mine:
        print(_ROUND_LOST)
        g["hearts"] = g.get("hearts", 1) - 1
    else:
        print(_ROUND_TIE)
        mugger_hearts -= 1
        g["hearts"] = g.get("hearts", 1) - 1
    g["MUGGER-HEARTS"] = mugger_hearts

    if mugger_hearts <= 0:
        _mugger_defeated(w)
    elif g["hearts"] <= 0:
        # Losing to the mugger is not death. He slips away and lies in wait
        # again: the next visit gets a fresh perception check.
        g["hearts"] = 1
        g["MUGGER-HEARTS"] = MUGGER_HEARTS
        w.set_global("MUGGER-SPOTTED", False)
        w.objects["MUGGER"].set_flag("INVISIBLE")
        print(_FIGHT_LOST)


def _mugger_defeated(w: World) -> None:
    from content import quests
    from content.combat import award_combat_xp
    print(_MUGGER_DOWN)
    w.set_global("MUGGER-DEAD", True)
    w.move_object(w.objects["MUGGER"], None)
    w.move_object(w.objects["LOCKPICKS"], w.rooms["BACK-ALLEY"])
    award_combat_xp(w, "mugger")
    quests.complete(w, "51")
    w.set_global("FREE-DRINK-PENDING", True)
