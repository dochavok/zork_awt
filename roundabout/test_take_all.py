"""
TAKE ALL leaves out what the player already carries (Zork's TAKE searches
the floor and the room only — gsyntax.zil). A TAKE ALL that finds nothing
says so, as in Zork (gmain.zil).
Run with: pytest roundabout/test_take_all.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do

_NOTHING = "There's nothing here you can take."


def _setup():
    w, g = _make_world(cls="warrior")
    w.move_object(w.objects["ROPE"], w.player)
    return w, g


def test_take_all_skips_carried_items():
    w, g = _setup()
    out = _do(g, "take all")
    assert "already have" not in out
    assert _NOTHING in out


def test_take_all_takes_floor_items_only():
    w, g = _setup()
    w.move_object(w.objects["SHOVEL"], w.here)
    out = _do(g, "take all")
    assert "You take the" in out and "shovel" in out
    assert "already have" not in out
    assert w.objects["SHOVEL"].location is w.player


def test_take_all_but_skips_carried_items():
    w, g = _setup()
    w.move_object(w.objects["SHOVEL"], w.here)
    out = _do(g, "take all but shovel")
    assert "already have" not in out
    assert _NOTHING in out
    assert w.objects["SHOVEL"].location is w.here


def test_take_named_carried_item_still_answers():
    w, g = _setup()
    assert "You already have the coil of rope." in _do(g, "take rope")
