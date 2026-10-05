"""
The Flooding Room (Trap 41, upper tier) and The Spillway (mid-tier trap side).

Design: locations.md (Flooding Room, Trap Side — The Spillway), traps.md
(Trap 41), experience.md (Trap 41 disarm 5 XP), quests.md (Quest 50).

- The plate works like Trap 29's: a Medium perception check on arrival. Missed:
  stepped on unawares. Spotted with Actually Enchanted Glasses: the player
  chooses (JUMP ON PLATE / DISARM PLATE). Spotted without them: the disarm
  rolls automatically. Once spotted, the player walks around it.
- The plate opens the sluice. Two turns (any command counts): after the first,
  the warning; after the second, the player is swept one-way to the Spillway.
  The middle lever closes the sluice; the plate re-arms. Left and right levers
  are spent once pulled. Leaving south while it floods closes the sluice too.
- Disarming jams the plate for good (Quest 50's posting would go — todo.md).

State: FLOOD-PLATE-SPOTTED, FLOOD-PLATE (None | "disarmed"),
       FLOOD-TURNS (None while closed; 0, 1 while flooding), LEVER-LEFT, LEVER-RIGHT
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_BEG, M_ENTER, M_LOOK, M_END
from engine.world import Room, Exit, RLANDBIT

if TYPE_CHECKING:
    from engine.world import World

_ROOM = (
    "A low cave, the floor dipping toward the middle and slick with old silt. Three "
    "iron levers stand in a row on the north wall — left, middle, right — above a "
    "grated sluice mouth. The only way out is back south."
)
_TRAP41 = "a suspiciously clean pressure plate set into the cave floor"
_TRAP_DISARMED = "You spot {d} and are able to disarm it, neutralizing it."
_TRAP_BOTCHED = "You see {d}, but your attempt to disarm it fails miserably."
_SPOTTED = ("In the middle of the floor, one stone is cleaner than everything around "
            "it — no silt, no grime. A pressure plate.")
_FIRES = ("Something clicks underfoot. Behind the grate the sluice bangs open, and "
          "water comes through fast and cold, spreading across the floor.")
_LEFT = "The lever grinds but won't move."
_RIGHT = "The lever snaps off in your hand."
_SPENT = "You already tried that one."
_MIDDLE = ("The middle lever comes down with a heavy clunk. Behind the grate the sluice "
           "slams shut, and the water drains away through the floor.")
_WARNING = "The water is at your knees. One turn left."
_SWEPT = ("The water closes over your head and the floor drops away. The current takes "
          "you down through the sluice, turning you over in the dark, and lets go.")

_SPILLWAY = (
    "The sluice deposits you here — wet stone, low ceiling, the sound of water "
    "draining somewhere below. The chamber is small and close. There's no way back "
    "up. The passage continues south."
)


def _here(w: World) -> bool:
    return w.here is not None and w.here.name == "FLOODING-ROOM"


def _flooding(w: World) -> bool:
    return w.get_global("FLOOD-TURNS") is not None


def _fire(w: World) -> None:
    print(_FIRES)
    w.set_global("FLOOD-TURNS", 0)
    w.set_global("FLOOD-JUST-OPENED", True)


def _disarmed(w: World) -> None:
    from content.experience import award_xp
    w.set_global("FLOOD-PLATE", "disarmed")
    award_xp(w, 5 + (5 if w.globals.get("player_class") == "rogue" else 0))


def _on_arrival(w: World) -> None:
    from content.player import check_perception, roll_class_bonus
    from content.perception import MEDIUM
    if not check_perception(w, MEDIUM):
        _fire(w)                          # stepped on it unawares
        return
    w.set_global("FLOOD-PLATE-SPOTTED", True)
    w.objects["FLOOD-PLATE"].clear_flag("INVISIBLE")
    if w.globals.get("actually_enchanted_glasses_worn"):
        print(_SPOTTED)                   # revealed; the player chooses
        return
    if roll_class_bonus(w, "trap") >= MEDIUM:
        print(_TRAP_DISARMED.format(d=_TRAP41))
        _disarmed(w)
    else:
        print(_TRAP_BOTCHED.format(d=_TRAP41))
        _fire(w)


def handles_plate(w: World) -> bool:
    """JUMP ON / DISARM PLATE in the Flooding Room go here (verbs.py)."""
    return _here(w)


def jump_on_plate(w: World) -> None:
    if w.get_global("FLOOD-PLATE") == "disarmed" or _flooding(w):
        print("Nothing happens.")
    else:
        _fire(w)


def disarm_plate(w: World) -> None:
    if not w.get_global("FLOOD-PLATE-SPOTTED"):
        print("There's nothing here to disarm.")
        return
    if w.get_global("FLOOD-PLATE") == "disarmed" or _flooding(w):
        print("Nothing happens.")
        return
    from content.player import roll_class_bonus
    from content.perception import MEDIUM
    if roll_class_bonus(w, "trap") >= MEDIUM:
        print(_TRAP_DISARMED.format(d=_TRAP41))
        _disarmed(w)
    else:
        print(_TRAP_BOTCHED.format(d=_TRAP41))
        _fire(w)


def _pull(w: World, lever) -> None:
    if lever.name == "LEVER-MIDDLE":
        if _flooding(w):
            print(_MIDDLE)
            w.set_global("FLOOD-TURNS", None)
        else:
            print("Nothing happens.")
        return
    if w.get_global(lever.name):
        print(_SPENT)
        return
    w.set_global(lever.name, True)
    print(_LEFT if lever.name == "LEVER-LEFT" else _RIGHT)


def _sweep(w: World) -> None:
    print(_SWEPT)
    w.set_global("FLOOD-TURNS", None)
    w.game.enter_room(w.rooms["SPILLWAY"])


class _LeaveExit(Exit):
    """South out of the Flooding Room: the sluice shuts behind you."""
    def resolve(self, world):
        world.set_global("FLOOD-TURNS", None)
        return super().resolve(world)


def flooding_room_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        print(_ROOM)
        return M_HANDLED
    if msg == M_ENTER:
        w.set_global("ARRIVED-FLOODING", True)
        return M_NOT_HANDLED
    if msg == M_BEG:
        if w.prsa == "V-PULL" and w.prso is not None and w.prso.name.startswith("LEVER-"):
            _pull(w, w.prso)
            return M_HANDLED
        return M_NOT_HANDLED
    if msg == M_END and _here(w):
        if w.get_global("ARRIVED-FLOODING"):
            w.set_global("ARRIVED-FLOODING", False)
            if w.get_global("FLOOD-PLATE") is None and not w.get_global("FLOOD-PLATE-SPOTTED"):
                _on_arrival(w)
            w.set_global("FLOOD-JUST-OPENED", False)   # the arrival turn is the opening turn
            return M_NOT_HANDLED
        if not _flooding(w):
            return M_NOT_HANDLED
        if w.get_global("FLOOD-JUST-OPENED"):
            w.set_global("FLOOD-JUST-OPENED", False)
            return M_NOT_HANDLED
        turns = w.get_global("FLOOD-TURNS") + 1
        w.set_global("FLOOD-TURNS", turns)
        if turns == 1:
            print(_WARNING)
        else:
            _sweep(w)
    return M_NOT_HANDLED


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

    flooding = room("FLOODING-ROOM", "Flooding Room", flooding_room_action, 1)
    room("SPILLWAY", "The Spillway", spillway_action, 2)   # south → Dream Corridor (LL)
    world.rooms["CREATURE-DEN"].exits["north"] = Exit(destination="FLOODING-ROOM")
    flooding.exits["south"] = _LeaveExit(destination="CREATURE-DEN")
