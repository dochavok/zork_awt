"""
Bog items (locations.md — Bog of Eternal Stench NE / NW / SW; items.md —
Rune Stones, Music Box Key, Bog Thyme). Each is found by a Level 2 perception
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


def reveal(w: World, room_name: str) -> bool:
    """M_ENTER (and SEARCH): silent Level 2 check until found (before the room
    description). True if found just now."""
    from content.perception import LEVEL_2, reveal_if_found
    names = _FINDS.get(room_name, ())
    if names and reveal_if_found(w, names[0], LEVEL_2):
        for other in names[1:]:          # the key is found with its log
            w.objects[other].clear_flag("INVISIBLE")
        return True
    return False


def key_taken(w: World) -> None:
    """After TAKE KEY: the log is empty; the key lists normally from now on."""
    w.objects["MUSIC-BOX-KEY"].clear_flag(NDESCBIT)
    log = w.objects["HOLLOW-LOG"]
    log.fdesc = LOG_EMPTY
    log.examine = LOG_EXAMINE_EMPTY
