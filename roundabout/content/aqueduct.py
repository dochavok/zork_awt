"""
Quest 22 — The Ruined Aqueduct: the Collapsed Aqueduct and the Collapsed
Gallery (Dungeon Upper Tier, south of the Storage Area).

Design: locations.md (Storage Area, Collapsed Aqueduct, Collapsed Gallery,
Rickety Bridge), quests.md (Quest 22, Quest 38), items.md (Mortar Compound).

- Collapsed Aqueduct: PLACE BLOCKS three times (one Medium strength check
  each; a failure makes no progress), then SEAL JOINTS WITH MORTAR (or USE
  MORTAR ON JOINTS / BLOCKS / AQUEDUCT). The mortar is used up, Quest 22
  completes and the Town Square fountain runs.
- Collapsed Gallery: flooded until Quest 22 is done. EAST to the Rickety
  Bridge needs both Quest 38 (timbers) and Quest 22 (flood).
- Deferred: Quest 38 itself (pickaxe, three timber strength checks, support
  beam). The timbers stay up, so the Gallery's east exit stays closed.
- Quest 22's food & drink price cut is the FOOD-DISCOUNT flag only — buying
  food and drink isn't built yet.

State: BLOCKS-PLACED (0–3), AQUEDUCT-SEALED, TIMBERS-CLEARED, FOUNTAIN-RUNNING,
       FOOD-DISCOUNT
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_BEG, M_LOOK
from engine.world import Room, Exit, RLANDBIT

if TYPE_CHECKING:
    from engine.world import World

_CHANNEL = (
    "A stone channel runs through the room at waist height, east to west — an "
    "aqueduct, old work and good work, until here. A section of it has given way. "
)
_BLOCKS_STATE = [
    "Three of its blocks lie tumbled on the floor below the gap, and water spills "
    "from the broken end, runs across the stone and away down the passage south.",
    "One block sits back in the gap; the other two lie on the floor below it. "
    "Water still spills through what's left of the break and away down the passage south.",
    "Two blocks sit back in the gap; the last lies on the floor below it. Water "
    "still spills through what's left of the break and away down the passage south.",
    "All three blocks sit back in the gap, but water seeps through every joint "
    "and runs away down the passage south.",
]
_SEALED_ROOM = (
    "A stone channel runs through the room at waist height, east to west — an "
    "aqueduct, old work and good work, with a mended section in the middle where "
    "the mortar is still pale. Water moves through it quietly, on its way to "
    "somewhere it's needed."
)
_PLACED = [
    "You get your arms under the first block and heave it up into the gap. It "
    "grinds into place. Water finds its way around it, but less of it.",
    "The second block is heavier, or you're more tired. It goes in beside the "
    "first with a sound like a door shutting.",
    "The last block fights you the whole way up. Then it seats, and the gap is "
    "closed — though water still beads and runs at every joint.",
]
_SLIPS = (
    "The block gets as far as your knees and no further. You set it down before "
    "it sets you down."
)
_ALL_IN = "The blocks are all in place. The joints still need sealing."
_WHOLE = "The aqueduct is whole."
_TOO_HEAVY = "They're far too heavy to carry off. They belong in the channel."
_SEALED = (
    "You work the mortar into every joint, pressing it in with your thumbs until "
    "the seeping stops. For a moment the channel is silent. Then the water finds "
    "its way through — the whole length of the aqueduct, running toward town."
)
_STILL_GAP = "There's still a gap. Mortar won't hold back that much water."
_NO_MORTAR = "You'd need something to seal them with."

_GALLERY_BLOCKED = (
    "The passage runs east but doesn't get far. Heavy timbers have come down "
    "across it — not from collapse exactly, more like someone wedged them there "
    "deliberately. The wood is old but solid. Beyond them, darkness."
)
_GALLERY_CLEARED = (
    "The passage runs east, clear now. The timbers that blocked it are gone, the "
    "support beam holding the way open. The shortcut saves time — significant time."
)
_FLOOD = (
    "Water from the passage north pools across the floor here and runs on into "
    "the dark, deep enough at the far end that there's no telling what's under it."
)
_TOO_DEEP = "The water's too deep at the far end to wade, and it's moving fast."


def _placed(w: World) -> int:
    return int(w.get_global("BLOCKS-PLACED") or 0)


# ---------------------------------------------------------------------------
# Collapsed Aqueduct
# ---------------------------------------------------------------------------

def aqueduct_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        if w.get_global("AQUEDUCT-SEALED"):
            print(_SEALED_ROOM)
        else:
            print(_CHANNEL + _BLOCKS_STATE[_placed(w)])
        return M_HANDLED
    if msg == M_BEG and w.prsa == "V-TAKE" and w.prso is w.objects["AQUEDUCT-BLOCKS"]:
        print(_TOO_HEAVY)
        return M_HANDLED
    return M_NOT_HANDLED


def place_blocks(w: World) -> None:
    if w.get_global("AQUEDUCT-SEALED"):
        print(_WHOLE)
        return
    n = _placed(w)
    if n >= 3:
        print(_ALL_IN)
        return
    from content.player import roll_class_bonus
    from content.perception import MEDIUM
    if roll_class_bonus(w, "strength") < MEDIUM:
        print(_SLIPS)
        return
    print(_PLACED[n])
    w.set_global("BLOCKS-PLACED", n + 1)


def seal(w: World) -> None:
    """SEAL JOINTS WITH MORTAR / USE MORTAR ON JOINTS."""
    if w.get_global("AQUEDUCT-SEALED"):
        print(_WHOLE)
        return
    mortar = w.objects["MORTAR"]
    if mortar not in w.player.contents:
        print(_NO_MORTAR)
        return
    if _placed(w) < 3:
        print(_STILL_GAP)
        return
    from content import quests
    print(_SEALED)
    w.move_object(mortar, None)            # used up
    w.set_global("AQUEDUCT-SEALED", True)
    w.set_global("FOUNTAIN-RUNNING", True)
    w.set_global("FOOD-DISCOUNT", True)    # Quest 22 reward; food buying not built yet
    quests.complete(w, "22")


def is_aqueduct_part(obj) -> bool:
    return obj is not None and obj.name in ("AQUEDUCT-BLOCKS", "AQUEDUCT")


# ---------------------------------------------------------------------------
# Collapsed Gallery
# ---------------------------------------------------------------------------

def gallery_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        print(_GALLERY_CLEARED if w.get_global("TIMBERS-CLEARED") else _GALLERY_BLOCKED)
        if not w.get_global("AQUEDUCT-SEALED"):
            print(_FLOOD)
        return M_HANDLED
    return M_NOT_HANDLED


class _GalleryEast(Exit):
    """Gallery EAST → Rickety Bridge: the timbers (Quest 38), then the flood (Quest 22)."""

    def resolve(self, world):
        if not world.get_global("TIMBERS-CLEARED"):
            return None, "The timbers block the way."
        if not world.get_global("AQUEDUCT-SEALED"):
            return None, _TOO_DEEP
        return super().resolve(world)


class _BridgeWest(Exit):
    """Rickety Bridge WEST → Collapsed Gallery: the same two gates from the other side."""

    def resolve(self, world):
        if not (world.get_global("TIMBERS-CLEARED") and world.get_global("AQUEDUCT-SEALED")):
            return None, "You can't go that way."
        return super().resolve(world)


# ---------------------------------------------------------------------------
# Rooms
# ---------------------------------------------------------------------------

def make_rooms(world) -> None:
    def room(name, desc):
        r = Room(name=name, desc=desc, ldesc="", value=1)
        r.set_flag(RLANDBIT)   # dark
        world.register_room(r)
        return r

    aqueduct = room("COLLAPSED-AQUEDUCT", "Collapsed Aqueduct")
    gallery = room("COLLAPSED-GALLERY", "Collapsed Gallery")

    world.rooms["STORAGE-AREA"].exits["south"] = Exit(destination="COLLAPSED-AQUEDUCT")
    aqueduct.exits.update(north=Exit(destination="STORAGE-AREA"), south=Exit(destination="COLLAPSED-GALLERY"))
    gallery.exits.update(north=Exit(destination="COLLAPSED-AQUEDUCT"),
                         east=_GalleryEast(destination="RICKETY-BRIDGE"))
    world.rooms["RICKETY-BRIDGE"].exits["west"] = _BridgeWest(destination="COLLAPSED-GALLERY")

    aqueduct.action = aqueduct_action
    gallery.action = gallery_action
