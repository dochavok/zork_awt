"""
The Pie Rat Ship heist in the mine (mechanics.md — The Pie Rat Ship Heist;
locations.md — Mine Entrance, Assay Room, Mine Tunnels).

Weak point in the Mine Tunnels (Easy perception, every visit until found) →
DROP GUNPOWDER there → LIGHT GUNPOWDER (flint and steel carried) → 5-turn
fuse → the explosion seals the main entrance and draws the Pie Rats off the
ship. Still inside the mine when it goes: death.

Globals: WEAK-POINT-FOUND, GUNPOWDER-PLACED, FUSE-LIT, MINE-BLOWN, PIE-RATS-GONE.
"""

from __future__ import annotations
from engine.world import World, Room

FUSE_TURNS = 5
INSIDE = frozenset({"MINE-ENTRANCE", "MAIN-SHAFT", "ASSAY-ROOM", "MINE-TUNNELS", "RATS-NEST"})

_WEAK_POINT_FOUND = (
    "One of the timber supports has split along the grain, and the rock above it "
    "sags. If anything in this mine wanted to come down, it would start there."
)
WEAK_POINT_LISTING = "A split timber support sags under the rock above it."
_WEDGED = "You wedge the gunpowder in against the split timber."
_MAKES_A_MESS = "That would just make a mess. It needs to be somewhere that matters."
_NO_FLINT = "You've nothing to light it with."
_HOLDING = "Not while you're holding it."
_LIT = (
    "You strike the flint. The fuse catches with a sharp hiss. The gunpowder is "
    "burning. Time to leave."
)
_BOOM = (
    "A muffled BOOM shakes the ground beneath your feet. Dust and splinters billow "
    "from the mine entrance as it collapses inward. The Pie Rats go running to "
    "investigate — and the ship is unguarded."
)
_CAUGHT_INSIDE = "The mine finds its weak point. So does the ceiling above you."
_BURIED = "The way down is buried under the collapse."
_LIT_TAKE = "Only a madman (or a Pie Rat) would pick that up!"

_ENTRANCE = (
    "The entrance to Pie Rats Mining Inc. is a ragged wound in the earth, shored up "
    "with timber and optimism. A sign above the opening reads: PIE RATS MINING INC. "
    "— AUTHORIZED PERSONNEL ONLY."
)
_ENTRANCE_COLLAPSED = (
    "The entrance is gone. The explosion brought the whole thing down — timbers, "
    "signage, and a significant quantity of rock. Whatever was inside is inside "
    "permanently, or accessible some other way."
)


# ---------------------------------------------------------------------------
# Weak point — enter hook, after the room description
# ---------------------------------------------------------------------------

def on_enter(w: World, room: Room) -> None:
    if room.name != "MINE-TUNNELS" or w.get_global("WEAK-POINT-FOUND"):
        return
    from content.player import check_perception
    from content.perception import EASY
    if check_perception(w, EASY):
        w.set_global("WEAK-POINT-FOUND", True)
        w.objects["WEAK-POINT"].clear_flag("INVISIBLE")
        print(_WEAK_POINT_FOUND)


# ---------------------------------------------------------------------------
# DROP GUNPOWDER / LIGHT GUNPOWDER
# ---------------------------------------------------------------------------

def drop_gunpowder(w: World) -> bool:
    """At the found weak point the gunpowder is wedged in. Returns True if handled."""
    if w.here is None or w.here.name != "MINE-TUNNELS" or not w.get_global("WEAK-POINT-FOUND"):
        return False
    w.move_object(w.objects["GUNPOWDER"], w.here)
    w.set_global("GUNPOWDER-PLACED", True)
    print(_WEDGED)
    return True


def take_refused(w: World) -> bool:
    """TAKE GUNPOWDER once the fuse is lit. Returns True if refused."""
    if w.get_global("FUSE-LIT") and not w.get_global("MINE-BLOWN"):
        print(_LIT_TAKE)
        return True
    return False


def gunpowder_taken(w: World) -> None:
    """Picking it back up undoes the placing."""
    w.set_global("GUNPOWDER-PLACED", False)


def light_gunpowder(w: World) -> None:
    gunpowder = w.objects["GUNPOWDER"]
    if gunpowder in w.player.contents:
        print(_HOLDING)
        return
    if not w.get_global("GUNPOWDER-PLACED") or gunpowder.location is not w.rooms["MINE-TUNNELS"]:
        print(_MAKES_A_MESS)
        return
    if w.objects["FLINT-AND-STEEL"] not in w.player.contents:
        print(_NO_FLINT)
        return
    if w.get_global("FUSE-LIT"):
        return
    print(_LIT)
    w.set_global("FUSE-LIT", True)
    # Five more turns after this one (the clock also ticks on this turn)
    w.game.clock.queue("mine-fuse", _explode, FUSE_TURNS + 1)


def _explode(w: World) -> bool:
    w.set_global("MINE-BLOWN", True)
    w.set_global("PIE-RATS-GONE", True)
    w.move_object(w.objects["GUNPOWDER"], None)
    if w.here is not None and w.here.name in INSIDE:
        print(_CAUGHT_INSIDE + "\n\n*** GAME OVER ***")
        w.set_global("GAME-OVER", True)
        w.game.quit()
        return True
    print(_BOOM)
    return True


# ---------------------------------------------------------------------------
# After the cave-in
# ---------------------------------------------------------------------------

def sealed_check(w: World, room: Room):
    """Walk check: nothing goes down past the Mine Entrance once it's blown."""
    if (w.get_global("MINE-BLOWN") and room.name == "MAIN-SHAFT"
            and w.here is not None and w.here.name == "MINE-ENTRANCE"):
        return _BURIED
    return None


def entrance_action(w: World, msg=None):
    from engine.game import M_LOOK, M_HANDLED, M_NOT_HANDLED
    if msg == M_LOOK:
        print(_ENTRANCE_COLLAPSED if w.get_global("MINE-BLOWN") else _ENTRANCE)
        return M_HANDLED
    return M_NOT_HANDLED
