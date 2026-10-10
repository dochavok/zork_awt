"""
Dungeon middle tier, key side: Key Door Landing → Mine Passage → Stored Room,
and the drop into the lower tier (Pile of Rubble).

Design: locations.md (Key Door Landing, Mine Passage, Stored Room, Pile of
Rubble), mechanics.md (Shovel & Dig Mechanic), items.md (Rope, Shovel).

- Stored Room: DIG with the shovel collapses the floor for good — the room
  becomes the Hole to Below. TIE ROPE TO BEAM (the support timber) lets the
  player climb down and back up; once tied, the rope stays. JUMP into the hole
  is death.
- Any successful DIG: Will's 1-in-20 audio note.
- Mine Passage: charcoal (no check), silver dust (Medium perception each
  visit until found), iron chest — the lockpicks open it and the 20 Zenni are
  pocketed directly.
- The Crevice (Stored Room east): gold pocket watch on a skeleton's finger.
  Cut off for good once the floor is dug.
- Exits wired elsewhere: Pile of Rubble north/south in content/lower_tier.py,
  east (Antechamber) in content/still_den.py; Mine Passage south (Inscription
  Chamber) in content/inscription.py.

State: STORED-ROOM-DUG, ROPE-TIED, MINE-CHEST-OPEN
"""

from __future__ import annotations
import random
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_BEG, M_LOOK, M_ENTER
from engine.world import Room, Exit, RLANDBIT, NDESCBIT, TAKEBIT

if TYPE_CHECKING:
    from engine.world import World

_LANDING = (
    "The staircase deposits you in a rough cave at the bottom — low ceiling, "
    "unworked stone, the kind of room that exists because something had to be at "
    "the bottom of the stairs. The air is cooler here, damper. The passage "
    "continues south."
)
_MINE = (
    "A worked section of cave — support timbers at intervals, rusting tools left "
    "where they were dropped. The smell of old rock dust is thick here. Someone "
    "mined this passage, or used it as a route through to something being mined."
)
_CHEST_SHUT = "A large iron chest is bolted to the floor against one wall."
_CHEST_OPEN = "A large iron chest is bolted to the floor against one wall, its lid open."
_CHEST_LOCKED = "The chest is locked. The lock looks pickable — if you had the tools."
_CHEST_PICKED = (
    "The lockpicks find the pins one by one, and the lid comes up with a groan. "
    "Inside are 20 Zenni, which you pocket."
)
_CHEST_EMPTY = "The chest is empty."
CHEST_ZENNI = 20
_CREVICE = (
    "The passage pinches down to a crack in the far wall, and a skeleton is wedged "
    "into it at the shoulders — someone who tried to squeeze through and didn't fit."
)
_CREVICE_WATCH = (
    "One arm hangs back toward you, and from its outstretched finger dangles a gold "
    "pocket watch on a chain."
)
_CREVICE_EMPTY = "One arm hangs back toward you, the finger empty now."
_TOO_WIDE = "The gap where the floor used to be is far too wide to cross."
_STORED = (
    "The floor is packed tight with rubble — not the chaotic scatter of a cave-in, "
    "but deliberate, careful fill. Someone put this here on purpose."
)
_HOLE = (
    "Apparently the \"something\" being covered was a giant hole. The floor is "
    "gone — caved into the darkness below where the rubble gave way."
)
_TIMBER = "One of the old support timbers juts out over the edge, still sound."
_ROPE_HANGS = "A rope is knotted around the timber, hanging down into the dark."
_RUBBLE_PILE = (
    "The ceiling is a jagged wound — stone and packed earth hanging at the edge "
    "where the floor above used to be. Below that: the rubble that was the floor, "
    "now a rough-graded pile you're standing on. The air smells of disturbed "
    "earth and something older underneath it. Passages lead north, east, and south."
)

_DUG = (
    "The shovel bites into the packed rubble and the floor gives way — the fill "
    "cascades into the darkness below. You scramble back from the edge. A gaping "
    "hole now separates you from the eastern passage."
)
_NO_SHOVEL = "The fill is packed too tight to move by hand. You'd need a shovel."
_ALREADY_DUG = "The floor is already gone."
_TIED = (
    "You knot the rope around the timber and pay it out over the edge. It goes "
    "taut, then slack — the far end is resting on something solid."
)
_NOTHING_TO_TIE = "There's nothing here to tie it to."
_ROPE_STAYS = "You'd like a way back up. The rope stays."
_DROP_TOO_FAR = "The drop is serious. You'd need something to climb down on."
_JUMP = (
    "It occurs to you, as you fall, that this may not have been a good decision. "
    "You die."
)


def _game_over(w: World, text: str) -> None:
    print(text + "\n\n*** GAME OVER ***")
    w.set_global("GAME-OVER", True)
    w.game.quit()


def _walk(w: World, direction: str) -> int:
    w.walk_dir = direction
    return w.game.perform("V-WALK")


# ---------------------------------------------------------------------------
# Mine Passage
# ---------------------------------------------------------------------------

def open_chest(w: World) -> None:
    """OPEN / UNLOCK CHEST (WITH LOCKPICKS): the lockpicks open it, Zenni pocketed."""
    picks = w.objects["LOCKPICKS"]
    if w.get_global("MINE-CHEST-OPEN"):
        print(_CHEST_EMPTY)
    elif picks not in w.player.contents or w.prsi not in (None, picks):
        print(_CHEST_LOCKED)
    else:
        print(_CHEST_PICKED)
        w.set_global("MINE-CHEST-OPEN", True)
        w.globals["zenni"] = w.globals.get("zenni", 0) + CHEST_ZENNI


