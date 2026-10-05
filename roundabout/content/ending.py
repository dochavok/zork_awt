"""
SCORE and the end of the game.

Design: mechanics.md (Score; Trophy Case — treasure achievement tiers),
ring-rituals.md (Will's final scene; the game ends).

- Score = treasure points deposited in the Trophy Case (300 possible),
  worked out from what's in the case (content/trophy_case.py).
- SCORE during play: no denominators, no tier. At the end it runs
  automatically with denominators and the tier title.
- GIVE RING TO WILL with the bound ring: Will's final scene, the end-of-game
  SCORE, the closing line, then GAME OVER.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.world import World

MAX_POINTS = 300
TREASURES = 9

# (lowest points, title) — mechanics.md, Treasure achievement tiers
_TIERS = [
    (300, "Calder Finch"),
    (240, "Roundabout's Unhinged Treasure Enthusiast"),
    (180, "Plunder King"),
    (120, "Treasure Hunter"),
    (60, "Loot Goblin"),
    (1, "Scavenger"),
    (0, "Empty-Handed"),
]

_FINAL_SCENE = (
    "Will takes the ring from your hand. He holds it for a moment without looking "
    "at it — as though he's listening for something. Then, apparently satisfied, "
    "he sets it down on the desk.\n\n"
    "\"Good,\" he says.\n\n"
    "He looks at you properly for the first time since you walked in.\n\n"
    "\"You're alive,\" he says. \"I wasn't certain you would be. I should have told "
    "you that at the start.\" He pauses. \"I didn't, because I needed you to go.\"\n\n"
    "He picks up his pen.\n\n"
    "\"Well done, {name}.\"\n\n"
    "He means it. You can tell because he doesn't say anything else."
)
_CLOSING = "*** THE RING IS BOUND — GO BACK TO THE GUILD HALL FOR REWARDS ***"


def _title(points: int) -> str:
    return next(title for floor, title in _TIERS if points >= floor)


def score(w: World, final: bool = False) -> None:
    from content.experience import get_level
    from content import trophy_case
    points = trophy_case.points(w)
    count = trophy_case.count(w)
    xp = w.globals.get("xp", 0)
    if final:
        print(f"Score: {points} of {MAX_POINTS}")
        print(f"Level {get_level(w)} ({xp} XP)")
        print(f"{count} of {TREASURES} treasures on display.")
        print(f"Title: {_title(points)}")
    else:
        print(f"Score: {points}")
        print(f"Level {get_level(w)} ({xp} XP)")
        print(f"{count} treasure{'' if count == 1 else 's'} on display.")


def return_ring(w: World) -> None:
    """GIVE RING TO WILL with the bound ring: the end of the game."""
    name = w.globals.get("player_name", "")
    print(_FINAL_SCENE.format(name=name))
    w.move_object(w.objects["RING"], None)          # on Will's desk
    print()
    score(w, final=True)
    print()
    print(_CLOSING)
    w.set_global("GAME-OVER", True)
    w.game.quit()
