"""
Viking Trial 2 — The Ritual Circle (locations.md): the room lists the stones
without giving away the order; the Encampment banner gives it.
Run with: pytest roundabout/test_ritual_circle.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do

_ORDER = "Earth, Air, Fire, Water"


def _at(name):
    w, g = _make_world()
    w.move_object(w.player, w.rooms[name])
    w.here = w.rooms[name]
    return w, g


def test_circle_lists_the_stones_alphabetically_heart_last():
    w, g = _at("RITUAL-CIRCLE")
    out = _do(g, "look")
    assert "Air, Earth, Fire, Water, and one marked with a heart." in out
    assert _ORDER not in out


def test_banner_gives_the_order():
    w, g = _at("VIKING-ENCAMPMENT")
    assert f"left to right: {_ORDER}." in _do(g, "look at banner")
