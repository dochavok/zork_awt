"""
Combat Room, the Warden, and the Creature Den (upper tier, batch 2).

Design: locations.md (Combat Room, Creature Den), traps.md (Trap 29),
mechanics.md (Warden: 3d10, 5 hearts), experience.md (Warden XP; Warriors
+10 per kill).

- The Trap 29 plate fires the first time the player enters the Combat Room,
  from either side (redesigned 2026-10-14: no spotting, no disarm). The bell
  rings, the door begins to open, a pause, and the Warden comes out. One
  round per KILL WARDEN. The door stays open from then on.
- The Warden blocks EAST while he lives and strikes at anyone who tries;
  NORTH and SOUTH are free. Invisible, the player slips past.
- The flagstone is scenery, examine only.
- The Flooding Room (north of the Den, Trap 41) is in content/flooding.py.

State: PLATE-STATE (None | "fired"), WARDEN-OUT, WARDEN-HEARTS, WARDEN-DEAD
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_ENTER, M_LOOK, M_END
from engine.world import Room, Exit, RLANDBIT

if TYPE_CHECKING:
    from engine.world import World

WARDEN_HEARTS = 5
WARDEN_DICE = (3, 10)   # raised from 2d10 2026-10-12: it barely landed at Level 5

_ROOM_BASE = (
    "A long, low room, wider than it is deep, the floor scarred and the walls "
    "pocked with old damage. "
)
_ROOM_SHUT = "At the east end a heavy door is set into the stone, shut. "
_ROOM_OPEN = "At the east end the heavy door stands open. "
_ROOM_EXITS = "Doorways lead north and south. "
_ROOM_END = "Whatever happened in here happened more than once."

_TRIGGER = (
    "As you enter the room, a flagstone shifts under your foot and sinks with "
    "a heavy click. For a moment nothing happens, and that's somehow worse."
)
_BELL = (
    "Somewhere behind the heavy door, a bell rings — once, flat and loud. "
    "Something on the other side moves. Then, slowly, the door at the east "
    "end begins to grind open."
)
_WARDEN_EMERGES = (
    "The door swings the rest of the way. The thing that comes through it was "
    "a guard once — the scraps of a uniform still hang off it — but whatever "
    "it is now is mostly reach, teeth, and intent. The Warden."
)
PLATE_EXAMINE = (
    "One flagstone sits a finger's width lower than the rest. You found it "
    "the usual way."
)
WARDEN_BLOCKS = "The Warden is between you and that door, and it means to stay there."
_DODGE = "Its reach rakes the air where you were a heartbeat ago."
_SLIP_PAST = (
    "The Warden's head turns at something it can't see. You're past it and "
    "through the door before it decides what."
)
DOOR_EXAMINE = (
    "The heavy door stands open on the Creature Den. From this side you can "
    "see it was never meant to be opened from here."
)
_DOOR_OPEN = "It's already open."
_DOOR_WONT_CLOSE = "It won't budge. Whatever opened it isn't letting go."
_NOTHING_HAPPENS = "Nothing happens."
_NOTHING_TO_DISARM = "There's nothing here to disarm."
WARDEN_PRESENCE = "The Warden stands between you and the open door, swaying, waiting for you to move."
# A won round, by the Warden's hearts left after it (TODO #30); the killing blow
# takes the last line, then _WARDEN_DIES
_ROUND_WON = {
    4: "You land a solid blow. The Warden staggers, and comes on anyway.",
    3: "Another blow lands. Something in the Warden cracks, and it comes on anyway.",
    2: "You land a blow. The Warden is slower to straighten this time.",
    1: "The Warden reels. It's barely holding together.",
}
_ROUND_LOST = "The Warden's reach finds you. You take a hit."
_ROUND_TIE = "You trade blows. Both of you feel it."
_WARDEN_DIES = (
    "The Warden goes down hard and doesn't get up. Something rolls from its "
    "grip and clatters across the floor — a lantern, unlit, its glass faintly green."
)


class _DenDoor(Exit):
    """Combat Room east: the Warden blocks it while he lives, and strikes at
    anyone who tries (one roll; only he can hurt). Invisible, the player
    slips past (the Chuckle House rule)."""

    def resolve(self, world):
        if world.get_global("WARDEN-OUT") and not world.get_global("WARDEN-DEAD"):
            from content.chuckle import _visible
            if not _visible(world):
                room, _ = super().resolve(world)
                return room, _SLIP_PAST
            print(WARDEN_BLOCKS)
            _strike(world)
            return None, None
        return super().resolve(world)


def _strike(w: World) -> None:
    from content import combat
    if combat.player_roll(w) > combat._enemy_roll(WARDEN_DICE):
        print(_DODGE)
    else:                                       # lost or tied: he hits
        print(_ROUND_LOST)
        combat.take_damage(w, 1)


def combat_room_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        door = _ROOM_OPEN if w.get_global("PLATE-STATE") == "fired" else _ROOM_SHUT
        print(_ROOM_BASE + door + _ROOM_EXITS + _ROOM_END)
        return M_HANDLED
    if msg == M_ENTER:
        w.set_global("ARRIVED-COMBAT", True)
        if w.get_global("WARDEN-OUT") and not w.get_global("WARDEN-DEAD"):
            # Fleeing and coming back: the Warden is at full hearts again
            w.set_global("WARDEN-HEARTS", WARDEN_HEARTS)
    elif msg == M_END and w.get_global("ARRIVED-COMBAT"):
        w.set_global("ARRIVED-COMBAT", False)
        if w.get_global("PLATE-STATE") != "fired":   # an old save may say "disarmed"
            _fire_plate(w)
    return M_NOT_HANDLED


def _fire_plate(w: World) -> None:
    from content.char_create import _pause
    w.set_global("PLATE-STATE", "fired")
    w.ways_changed("COMBAT-ROOM")              # the Den door is open now
    print(_TRIGGER)
    print(_BELL)
    _pause()
    print(_WARDEN_EMERGES)
    w.set_global("WARDEN-OUT", True)
    w.set_global("WARDEN-HEARTS", WARDEN_HEARTS)
    w.move_object(w.objects["WARDEN"], w.rooms["COMBAT-ROOM"])


_DEN_BASE = (
    "A low den that stinks of old straw and older meat. Bones are piled in one "
    "corner with a care that's somehow worse than if they'd been scattered. "
)
_DEN_NORTH = "A passage leads on to the north; the combat room is back through the door to the west."
_DEN_SEALED = "The combat room is back through the door to the west."


def den_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    """The Den loses its way north once the Flooding Room's slab is down."""
    if msg == M_LOOK:
        print(_DEN_BASE + (_DEN_SEALED if w.get_global("FLOOD-FIRED") else _DEN_NORTH))
        return M_HANDLED
    return M_NOT_HANDLED


