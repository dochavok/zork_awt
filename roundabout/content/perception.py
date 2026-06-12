"""
Perception check system for Roundabout: The God-Forsaken Ring.

All checks are silent — player sees outcomes only, never roll numbers.
Sourced from AWT_story_line/mechanics.md — Perception section.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from content.player import check_perception
from content.experience import award_xp

if TYPE_CHECKING:
    from engine.world import World

# Difficulty tier constants
EASY      = 5
MEDIUM    = 9
HARD      = 14
VERY_HARD = 18


def reveal_if_found(
    world: "World",
    obj_name: str,
    difficulty: int,
    xp: int = 0,
    repeating: bool = True,
) -> bool:
    """
    Silently check perception for an invisible object. On success, reveal it.
    repeating=True: re-fires every room visit until found.
    Returns True if the object was just found this call.
    """
    obj = world.objects.get(obj_name)
    if obj is None:
        return False

    # Already visible — nothing to do
    from engine.world import INVISIBLE
    if INVISIBLE not in obj.flags:
        return False

    # Check if already attempted and failed this visit (for one-time checks)
    if not repeating:
        flag_key = f"perception_tried_{obj_name}"
        if world.globals.get(flag_key):
            return False
        world.globals[flag_key] = True

    if check_perception(world, difficulty):
        # Reveal: remove INVISIBLE flag
        obj.flags = obj.flags - {INVISIBLE}
        if xp:
            award_xp(world, xp)
        return True

    return False


def reveal_exit_if_found(
    world: "World",
    room_name: str,
    direction: str,
    difficulty: int,
    flag_key: str,
    xp: int = 0,
    repeating: bool = True,
) -> bool:
    """
    Check perception for a hidden exit in a room. On success, set a world global
    flag that the room's conditional exit uses to unlock passage.
    Returns True if the exit was just discovered.
    """
    if world.globals.get(flag_key):
        return False  # already found

    if not repeating:
        tried_key = f"perception_exit_tried_{flag_key}"
        if world.globals.get(tried_key):
            return False
        world.globals[tried_key] = True

    if check_perception(world, difficulty):
        world.globals[flag_key] = True
        if xp:
            award_xp(world, xp)
        return True

    return False


def check_and_reveal(
    world: "World",
    obj_name: str,
    difficulty: int,
    xp: int = 0,
) -> bool:
    """Convenience: repeating check for a single object. Returns True on find."""
    return reveal_if_found(world, obj_name, difficulty, xp=xp, repeating=True)
