"""
The Church of All nave only glimpses the altar (locations.md — Church of All
(Nave)): the altar and its dial are in The Altar, through the archway east.
Run with: pytest roundabout/test_church_nave.py  (from c:\\zork_awt)
"""

import sys
import os
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do
from content.altar import ALTAR_EAST


def _goto(w, name):
    w.move_object(w.player, w.rooms[name])
    w.here = w.rooms[name]


def test_the_nave_names_its_exits():
    w, g = _make_world()
    _goto(w, "CHURCH-NAVE")
    out = _do(g, "look")
    assert "To the east, through a low archway" in out
    assert "The street door is north" in out
    assert "the south lets out into the graveyard" in out


def test_the_altar_names_the_way_back():
    w, g = _make_world()
    _goto(w, "ALTAR")
    assert "The archway leads back west into the nave." in _do(g, "look")


@pytest.mark.parametrize("cmd", [
    "examine altar", "examine dial", "turn dial left", "turn dial right",
    "turn dial", "turn left", "turn right",
])
def test_altar_and_dial_from_the_nave_point_east(cmd):
    w, g = _make_world()
    _goto(w, "CHURCH-NAVE")
    assert ALTAR_EAST in _do(g, cmd)
    assert w.get_global("DIAL") is None          # nothing turned


def test_putting_the_ring_on_the_altar_from_the_nave_points_east():
    w, g = _make_world()
    _goto(w, "CHURCH-NAVE")
    ring = w.objects["RING"]
    w.move_object(ring, w.player)
    ring.clear_flag("INVISIBLE")
    assert ALTAR_EAST in _do(g, "put ring on altar")
    assert ring.location is w.player


def test_the_dial_still_turns_at_the_altar():
    w, g = _make_world()
    _goto(w, "ALTAR")
    out = _do(g, "turn dial right")
    assert "The dial is set to" in out
    assert ALTAR_EAST not in out
