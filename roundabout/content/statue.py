"""
Town Square statue — Quests 19 & 30 (silver stake).

Design: locations.md (Town Square; Town square statue), items.md (Silver
Stake), quests.md (Quests 19 & 30, step 2). USE CROWBAR ON STATUE opens the
hollow base (no roll): a silver stake and a folded note with the Keeper's
emerald wax seal. The note is a clue only.

State: STATUE-EXAMINED, STATUE-OPEN
"""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.world import World

_PRIED = (
    "You work the crowbar into the seam and lean on it. Stone grinds against "
    "stone, and the base of the statue swings open on a hinge nobody was meant "
    "to find. Inside, in the dark: a silver stake, and a folded note."
)
_CONTENTS = ("SILVER-STAKE", "STATUE-NOTE")


def statue_state(w: World) -> str:
    """unexamined | examined | open (something still inside) | looted (empty)."""
    if w.get_global("STATUE-OPEN"):
        square = w.rooms["TOWN-SQUARE"]
        if any(w.objects[n].location is square for n in _CONTENTS):
            return "open"
        return "looted"
    return "examined" if w.get_global("STATUE-EXAMINED") else "unexamined"


def pry_open(w: World) -> None:
    if w.here is None or w.here.name != "TOWN-SQUARE":
        print("There's no statue here.")
        return
    if w.objects["CROWBAR"] not in w.player.contents:
        print("You aren't carrying the crowbar.")
        return
    if w.get_global("STATUE-OPEN"):
        print("The base is already open.")
        return
    print(_PRIED)
    w.set_global("STATUE-OPEN", True)
    w.set_global("STATUE-EXAMINED", True)
    for name in _CONTENTS:
        w.move_object(w.objects[name], w.rooms["TOWN-SQUARE"])
