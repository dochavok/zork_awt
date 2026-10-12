"""
Ways round that skipped a block (TODO #11, locations.md):
- the mine after the cave-in: the collapse closes the Mine Entrance ↔ Main Shaft
  way in both directions — out is back through the Hidden Secondary Entrance;
- the Portcullis Corridor from the south (the Quest 38 shortcut): you're on the
  side you came in from, and the portcullis blocks the far side until propped.
Run with: pytest roundabout/test_pathing.py  (from c:\\zork_awt)
"""

import sys
import os
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _do
from test_traps import _world, _arrive, _cmd, HIGH


def _at(w, room):
    w.move_object(w.player, w.rooms[room])
    w.here = w.rooms[room]


# ---------------------------------------------------------------------------
# Mine, after the cave-in
# ---------------------------------------------------------------------------

def test_after_the_cave_in_the_way_up_is_buried():
    from content.mine import _BURIED_UP
    w, g = _world()
    w.set_global("MINE-BLOWN", True)
    _at(w, "MAIN-SHAFT")
    assert _BURIED_UP in _do(g, "up")
    assert w.here.name == "MAIN-SHAFT"


def test_after_the_cave_in_the_way_down_is_buried():
    from content.mine import _BURIED
    w, g = _world()
    w.set_global("MINE-BLOWN", True)
    _at(w, "MINE-ENTRANCE")
    assert _BURIED in _do(g, "down")
    assert w.here.name == "MINE-ENTRANCE"


def test_after_the_cave_in_the_way_out_is_the_hidden_entrance():
    w, g = _world()
    w.set_global("MINE-BLOWN", True)
    w.set_global("ASSAY-GAP-FOUND", True)
    _at(w, "MAIN-SHAFT")
    _do(g, "south")
    assert w.here.name == "ASSAY-ROOM"
    _do(g, "east")
    assert w.here.name == "HIDDEN-SECONDARY-ENTRANCE"


def test_before_the_cave_in_up_is_open():
    w, g = _world()
    _at(w, "MAIN-SHAFT")
    _do(g, "up")
    assert w.here.name == "MINE-ENTRANCE"


# ---------------------------------------------------------------------------
# Portcullis Corridor, from either side
# ---------------------------------------------------------------------------

def _from_south(w, g):
    """Come up from the Shrine Room, the charge already spotted and discharged."""
    _at(w, "SHRINE-ROOM")
    w.set_global("PORTCULLIS", "discharged")
    _do(g, "north")
    assert w.here.name == "PORTCULLIS-CORRIDOR"


@pytest.mark.parametrize("state", ["charged", "discharged"])
def test_from_the_south_north_is_blocked_until_propped(state):
    from content.shrine_path import _DOWN
    w, g = _world()
    _from_south(w, g)
    w.set_global("PORTCULLIS", state)
    assert _DOWN in _do(g, "north")
    assert w.here.name == "PORTCULLIS-CORRIDOR"
    _do(g, "south")                              # back the way you came
    assert w.here.name == "SHRINE-ROOM"


def test_from_the_north_south_is_blocked_and_north_is_open():
    from content.shrine_path import _DOWN
    w, g = _world()
    _at(w, "PRAYER-ALCOVE")
    w.set_global("PORTCULLIS", "discharged")
    _do(g, "south")
    assert _DOWN in _do(g, "south")
    _do(g, "north")
    assert w.here.name == "PRAYER-ALCOVE"


def test_propped_from_the_south_the_way_north_is_open():
    from content.shrine_path import _PROPPED_FROM_SOUTH
    w, g = _world()
    _from_south(w, g)
    w.move_object(w.objects["PORTCULLIS-BAR"], w.player)
    _cmd(g, "lift portcullis", HIGH)
    assert _PROPPED_FROM_SOUTH in _do(g, "use portcullis bar")
    _do(g, "north")
    assert w.here.name == "PRAYER-ALCOVE"


def test_propped_both_ways_are_open_from_either_side():
    w, g = _world()
    w.set_global("PORTCULLIS", "propped")
    _at(w, "SHRINE-ROOM")
    for step, room in [("north", "PORTCULLIS-CORRIDOR"), ("north", "PRAYER-ALCOVE"),
                       ("south", "PORTCULLIS-CORRIDOR"), ("south", "SHRINE-ROOM")]:
        _do(g, step)
        assert w.here.name == room


def test_the_side_survives_save_and_restore(tmp_path):
    from content.shrine_path import _DOWN
    from engine import savegame
    w, g = _world()
    _from_south(w, g)
    path = str(tmp_path / "south.sav")
    savegame.save(g, path)
    w2, g2 = _world()                             # a fresh game, then RESTORE
    assert savegame.restore(g2, path)
    assert g2.world.here.name == "PORTCULLIS-CORRIDOR"
    assert _DOWN in _do(g2, "north")
    assert g2.world.here.name == "PORTCULLIS-CORRIDOR"


def test_old_save_without_a_side_is_the_north_side():
    from content.shrine_path import _DOWN
    w, g = _world()
    _arrive(w, g, "PORTCULLIS-CORRIDOR", HIGH)   # placed, not walked in
    assert w.get_global("PORTCULLIS-SIDE") is None
    assert _DOWN in _do(g, "south")
