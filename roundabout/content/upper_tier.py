"""
Dungeon — Upper Tier (built in batches as section I1 needs it).

Batch 1: Ink Corridor (Trap 45), Supply Room, Narrow Passageway, Idol Room,
Storage Area. Design: locations.md (Dungeon — Upper Tier), traps.md
(Trap 45), items.md.

- Every room here is dark (light.py).
- Trap 45 (Ink Corridor): Medium perception, then Medium disarm (trap roll);
  missed or botched, the player is inked. Inked (INKED) cancels the ring's
  invisibility. NPC refusals and the inn bath come with those NPCs.
- Deferred: Trap 17 (Supply Room shelf — smoke jar, clay pot) and Trap 33
  (the idol, fixed in place until then).

State: TRAP45-DONE, INKED, HAND-CART-TAKEN
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_LOOK, M_END
from engine.world import Room, Exit, RLANDBIT

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
    idol.exits["north"] = Exit(destination="NARROW-PASSAGEWAY")
    # Storage Area south → Collapsed Aqueduct is wired in content/aqueduct.py
    storage.exits["west"] = Exit(destination="INK-CORRIDOR")

    ink.action = ink_corridor_action
    storage.action = storage_action
