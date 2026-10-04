"""
The Secret Tunnels' mine branch: The Undercroft north to The Forgotten Shaft,
west to the Hidden Secondary Entrance, west again through the gap into the
Assay Room.

Design: locations.md (The Undercroft, The Forgotten Shaft, Hidden Secondary
Entrance, Assay Room).

- Both new rooms are dark (tunnels); the Assay Room is lit (the mine).
- The gap from the mine side: Medium perception on every visit to the Assay
  Room until found (Actually Enchanted Glasses pass it). Coming through from
  the tunnel side finds it without a line. EAST before then is refused.
- The branch stays open after the mine entrance is blown.

State: ASSAY-GAP-FOUND
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_NOT_HANDLED, M_ENTER
from engine.world import Room, Exit, RLANDBIT

if TYPE_CHECKING:
    from engine.world import World

_SHAFT = (
    "The passage narrows as it goes — not dangerously, but noticeably. The stonework "
    "changes here, older and less deliberate, as if this part of the tunnel predates "
    "whoever dug the rest. The far wall has a gap in it that doesn't look entirely "
    "accidental."
)
_HIDDEN = (
    "The gap in the assay room wall opens into a rough passage that connects to the "
    "tunnel network below. It does not appear on any official plan of the mine. It "
    "would not."
)
_GAP_FOUND = (
    "Looking closer, the gap in the far wall goes further back than it should — a rough "
    "passage, just wide enough to squeeze through, running east into the dark."
)
_JUST_A_CRACK = "It's just a crack in the wall. Nothing you could get through."


class _GapExit(Exit):
    """Assay Room east: only once the gap's been found."""
    def resolve(self, world):
        if not world.get_global("ASSAY-GAP-FOUND"):
            return None, _JUST_A_CRACK
        return super().resolve(world)


def hidden_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_ENTER:
        w.set_global("ASSAY-GAP-FOUND", True)   # found from the tunnel side
    return M_NOT_HANDLED


def on_enter(w: World, room) -> None:
    """Enter hook: the Assay Room's perception check, every visit until found."""
    if room.name != "ASSAY-ROOM" or w.get_global("ASSAY-GAP-FOUND"):
        return
    from content.perception import MEDIUM
    from content.player import check_perception
    if check_perception(w, MEDIUM):
        w.set_global("ASSAY-GAP-FOUND", True)
        print(_GAP_FOUND)


def make_rooms(world) -> None:
    shaft = Room(name="FORGOTTEN-SHAFT", desc="The Forgotten Shaft", ldesc=_SHAFT, value=1)
    hidden = Room(name="HIDDEN-SECONDARY-ENTRANCE", desc="Hidden Secondary Entrance",
                  ldesc=_HIDDEN, value=2)
    for r in (shaft, hidden):
        r.set_flag(RLANDBIT)   # dark
        world.register_room(r)
    hidden.action = hidden_action

    world.rooms["UNDERCROFT"].exits["north"] = Exit(destination="FORGOTTEN-SHAFT")
    shaft.exits.update(south=Exit(destination="UNDERCROFT"),
                       west=Exit(destination="HIDDEN-SECONDARY-ENTRANCE"))
    hidden.exits.update(east=Exit(destination="FORGOTTEN-SHAFT"),
                        west=Exit(destination="ASSAY-ROOM"))
    world.rooms["ASSAY-ROOM"].exits["east"] = _GapExit(destination="HIDDEN-SECONDARY-ENTRANCE")
