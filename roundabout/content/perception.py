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

# Difficulty tier constants
EASY      = 5
MEDIUM    = 9
HARD      = 14
VERY_HARD = 18


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
    return True
