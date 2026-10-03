"""
Combat Room, the Warden, and the Creature Den (upper tier, batch 2).

Design: locations.md (Combat Room, Creature Den), traps.md (Trap 29),
mechanics.md (Warden: 2d10, 5 hearts), experience.md (Warden 12 XP; Warriors
+10 per kill; Trap 29 disarm 3 XP).

- The Trap 29 plate is at the Combat Room's north entrance. Arriving
  unawares steps on it. A Medium perception check spots it; with Actually
  Enchanted Glasses it's revealed and the player chooses (JUMP ON PLATE or
  DISARM PLATE); otherwise spotting it rolls the disarm automatically.
- The plate firing rings the bell and opens the Den door; the Warden comes
  out. One round per KILL WARDEN. A disarmed plate keeps the door shut until
  JUMP ON PLATE. The door stays open after the Warden is dead.
- The Flooding Room (north of the Den, Trap 41) is deferred.

State: PLATE-SPOTTED, PLATE-STATE (None | "disarmed" | "fired"),
       WARDEN-OUT, WARDEN-HEARTS, WARDEN-DEAD
"""

from __future__ import annotations
import random
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_ENTER, M_LOOK, M_END
from engine.world import Room, Exit, RLANDBIT

if TYPE_CHECKING:
    from engine.world import World

WARDEN_HEARTS = 5
WARDEN_DICE = (2, 10)

_ROOM_BASE = (
    "A long, low room, wider than it is deep, the floor scarred and the walls "
    "pocked with old damage. "
)
_ROOM_SHUT = "At the east end a heavy door is set into the stone, shut. "
_ROOM_OPEN = "At the east end the heavy door stands open. "
_ROOM_END = "Whatever happened in here happened more than once."

_TRAP29 = "a pressure plate set into the corridor floor"
_TRAP_DISARMED = "You spot {d} and are able to disarm it, neutralizing it."
_TRAP_BOTCHED = "You see {d}, but your attempt to disarm it fails miserably."
_PLATE_SPOTTED = (
    "Just inside the doorway, one flagstone sits a fraction higher than the "
    "rest — a pressure plate."
)
_BELL = (
    "Somewhere behind the heavy door, a bell rings — once, flat and loud. "
    "Something on the other side moves."
)
_WARDEN_EMERGES = (
    "The door at the east end grinds open. The thing that comes through it was "
    "a guard once — the scraps of a uniform still hang off it — but whatever "
    "it is now is mostly reach, teeth, and intent. The Warden."
)
WARDEN_PRESENCE = "The Warden stands between you and the open door, swaying, waiting for you to move."
_ROUND_WON = "You land a solid blow. The Warden staggers, and comes on anyway."
_ROUND_LOST = "The Warden's reach finds you. You take a hit."
_ROUND_TIE = "You trade blows. Both of you feel it."
_WARDEN_DIES = (
    "The Warden goes down hard and doesn't get up. Something rolls from its "
    "grip and clatters across the floor — a lantern, unlit, its glass faintly green."
)


class _DenDoor(Exit):
    """Combat Room east: shut until the plate fires."""

    def resolve(self, world):
        if world.get_global("PLATE-STATE") != "fired":
            return None, "The door is shut."
        return super().resolve(world)


def combat_room_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        door = _ROOM_OPEN if w.get_global("PLATE-STATE") == "fired" else _ROOM_SHUT
        print(_ROOM_BASE + door + _ROOM_END)
        return M_HANDLED
    if msg == M_ENTER:
        w.set_global("ARRIVED-COMBAT", True)
        if w.get_global("WARDEN-OUT") and not w.get_global("WARDEN-DEAD"):
            # Fleeing and coming back: the Warden is at full hearts again
            w.set_global("WARDEN-HEARTS", WARDEN_HEARTS)
    elif msg == M_END and w.get_global("ARRIVED-COMBAT"):
        w.set_global("ARRIVED-COMBAT", False)
        if w.get_global("PLATE-STATE") is None and not w.get_global("PLATE-SPOTTED"):
            _plate_on_arrival(w)
    return M_NOT_HANDLED


