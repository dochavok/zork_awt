"""
Plain CAST lists the spells the player knows (mechanics.md — Spells), and
doesn't use a turn.
Run with: pytest roundabout/test_cast_what.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do


def test_no_spells():
    w, g = _make_world(cls="warrior")
    assert "You don't know any spells." in _do(g, "cast")


def test_one_spell():
    w, g = _make_world(cls="warrior")
    w.globals["spell_unbind_undead"] = True
    assert "Cast what? You know Unbind Undead." in _do(g, "cast")


def test_all_spells_in_order():
    w, g = _make_world(cls="warrior")
    for flag in ("spell_fireball", "spell_light", "spell_unbind_undead"):
        w.globals[flag] = True
    assert "Cast what? You know Light, Unbind Undead and Fireball." in _do(g, "cast")


def test_two_spells():
    w, g = _make_world(cls="warrior")
    w.globals["spell_light"] = True
    w.globals["spell_fireball"] = True
    assert "Cast what? You know Light and Fireball." in _do(g, "cast")


def test_plain_cast_takes_no_turn():
    w, g = _make_world(cls="warrior")
    moves = w.moves
    _do(g, "cast")
    assert w.moves == moves


def test_named_spell_still_casts():
    w, g = _make_world(cls="warrior")
    w.globals["spell_unbind_undead"] = True
    assert "Nothing here answers the spell." in _do(g, "cast unbind undead")
