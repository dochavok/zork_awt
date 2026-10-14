"""
Which takeable things a room's own text describes (World.listing_filter;
mechanics.md — Floor listings; TODO #20, 2026-10-14).

A takeable item is left out of the room listing only while it lies where its
room's text describes it. Anywhere else it's listed like any other item,
whatever its NDESCBIT says — the flag used to follow these items everywhere,
so a hand cart dropped on the Rickety Bridge (or a gold watch, a support beam,
an altar artifact taken by WEAR) vanished from LOOK.
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from engine.world import World


def _at(w: World, obj, room: str) -> bool:
    return obj.location is w.rooms[room]


# object -> where its room's text describes it
DESCRIBED = {
    # The Storage Area's "a hand cart against one wall"; the Graveyard's line once
    # the gravestone is back
    "HAND-CART": lambda w, o: _at(w, o, "STORAGE-AREA")
    or (_at(w, o, "GRAVEYARD") and bool(w.get_global("GRAVESTONE-RETURNED"))),
    # The Storage Area's "a heavy support beam"; the Gallery once it props the way
    "SUPPORT-BEAM": lambda w, o: _at(w, o, "STORAGE-AREA")
    or (_at(w, o, "COLLAPSED-GALLERY") and bool(w.get_global("TIMBERS-CLEARED"))),
    # The Crevice's skeleton's finger
    "GOLD-WATCH": lambda w, o: _at(w, o, "THE-CREVICE"),
    # The Altar's own artifact lines
    "CRYSTAL-BOWL": lambda w, o: _at(w, o, "ALTAR")
    or (_at(w, o, "ROUNDABOUT-FOREST") and o.has_flag("NDESCBIT")),   # on the pedestal
    "WEREWOLFS-AMULET": lambda w, o: _at(w, o, "ALTAR"),
    "PALE-BLADE": lambda w, o: _at(w, o, "ALTAR"),
}


def listing_filter(w: World, obj) -> Optional[bool]:
    described = DESCRIBED.get(obj.name)
    return None if described is None else described(w, obj)