def _plate_on_arrival(w: World) -> None:
    from content.player import check_perception, roll_class_bonus
    from content.perception import MEDIUM
    if not check_perception(w, MEDIUM):
        _fire_plate(w)                   # stepped on it unawares
        return
    w.set_global("PLATE-SPOTTED", True)
    w.objects["PRESSURE-PLATE"].clear_flag("INVISIBLE")
    if w.globals.get("actually_enchanted_glasses_worn"):
        print(_PLATE_SPOTTED)            # revealed; the player chooses
        return
    if roll_class_bonus(w, "trap") >= MEDIUM:
        print(_TRAP_DISARMED.format(d=_TRAP29))
        _disarmed(w)
    else:
        print(_TRAP_BOTCHED.format(d=_TRAP29))
        _fire_plate(w)


def _disarmed(w: World) -> None:
    from content.experience import award_xp
    w.set_global("PLATE-STATE", "disarmed")
    award_xp(w, 3 + (5 if w.globals.get("player_class") == "rogue" else 0))


def _fire_plate(w: World) -> None:
    w.set_global("PLATE-STATE", "fired")
    print(_BELL)
    print(_WARDEN_EMERGES)
    w.set_global("WARDEN-OUT", True)
    w.set_global("WARDEN-HEARTS", WARDEN_HEARTS)
    w.move_object(w.objects["WARDEN"], w.rooms["COMBAT-ROOM"])


def jump_on_plate(w: World) -> None:
    if w.here is None or w.here.name != "COMBAT-ROOM":
        print("There's nothing here to jump on.")
    elif w.get_global("PLATE-STATE") == "fired":
        print("Nothing happens.")
    else:
        _fire_plate(w)


def disarm_plate(w: World) -> None:
    if w.here is None or w.here.name != "COMBAT-ROOM" or not w.get_global("PLATE-SPOTTED"):
        print("There's nothing here to disarm.")
        return
    if w.get_global("PLATE-STATE") is not None:
        print("Nothing happens.")
        return
    from content.player import roll_class_bonus
    from content.perception import MEDIUM
    if roll_class_bonus(w, "trap") >= MEDIUM:
        print(_TRAP_DISARMED.format(d=_TRAP29))
        _disarmed(w)
    else:
        print(_TRAP_BOTCHED.format(d=_TRAP29))
        _fire_plate(w)


def fight_round(w: World) -> None:
    """KILL WARDEN — one round. Higher roll hits for 1 heart; ties hit both."""
    from content.player import roll
    from content.combat import _take_damage
    g = w.globals
    mine = roll(w)
    his = sum(random.randint(1, WARDEN_DICE[1]) for _ in range(WARDEN_DICE[0]))
    hearts = int(g.get("WARDEN-HEARTS", WARDEN_HEARTS))
    if mine > his:
        print(_ROUND_WON)
        hearts -= 1
    elif his > mine:
        print(_ROUND_LOST)
        _take_damage(w, 1)
    else:
        print(_ROUND_TIE)
        hearts -= 1
        _take_damage(w, 1)
    g["WARDEN-HEARTS"] = hearts
    if hearts <= 0 and not w.get_global("GAME-OVER"):
        _warden_dies(w)


def _warden_dies(w: World) -> None:
    from content.combat import award_combat_xp
    print(_WARDEN_DIES)
    w.set_global("WARDEN-DEAD", True)
    w.set_global("WARDEN-OUT", False)
    w.move_object(w.objects["WARDEN"], None)
    w.move_object(w.objects["GUARDIANS-LANTERN"], w.rooms["COMBAT-ROOM"])
    award_combat_xp(w, "warden")


def make_rooms(world) -> None:
    combat = Room(name="COMBAT-ROOM", desc="Combat Room", ldesc="", value=1)
    combat.set_flag(RLANDBIT)
    world.register_room(combat)
    den = Room(
        name="CREATURE-DEN", desc="Creature Den", value=1,
        ldesc=("A low den that stinks of old straw and older meat. Bones are piled "
               "in one corner with a care that's somehow worse than if they'd been "
               "scattered. A passage leads on to the north."),
    )
    den.set_flag(RLANDBIT)
    world.register_room(den)

    world.rooms["IDOL-ROOM"].exits["south"] = Exit(destination="COMBAT-ROOM")
    # Combat Room south → Prayer Alcove comes with batch 3
    combat.exits.update(north=Exit(destination="IDOL-ROOM"),
                        east=_DenDoor(destination="CREATURE-DEN"))
    # Creature Den north → Flooding Room (Trap 41) is deferred
    den.exits["west"] = Exit(destination="COMBAT-ROOM")

    combat.action = combat_room_action
