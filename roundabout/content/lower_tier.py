"""
Dungeon lower tier, west end: Lower Crypt, Thermal Vent Room, The Encampment
(Pile of Rubble itself is in content/mid_tier.py).

Design: locations.md (Lower Crypt, The Encampment, Thermal Vent Room),
items.md (Keeper's Key Ring, Fire Clay), traps.md (Trap 5 — inert pendulum),
mechanics.md (LOOK UP).

- Lower Crypt: the Keeper's skeleton under the inert pendulum; TAKE KEYS.
  The skeleton, emerald seal and blade are scenery; the seal can't be taken.
- Thermal Vent Room: LOOK UP (or LOOK AT CEILING) reveals the fire clay.
  No perception check. Anywhere else LOOK UP is a plain LOOK.
  LOOK AT CEILING parses as EXAMINE CEILING (the VENT-CEILING scenery).
- The Encampment: lore only.

State: CLAY-FOUND
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_BEG
from engine.world import Room, Exit, RLANDBIT

if TYPE_CHECKING:
    from engine.world import World

_CRYPT = (
    "A rough cave, low-ceilinged and close. A pendulum blade hangs motionless "
    "from the ceiling — triggered long ago, dried blood on the edge. Beneath it, "
    "a skeleton in robes. Whatever the Keeper came down here to do, this is as "
    "far as he got."
)
_ENCAMPMENT = (
    "The camp is old but not abandoned — abandoned implies a choice. Bedrolls "
    "still laid out. Equipment set down mid-use. Journals open to pages no one "
    "finished. Whatever happened here, no one saw it coming."
)
_VENT = (
    "A dead end, and a warm one. Heat rises from fissures in the floor, faint but "
    "steady, and the air smells of hot stone. The only way out is back south."
)
_CLAY_SEEN = (
    "Above you, the rock bulges into a low overhang. Pressed into its underside "
    "is a seam of reddish clay, warm and still soft."
)
_CLAY_GONE = "The overhang is bare where the clay was."
_SEAL_STAYS = "It's the Keeper's. You leave it with him."


def look_up(w: World) -> None:
    """LOOK UP / LOOK AT CEILING: the fire clay in the Thermal Vent Room."""
    if w.here is None or w.here.name != "THERMAL-VENT-ROOM":
        from content.verbs import v_look
        v_look(w)
        return
    clay = w.objects["FIRE-CLAY"]
    if w.get_global("CLAY-FOUND") and clay.location is not w.here:
        print(_CLAY_GONE)
        return
    print(_CLAY_SEEN)
    w.set_global("CLAY-FOUND", True)
    clay.clear_flag("INVISIBLE")


def ceiling_action(w: World) -> int:
    """LOOK AT CEILING parses as EXAMINE CEILING — same as LOOK UP."""
    if w.prsa == "V-EXAMINE":
        look_up(w)
        return M_HANDLED
    return M_NOT_HANDLED


def crypt_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_BEG and w.prsa == "V-TAKE" and w.prso is w.objects["KEEPER-SEAL"]:
        print(_SEAL_STAYS)
        return M_HANDLED
    return M_NOT_HANDLED


def make_rooms(world) -> None:
    def room(name, desc, ldesc):
        r = Room(name=name, desc=desc, ldesc=ldesc, value=2)
        r.set_flag(RLANDBIT)   # dark
        world.register_room(r)
        return r

    crypt = room("LOWER-CRYPT", "Lower Crypt", _CRYPT)
    vent = room("THERMAL-VENT-ROOM", "Thermal Vent Room", _VENT)
    camp = room("LOWER-ENCAMPMENT", "The Encampment", _ENCAMPMENT)

    rubble = world.rooms["PILE-OF-RUBBLE"]
    # Pile of Rubble east → Antechamber is wired in content/still_den.py
    rubble.exits.update(north=Exit(destination="LOWER-CRYPT"), south=Exit(destination="LOWER-ENCAMPMENT"))
    crypt.exits.update(south=Exit(destination="PILE-OF-RUBBLE"), north=Exit(destination="THERMAL-VENT-ROOM"))
    vent.exits.update(south=Exit(destination="LOWER-CRYPT"))
    camp.exits.update(north=Exit(destination="PILE-OF-RUBBLE"))

    crypt.action = crypt_action
