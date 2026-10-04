"""
Dungeon lower tier, north of The Lower Crossing: the Tool Alcove (Quest 34's
speaking door).

Design: locations.md (Tool Alcove, The Lower Crossing — 50/50 pull-back text),
quests.md (Quest 34).

- Tool Alcove: Medium perception on every visit until the speaking door is
  found. Found: "Something in the back wall notices you", then the wall's
  question. EXAMINE WALL / LISTEN show the question once it's found.
- Leaving south before the door is found: one of two pull-back lines in The
  Lower Crossing, once only.
- Deferred to JJ: READ SCROLL opens the wall; The Flooded Passage beyond.

State: ALCOVE-FOUND, ALCOVE-OPEN, ALCOVE-PULLBACK (None / "pending" / "done")
"""

from __future__ import annotations
import random
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_BEG, M_LOOK, M_ENTER
from engine.world import Room, Exit, RLANDBIT

if TYPE_CHECKING:
    from engine.world import World

_BRACKETS = (
    "The passage ends at a shallow recess lined with iron brackets — the kind used "
    "to hang tools or equipment. The brackets are empty. The back wall is flat and "
    "featureless."
)
_NOTICES = "Something in the back wall notices you. You're not sure how you know that, but you do."
_ASKS = (
    "As you focus on the back wall, it asks you something. Once. The sound of it "
    "fills the alcove and then is gone, leaving only the clear impression that an "
    "answer is expected."
)
_OPEN = (
    "The passage ends at a shallow recess lined with empty iron brackets. The back "
    "wall stands open. It has nothing left to ask."
)
_PULLBACK = (
    "As you step back into the crossing, you're not sure why, but you feel like you "
    "left something unfinished back there.",
    "Behind you, north, there's a sound — or almost a sound. Gone before you can name it.",
)


def alcove_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_ENTER:
        if not w.get_global("ALCOVE-FOUND"):
            from content.perception import MEDIUM
            from content.player import check_perception
            if check_perception(w, MEDIUM):
                w.set_global("ALCOVE-FOUND", True)
                w.set_global("ALCOVE-JUST-FOUND", True)
        return M_NOT_HANDLED
    if msg == M_LOOK:
        if w.get_global("ALCOVE-OPEN"):
            print(_OPEN)
        elif w.get_global("ALCOVE-FOUND"):
            print(_BRACKETS)
            if w.get_global("ALCOVE-JUST-FOUND"):
                print(_NOTICES)
                w.set_global("ALCOVE-JUST-FOUND", False)
            print(_ASKS)
        else:
            print(_BRACKETS)
        return M_HANDLED
    if msg != M_BEG:
        return M_NOT_HANDLED

    wall = w.objects["ALCOVE-WALL"]
    if (w.prsa == "V-EXAMINE" and w.prso is wall) or w.prsa == "V-LISTEN":
        if w.get_global("ALCOVE-OPEN"):
            print(_OPEN)
        elif w.get_global("ALCOVE-FOUND"):
            print(_ASKS)
        elif w.prsa == "V-EXAMINE":
            print(_BRACKETS)
        else:
            return M_NOT_HANDLED
        return M_HANDLED
    if (w.prsa == "V-WALK" and w.walk_dir == "south" and not w.get_global("ALCOVE-FOUND")
            and w.get_global("ALCOVE-PULLBACK") is None):
        w.set_global("ALCOVE-PULLBACK", "pending")
    return M_NOT_HANDLED


def on_enter(w: World, room) -> None:
    """The 50/50 pull-back line, after The Lower Crossing's description; and the
    door found on a return visit (the short description skips M_LOOK)."""
    if room.name == "TOOL-ALCOVE" and w.get_global("ALCOVE-JUST-FOUND"):
        w.set_global("ALCOVE-JUST-FOUND", False)
        print(_NOTICES)
        print(_ASKS)
    if room.name == "LOWER-CROSSING" and w.get_global("ALCOVE-PULLBACK") == "pending":
        w.set_global("ALCOVE-PULLBACK", "done")
        print(_PULLBACK[random.randint(1, 2) - 1])


def make_rooms(world) -> None:
    alcove = Room(name="TOOL-ALCOVE", desc="Tool Alcove", ldesc="", value=3)
    alcove.set_flag(RLANDBIT)   # dark
    world.register_room(alcove)
    world.rooms["LOWER-CROSSING"].exits["north"] = Exit(destination="TOOL-ALCOVE")
    # North (The Flooded Passage) opens with READ SCROLL — section JJ
    alcove.exits.update(south=Exit(destination="LOWER-CROSSING"))
    alcove.action = alcove_action
