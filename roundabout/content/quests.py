"""
Quest state machine for Roundabout: The God-Forsaken Ring.

States: UNDISCOVERED → DISCOVERED → IN_PROGRESS → COMPLETE
All quest IDs match the AWT_story_line/quests.md numbering.

Sourced from AWT_story_line/quests.md and experience.md.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from content.experience import award_xp

if TYPE_CHECKING:
    from engine.world import World

# State constants
UNDISCOVERED = "undiscovered"
DISCOVERED   = "discovered"
IN_PROGRESS  = "in_progress"
COMPLETE     = "complete"

# Quest metadata: {quest_id: {"name": str, "xp": int, "zenni": int}}
_QUEST_META: dict[str, dict] = {
    "4":   {"name": "The Whispering Jar",        "xp": 10, "zenni": 5},
    "7":   {"name": "The Bone Flute",            "xp": 6,  "zenni": 3},
    "12":  {"name": "The Locked Music Box",      "xp": 10, "zenni": 5},
    "17":  {"name": "The Frozen Watch",          "xp": 17, "zenni": 8},
    "19":  {"name": "The Hollow Statue",         "xp": 11, "zenni": 5},
    "22":  {"name": "The Ruined Aqueduct",       "xp": 10, "zenni": 5},
    "24":  {"name": "The Beekeeper's Swarm",     "xp": 10, "zenni": 5},
    "25":  {"name": "The Flooded Cellar",        "xp": 10, "zenni": 5},
    "27":  {"name": "The Toll Bridge Operator",  "xp": 6,  "zenni": 3},
    "28":  {"name": "The Archivist's Request",   "xp": 6,  "zenni": 3},
    "30":  {"name": "The Undead Warden",         "xp": 11, "zenni": 5},
    "32":  {"name": "The Missing Gravestone",    "xp": 12, "zenni": 6},
    "34":  {"name": "The Frozen Soldier",        "xp": 17, "zenni": 8},
    "38":  {"name": "The Collapsed Passage",     "xp": 8,  "zenni": 4},
    "40":  {"name": "Shamus's Recipe",           "xp": 6,  "zenni": 3},
    "41":  {"name": "The Child's Kite",          "xp": 4,  "zenni": 3},
    "42":  {"name": "The Brotherhood Stones",    "xp": 12, "zenni": 6},
    "49":  {"name": "The Ruined Shrine",         "xp": 17, "zenni": 8},
    "50":  {"name": "The Lost Apprentice",       "xp": 12, "zenni": 6},
    "51":  {"name": "The Back Alley Mugger",     "xp": 6,  "zenni": 3},
    "52":  {"name": "Make Litlock Laugh",        "xp": 6,  "zenni": 3},
    "53":  {"name": "Will's Glasses",            "xp": 10, "zenni": 5},  # 20 if enchanted
    "54":  {"name": "Fight the Knight",          "xp": 8,  "zenni": 4},
    "55":  {"name": "The Archer's Trial",        "xp": 6,  "zenni": 3},
    "56":  {"name": "Will's Teaching",           "xp": 4,  "zenni": 2},
    "57":  {"name": "The Viking Trust Trials",   "xp": 12, "zenni": 5},
    "58":  {"name": "The Dragon-Nip",            "xp": 4,  "zenni": 2},
    "59":  {"name": "Beat Lynds",                "xp": 5,  "zenni": 3},
}

# Quest board postings: {quest_id: True} means quest is posted on board
# Initial postings set in init.py globals
_BOARD_QUESTS = {"22", "50"}


def get_state(world: "World", quest_id: str) -> str:
    return world.globals.get("quest_states", {}).get(quest_id, UNDISCOVERED)


def set_state(world: "World", quest_id: str, state: str) -> None:
    qs = world.globals.setdefault("quest_states", {})
    qs[quest_id] = state


def discover(world: "World", quest_id: str) -> None:
    """Mark quest discovered if not already progressed."""
    if get_state(world, quest_id) == UNDISCOVERED:
        set_state(world, quest_id, DISCOVERED)


def start(world: "World", quest_id: str) -> None:
    """Advance quest to IN_PROGRESS."""
    current = get_state(world, quest_id)
    if current in (UNDISCOVERED, DISCOVERED):
        set_state(world, quest_id, IN_PROGRESS)


def complete(
    world: "World",
    quest_id: str,
    *,
    xp_override: int | None = None,
    zenni_override: int | None = None,
    cascade_quests: list[str] | None = None,
) -> None:
    """
    Mark quest complete. Award XP and Zenni. Trigger cascade postings.
    xp_override / zenni_override allow special-case values (Quest 53 variable XP).
    """
    if get_state(world, quest_id) == COMPLETE:
        return

    set_state(world, quest_id, COMPLETE)

    meta = _QUEST_META.get(quest_id, {})
    xp    = xp_override    if xp_override    is not None else meta.get("xp", 0)
    zenni = zenni_override if zenni_override is not None else meta.get("zenni", 0)

    award_xp(world, xp)
    if zenni:
        world.globals["zenni"] = world.globals.get("zenni", 0) + zenni

    # Cascade: post related quests to board
    if cascade_quests:
        for q in cascade_quests:
            _post_to_board(world, q)


def _post_to_board(world: "World", quest_id: str) -> None:
    """Post quest to board; sets DISCOVERED state if previously unknown."""
    posted = world.globals.setdefault("board_quest_posted", {})
    posted[quest_id] = True
    discover(world, quest_id)


def is_complete(world: "World", quest_id: str) -> bool:
    return get_state(world, quest_id) == COMPLETE


def is_discovered(world: "World", quest_id: str) -> bool:
    return get_state(world, quest_id) in (DISCOVERED, IN_PROGRESS, COMPLETE)


def active_quest_ids(world: "World") -> list[str]:
    """Return list of quest IDs that are discovered or in progress (not complete)."""
    qs = world.globals.get("quest_states", {})
    return [qid for qid, state in qs.items() if state in (DISCOVERED, IN_PROGRESS)]