def mine_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_ENTER:
        from content.perception import MEDIUM, reveal_if_found
        reveal_if_found(w, "SILVER-DUST", MEDIUM)
    elif msg == M_LOOK:
        print(_MINE + " " + (_CHEST_OPEN if w.get_global("MINE-CHEST-OPEN") else _CHEST_SHUT))
        return M_HANDLED
    return M_NOT_HANDLED


# ---------------------------------------------------------------------------
# The Crevice
# ---------------------------------------------------------------------------

def crevice_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        watch_here = w.objects["GOLD-WATCH"] in w.here.contents
        print(_CREVICE + " " + (_CREVICE_WATCH if watch_here else _CREVICE_EMPTY))
        return M_HANDLED
    return M_NOT_HANDLED


class _CreviceExit(Exit):
    """Stored Room EAST: open until the dig, then the hole is too wide."""

    def resolve(self, world):
        if world.get_global("STORED-ROOM-DUG"):
            return None, _TOO_WIDE
        return super().resolve(world)


# ---------------------------------------------------------------------------
# Stored Room / Hole to Below
# ---------------------------------------------------------------------------

def _dig(w: World) -> None:
    if w.get_global("STORED-ROOM-DUG"):
        print(_ALREADY_DUG)
        return
    if w.objects["SHOVEL"] not in w.player.contents:
        print(_NO_SHOVEL)
        return
    print(_DUG)
    w.set_global("STORED-ROOM-DUG", True)
    w.game.apply_room_names()                        # now the Hole to Below
    w.objects["SUPPORT-TIMBER"].clear_flag("INVISIBLE")
    dig_note(w)


def dig_note(w: World) -> None:
    """Will's audio note: 1-in-20 on any successful DIG (mechanics.md)."""
    from content.will import DIG_NOTE
    if random.randint(1, 20) <= 1:
        print(DIG_NOTE)


def _tie_rope(w: World) -> None:
    timber = w.objects["SUPPORT-TIMBER"]
    if w.get_global("ROPE-TIED"):
        print(_ROPE_HANGS)
    elif not w.get_global("STORED-ROOM-DUG") or w.prsi not in (None, timber):
        print(_NOTHING_TO_TIE)
    else:
        print(_TIED)
        rope = w.objects["ROPE"]
        w.set_global("ROPE-TIED", True)
        w.move_object(rope, w.here)
        rope.set_flag(NDESCBIT)      # the room description carries it
        rope.clear_flag(TAKEBIT)


def stored_room_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        if not w.get_global("STORED-ROOM-DUG"):
            print(_STORED)
        else:
            print(_HOLE)
            print(_TIMBER)
            if w.get_global("ROPE-TIED"):
                print(_ROPE_HANGS)
        return M_HANDLED
    if msg != M_BEG:
        return M_NOT_HANDLED

    dug = w.get_global("STORED-ROOM-DUG")
    rope = w.objects["ROPE"]
    if w.prsa == "V-DIG":
        _dig(w)
        return M_HANDLED
    if w.prsa == "V-TIE" and w.prso is rope:
        _tie_rope(w)
        return M_HANDLED
    if w.prsa in ("V-UNTIE", "V-TAKE") and w.prso is rope and w.get_global("ROPE-TIED"):
        print(_ROPE_STAYS)
        return M_HANDLED
    if w.prsa == "V-JUMP" and dug:
        _game_over(w, _JUMP)
        return M_HANDLED
    if w.prsa == "V-CLIMB-DOWN" and dug:
        return _walk(w, "down")
    return M_NOT_HANDLED


class _HoleExit(Exit):
    """Stored Room DOWN: no hole before the dig; the rope makes it climbable."""

    def resolve(self, world):
        if not world.get_global("STORED-ROOM-DUG"):
            return None, "You can't go that way."
        if not world.get_global("ROPE-TIED"):
            return None, _DROP_TOO_FAR
        return super().resolve(world)


# ---------------------------------------------------------------------------
# Pile of Rubble (lower tier, Room 1)
# ---------------------------------------------------------------------------

def rubble_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_BEG and w.prsa == "V-CLIMB-UP":
        return _walk(w, "up")
    return M_NOT_HANDLED


# ---------------------------------------------------------------------------
# Rooms
# ---------------------------------------------------------------------------

def make_rooms(world) -> None:
    def room(name, desc, ldesc, value=1):
        r = Room(name=name, desc=desc, ldesc=ldesc, value=value)
        r.set_flag(RLANDBIT)   # dark
        world.register_room(r)
        return r

    landing = room("KEY-DOOR-LANDING", "Key Door Landing", _LANDING)
    mine = room("MINE-PASSAGE", "Mine Passage", "")
    stored = room("STORED-ROOM", "Stored Room", "")
    world.game.register_room_name("STORED-ROOM", "STORED-ROOM-DUG", "Hole to Below")
    crevice = room("THE-CREVICE", "The Crevice", "")
    rubble = room("PILE-OF-RUBBLE", "Pile of Rubble", _RUBBLE_PILE, value=2)

    landing.exits.update(north=Exit(destination="MID-TIER-KEY-DOOR"), south=Exit(destination="MINE-PASSAGE"))
    # Mine Passage south → Inscription Chamber is deferred
    mine.exits.update(north=Exit(destination="KEY-DOOR-LANDING"), east=Exit(destination="STORED-ROOM"))
    stored.exits.update(west=Exit(destination="MINE-PASSAGE"), east=_CreviceExit(destination="THE-CREVICE"),
                        down=_HoleExit(destination="PILE-OF-RUBBLE"))
    crevice.exits.update(west=Exit(destination="STORED-ROOM"))
    # The rope is always tied by the time the player is down here
    rubble.exits.update(up=Exit(destination="STORED-ROOM"))

    mine.action = mine_action
    crevice.action = crevice_action
    stored.action = stored_room_action
    rubble.action = rubble_action
