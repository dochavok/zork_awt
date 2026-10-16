"""
CAST alone, or with anything that isn't a spell name, lists the spells the
player knows (mechanics.md — Parser Verbs), and
doesn't use a turn.
Run with: pytest roundabout/test_cast_what.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import pytest
from testkit import _make_world, _do


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


@pytest.mark.parametrize("cmd", [
    "cast crowbar", "cast heal", "cast heal at crowbar",
    "cast crowbar at torch", "incant shovel", "chant",
])
def test_anything_but_a_spell_gets_the_plain_cast_list(cmd):
    w, g = _make_world(cls="warrior")
    w.globals["spell_light"] = True
    w.move_object(w.objects["CROWBAR"], w.player)
    moves = w.moves
    assert "Cast what? You know Light." in _do(g, cmd)
    assert w.moves == moves


def test_unlearned_spell_name_is_still_refused():
    w, g = _make_world(cls="warrior")
    w.globals["spell_light"] = True
    assert "You don't know that spell." in _do(g, "cast fireball")


def test_spell_is_not_cast():
    w, g = _make_world(cls="warrior")
    w.globals["spell_light"] = True
    out = _do(g, "spell light")
    assert "Cast what?" not in out and not w.get_global("LIGHT-SPELL-ACTIVE")


def test_named_spell_still_casts():
    w, g = _make_world(cls="warrior")
    w.globals["spell_unbind_undead"] = True
    assert "Nothing here answers the spell." in _do(g, "cast unbind undead")


def test_unbind_undead_frees_ghost_and_drops_watch():
    w, g = _make_world(cls="warrior")
    w.globals["spell_unbind_undead"] = True
    w.move_object(w.player, w.rooms["GHOSTS-ROOM"])
    w.here = w.rooms["GHOSTS-ROOM"]
    out = _do(g, "cast unbind undead")
    assert '"Thank you. I can rest now."' in out
    assert "a pocket watch." in out
    assert w.objects["POCKET-WATCH"].location is w.rooms["GHOSTS-ROOM"]