def den_door_action(w: World) -> int:
    """The Den door: open from the plate's first firing on (the player never
    gets a turn with it shut)."""
    if w.prsa == "V-OPEN":
        print(_DOOR_OPEN)
        return M_HANDLED
    if w.prsa == "V-CLOSE":
        print(_DOOR_WONT_CLOSE)
        return M_HANDLED
    return M_NOT_HANDLED


def jump_on_plate(w: World) -> None:
    if w.here is None or w.here.name != "COMBAT-ROOM":
        print("There's nothing here to jump on.")
    else:
        print(_NOTHING_HAPPENS)                # the flagstone is spent


def disarm_plate(w: World) -> None:
    print(_NOTHING_TO_DISARM)


def fight_round(w: World) -> None:
    """KILL WARDEN — one round (content/combat.py)."""
    from content import combat
    g = w.globals
    hearts = int(g.get("WARDEN-HEARTS", WARDEN_HEARTS))
    won = _ROUND_WON[min(4, max(1, hearts - 1))]
    hearts -= combat.fight_round(w, WARDEN_DICE, won, _ROUND_LOST, _ROUND_TIE)
    g["WARDEN-HEARTS"] = hearts
    if hearts <= 0 and not w.get_global("GAME-OVER"):
        _warden_dies(w)


def fireball_hit(w: World) -> None:
    """CAST FIREBALL at the Warden: 1 heart, no roll, no strike back."""
    hearts = int(w.globals.get("WARDEN-HEARTS", WARDEN_HEARTS)) - 1
    w.globals["WARDEN-HEARTS"] = hearts
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
    den = Room(name="CREATURE-DEN", desc="Creature Den", value=1, ldesc="")
    den.set_flag(RLANDBIT)
    den.action = den_action
    world.register_room(den)

    world.rooms["IDOL-ROOM"].exits["south"] = Exit(destination="COMBAT-ROOM")
    # Combat Room south → Prayer Alcove comes with batch 3
    combat.exits.update(north=Exit(destination="IDOL-ROOM"),
                        east=_DenDoor(destination="CREATURE-DEN"))
    # Creature Den north → Flooding Room (Trap 41): content/flooding.py
    den.exits["west"] = Exit(destination="COMBAT-ROOM")

    combat.action = combat_room_action
