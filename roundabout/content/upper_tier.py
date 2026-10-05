"""
Dungeon — Upper Tier.

Ink Corridor (Trap 45), Supply Room (Trap 17), Narrow Passageway, Idol Room
(Trap 33), Storage Area. Design: locations.md (Dungeon — Upper Tier),
traps.md (Traps 17, 33, 45), items.md.

- Every room here is dark (light.py).
- Trap 45 (Ink Corridor): Medium perception, then Medium disarm (trap roll);
  missed or botched, the player is inked. Inked (INKED) cancels the ring's
  invisibility. The inked NPC refusals and the inn bath aren't built yet.
- Trap 17 (Supply Room shelf — smoke jar, clay pot) and Trap 33 (the idol's
  pedestal; SWAP IDOL WITH SALT) are below.

State: TRAP45-DONE, INKED, HAND-CART-TAKEN
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_LOOK, M_END, M_ENTER
from engine.world import Room, Exit, RLANDBIT, NDESCBIT, TAKEBIT

if TYPE_CHECKING:
    from engine.world import World

_TRAP45 = "a near-invisible thread strung at chest height across the corridor"
_TRAP_DISARMED = "You spot {d} and are able to disarm it, neutralizing it."
_TRAP_BOTCHED = "You see {d}, but your attempt to disarm it fails miserably."
_INKED = (
    "Something snags across your chest — a thread, there and gone. Above you, "
    "something bursts. Ink comes down in a cold black sheet and doesn't stop "
    "until you're wearing all of it."
)

_STORAGE_BASE = (
    "A wide chamber, larger than expected — the dungeon opens up here before "
    "closing back down. The walls are rough, the floor uneven. "
)
_STORAGE_BOTH = "Equipment has been left here: a hand cart against one wall, a heavy support beam laid across the floor. "
_STORAGE_BEAM = "Equipment has been left here: a heavy support beam laid across the floor. "
_STORAGE_END = (
    "The east wall is solid. A passage leads south, and from somewhere down it "
    "comes the sound of water."
)


def ink_corridor_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    """Trap 45 fires the first time the player passes through."""
    if msg == M_END and not w.get_global("TRAP45-DONE"):
        w.set_global("TRAP45-DONE", True)
        from content.player import check_perception, roll_class_bonus
        from content.perception import MEDIUM
        if check_perception(w, MEDIUM):
            if roll_class_bonus(w, "trap") >= MEDIUM:
                print(_TRAP_DISARMED.format(d=_TRAP45))
                _award_disarm(w)
                return M_NOT_HANDLED
            print(_TRAP_BOTCHED.format(d=_TRAP45))
        print(_INKED)
        w.set_global("INKED", True)
        from content import chuckle
        chuckle.update_ghost_visibility(w)
    return M_NOT_HANDLED


def _award_disarm(w: World) -> None:
    """experience.md — Trap 45: 5 XP; Rogues +5 per trap disarmed."""
    from content.experience import award_xp
    award_xp(w, 5 + (5 if w.globals.get("player_class") == "rogue" else 0))


def storage_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        cart_here = w.objects["HAND-CART"].location is w.here
        print(_STORAGE_BASE + (_STORAGE_BOTH if cart_here else _STORAGE_BEAM) + _STORAGE_END)
        return M_HANDLED
    return M_NOT_HANDLED


# ---------------------------------------------------------------------------
# Trap 17 — Smoke Bomb Cache (Supply Room): Medium perception, Medium disarm,
# on the first entry. Fired: 1 heart smoke damage. Either way the smoke jar
# and the small clay pot are then on the shelf (traps.md, locations.md).
# ---------------------------------------------------------------------------

_TRAP17 = "an unstable arrangement of clay pots, one of them the trigger"
_SMOKE = (
    "Your foot catches on something in the floor. On the shelf beside you a clay "
    "pot tips, falls and bursts, and the room fills with choking grey smoke. When "
    "it clears, your eyes are streaming and your chest aches."
)
_SUPPLY_BASE = (
    "A storage room, wide and low. Shelves run along three walls — some collapsed, "
    "most still holding whatever was left here when this place was abandoned.\n"
    "The contents are various: tools, containers, materials that suggest someone "
    "was keeping this dungeon supplied. It smells of old wood and something "
    "chemical underneath."
)
_SUPPLY_SPOTTED = (
    "One of the shelves near the entrance has a trip mechanism built into the "
    "floor in front of it — barely visible. Whatever it triggers, it isn't subtle."
)


def supply_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        print(_SUPPLY_BASE)
        if w.get_global("TRAP17-SPOTTED"):
            print(_SUPPLY_SPOTTED)
        return M_HANDLED
    if msg == M_END and not w.get_global("TRAP17-DONE"):
        w.set_global("TRAP17-DONE", True)
        from content.player import check_perception, roll_class_bonus
        from content.perception import MEDIUM
        fired = True
        if check_perception(w, MEDIUM):
            w.set_global("TRAP17-SPOTTED", True)
            if roll_class_bonus(w, "trap") >= MEDIUM:
                print(_TRAP_DISARMED.format(d=_TRAP17))
                from content.experience import award_xp
                award_xp(w, 3 + (5 if w.globals.get("player_class") == "rogue" else 0))
                fired = False
            else:
                print(_TRAP_BOTCHED.format(d=_TRAP17))
        if fired:
            print(_SMOKE)
        for name in ("SMOKE-JAR", "SMALL-CLAY-POT"):
            w.objects[name].clear_flag("INVISIBLE")
        if fired:
            from content.combat import _take_damage
            _take_damage(w, 1)
    return M_NOT_HANDLED


# ---------------------------------------------------------------------------
# Trap 33 — Weight-Sensitive Pedestal (Idol Room). Medium perception (every
# visit until found) shows the plate. SWAP IDOL WITH SALT is the safe swap
# (5 XP). Taking the idol without it seals the north doorway; the way south
# stays open, so the crowbar can be fetched — PRY DOOR, Medium strength.
# ---------------------------------------------------------------------------

_IDOL_BASE = (
    "The room is small and oddly formal — the stonework here is more deliberate "
    "than the corridors outside, the walls smoothed, the floor level.\n"
    "{centre} The room has the feeling of something that has been waiting for "
    "someone to make a mistake."
)
_CENTRE_IDOL = "At the center, a stone pedestal holds a figurine."
_CENTRE_EMPTY = "At the center stands a stone pedestal."
_IDOL_SPOTTED = (
    "The pedestal has a pressure plate built into its surface — the figurine's "
    "weight is the only thing keeping it inactive."
)
_SWAPPED = (
    "You set the sack of salt on the pedestal and lift the idol away in the same "
    "motion. The pedestal doesn't so much as twitch."
)
_NO_SWAP = "You'd need something of the same weight to put in its place."
SALT_ON_PEDESTAL = "A sack of salt sits on the pedestal where the idol was."
_SLAM = (
    "You lift the idol. Somewhere under the pedestal something clicks, and a slab "
    "of stone drops into the doorway with a boom you feel in your teeth. The way "
    "out is gone."
)
SLAB_BLOCKS = "The stone slab fills the doorway. It isn't moving."
_PRIED = (
    "You work the crowbar into the gap and heave. The slab grinds up a hand's "
    "width, then enough. You squeeze through before it changes its mind."
)
_PRY_FAILED = "The crowbar bites, the slab shifts a fraction, and settles back. Not this time."


def idol_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_ENTER and not w.get_global("IDOL-PLATE-SPOTTED"):
        from content.player import check_perception
        from content.perception import MEDIUM
        if check_perception(w, MEDIUM):
            w.set_global("IDOL-PLATE-SPOTTED", True)
    if msg == M_LOOK:
        centre = _CENTRE_IDOL if _idol_on_pedestal(w) else _CENTRE_EMPTY
        print(_IDOL_BASE.format(centre=centre))
        if w.get_global("IDOL-PLATE-SPOTTED"):
            print(_IDOL_SPOTTED)
        return M_HANDLED
    return M_NOT_HANDLED


def _idol_on_pedestal(w: World) -> bool:
    return w.objects["IDOL"].location is w.rooms["IDOL-ROOM"]


def take_idol(w: World) -> bool:
    """TAKE IDOL. Off the pedestal without a swap: the north doorway seals.
    Returns True if handled here."""
    idol = w.objects["IDOL"]
    if not _idol_on_pedestal(w):
        return False
    w.move_object(idol, w.player)
    idol.clear_flag(NDESCBIT)
    w.set_global("IDOL-DOOR-SHUT", True)
    print(_SLAM)
    return True


def swap_idol(w: World) -> None:
    """SWAP IDOL WITH SALT — the safe swap (Trap 33 disarm, 5 XP)."""
    idol, salt = w.objects["IDOL"], w.objects["SACK-OF-SALT"]
    if w.here is None or w.here.name != "IDOL-ROOM" or not _idol_on_pedestal(w):
        print("There's nothing here to swap.")
        return
    if salt not in w.player.contents:
        print(_NO_SWAP)
        return
    w.move_object(salt, w.here)
    salt.fdesc = SALT_ON_PEDESTAL
    salt.touched = False
    salt.clear_flag(TAKEBIT)              # it's holding the pedestal down now
    w.move_object(idol, w.player)
    idol.clear_flag(NDESCBIT)
    w.set_global("IDOL-SWAPPED", True)
    print(_SWAPPED)
    from content.experience import award_xp
    award_xp(w, 5 + (5 if w.globals.get("player_class") == "rogue" else 0))


def pry_idol_door(w: World) -> None:
    """PRY DOOR — the slab over the north doorway; crowbar + Medium strength."""
    if not w.get_global("IDOL-DOOR-SHUT"):
        print("You can't get any leverage on that.")
        return
    if w.objects["CROWBAR"] not in w.player.contents:
        print("You can't get any leverage on that.")
        return
    from content.player import check_strength
    from content.perception import MEDIUM
    if check_strength(w, MEDIUM):
        w.set_global("IDOL-DOOR-SHUT", False)
        print(_PRIED)
    else:
        print(_PRY_FAILED)


class _IdolNorthExit(Exit):
    """Idol Room north: shut by the slab once Trap 33 fires, until pried."""

    def resolve(self, world):
        if world.get_global("IDOL-DOOR-SHUT"):
            return None, SLAB_BLOCKS
        return super().resolve(world)


def make_rooms(world) -> None:
    def room(name, desc, ldesc):
        r = Room(name=name, desc=desc, ldesc=ldesc, value=1)
        r.set_flag(RLANDBIT)   # no ONBIT — the dungeon is dark
        world.register_room(r)
        return r

    ink = room(
        "INK-CORRIDOR", "Ink Corridor",
        "The corridor is narrow and plain — bare stone, low ceiling, torch "
        "brackets empty. It feels like an entrance to something, which it is. "
        "The passage splits ahead — west, east, and on to the south.",
    )
    supply = room(
        "SUPPLY-ROOM", "Supply Room",
        "A storage room, wide and low. Shelves run along three walls — some "
        "collapsed, most still holding whatever was left here when this place "
        "was abandoned. The contents are various: tools, containers, materials "
        "that suggest someone was keeping this dungeon supplied. It smells of "
        "old wood and something chemical underneath.",
    )
    narrow = room(
        "NARROW-PASSAGEWAY", "Narrow Passageway",
        "A short passage, plain stone, lower-ceilinged than the corridor behind "
        "you. It goes south and ends at a doorway. The kind of passage that "
        "exists to connect two places and has no opinion about either of them.",
    )
    idol = room(
        "IDOL-ROOM", "Idol Room",
        "The room is small and oddly formal — the stonework here is more "
        "deliberate than the corridors outside, the walls smoothed, the floor "
        "level. At the center, a stone pedestal holds a figurine. The room has "
        "the feeling of something that has been waiting for someone to make a "
        "mistake.",
    )
    storage = room("STORAGE-AREA", "Storage Area", "")

    world.rooms["DUNGEON-ENTRANCE"].exits["south"] = Exit(destination="INK-CORRIDOR")
    ink.exits.update(north=Exit(destination="DUNGEON-ENTRANCE"), west=Exit(destination="SUPPLY-ROOM"),
                     east=Exit(destination="STORAGE-AREA"), south=Exit(destination="NARROW-PASSAGEWAY"))
    supply.exits["east"] = Exit(destination="INK-CORRIDOR")
    narrow.exits.update(north=Exit(destination="INK-CORRIDOR"), south=Exit(destination="IDOL-ROOM"))
    # Idol Room south → Combat Room comes with batch 2
    idol.exits["north"] = _IdolNorthExit(destination="NARROW-PASSAGEWAY")
    # Storage Area south → Collapsed Aqueduct is wired in content/aqueduct.py
    storage.exits["west"] = Exit(destination="INK-CORRIDOR")

    ink.action = ink_corridor_action
    storage.action = storage_action
    supply.action = supply_action
    idol.action = idol_action
    supply.ldesc = ""     # supply_action / idol_action (perception variants)
    idol.ldesc = ""
