"""
The Zenni total: last line of INVENTORY, and a line in SCORE during play
(mechanics.md — Inventory Display, Score).
Run with: pytest roundabout/test_zenni_display.py  (from c:\\zork_awt)
"""

import sys
import os
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
