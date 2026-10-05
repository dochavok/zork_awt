"""
The Pie Rat Ship after the heist: the treasure map, Desert Island's buried
chest, and returning the ship (locations.md — Pie Rat Ship, Desert Island;
items.md — Treasure Map, Buried Chest, Pie Rat Coin).

Globals: MAP-FOUND, SHIP-AWAY, SHIP-RETURNED, CHEST-DUG, CHEST-OPEN.
"""

from __future__ import annotations
import random
from engine.world import World, Room, INVISIBLE

MAP_DIFFICULTY = 14          # Hard (mechanics.md — Difficulty tiers)
CHEST_ZENNI = 30

_MAP_FOUND = (
    "Wedged under a barrel lashed to the rail is a fold of oilcloth. Inside is a "
    "hand-drawn map: a small island just off the sea lane, a dotted line, and an X "
    "near the trees. You tuck it away."
)
_NO_SHOVEL = "The sand just slides back into the hole. You'd need a shovel."
_DUG_WITH_MAP = (
    "You pace it out from the map — up the beach, toward the trees, to where the X "
    "should be. Two feet down, the shovel hits wood: a small chest, iron-banded and "
    "crusted with salt."
)
_DUG_LUCKY = (
    "Two feet down, the shovel hits wood: a small chest, iron-banded and crusted "
    "with salt. Lucky."
)
_DUG_NOTHING = "You dig a hole. It's a perfectly good hole. There's nothing in it."
_ALREADY_DUG = "You've already found what was buried here."
_CHEST_OPENED = (
    "The hinges complain, but the lid comes up. Inside, wrapped in oilcloth: "
    "30 Zenni. You pocket them."
)
_CHEST_EMPTY = "The chest is open, and empty."
_NO_COIN = (
    'A Pie Rat blocks the gangplank. "Coin," he says, and holds out a hand, palm '
    "up — not to take it, just to see it. You don't have it. He doesn't move."
)
_NO_DISGUISE = (
    "A Pie Rat on deck looks you over with the thoroughness of someone whose job "
    'is exactly this. "You don\'t even look like a pirate." He doesn\'t move. '
    "Neither, apparently, will you."
)
_CREW_ABOARD = (
    "The Pie Rat at the gangplank squints at your coat, then at you. "
    '"Crew\'s all aboard. Don\'t know you." He doesn\'t move.'
)
CHEST_CLOSED_LISTING ="A salt-crusted chest sits in the hole you dug."
CHEST_EMPTY_LISTING = "An empty chest sits in the hole you dug."
NOTHING_TO_DIG = "There's nothing here worth digging for."
_RETURNED = (
    "The Pie Rats are waiting on the dock. Nobody says anything for a while. The "
    "biggest of them walks the deck stem to stern and finds nothing wrong with his "
    "ship, which seems to annoy him more than damage would have. He snorts, digs in "
    "a pocket, and flips you a coin. It rings on the boards at your feet."
)

# Rooms that count as "aboard the ship" for the map check
_ABOARD = frozenset({
    "SHIP-DECK", "SEA-WEST", "SEA-MID", "SEA-EAST", "LAND-HO",
    *(f"OPEN-OCEAN-{i}" for i in range(1, 70)),
})


# ---------------------------------------------------------------------------
# Treasure map — Hard perception check every turn aboard until found
# ---------------------------------------------------------------------------

def on_enter(w: World, room: Room) -> None:
    """Enter hook: arm the map check when the player comes aboard; mark the
    ship away from harbor once it reaches open water."""
    if room.name in _ABOARD and room.name != "SHIP-DECK":
        w.set_global("SHIP-AWAY", True)
    if room.name in _ABOARD and not w.get_global("MAP-FOUND"):
        clock = w.game.clock
        if clock.get("map-clock") is None:
            clock.add_demon("map-clock", _map_demon)
        event = clock.get("map-clock")
        event.enabled = True
        event.ticks = 1


def _map_demon(w: World) -> bool:
    if w.get_global("MAP-FOUND") or w.here is None or w.here.name not in _ABOARD:
        return False
    from content.player import check_perception
    if check_perception(w, MAP_DIFFICULTY):
        w.set_global("MAP-FOUND", True)
        w.move_object(w.objects["TREASURE-MAP"], w.player)
        print(_MAP_FOUND)
        return True
    w.game.clock.get("map-clock").ticks = 1
    return False


# ---------------------------------------------------------------------------
# Desert Island — buried chest
# ---------------------------------------------------------------------------

def dig(w: World) -> None:
    if w.get_global("CHEST-DUG"):
        print(_ALREADY_DUG)
        return
    if w.objects["SHOVEL"] not in w.player.contents:
        print(_NO_SHOVEL)
        return
    has_map = w.objects["TREASURE-MAP"] in w.player.contents
    if has_map:
        print(_DUG_WITH_MAP)
    elif random.randint(1, 10) <= 1:     # 10% without the map
        print(_DUG_LUCKY)
    else:
        print(_DUG_NOTHING)
        return
    w.set_global("CHEST-DUG", True)
    chest = w.objects["BURIED-CHEST"]
    chest.clear_flag(INVISIBLE)
    from content.mid_tier import dig_note
    dig_note(w)


def open_chest(w: World) -> None:
    if w.get_global("CHEST-OPEN"):
        print(_CHEST_EMPTY)
        return
    w.set_global("CHEST-OPEN", True)
    w.objects["BURIED-CHEST"].fdesc = CHEST_EMPTY_LISTING
    w.globals["zenni"] = w.globals.get("zenni", 0) + CHEST_ZENNI
    print(_CHEST_OPENED)


# ---------------------------------------------------------------------------
# Returning the ship — the Pie Rat Coin
# ---------------------------------------------------------------------------

def gangplank_refusal(w: World):
    """Boarding from the Docks (BOARD SHIP or EAST — locations.md, The
    gangplank). Returns the refusal line, or None to let the player aboard."""
    carried = w.player.contents
    if w.objects["PIE-RAT-COIN"] in carried:
        return None
    if w.get_global("SHIP-RETURNED"):
        return _NO_COIN
    if w.objects["PIE-RAT-DISGUISE"] not in carried:
        return _NO_DISGUISE
    if not w.get_global("PIE-RATS-GONE"):
        return _CREW_ABOARD
    return None


def gangplank_check(w: World, room: Room):
    """Walk check: EAST from the Docks onto the deck is BOARD SHIP."""
    if room.name == "SHIP-DECK" and w.here is not None and w.here.name == "DOCKS":
        return gangplank_refusal(w)
    return None


def ship_returned(w: World) -> None:
    """Call after the player arrives back in harbor (DOCK, or sailing in)."""
    w.set_global("SHIP-OCEAN-POS", None)
    if not w.get_global("SHIP-AWAY") or w.get_global("SHIP-RETURNED"):
        return
    w.set_global("SHIP-RETURNED", True)
    print(_RETURNED)
    w.move_object(w.objects["PIE-RAT-COIN"], w.here)
