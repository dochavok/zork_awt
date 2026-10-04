"""
The dark branch south of The Lower Crossing: Dark Room, Spirit Room, Burial
Chamber.

Design: locations.md (Dark Room, Spirit Room, Burial Chamber), items.md
(Guardian's Lantern, Funeral Mask of Hammered Gold), mechanics.md (Lighting
System, Guardian's Lantern — Dark Room Interaction).

- Dark Room: magical darkness. It can be entered whatever light you carry, but
  torch and Light spell do nothing; south is blocked until LIGHT LANTERN (or
  TURN ON LANTERN). The lantern then hangs on the wall for good and lights the
  room itself — the room isn't naturally lit, so the Light spell stays on.
  Anywhere else the lantern only flickers.
- Spirit Room: the spirits block both ways while the player is visible (the
  ring on, and not inked — as in the Chuckle House). They can't be harmed.
- Burial Chamber: the Funeral Mask on its plinth. The spirits don't react.

State: LANTERN-HUNG, MASK-MOVED
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_BEG, M_LOOK, M_END
from engine.world import Room, Exit, RLANDBIT, ONBIT, NDESCBIT, TAKEBIT

if TYPE_CHECKING:
    from engine.world import World

_LIGHT_VERBS = ("V-LIGHT", "V-LAMP-ON", "V-TURN-ON")

# --- Dark Room ----------------------------------------------------------------

_DARK = ("You cannot see anything. This is not like being in the dark. This is "
         "something the dark is doing on purpose.")
_REVEAL = (
    "The lantern opens and the darkness collapses. No gradual brightening — one moment "
    "nothing, the next a plain stone room, fully lit, as if it had always been waiting "
    "to be seen.\n"
    "Unremarkable in every way except one: it is not dark. After what just happened, "
    "that feels like quite a lot.\n"
    "There is a hook on the wall. You hang the lantern on it. It feels like the right "
    "thing to do, and apparently it was."
)
_LIT = (
    "A plain stone room, unremarkable in every way. Stone walls, stone floor, passages "
    "north and south. The Guardian's Lantern burns steadily on the wall. It is not dark."
)
_DARK_SOUTH = ("You take a step into it and the dark doesn't give. There's no telling "
               "where the passage goes, or whether it goes anywhere at all.")
_LIGHT_SPELL_FAILS = (
    "The spell reaches out and finds nothing to push against. This is not like being "
    "in the dark. This is something the dark is doing on purpose."
)
_LANTERN_ELSEWHERE = ("The lantern flickers, as if it wants to light and can't decide "
                      "where. Not here, apparently.")
_LANTERN_HUNG = "The lantern stays on its hook. It seems to belong there now."

# --- Spirit Room --------------------------------------------------------------

_SPIRITS_SEE = (
    "The room is silent. Shapes drift through it — sparse, irregular, neither here nor "
    "entirely anywhere. They are not human. They are not entirely not human. They take "
    "note of you the moment you enter. The passages on either side are visible. "
    "Getting to them is another matter."
)
_SPIRITS_IGNORE = (
    "The room is silent. Shapes drift through it — sparse, irregular, neither here nor "
    "entirely anywhere. They pay you no attention at all. Passages lead north and south."
)
_BLOCKED = (
    "The shapes collect between you and the passage. Not blocking — just there, "
    "watching, closer than they were. You sense that pressing forward would be a "
    "mistake you wouldn't finish making."
)
_RING_ON = (
    "The attention in the room drops all at once — not gradually, immediately. The "
    "shapes drift back to their own patterns. They have forgotten you entirely."
)
_RING_OFF = "The shapes stop drifting. One by one, they turn toward you."
_SPIRITS_EXAMINE = (
    "Shapes, mostly. Sparse, irregular, never quite where you looked. Somewhere between "
    "six and nine of them; they won't hold still long enough to count."
)
_SPIRITS_ATTACK = ("Your weapon passes through the nearest shape without finding "
                   "anything. It doesn't seem to mind. The others watch.")

# --- Burial Chamber -----------------------------------------------------------

_CHAMBER = (
    "The chamber is circular, the walls carved with processions of figures — mourners, "
    "by the look of them, rendered in a style no living hand in Roundabout would "
    "recognize. Niches hold candles that have not burned in centuries, wax melted flat "
    "and cold. {plinth} Everything in this room was arranged deliberately, long ago, by "
    "people who are not coming back."
)
_PLINTH_MASK = "The plinth at the center holds the mask."
_PLINTH_EMPTY = "The plinth at the center stands empty."


def _in_dark_room(w: World) -> bool:
    return w.here is not None and w.here.name == "DARK-ROOM"


def magic_dark(w: World) -> bool:
    """True in the Dark Room before the lantern is hung (light.py checks this)."""
    return _in_dark_room(w) and not w.get_global("LANTERN-HUNG")


def light_spell_fails() -> None:
    print(_LIGHT_SPELL_FAILS)


def light_lantern(w: World) -> None:
    """LIGHT LANTERN / TURN ON LANTERN, carried."""
    lantern = w.objects["GUARDIANS-LANTERN"]
    if not magic_dark(w):
        print(_LANTERN_ELSEWHERE)
        return
    lantern.set_flag(ONBIT)
    lantern.set_flag(NDESCBIT)
    lantern.clear_flag(TAKEBIT)
    w.move_object(lantern, w.here)
    w.set_global("LANTERN-HUNG", True)
    print(_REVEAL)


def _visible(w: World) -> bool:
    from content import chuckle
    return chuckle._visible(w)


class _DarkExit(Exit):
    """South out of the Dark Room: nothing until the lantern is hung."""
    def resolve(self, world):
        if not world.get_global("LANTERN-HUNG"):
            print(_DARK_SOUTH)
            return None, None
        return super().resolve(world)


class _SpiritExit(Exit):
    """Out of the Spirit Room, either way: only unseen."""
    def resolve(self, world):
        if _visible(world):
            print(_BLOCKED)
            return None, None
        return super().resolve(world)


def dark_room_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        print(_LIT if w.get_global("LANTERN-HUNG") else _DARK)
        return M_HANDLED
    if msg != M_BEG:
        return M_NOT_HANDLED
    lantern = w.objects["GUARDIANS-LANTERN"]
    if w.get_global("LANTERN-HUNG") and w.prso is lantern and w.prsa == "V-TAKE":
        print(_LANTERN_HUNG)
        return M_HANDLED
    if w.prsa in _LIGHT_VERBS and w.prso is lantern and lantern in w.player.contents:
        light_lantern(w)
        return M_HANDLED
    return M_NOT_HANDLED


def spirit_room_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        print(_SPIRITS_SEE if _visible(w) else _SPIRITS_IGNORE)
        return M_HANDLED
    if msg == M_BEG:
        w.set_global("SPIRITS-SAW", _visible(w))
        spirits = w.objects["SPIRITS"]
        if w.prso is spirits and w.prsa == "V-EXAMINE":
            print(_SPIRITS_EXAMINE)
            return M_HANDLED
        if w.prso is spirits and w.prsa == "V-MELEE":
            print(_SPIRITS_ATTACK)
            return M_HANDLED
        return M_NOT_HANDLED
    if msg == M_END and w.here is not None and w.here.name == "SPIRIT-ROOM":
        # The ring went on (or came off) this turn, in front of them
        saw, sees = w.get_global("SPIRITS-SAW"), _visible(w)
        if saw and not sees:
            print(_RING_ON)
        elif sees and saw is False:
            print(_RING_OFF)
        w.set_global("SPIRITS-SAW", None)
    return M_NOT_HANDLED


def burial_chamber_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    mask = w.objects["FUNERAL-MASK"]
    if msg == M_LOOK:
        on_plinth = mask.location is w.here and not w.get_global("MASK-MOVED")
        print(_CHAMBER.format(plinth=_PLINTH_MASK if on_plinth else _PLINTH_EMPTY))
        return M_HANDLED
    if msg == M_END and mask.location is not w.rooms["BURIAL-CHAMBER"] \
            and not w.get_global("MASK-MOVED"):
        w.set_global("MASK-MOVED", True)
        mask.clear_flag(NDESCBIT)     # described like any other item from now on
    return M_NOT_HANDLED


def make_rooms(world) -> None:
    def room(name, desc, action, value):
        r = Room(name=name, desc=desc, ldesc="", value=value)
        r.set_flag(RLANDBIT)   # dark
        r.action = action
        world.register_room(r)
        return r

    dark = room("DARK-ROOM", "Dark Room", dark_room_action, 2)
    spirit = room("SPIRIT-ROOM", "Spirit Room", spirit_room_action, 2)
    chamber = room("BURIAL-CHAMBER", "Burial Chamber", burial_chamber_action, 3)
    world.rooms["LOWER-CROSSING"].exits["south"] = Exit(destination="DARK-ROOM")
    dark.exits.update(north=Exit(destination="LOWER-CROSSING"),
                      south=_DarkExit(destination="SPIRIT-ROOM"))
    spirit.exits.update(north=_SpiritExit(destination="DARK-ROOM"),
                        south=_SpiritExit(destination="BURIAL-CHAMBER"))
    chamber.exits["north"] = Exit(destination="SPIRIT-ROOM")
