"""
The Zenni total: last line of INVENTORY, and a line in SCORE during play
(mechanics.md — Inventory Display, Score).
Run with: pytest roundabout/test_zenni_display.py  (from c:\\zork_awt)
"""

import sys
import os
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do


def _empty_handed(zenni):
    w, g = _make_world(cls="warrior", zenni=zenni)
    for obj in list(w.player.contents):
        w.move_object(obj, None)
    return w, g


def test_inventory_ends_with_purse():
    w, g = _make_world(cls="warrior", zenni=12)
    w.move_object(w.objects["ROPE"], w.player)
    out = _do(g, "inventory")
    assert "You are carrying:" in out
    assert out.rstrip().endswith("You have 12 Zenni.")


def test_inventory_one_zenni():
    w, g = _make_world(cls="warrior", zenni=1)
    assert "You have 1 Zenni." in _do(g, "i")


def test_inventory_no_zenni():
    w, g = _make_world(cls="warrior", zenni=0)
    assert "You have no Zenni." in _do(g, "i")


def test_empty_handed_prints_both():
    w, g = _empty_handed(7)
    out = _do(g, "i")
    assert "You are empty-handed." in out and "You have 7 Zenni." in out


def test_inventory_uses_no_turn_change_to_zenni():
    w, g = _make_world(cls="warrior", zenni=12)
    _do(g, "i")
    assert w.globals["zenni"] == 12


def test_score_shows_zenni():
    w, g = _make_world(cls="warrior", zenni=12)
    out = _do(g, "score")
    lines = [l.strip() for l in out.splitlines() if l.strip()]
    i = next(n for n, l in enumerate(lines) if l.startswith("Level "))
    assert lines[i + 1] == "Zenni: 12"


@pytest.mark.parametrize("cmd", ["count", "count zenni", "count money", "count my coins", "COUNT CASH"])
def test_count_zenni_is_the_purse_line_no_turn(cmd):
    w, g = _make_world(cls="warrior", zenni=12)
    moves = w.moves
    assert "You have 12 Zenni." in _do(g, cmd)
    assert w.moves == moves


def test_count_with_no_zenni():
    w, g = _make_world(cls="warrior", zenni=0)
    assert "You have no Zenni." in _do(g, "count zenni")


def test_count_anything_else():
    w, g = _make_world(cls="warrior")
    w.move_object(w.objects["ROPE"], w.player)
    moves = w.moves
    assert "You have lost your mind." in _do(g, "count rope")
    assert w.moves == moves + 1
