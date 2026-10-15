"""
The Flooding Room (Trap 41, upper tier) and The Spillway (mid-tier trap side).

Design: locations.md (Flooding Room, Creature Den, Trap Side — The Spillway),
traps.md (Trap 41), quests.md (Quest 50).

- Redesigned 2026-10-14: the plate fires on entry, the first and only visit.
  No spotting, no disarm, no timer. A slab drops behind the player (the room
  has no south exit) and water pours in.
- Three levers, one pull each: the right snaps off and the water rises; the
  middle stops it; the left sweeps the player one-way down to the Spillway.
- Once the player has been in, the Creature Den's way north is sealed.

State: FLOOD-FIRED, LEVER-LEFT, LEVER-MIDDLE, LEVER-RIGHT
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_BEG, M_ENTER, M_LOOK, M_END
from engine.world import Room, Exit, RLANDBIT

if TYPE_CHECKING:
    from engine.world import World

_ROOM_FIRST = (
    "A low cave, the floor dipping toward the middle and slick with old silt. Three "
    "iron levers stand in a row on the north wall — left, middle, right — above a "
    "grated sluice mouth."
)
_ROOM = (
    "A low cave, the floor dipping toward the middle. Three iron levers stand in a "
    "row on the north wall — left, middle, right — above a grated sluice mouth. A "
    "stone slab seals the doorway to the south."
)
_WATER_ENTRY = "Water churns knee-deep across the floor, still pouring through the grate."
_WATER_RISEN = ("Water churns waist-deep across the floor, pouring through the grate "
                "harder than ever.")
_WATER_STILL = ("Water stands knee-deep across the floor, flat and still. The grate has "
                "stopped pouring.")
_WATER_RISEN_STILL = ("Water stands waist-deep across the floor, flat and still. The "
                      "grate has stopped pouring.")

_TRIGGER = (
    "Your foot comes down on a stone that sinks a little too easily. Click. You're "
    "starting to suspect the builders got a discount on pressure plates."
)
_SLAB = (
    "Behind you, a stone slab drops across the doorway with a boom you feel in your "
    "teeth. The grate on the north wall bursts open and water comes through in a "
    "cold, roaring sheet. In a few heartbeats it's above your knees."
)
_URGENCY = "The levers on the north wall suddenly look very interesting."

_RIGHT = ("The lever snaps off in your hand. Behind the grate something gives with a "
          "groan, and a fresh surge pushes the water up to your waist.")
_MIDDLE = ("The middle lever comes down with a heavy clunk. Behind the grate the sluice "
           "slams shut, and the water stops coming. It doesn't go anywhere, either.")
_LEFT = ("The left lever fights you, then comes down all at once. Under the water, "
         "something in the floor opens with a deep, sucking roar.")
_SPENT = "You already tried that one."
_SWEPT = ("The water closes over your head and the floor drops away. The current takes "
          "you down through the sluice, turning you over in the dark, and lets go.")

LEVERS_EXAMINE = "Three iron levers in a row — left, middle, right. Nothing says which does what."
_STUMP = "The right one is a stump now."
SLUICE_POURING = ("A square mouth low in the north wall, barred with an iron grate. Water "
                  "is pouring through it.")
SLUICE_STOPPED = ("A square mouth low in the north wall, barred with an iron grate. "
                  "Nothing comes through it now.")
PLATE_EXAMINE = ("Somewhere under the water is the stone that started this. You don't "
                 "need to see it again.")
_NOTHING_HAPPENS = "Nothing happens."
_NOTHING_TO_DISARM = "There's nothing here to disarm."

DEN_SEALED = ("The passage north ends at a stone slab now, wet around its edges. That way "
              "is closed.")

_SPILLWAY = (
    "The sluice deposited you here — wet stone, low ceiling, the sound of water "
    "draining somewhere below. The chamber is small and close. There's no way back "
    "up. The passage continues south."
)


def _here(w: World) -> bool:
    return w.here is not None and w.here.name == "FLOODING-ROOM"


def _water_line(w: World) -> str:
    risen = w.get_global("LEVER-RIGHT")
    if w.get_global("LEVER-MIDDLE"):
        return _WATER_RISEN_STILL if risen else _WATER_STILL
    return _WATER_RISEN if risen else _WATER_ENTRY


def _fire(w: World) -> None:
    w.set_global("FLOOD-FIRED", True)
    w.ways_changed("CREATURE-DEN")              # the way north is sealed now
    print(_TRIGGER)
    print(_SLAB)
    print(_URGENCY)


def handles_plate(w: World) -> bool:
    """JUMP ON / DISARM PLATE in the Flooding Room go here (verbs.py)."""
    return _here(w)


def jump_on_plate(w: World) -> None:
    print(_NOTHING_HAPPENS)


def disarm_plate(w: World) -> None:
    print(_NOTHING_TO_DISARM)


def levers_examine(w: World) -> str:
    if w.get_global("LEVER-RIGHT"):
        return LEVERS_EXAMINE + " " + _STUMP
    return LEVERS_EXAMINE


def lever_action(w: World) -> int:
    """EXAMINE any lever, or the levers: the row of three."""
    if w.prsa == "V-EXAMINE":
        print(levers_examine(w))
        return M_HANDLED
    return M_NOT_HANDLED


def sluice_action(w: World) -> int:
    if w.prsa in ("V-EXAMINE", "V-LOOK-INSIDE"):
        print(SLUICE_STOPPED if w.get_global("LEVER-MIDDLE") else SLUICE_POURING)
        return M_HANDLED
    return M_NOT_HANDLED


def _pull(w: World, lever) -> None:
    if w.get_global(lever.name):
        print(_SPENT)
        return
    w.set_global(lever.name, True)
    if lever.name == "LEVER-RIGHT":
        print(_RIGHT)
    elif lever.name == "LEVER-MIDDLE":
        print(_MIDDLE)
    else:
        print(_LEFT)
        _sweep(w)


_PAPER_RUINED = ("The thin paper didn't survive the trip. What's left of it comes apart "
                 "in your fingers.")


def _carried(w: World, obj) -> bool:
    loc = obj.location
    while loc is not None:
        if loc is w.player:
            return True
        loc = getattr(loc, "location", None)
    return False


def _sweep(w: World) -> None:
    print(_SWEPT)
    # items.md — Thin Paper: the sweep is the one thing that soaks the player.
    # Out of the world, it's back on Shamus's slate.
    paper = w.objects["THIN-PAPER"]
    if _carried(w, paper):
        w.move_object(paper, None)
        print(_PAPER_RUINED)
    w.game.enter_room(w.rooms["SPILLWAY"])


def flooding_room_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        if w.get_global("FLOOD-FIRED"):
            print(_ROOM + " " + _water_line(w))
        else:
            print(_ROOM_FIRST)
        return M_HANDLED
    if msg == M_ENTER:
        w.set_global("ARRIVED-FLOODING", True)
        return M_NOT_HANDLED
    if msg == M_BEG:
        if w.prsa == "V-PULL" and w.prso is not None and w.prso.name in (
                "LEVER-LEFT", "LEVER-MIDDLE", "LEVER-RIGHT"):
            _pull(w, w.prso)
            return M_HANDLED
        return M_NOT_HANDLED
    if msg == M_END and _here(w) and w.get_global("ARRIVED-FLOODING"):
        w.set_global("ARRIVED-FLOODING", False)
        if not w.get_global("FLOOD-FIRED"):
            _fire(w)
    return M_NOT_HANDLED


class _DenNorth(Exit):
    """Creature Den north: sealed by the slab once the player has been in."""
    def resolve(self, world):
        if world.get_global("FLOOD-FIRED"):
            return None, DEN_SEALED
        return super().resolve(world)


def spillway_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        print(_SPILLWAY)
        return M_HANDLED
    return M_NOT_HANDLED


def make_rooms(world) -> None:
    def room(name, desc, action, value):
        r = Room(name=name, desc=desc, ldesc="", value=value)
        r.set_flag(RLANDBIT)   # dark
        r.action = action
        world.register_room(r)
        return r

    room("FLOODING-ROOM", "Flooding Room", flooding_room_action, 1)   # no exits: the slab
    room("SPILLWAY", "The Spillway", spillway_action, 2)   # south → Dream Corridor (LL)
    world.rooms["CREATURE-DEN"].exits["north"] = _DenNorth(destination="FLOODING-ROOM")
