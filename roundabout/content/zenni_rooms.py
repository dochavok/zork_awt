"""
Hidden Zenni rooms (mechanics.md — Zenni Rooms).

36 rooms are chosen at game initialization from the eligible pool and fixed
for the playthrough: 18 Easy / 10 Medium / 2 Hard pay 1–3 Zenni each, 6 Very
Hard pay 5. A silent perception check fires on every visit until the room's
Zenni is found. Actually Enchanted Glasses pass every check.

The pool uses room IDs. Rooms not built yet are listed under the ID they must
be given when built; a chosen room that doesn't exist yet simply can't be
visited until it does.
"""

from __future__ import annotations
import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.world import World


ELIGIBLE_ROOMS = [
    # Overworld & Town
    "WHITE-HOUSE", "WIZARDS-TOWER", "WIZARDS-BEDROOM",
    "MAIN-WEST", "TOWN-SQUARE", "MAIN-EAST", "ALLEY", "BACK-ALLEY",
    "TOWN-HALL-EXTERIOR", "COUNCIL-CHAMBER", "RECORDS-ROOM", "UPPER-HALL", "TOWN-HALL-TOWER",
    "TALE-AND-ALE", "BAR", "CASINO-CORNER", "PIPE-ROOM", "KITCHEN", "UPSTAIRS-HALL",
    "GUEST-ROOM-1", "GUEST-ROOM-2", "GUEST-ROOM-3", "CELLAR",
    "LIBRARY", "STACKS",
    "CHURCH-NAVE", "ALTAR", "KEEPERS-CHAMBER",
    "GRAVEYARD", "MAUSOLEUM", "CRYPT",
    "ROUNDABOUT-WASTELAND", "VOLCANO", "PYRONICUS-FORGE",
    "ARCHERY-RANGE", "VIKING-ENCAMPMENT", "HAALVARS-HUT", "RITUAL-CIRCLE", "FIRE-PIT",
    "ROUNDABOUT-POND",
    "DANKHAUS-COMMON-ROOM", "DANKHAUS-HEARTH-ROOM", "DANKHAUS-GARDEN",
    "LITLOCKS-ROOM", "LITLOCKS-STUDY", "LYNDS-ROOM", "AURIX-ROOM",
    "BEACH-ROAD", "OLD-OAK", "BEEKEEPERS-COTTAGE", "SWARM-TREE", "ROUNDABOUT-FOREST",
    "ROUNDABOUT-BEACH", "LIGHTHOUSE", "DOCKS", "SHIP-DECK",
    # Dungeon — Upper Tier
    "INK-CORRIDOR", "SUPPLY-ROOM", "NARROW-PASSAGEWAY", "IDOL-ROOM", "STORAGE-AREA",
    "COLLAPSED-GALLERY", "CREATURE-DEN", "COMBAT-ROOM", "PRAYER-ALCOVE",
    "PORTCULLIS-CORRIDOR", "SHRINE-ROOM", "MID-TIER-KEY-DOOR",
    # Dungeon — Mid Tier (Dream Corridor excluded)
    "KEY-DOOR-LANDING", "STORED-ROOM", "INSCRIPTION-CHAMBER", "CAVE-CREATURES-LAIR",
    "ECHO-ALCOVE", "MAGNETIC-VAULT", "DEEP-LOCK-DOOR",
    "SPILLWAY", "LOST-APPRENTICES-CELL", "SUPPLY-CACHE", "FLOOD-SUMP",
    # Dungeon — Lower Tier
    "LOWER-CRYPT", "LOWER-ENCAMPMENT", "THERMAL-VENT-ROOM", "LOWER-CROSSING",
    "NARROW-PASS", "STILL-DEN", "TOOL-ALCOVE", "FLOODED-PASSAGE", "FOUNTAIN-ROOM",
    "SPIRIT-ROOM", "BURIAL-CHAMBER",
]

# (tier difficulty, count, zenni) — difficulty targets from content/perception.py
_TIERS = [("EASY", 18, None), ("MEDIUM", 10, None), ("HARD", 2, None), ("VERY_HARD", 6, 5)]

_FOUND = "Something catches your eye, tucked out of sight: {n} Zenni. You pocket {it}."


def assign(world: World, rng: random.Random) -> None:
    """Pick the 36 Zenni rooms for this playthrough. Called once at init."""
    from content import perception
    chosen = rng.sample(ELIGIBLE_ROOMS, sum(count for _, count, _ in _TIERS))
    rooms: dict[str, dict] = {}
    i = 0
    for tier, count, fixed in _TIERS:
        for room_id in chosen[i:i + count]:
            rooms[room_id] = {
                "difficulty": getattr(perception, tier),
                "zenni": fixed if fixed is not None else rng.randint(1, 3),
                "found": False,
            }
        i += count
    world.set_global("ZENNI-ROOMS", rooms)


def on_enter(world: World, room) -> None:
    """Silent perception check on every visit until the room's Zenni is found."""
    entry = (world.get_global("ZENNI-ROOMS") or {}).get(room.name)
    if entry is None or entry["found"]:
        return
    from content.player import check_perception
    if not check_perception(world, entry["difficulty"]):
        return
    entry["found"] = True
    n = entry["zenni"]
    world.globals["zenni"] = world.globals.get("zenni", 0) + n
    print(_FOUND.format(n=n, it="it" if n == 1 else "them"))
