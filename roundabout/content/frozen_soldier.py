"""
Quest 34 beyond the Tool Alcove: The Flooded Passage and The Fountain Room.

Design: locations.md (Tool Alcove, The Flooded Passage, The Fountain Room),
quests.md (Quest 34), items.md (Vial of Glacier Melt, Ivory Torch, The
Forgotten Blade), npcs.md (The Soldier).

- Flooded Passage: NORTH / SWIM / ENTER POOL before the pool is frozen — 1 heart
  of arcane damage, back at the doorway. POUR VIAL IN WATER freezes it (the vial
  is used up); north is open after that.
- Fountain Room: HOLD TORCH NEAR ICE / MELT ICE WITH TORCH, twice, with the
  Ivory Torch. The second turn frees the soldier: the Forgotten Blade goes to
  the inventory and Quest 34 completes. The ordinary torch doesn't touch it.

State: POOL-FROZEN, ICE-THAW (0 / 1 / 2)
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_BEG, M_LOOK
from engine.world import Room, Exit, RLANDBIT

if TYPE_CHECKING:
    from engine.world import World

# --- The Flooded Passage ------------------------------------------------------

_POOL = (
    "Everything in this room is becoming the pool. Water seeps through the walls in "
    "thin lines, runs down the stone, disappears into the dark surface below. The "
    "ceiling drips. The pool fills the room wall to wall — narrow, long, bottomless "
    "as far as you can tell. The passage north is visible on the other side. The "
    "water is between you and it."
)
_POOL_FROZEN = (
    "The pool fills the room wall to wall, frozen solid. Water still seeps down the "
    "walls and stops where it meets the ice. The passage north is on the other side, "
    "and nothing stands between you and it now."
)
_SWIM = (
    "The moment you enter, the water is inside you somehow — not wet, not cold, just "
    "wrong. The pain that follows is real and serious and spreads fast. You are back "
    "at the doorway, bleeding from nowhere you can see."
)
_FREEZE = (
    "You unstopper the vial and tip it over the pool. The glacier melt hits the "
    "surface and the cold spreads out from it in a white rush, wall to wall, faster "
    "than water should freeze. The pool goes still. Then it goes solid."
)

# --- The Fountain Room ----------------------------------------------------------

_FOUNTAIN = (
    "Cold stops you at the threshold — not wind, just cold, settled and absolute. The "
    "fountain to your left has been frozen mid-pour for what might be a very long "
    "time. The block of ice in the center of the room is frosted thick, but not so "
    "thick you can't see the shape inside it. A person. Standing. Composed."
)
_FOUNTAIN_AFTER = (
    "The fountain to your left is still frozen mid-pour. Where the block of ice stood, "
    "there's only a spreading wet patch on the floor and a few sheets of ice melting "
    "at its edges."
)
_THAW_1 = (
    "The ivory torch throws heat that seems wrong for its size. Where the flame meets "
    "the ice, the frost retreats — a wet gleam spreading outward from the torch's "
    "reach.\n"
    "A single deep crack sounds from somewhere inside the block — not shattering, "
    "just shifting.\n"
    "A small clear window opens in the surface. Through it, the figure is closer than "
    "expected. Still composed. Still waiting."
)
_THAW_2 = (
    "The crack deepens — then several more, fast, branching outward from the window. "
    "The block doesn't collapse so much as release. The ice falls away in sheets, and "
    "the soldier steps forward out of it as if he had been about to do so anyway. He "
    "blinks. He looks at his hands. He looks at you."
)
_HANDOFF = (
    "He looks at the sword at his side as if surprised to find it still there. He "
    "draws it and holds it out to you without ceremony. \"The Forgotten Blade,\" he "
    "says. \"It has no business down here.\" Neither, apparently, does he — he moves "
    "past you and is gone before you can speak.\n"
    "[The Forgotten Blade added to inventory.]"
)
_ICE = "Frosted thick. Inside, a soldier stands composed, eyes open, waiting."
_ICE_WINDOW = "A small clear window has opened in the frost. The soldier inside hasn't moved."
_PLAIN_TORCH_LIT = (
    "You hold the torch to the ice. The flame gutters against the frost and leaves no "
    "mark. Whatever holds this ice, ordinary fire isn't going to move it."
)
_PLAIN_TORCH_OUT = "The torch is burnt out. It wouldn't have been enough anyway."


def _hurt(w: World) -> None:
    """Swimming: 1 heart of arcane damage (not combat — the tunic doesn't apply)."""
    w.globals["hearts"] = w.globals.get("hearts", 1) - 1
    if w.globals["hearts"] <= 0:
        from content.combat import _handle_death
        _handle_death(w)


class _PoolExit(Exit):
    """North across the pool: swimming until it's frozen."""
    def resolve(self, world):
        if not world.get_global("POOL-FROZEN"):
            print(_SWIM)
            _hurt(world)
            return None, None
        return super().resolve(world)


def passage_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        print(_POOL_FROZEN if w.get_global("POOL-FROZEN") else _POOL)
        return M_HANDLED
    if msg != M_BEG:
        return M_NOT_HANDLED
    pool, vial = w.objects["FLOODED-POOL"], w.objects["GLACIER-MELT"]
    if (w.prsa == "V-POUR" and w.prso is vial and w.prsi in (pool, None)
            and vial in w.player.contents and not w.get_global("POOL-FROZEN")):
        w.move_object(vial, None)            # used up
        w.set_global("POOL-FROZEN", True)
        print(_FREEZE)
        return M_HANDLED
    if not w.get_global("POOL-FROZEN") and (
            w.prsa == "V-SWIM" or (w.prsa == "V-ENTER" and w.prso is pool)):
        print(_SWIM)
        _hurt(w)
        return M_HANDLED
    return M_NOT_HANDLED


def _thaw(w: World, torch) -> bool:
    """True if handled (a torch); anything else falls through."""
    from content import quests
    if torch.name == "TORCH":
        print(_PLAIN_TORCH_LIT if torch.has_flag("ONBIT") else _PLAIN_TORCH_OUT)
        return True
    if torch.name != "IVORY-TORCH":
        return False
    if w.get_global("ICE-THAW", 0) == 0:
        w.set_global("ICE-THAW", 1)
        print(_THAW_1)
        return True
    w.set_global("ICE-THAW", 2)
    print(_THAW_2)
    print(_HANDOFF)
    w.move_object(w.objects["ICE-BLOCK"], None)
    w.move_object(w.objects["FORGOTTEN-BLADE"], w.player)
    quests.complete(w, "34")     # 8 Zenni, paid silently
    return True


def fountain_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        print(_FOUNTAIN_AFTER if w.get_global("ICE-THAW", 0) >= 2 else _FOUNTAIN)
        return M_HANDLED
    if msg != M_BEG:
        return M_NOT_HANDLED
    ice = w.objects["ICE-BLOCK"]
    if ice.location is not w.here:
        return M_NOT_HANDLED
    if w.prsa == "V-EXAMINE" and w.prso is ice:
        print(_ICE_WINDOW if w.get_global("ICE-THAW", 0) == 1 else _ICE)
        return M_HANDLED
    # MELT ICE WITH TORCH / HOLD TORCH NEAR ICE
    if w.prsa == "V-MELT" and w.prso is ice and w.prsi is not None:
        return M_HANDLED if _thaw(w, w.prsi) else M_NOT_HANDLED
    if w.prsa == "V-HOLD-NEAR" and w.prsi is ice and w.prso is not None:
        return M_HANDLED if _thaw(w, w.prso) else M_NOT_HANDLED
    return M_NOT_HANDLED


def make_rooms(world) -> None:
    def room(name, desc, action):
        r = Room(name=name, desc=desc, ldesc="", value=2)
        r.set_flag(RLANDBIT)   # dark
        r.action = action
        world.register_room(r)
        return r

    passage = room("FLOODED-PASSAGE", "The Flooded Passage", passage_action)
    fountain = room("FOUNTAIN-ROOM", "The Fountain Room", fountain_action)
    passage.exits.update(south=Exit(destination="TOOL-ALCOVE"),
                         north=_PoolExit(destination="FOUNTAIN-ROOM"))
    fountain.exits["south"] = Exit(destination="FLOODED-PASSAGE")
