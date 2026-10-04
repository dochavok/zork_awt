"""
Bog items (locations.md — Bog of Eternal Stench NE / NW / SW; items.md —
Rune Stones, Music Box Key, Bog Thyme). Each is found by a Medium perception
check on every visit until found, then listed in the room description.
"""

from __future__ import annotations
from engine.world import World, NDESCBIT

LOG_WITH_KEY = (
    "A hollow log lies half-sunk among the reeds. Something small and metal "
    "glints inside it."
)
LOG_EMPTY = "A hollow log lies half-sunk among the reeds."
LOG_EXAMINE_KEY = "Rotten through the middle and hollow end to end. Wedged inside: a small brass key."
LOG_EXAMINE_EMPTY = "Rotten through the middle and hollow end to end."

# Room → objects revealed there
_FINDS = {
    "BOG-NE": ("BOG-RUNE-STONE",),
    "BOG-NW": ("HOLLOW-LOG", "MUSIC-BOX-KEY"),
    "BOG-SW": ("BOG-THYME",),
}


def reveal(w: World, room_name: str) -> None:
    """M_ENTER: silent Medium check until found (before the room description)."""
    from content.perception import MEDIUM, reveal_if_found
    names = _FINDS.get(room_name, ())
    if names and reveal_if_found(w, names[0], MEDIUM):
        for other in names[1:]:          # the key is found with its log
            w.objects[other].clear_flag("INVISIBLE")


def key_taken(w: World) -> None:
    """After TAKE KEY: the log is empty; the key lists normally from now on."""
    w.objects["MUSIC-BOX-KEY"].clear_flag(NDESCBIT)
    log = w.objects["HOLLOW-LOG"]
    log.fdesc = LOG_EMPTY
    log.examine = LOG_EXAMINE_EMPTY
