"""
Player dice rolling and stat helpers for Roundabout.

All rolls are hidden from the player — outcomes only, never numbers.
Sourced from AWT_story_line/experience.md and mechanics.md.
"""

from __future__ import annotations

import random
from typing import TYPE_CHECKING

from content.experience import get_dice, get_level

if TYPE_CHECKING:
    from engine.world import World


def roll(world: "World", *, corruption_roll: bool = False) -> int:
    """
    Roll the player's current dice pool and return total.

    corruption_roll=True: uses level dice only with no bonus (ring removal challenge).
    """
    num_dice, die_sides, bonus = get_dice(world)
    total = sum(random.randint(1, die_sides) for _ in range(num_dice))

    if corruption_roll:
        return total  # no bonus for ring removal

    level = get_level(world)

    # Level 4 Lucky: reroll 1s
    if level >= 4:
        total = _reroll_ones(num_dice, die_sides, bonus)
        return total

    return total + bonus


def _reroll_ones(num_dice: int, die_sides: int, bonus: int) -> int:
    """Roll with Lucky (Level 4+): reroll each die that shows 1."""
    results = []
    for _ in range(num_dice):
        r = random.randint(1, die_sides)
        if r == 1:
            r = random.randint(1, die_sides)  # reroll once
        results.append(r)
    return sum(results) + bonus


def roll_bonus(world: "World", bonus: int) -> int:
    """Roll with an additional flat bonus (e.g. bow +5 on round 1)."""
    return roll(world) + bonus


def roll_class_bonus(world: "World", roll_type: str) -> int:
    """
    Roll with the applicable class bonus for a given roll_type.
    roll_type: 'perception' | 'strength' | 'agility' | 'trap' | 'fishing'
    """
    base = roll(world)
    player_class = world.globals.get("player_class", "")
    extra = _class_bonus(player_class, roll_type)

    # Enchanted Glasses: small perception bonus
    if roll_type == "perception":
        if world.globals.get("actually_enchanted_glasses_worn"):
            return 999  # auto-pass everything
        if world.globals.get("enchanted_glasses_worn"):
            extra += 2

    # Level 5 Second Glance: reroll failed perception checks once (invisible)
    if roll_type == "perception":
        result = base + extra
        return result  # caller handles second glance if needed

    return base + extra


def _class_bonus(player_class: str, roll_type: str) -> int:
    bonuses = {
        "warrior": {"strength": 3},
        "mage":    {"perception": 3},
        "rogue":   {"perception": 3, "trap": 3, "fishing": 3},
    }
    return bonuses.get(player_class, {}).get(roll_type, 0)


def check_perception(world: "World", difficulty: int) -> bool:
    """
    Perform a silent perception check. Returns True on success.
    Handles Second Glance (Level 5) automatically.
    """
    # Actually Enchanted Glasses auto-pass
    if world.globals.get("actually_enchanted_glasses_worn"):
        return True

    result = roll_class_bonus(world, "perception")
    if result >= difficulty:
        return True

    # Level 5+ Second Glance: one silent reroll on failure
    if get_level(world) >= 5:
        result = roll_class_bonus(world, "perception")
        return result >= difficulty

    return False


def check_strength(world: "World", difficulty: int) -> bool:
    return roll_class_bonus(world, "strength") >= difficulty


def check_trap_disarm(world: "World", difficulty: int) -> bool:
    return roll_class_bonus(world, "trap") >= difficulty


def check_fishing(world: "World", difficulty: int) -> bool:
    return roll_class_bonus(world, "fishing") >= difficulty
