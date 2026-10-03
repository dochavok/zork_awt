"""
Church of All (Nave), Graveyard, Mausoleum, and the Chuckle House — Quest 17.

Design: locations.md (Church of All, Graveyard, The Mausoleum, The Chuckle
House), traps.md (Trap 16), mechanics.md (Chuckle House mirrors; Ghost's Room
exit mechanic), quests.md (Quest 17).

- The Chuckle House (east of the Graveyard) exists only after Litlock's bonk.
- Mirrors repel visible players until the ghost is freed: going south into a
  mirror room while visible fails and leaves the player where they were.
- Trap 16 (Shatter Trap Mirror): Medium perception, then Medium disarm (trap
  roll). Missed or botched: the crossbow fires once (1 heart). Either way it's
  spent.
- Ghost's Room: ghost visible only while the ring is worn; hostility is
  atmosphere only. Leaving fails 50% of the time, permanently.
- CAST UNBIND UNDEAD frees the ghost (content/spells.py): he drops the watch
  and the mirrors stop repelling.

State: CHUCKLE-HOUSE-VISIBLE (set by Litlock), CHUCKLE-ENTERED, TRAP16-DONE,
       GHOST-FREED
"""

from __future__ import annotations
import random
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_ENTER, M_LOOK, M_END
from engine.world import Room, Exit, ONBIT, RLANDBIT

if TYPE_CHECKING:
    from engine.world import World


_GRAVEYARD_BASE = (
    "The graves here are old, most of them. Headstones lean at angles that "
    "suggest the ground beneath has shifted, or decided it no longer agrees "
    "with what's above it.\n"
    "The church stands to the north. The mausoleum sits at the far end to the "
    "south, grey and patient."
)
_GRAVEYARD_CHUCKLE = (
    "To the east, a low building stands where there was nothing before — and "
    "you are not sure how you missed it.\n"
    "It is a low structure with a painted facade — or was, once. The paint "
    "shows something cheerful from a distance: bright colors, broad shapes, a "
    "kind of deliberate festivity.\n"
    "Up close, the colors are gone to grey and the shapes resolve into faces. "
    "They are smiling. They have been smiling for a very long time."
)
_GRAVEYARD_AIR = "The air is still in a way that has nothing to do with wind."

_ENTRANCE_FIRST = (
    "Something in the walls makes a sound as you cross the threshold — not "
    "quite a creak, not quite a welcome."
)
_MIRROR_REPEL = (
    "The mirror finds you. Your reflection looks back at you with an "
    "expression you aren't making — and then you are back where you started, "
    "with no memory of turning around."
)
_DISORIENTED = (
    "You head for the door. The mirrors turn you around somewhere along the "
    "way, and you find yourself back in the middle of the room."
)

# Trap 16 (traps.md) — general spot/disarm lines from mechanics.md
_TRAP16 = "a firing pin behind the mirror's frame, a crossbow cocked and ready"
_TRAP_DISARMED = "You spot {d} and are able to disarm it, neutralizing it."
_TRAP_BOTCHED = "You see {d}, but your attempt to disarm it fails miserably."
_CROSSBOW = (
    "Something clicks behind the frame. A bolt cracks out of the dark and "
    "catches you before you can move."
)

GHOST_PRESENCE = (
    "A figure stands among the reflections, grey and thin and turned toward "
    "you — the only thing in the room that isn't repeated."
)
_GHOST_FREED = '"Thank you. I can rest now."'


def _visible(w: World) -> bool:
    """Invisible only with the ring on — and ink (Trap 45) cancels that."""
    return not w.globals.get("ring_worn") or bool(w.get_global("INKED"))


class _MirrorExit(Exit):
    """Southward into a mirror room: repels visible players until the ghost is freed."""

    def resolve(self, world):
        if _visible(world) and not world.get_global("GHOST-FREED"):
            return None, _MIRROR_REPEL
        return super().resolve(world)


class _GhostRoomExit(Exit):
    """Leaving the Ghost's Room fails half the time — permanently."""

    def resolve(self, world):
        if random.randint(1, 2) == 1:
            return None, _DISORIENTED
        return super().resolve(world)


class _ChuckleDoor(Exit):
    """Graveyard east: the Chuckle House isn't there until Litlock's bonk."""

    def resolve(self, world):
        if not world.get_global("CHUCKLE-HOUSE-VISIBLE"):
            return None, "You can't go that way."
        return super().resolve(world)


# ---------------------------------------------------------------------------
# Room actions
# ---------------------------------------------------------------------------

def graveyard_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        print(_GRAVEYARD_BASE)
        if w.get_global("CHUCKLE-HOUSE-VISIBLE"):
            print(_GRAVEYARD_CHUCKLE)
        print(_GRAVEYARD_AIR)
        return M_HANDLED
    return M_NOT_HANDLED


def entrance_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_END and not w.get_global("CHUCKLE-ENTERED"):
        w.set_global("CHUCKLE-ENTERED", True)
        print(_ENTRANCE_FIRST)
    return M_NOT_HANDLED


def shatter_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    """Trap 16 fires on the first pass through, visible or invisible."""
    if msg == M_END and not w.get_global("TRAP16-DONE"):
        w.set_global("TRAP16-DONE", True)
        from content.player import check_perception, roll_class_bonus
        from content.perception import MEDIUM
        if check_perception(w, MEDIUM):
            if roll_class_bonus(w, "trap") >= MEDIUM:
                print(_TRAP_DISARMED.format(d=_TRAP16))
                _award_disarm(w)
                return M_NOT_HANDLED
            print(_TRAP_BOTCHED.format(d=_TRAP16))
        print(_CROSSBOW)
        from content.combat import _take_damage
        _take_damage(w, 1)
    return M_NOT_HANDLED


