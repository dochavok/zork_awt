"""
The ring can't be dropped (items.md — The God-Forsaken Ring).
Run with: pytest roundabout/test_ring_keep.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do

KEEP = '"Bring it to me, or keep it close," Will said. You keep it close.'


def _with_ring(room="TOWN-SQUARE", worn=False):
    w, g = _make_world()
    w.move_object(w.player, w.rooms[room])
    w.here = w.rooms[room]
    w.move_object(w.objects["RING"], w.player)
    if worn:
        _do(g, "wear ring")
    return w, g


def _carry(w, name):
    obj = w.objects[name]
    obj.flags.discard("INVISIBLE")
    w.move_object(obj, w.player)


def test_drop_ring_refused():
    w, g = _with_ring()
    assert KEEP in _do(g, "drop ring")
    assert w.objects["RING"].location is w.player


def test_throw_ring_refused():
    w, g = _with_ring()
    assert KEEP in _do(g, "throw ring")
    assert w.objects["RING"].location is w.player


def test_put_ring_in_trophy_case_refused():
    w, g = _with_ring("TOWN-HALL-TOWER")
    w.set_global("CASE-OPEN", True)
    assert KEEP in _do(g, "put ring in case")
    assert w.objects["RING"].location is w.player


def test_worn_drop_refused_without_removal():
    from unittest.mock import patch
    w, g = _with_ring(worn=True)
    w.globals["ring_corruption"] = 45            # removal would need a roll
    with patch("content.player.roll") as roll:
        out = _do(g, "drop ring")
    assert KEEP in out
    roll.assert_not_called()
    assert w.globals["ring_worn"]


def test_remove_ring_unchanged():
    w, g = _with_ring(worn=True)
    out = _do(g, "remove ring")
    assert KEEP not in out and not w.globals["ring_worn"]


def test_drop_all_skips_the_ring():
    w, g = _with_ring()
    _carry(w, "KITE")
    out = _do(g, "drop all")
    assert KEEP not in out and "ring" not in out.lower()
    assert w.objects["KITE"].location is w.here
    assert w.objects["RING"].location is w.player


def test_drop_all_empty_handed():
    w, g = _make_world()
    assert _do(g, "drop all").strip() == "You are empty-handed."


def test_drop_all_only_worn():
    w, g = _make_world()
    _carry(w, "ENCHANTED-GLASSES")
    _do(g, "wear glasses")
    w.move_object(w.objects["RING"], w.player)
    _do(g, "wear ring")
    assert _do(g, "drop all").strip() == "You'll need to remove anything you want to drop."


def test_drop_all_only_the_ring():
    w, g = _with_ring()
    assert _do(g, "drop all").strip() == KEEP
    _do(g, "wear ring")
    assert _do(g, "drop all").strip() == KEEP


def test_drop_all_but_ring_unchanged():
    w, g = _with_ring()
    _carry(w, "KITE")
    out = _do(g, "drop all but ring")
    assert KEEP not in out
    assert w.objects["KITE"].location is w.here


KEPT = "That leaves nothing to drop."


def test_drop_all_but_keeps_everything():
    w, g = _make_world()
    _carry(w, "SHOVEL")
    assert _do(g, "drop all but shovel").strip() == KEPT
    _carry(w, "ROPE")
    assert _do(g, "drop all but shovel and rope").strip() == KEPT
    assert w.objects["SHOVEL"].location is w.player
    assert w.objects["ROPE"].location is w.player


def test_drop_all_but_ring_line_comes_first():
    w, g = _with_ring()
    _carry(w, "SHOVEL")
    assert _do(g, "drop all but shovel").strip() == KEEP


def test_drop_all_but_worn_line_comes_first():
    w, g = _with_ring()
    _carry(w, "SHOVEL")
    _carry(w, "ENCHANTED-GLASSES")
    _do(g, "wear glasses")
    assert _do(g, "drop all but shovel").strip() == "You'll need to remove anything you want to drop."


def test_ring_weighs_nothing():
    w, _g = _with_ring()
    assert w.objects["RING"].size == 0


def test_every_listed_weight_is_applied():
    from content.objects import _WEIGHTS
    w, _g = _make_world()
    wrong = {n: w.objects[n].size for n, s in _WEIGHTS.items() if w.objects[n].size != s}
    assert not wrong
