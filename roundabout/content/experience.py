"""
XP and leveling system for Roundabout: The God-Forsaken Ring.

Sourced from AWT_story_line/experience.md.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.world import World

# Cumulative XP thresholds to reach each level
_LEVEL_THRESHOLDS = {
    1: 0,
    2: 20,
    3: 45,
    4: 85,
    5: 145,
    6: 225,
    7: 320,
    8: 420,
}

# Dice pool per level: (num_dice, die_sides, bonus)
_DICE_BY_LEVEL = {
    1: (1, 6,  0),
    2: (2, 6,  1),
    3: (2, 8,  2),
    4: (2, 10, 3),
    5: (3, 10, 4),
    6: (3, 12, 5),
    7: (2, 20, 6),
    8: (3, 20, 7),
}

# Hearts added at each level transition (None = no heart gain)
_HEARTS_AT_LEVEL = {
    3: 1,
    5: 1,
    7: 1,
}


def award_xp(world: "World", amount: int) -> None:
    """Add XP to player total. Auto-levels if threshold crossed."""
    if amount <= 0:
        return
    g = world.globals
    g["xp"] = g.get("xp", 0) + amount
    _check_level_up(world)


def _check_level_up(world: "World") -> None:
    g = world.globals
    current = g.get("level", 1)
    xp = g.get("xp", 0)

    while current < 8:
        next_level = current + 1
        if xp >= _LEVEL_THRESHOLDS[next_level]:
            current = next_level
            g["level"] = current
            _apply_level_up(world, current)
        else:
            break


def _apply_level_up(world: "World", level: int) -> None:
    g = world.globals
    print(f"You hear music — a familiar melody. You have reached level {level}!")

    # Heart increase
    hearts_gained = _HEARTS_AT_LEVEL.get(level, 0)
    if hearts_gained:
        g["max_hearts"] = g.get("max_hearts", 5) + hearts_gained
        g["hearts"] = g.get("hearts", 5) + hearts_gained

    # Level 6 — REST spell granted silently except for flavor message
    if level == 6:
        g["spell_rest"] = True
        print(
            "You feel a deeper sense of calm settle over you — the kind that comes with "
            "hard-won experience. You can now REST to recover when the fighting stops."
        )

    # Level 7 — Nobu's Favor (silent; no announcement)
    if level == 7:
        g["nobus_favor_available"] = True

    # Level 8 — Finishing Move (silent; no announcement)
    if level == 8:
        g["finishing_move_available"] = True


def get_dice(world: "World") -> tuple[int, int, int]:
    """Return (num_dice, die_sides, bonus) for current player level."""
    level = world.globals.get("level", 1)
    return _DICE_BY_LEVEL.get(level, (1, 6, 0))


def get_level(world: "World") -> int:
    return world.globals.get("level", 1)
