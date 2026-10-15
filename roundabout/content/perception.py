"""
Perception check system for Roundabout: The God-Forsaken Ring.

All checks are silent — player sees outcomes only, never roll numbers.
Sourced from AWT_story_line/mechanics.md — Perception section.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from content.player import check_perception

if TYPE_CHECKING:
    from engine.world import World

# Difficulty tiers (mechanics.md — Difficulty tiers, 2026-10-15): a Level N check
# is passed about a third of the time by a level-N player with no class bonus
# (Lucky counted, Second Glance not); a level below passes it rarely, a level
# above usually. Levels 1–4 were Easy, Medium, Hard and Very Hard (same targets).
LEVEL_1 = 5
LEVEL_2 = 9
LEVEL_3 = 14
LEVEL_4 = 18
LEVEL_5 = 24
LEVEL_6 = 28
LEVEL_7 = 32
LEVEL_8 = 44


def reveal_if_found(world: "World", obj_name: str, difficulty: int) -> bool:
    """
    Silently check perception for an invisible object; on success, reveal it.
    Callers run it on every visit until found (mechanics.md — repeating checks).
    Returns True if the object was just found this call.
    """
    from engine.world import INVISIBLE
    obj = world.objects[obj_name]
    if INVISIBLE not in obj.flags:
        return False                     # already found
    if not check_perception(world, difficulty):
        return False
    obj.flags = obj.flags - {INVISIBLE}
    return True


def reveal_exit_if_found(world: "World", difficulty: int, flag_key: str) -> bool:
    """
    Check perception for a hidden exit. On success, set `flag_key`, which the
    room's conditional exit reads. Returns True if the exit was just found.
    """
    if world.globals.get(flag_key):
        return False                     # already found
    if not check_perception(world, difficulty):
        return False
    world.globals[flag_key] = True
    if world.here is not None:
        world.ways_changed(world.here.name)   # found on arrival: this description is full
    return True
