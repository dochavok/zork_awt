"""
The Keeper's Chamber (Church of All) and the consecrated silver stake.

Design: locations.md (Church of All — Keeper's Chamber door; Keeper's Chamber),
items.md (Keeper's Key Ring, Holy Water, Consecrated Silver Stake),
ring-rituals.md (Werewolf's Amulet, Step 4).

- Nave west door: UNLOCK DOOR WITH KEYS (the keys stay in the lock; the door
  stays open). WEST / OPEN DOOR while locked: "The door is locked."
- Keeper's Chamber (lit): vial of holy water on the desk; the Keeper's note is
  readable, not takeable.
- POUR HOLY WATER ON STAKE (both carried, anywhere): the vial is used up and
  the silver stake becomes the consecrated silver stake.

State: KEEPER-DOOR-UNLOCKED, HOLY-WATER-TAKEN, STAKE-CONSECRATED
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_BEG, M_LOOK
from engine.world import Room, Exit, ONBIT, RLANDBIT, NDESCBIT

if TYPE_CHECKING:
    from engine.world import World

_DOOR_LOCKED = (
    "In the west wall, a narrow door of dark wood is shut tight, a heavy lock "
    "beneath the latch."
)
_DOOR_OPEN = (
    "The narrow door in the west wall stands open, a ring of keys hanging from "
    "its lock."
)
_UNLOCKED = (
    "The third key you try is the right one. The lock gives with a dry click, and "
    "the door swings inward on a small, plain room. You leave the keys hanging in "
    "the lock."
)
_LOCKED = "The door is locked."
_WRONG_KEY = "That key doesn't fit."
_NO_KEY = "You don't have the key to it."

_CHAMBER = (
    "A small room, plainly kept. A narrow bed, a writing desk, a shelf of "
    "religious texts. The kind of room that belongs to someone who doesn't spend "
    "much time in it."
)
_DESK_VIAL = (
    " On the desk: a vial of clear liquid, and a note in a careful hand. Whatever "
    "the Keeper was preparing for, he prepared it here."
)
_DESK_NOTE = " On the desk: a note in a careful hand."
_NOTE_STAYS = "You leave it where the Keeper left it."

_POURED = (
    "You unstop the vial and pour it slowly along the stake, end to end. The "
    "silver drinks it — there's no other word for it. When the last drop is gone, "
    "the metal holds a faint, steady sheen, as if lit from somewhere you can't see."
)
_NO_WASTE = "You'd rather not waste it."
_CONSECRATED = (
    "A slim stake of solid silver, the point still sharp. It holds a faint, "
    "steady sheen that has nothing to do with the light."
)


# ---------------------------------------------------------------------------
# Nave: the west door
# ---------------------------------------------------------------------------

def nave_line(w: World) -> str:
    """Last line of the Nave description."""
    return _DOOR_OPEN if w.get_global("KEEPER-DOOR-UNLOCKED") else _DOOR_LOCKED


_nave_base = ""   # the Nave's own description, taken over from chuckle.py


def nave_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        print(_nave_base)
        print(nave_line(w))
        return M_HANDLED
    return M_NOT_HANDLED


def unlock_door(w: World) -> None:
    if w.get_global("KEEPER-DOOR-UNLOCKED"):
        print("It's already unlocked. The keys are still in the lock.")
        return
    keys = w.objects["KEY-RING"]
    if w.prsi is not None and w.prsi is not keys:
        print(_WRONG_KEY)
        return
    if keys not in w.player.contents:
        print(_NO_KEY)
        return
    print(_UNLOCKED)
    w.set_global("KEEPER-DOOR-UNLOCKED", True)
    w.move_object(keys, w.objects["KEEPER-DOOR"])   # stays in the lock


def open_door(w: World) -> None:
    print("It's already open." if w.get_global("KEEPER-DOOR-UNLOCKED") else _LOCKED)


class _KeeperDoor(Exit):
    def resolve(self, world):
        if not world.get_global("KEEPER-DOOR-UNLOCKED"):
            return None, _LOCKED
        return super().resolve(world)


# ---------------------------------------------------------------------------
# Keeper's Chamber
# ---------------------------------------------------------------------------

def chamber_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        print(_CHAMBER + (_DESK_NOTE if w.get_global("HOLY-WATER-TAKEN") else _DESK_VIAL))
        return M_HANDLED
    if msg != M_BEG:
        return M_NOT_HANDLED
    if w.prsa == "V-TAKE" and w.prso is w.objects["KEEPER-NOTE"]:
        print(_NOTE_STAYS)
        return M_HANDLED
    if w.prsa == "V-TAKE" and w.prso is w.objects["HOLY-WATER"] \
            and not w.get_global("HOLY-WATER-TAKEN"):
        w.set_global("HOLY-WATER-TAKEN", True)
        w.prso.clear_flag(NDESCBIT)    # the room description no longer covers it
    return M_NOT_HANDLED


# ---------------------------------------------------------------------------
# POUR HOLY WATER ON STAKE
# ---------------------------------------------------------------------------

def pour(w: World) -> bool:
    """POUR with the holy water. True if handled here."""
    water = w.objects["HOLY-WATER"]
    if w.prso is not water:
        return False
    stake = w.objects["SILVER-STAKE"]
    held = w.player.contents
    if water not in held or w.prsi is not stake or stake not in held \
            or w.get_global("STAKE-CONSECRATED"):
        print(_NO_WASTE)
        return True
    print(_POURED)
    w.move_object(water, None)          # used up
    w.set_global("STAKE-CONSECRATED", True)
    stake.desc = "consecrated silver stake"
    stake.ldesc = _CONSECRATED
    stake.adjectives = list(stake.adjectives) + ["consecrated"]
    return True


# ---------------------------------------------------------------------------
# Rooms
# ---------------------------------------------------------------------------

def make_rooms(world) -> None:
    chamber = Room(name="KEEPERS-CHAMBER", desc="Keeper's Chamber", ldesc="", value=1)
    chamber.set_flag(ONBIT)      # part of the church — not on the dark room list
    chamber.set_flag(RLANDBIT)
    world.register_room(chamber)

    global _nave_base
    nave = world.rooms["CHURCH-NAVE"]
    _nave_base, nave.ldesc = nave.ldesc, ""   # an ldesc would bypass the action
    nave.exits["west"] = _KeeperDoor(destination="KEEPERS-CHAMBER")
    nave.action = nave_action
    chamber.exits["east"] = Exit(destination="CHURCH-NAVE")
    chamber.action = chamber_action
