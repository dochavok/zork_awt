"""
World initialization for Roundabout: The God-Forsaken Ring.

Call initialize_world(world, game) once at startup before game.run().
Phases wired in as content modules are implemented:
  Phase 1 — stub: creates player, places in starting room, registers no-op verbs
  Phase 2 — make_rooms() fully populated
  Phase 3 — make_objects() fully populated
  Phase 4+ — corruption, perception, combat, quests, experience registered
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from engine.world import (
    GameObject, Room, Exit, World,
    TAKEBIT, ACTORBIT, ONBIT, INVISIBLE, NDESCBIT, CONTBIT, OPENBIT,
)

if TYPE_CHECKING:
    from engine.game import Game


def initialize_world(world: "World", game: "Game") -> None:
    """Populate world with Roundabout content and register all verb handlers."""
    from content.verbs import register_verbs
    from content.traps import register_traps

    _make_starting_room(world)
    _create_player(world)
    _init_globals(world)
    register_verbs(game)
    register_traps(world)


# ---------------------------------------------------------------------------
# Starting room — Tale and Ale Main Room (Phase 1 placeholder)
# ---------------------------------------------------------------------------

def _make_starting_room(world: "World") -> None:
    """Populate world with rooms and objects."""
    from content.rooms import make_rooms
    from content.objects import make_objects
    make_rooms(world)
    make_objects(world)


# ---------------------------------------------------------------------------
# Player
# ---------------------------------------------------------------------------

def _create_player(world: "World") -> None:
    player = GameObject(
        name="player",
        synonyms=frozenset({"me", "myself", "self"}),
        flags=frozenset({ACTORBIT}),
        desc="You look as ready as you'll ever be.",
    )
    world.register_object(player)
    starting_room = world.rooms.get("white-house")
    if starting_room is None:
        # Fallback: use first registered room
        starting_room = next(iter(world.rooms.values()), None)
    if starting_room is not None:
        world.move_object(player, starting_room)
    world.player = player
    world.winner = player
    world.here = starting_room


# ---------------------------------------------------------------------------
# Global flags and counters
# ---------------------------------------------------------------------------

def _init_globals(world: "World") -> None:
    world.globals.update({
        # Player class — set during character creation (Phase 8)
        "player_class": None,          # "warrior" | "mage" | "rogue"

        # Hearts
        "hearts": 5,
        "max_hearts": 5,

        # Currency
        "zenni": 0,

        # XP and leveling
        "xp": 0,
        "level": 1,

        # The God-Forsaken Ring corruption state
        "ring_corruption": 0,          # 0–50; 50 = game over
        "ring_worn": False,            # True while ring is on player's finger
        "nobus_favor_available": False, # set True at Level 7
        "nobus_favor_used": False,

        # Quest states: {quest_id: "undiscovered"|"discovered"|"in_progress"|"complete"}
        "quest_states": {},

        # Tip Journal
        "has_journal": False,
        "journal_hints": {},           # {quest_id: [tier1_text, tier2_text, ...]}

        # Torch state
        "torch_turns_remaining": 0,    # 0 = no torch, 100 = full torch
        "torch_ignited": False,        # True once first dark-room entry

        # Light spell
        "has_light_spell": False,
        "light_spell_active": False,

        # Free drink flag (for May)
        "free_drink_pending": False,
        "free_drink_reason": "",

        # May hint: Raznak nudge fired flag
        "may_raznak_nudge_given": False,

        # Archery Range visited flag (for May's Raznak nudge)
        "archery_range_visited": False,

        # Raznak dialogue state
        "raznak_dialogue_stage": 0,

        # Skills
        "skill_melee": False,
        "skill_bow": False,
        "skill_spell": False,

        # Spells learned
        "spell_light": False,
        "spell_unbind_undead": False,
        "spell_fireball": False,
        "spell_rest": False,           # granted at level 6, no scroll

        # Combat cooldowns (turns remaining until available again)
        "fireball_cooldown": 0,
        "rest_cooldown": 0,

        # Finishing move (Level 8, secret)
        "finishing_move_available": False,

        # Quest board cascade flags
        "board_quest_22_posted": True,  # posted at game start
        "board_quest_50_posted": True,  # posted at game start
        "shamus_met": False,

        # Ship state
        "ship_stolen": False,
        "at_sea": False,

        # Ty's casino
        "ty_bankroll": 30,

        # Trophy case
        "trophy_count": 0,
        "trophy_items": [],

        # Zenni rooms: list of (room_name, difficulty_target, zenni_amount) assigned at init
        "zenni_rooms": [],

        # Bag of Holding flag (if added as item later)
        "has_bag": False,
    })