def _award_disarm(w: World) -> None:
    """experience.md — Trap 16: 3 XP; Rogues +5 per trap disarmed."""
    from content.experience import award_xp
    xp = 3 + (5 if w.globals.get("player_class") == "rogue" else 0)
    award_xp(w, xp)


def ghost_room_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg in (M_ENTER, M_END):
        update_ghost_visibility(w)
    return M_NOT_HANDLED


def update_ghost_visibility(w: World) -> None:
    """The ghost is seen only while the ring is worn (and until he's freed)."""
    ghost = w.objects.get("GHOST")
    if ghost is None:
        return
    if not _visible(w) and not w.get_global("GHOST-FREED"):
        ghost.clear_flag("INVISIBLE")
    else:
        ghost.set_flag("INVISIBLE")


def free_ghost(w: World) -> bool:
    """CAST UNBIND UNDEAD in the Ghost's Room. Returns True if there was a ghost."""
    if w.here is None or w.here.name != "GHOSTS-ROOM" or w.get_global("GHOST-FREED"):
        return False
    print(_GHOST_FREED)
    w.set_global("GHOST-FREED", True)    # mirrors stop repelling everywhere
    w.move_object(w.objects["GHOST"], None)
    w.move_object(w.objects["POCKET-WATCH"], w.rooms["GHOSTS-ROOM"])
    return True


# ---------------------------------------------------------------------------
# Rooms
# ---------------------------------------------------------------------------

def make_rooms(world) -> None:
    def room(name, desc, ldesc, value=1):
        r = Room(name=name, desc=desc, ldesc=ldesc, value=value)
        r.set_flag(ONBIT)
        r.set_flag(RLANDBIT)
        world.register_room(r)
        return r

    nave = room(
        "CHURCH-NAVE", "Church of All",
        "The church is plain inside — stone floor, wooden pews worn smooth, "
        "light coming through narrow windows in thin bars. It could belong to "
        "any faith. That appears to be the point.\n"
        "At the far end, where an altar would normally hold a single symbol, "
        "there is instead a stone altar with a brass dial mounted at its face. "
        "Seven marks around the dial. Whatever is currently selected glows faintly.",
    )
    graveyard = room("GRAVEYARD", "Graveyard", "")
    mausoleum = room(
        "MAUSOLEUM", "The Mausoleum",
        "The mausoleum is older than anything around it. The stone is dark with "
        "age and moisture, the carved details worn to suggestions. The door is "
        "heavy iron, pitted with rust but still on its hinges. Whatever family "
        "name was once above the entrance has been lost to weather. Steps descend "
        "inside toward the crypt below.",
    )
    entrance = room(
        "CHUCKLE-ENTRANCE", "The Entrance",
        "The entrance hall is wider than the exterior suggests. A faded runner "
        "covers the floor — the pattern beneath the grime might have been "
        "geometric once, or might have been faces too; it's hard to say now.\n"
        "The ceiling is low and painted, or was. Hooks on the wall where coats "
        "or hats once hung, empty now.\n"
        "A ticket booth stands to one side, the glass cracked, the stool inside "
        "still in place as if whoever left simply forgot to come back.\n"
        "The building has the quality of a held breath.",
    )
    rejection = room(
        "REJECTION-MIRROR", "The Rejection Mirror",
        "A narrow room with a single tall mirror filling the far wall, its frame "
        "carved with grinning faces. The glass is old and silvered at the edges. "
        "The doorway to the south is beside it — you'd have to pass right in "
        "front of it to get there.",
    )
    shatter = room(
        "SHATTER-TRAP-MIRROR", "The Shatter Trap Mirror",
        "Another mirror, another frame of carved smiles. This one is larger than "
        "the last, the glass faintly rippled with age, so your reflection wavers "
        "as you move. The way on is past it, to the south.",
    )
    ghost_room = room(
        "GHOSTS-ROOM", "Ghost's Room",
        "Mirrors on every wall, angled at each other so the room goes on in "
        "every direction at once. Your reflections are wrong by a fraction — a "
        "beat late, or a beat early. It is very cold.",
    )

    # Main East ↔ Nave ↔ Graveyard ↔ Mausoleum. Nave east (Altar), west
    # (Keeper's Chamber) and Mausoleum down (Crypt) come with later sections.
    world.rooms["MAIN-EAST"].exits["south"] = Exit(destination="CHURCH-NAVE")
    nave.exits.update(north=Exit(destination="MAIN-EAST"), south=Exit(destination="GRAVEYARD"))
    graveyard.exits.update(north=Exit(destination="CHURCH-NAVE"), south=Exit(destination="MAUSOLEUM"),
                           east=_ChuckleDoor(destination="CHUCKLE-ENTRANCE"))
    mausoleum.exits["north"] = Exit(destination="GRAVEYARD")

    # Chuckle House: Entrance east of the Graveyard, the rest run south.
    entrance.exits.update(west=Exit(destination="GRAVEYARD"),
                          south=_MirrorExit(destination="REJECTION-MIRROR"))
    rejection.exits.update(north=Exit(destination="CHUCKLE-ENTRANCE"),
                           south=_MirrorExit(destination="SHATTER-TRAP-MIRROR"))
    shatter.exits.update(north=Exit(destination="REJECTION-MIRROR"),
                         south=_MirrorExit(destination="GHOSTS-ROOM"))
    ghost_room.exits["north"] = _GhostRoomExit(destination="SHATTER-TRAP-MIRROR")

    graveyard.action  = graveyard_action
    entrance.action   = entrance_action
    shatter.action    = shatter_action
    ghost_room.action = ghost_room_action
