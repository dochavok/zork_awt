"""
Ring corruption system for Roundabout: The God-Forsaken Ring.

SACRED CONSTRAINT: Ring corruption must NEVER be reduced, slowed, or mitigated
by any mechanic, item, or quest reward. This module enforces that invariant.

Sourced from AWT_story_line/mechanics.md — The God-Forsaken Ring section.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.world import World

# Corruption milestones and their messages
_MILESTONE_MESSAGES = {
    10: (
        "The ring is warm. You hadn't noticed until just now. "
        "You're not sure when it started."
    ),
    25: (
        "The ring is heavier than it was. Not in weight — in presence. "
        "It knows you're wearing it. You find yourself aware of it "
        "in a way you weren't before."
    ),
    40: (
        "The ring is harder to ignore than it was. You are aware of it "
        "the way you're aware of a sound that hasn't stopped. "
        "You should take it off. You know you should take it off."
    ),
}

# Late-stage removal difficulty targets (ticks 41-49)
_REMOVAL_DIFFICULTY = {
    41: 5,  42: 7,  43: 9,  44: 11,
    45: 13, 46: 15, 47: 17, 48: 19, 49: 21,
}


def tick_corruption(world: "World") -> None:
    """
    Advance corruption by 1 tick. Called every turn ring is worn.
    NEVER call this when ring is not worn or when at an altar.
    """
    g = world.globals
    if not g.get("ring_worn", False):
        return

    old = g.get("ring_corruption", 0)
    new = old + 1
    g["ring_corruption"] = new

    # Milestone messages
    if new in _MILESTONE_MESSAGES:
        print(_MILESTONE_MESSAGES[new])

    # Game over at 50
    if new >= 50:
        _full_corruption(world)


def _full_corruption(world: "World") -> None:
    print(
        "You reach for the ring. Your hand doesn't move. "
        "You watch it not move. The ring is warm and patient and it has been waiting "
        "for exactly this. You are not going to take it off.\n\n"
        "*** GAME OVER ***"
    )
    world.set_global("GAME-OVER", True)   # fail condition — no resurrection
    world.game.quit()


def try_remove_ring(world: "World") -> bool:
    """
    Attempt to remove the ring. Returns True if successful.
    At ticks 41-49 requires a challenge roll (level dice only, no bonus).
    Always succeeds at ticks 0-40.
    """
    from content.player import roll
    g = world.globals
    tick = g.get("ring_corruption", 0)

    if tick < 41:
        # Normal removal
        _do_remove_ring(world)
        return True

    if tick >= 50:
        # Already at full corruption — jigs_up already called
        return False

    # Challenge roll: level dice only, no bonus
    difficulty = _REMOVAL_DIFFICULTY.get(tick, 21)
    result = roll(world, corruption_roll=True)

    if result >= difficulty:
        # Distinguish clean success vs near-miss
        near_miss_threshold = difficulty + 3
        if result < near_miss_threshold:
            print(
                "The ring comes off. It didn't want to. "
                "You're not sure you could have held out another moment."
            )
        else:
            print("You remove the ring. Whatever it wants, it didn't get it this time.")
        _do_remove_ring(world)
        return True
    else:
        print("You try to take the ring off. Your fingers find it. They don't do what you ask.")
        return False


def _do_remove_ring(world: "World") -> None:
    world.globals["ring_worn"] = False
    # Disable corruption clock (stop ticking while ring is off)
    world.game.clock.disable("ring-corruption-clock")


def wear_ring(world: "World") -> None:
    """Put the ring on. Starts/resumes corruption ticking."""
    g = world.globals
    tick = g.get("ring_corruption", 0)
    if tick >= 50:
        print("The ring is warm and patient. You are not putting it back on.")
        return

    # Bound state: ring won't go on after binding ceremony
    if g.get("ring_bound", False):
        print("The ring won't go on. It simply won't.")
        return

    g["ring_worn"] = True

    # Register corruption demon if not already registered; then arm it
    ensure_clock(world)
    event = world.game.clock.get("ring-corruption-clock")
    if event:
        event.enabled = True
        event.ticks = 1  # fire on next turn


def ensure_clock(world: "World") -> None:
    """Register the per-turn corruption demon if not already registered."""
    clock = world.game.clock
    if clock.get("ring-corruption-clock") is not None:
        return

    def _corruption_demon(w: "World") -> bool:
        tick_corruption(w)
        # Re-arm for next turn if ring is still worn
        if w.globals.get("ring_worn"):
            event = w.game.clock.get("ring-corruption-clock")
            if event:
                event.ticks = 1
        return False

    clock.add_demon("ring-corruption-clock", _corruption_demon)


def is_worn(world: "World") -> bool:
    return bool(world.globals.get("ring_worn", False))


def get_tick(world: "World") -> int:
    return world.globals.get("ring_corruption", 0)
