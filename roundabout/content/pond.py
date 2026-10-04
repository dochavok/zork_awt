"""
Roundabout Pond — the Ship-in-a-Bottle (locations.md — Roundabout Pond;
items.md — Ship-in-a-Bottle).

The bottle is spotted by a Medium perception check on each visit until seen,
then fished out with the rod and a Hard fishing roll. It lands on the bank.

Globals: POND-BOTTLE-SEEN, POND-BOTTLE-LANDED.
"""

from __future__ import annotations
from engine.world import World, Room, INVISIBLE, TAKEBIT

SIGHT_DIFFICULTY = 9     # Medium
FISH_DIFFICULTY = 14     # Hard

BOTTLE_IN_POND = "You see a bottle at the bottom of the pond."
BOTTLE_ON_BANK = "A Ship-in-a-Bottle lies in the reeds at the water's edge."
_CAUGHT = (
    "You cast, let the hook sink, and drag it slowly along the bottom. On the "
    "third pass it catches on something with weight. You reel it in carefully: "
    "a bottle, green glass furred with pond-scum, and inside it a tiny ship in "
    "full sail. You set it on the bank."
)
_SLIPPED = (
    "You drag the hook along the bottom. It catches, holds for a moment, and "
    "slips free. The bottle settles back into the silt."
)
_NOTHING_SEEN = "You fish for a while. Nothing bites, and nothing on the bottom catches the hook."
_ALREADY = "The pond has given up the only thing worth catching."
_NO_ROD = "You'd need a fishing rod."
_NOWHERE = "There's nowhere to fish here."


def on_enter(w: World, room: Room) -> None:
    """Enter hook: silent sighting check on each visit until the bottle is seen."""
    if room.name != "ROUNDABOUT-POND" or w.get_global("POND-BOTTLE-SEEN"):
        return
    from content.player import check_perception
    if check_perception(w, SIGHT_DIFFICULTY):
        w.set_global("POND-BOTTLE-SEEN", True)
        w.objects["SHIP-IN-A-BOTTLE"].clear_flag(INVISIBLE)
        print(BOTTLE_IN_POND)


def fish(w: World) -> None:
    if w.here is None or w.here.name != "ROUNDABOUT-POND":
        print(_NOWHERE)
        return
    if w.objects["FISHING-ROD"] not in w.player.contents:
        print(_NO_ROD)
        return
    if w.get_global("POND-BOTTLE-LANDED"):
        print(_ALREADY)
        return
    if not w.get_global("POND-BOTTLE-SEEN"):
        print(_NOTHING_SEEN)
        return
    from content.player import check_fishing
    if not check_fishing(w, FISH_DIFFICULTY):
        print(_SLIPPED)
        return
    print(_CAUGHT)
    w.set_global("POND-BOTTLE-LANDED", True)
    bottle = w.objects["SHIP-IN-A-BOTTLE"]
    bottle.desc = "Ship-in-a-Bottle"
    bottle.fdesc = BOTTLE_ON_BANK
    bottle.set_flag(TAKEBIT)
