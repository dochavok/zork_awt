"""
CUT X [WITH Y] and KICK X (mechanics.md — Parser Verbs): an attack on something the
player can fight, "[Name] wouldn't appreciate that." for other NPCs, Zork's
line for anything else; CUT ROPE once tied keeps the rope (locations.md).
And ATTACK / SHOOT on a non-enemy name NPCs as GIVE does (mechanics.md — Bow).
Run with: pytest roundabout/test_cut.py  (from c:\\zork_awt)
"""

import sys
import os
from unittest.mock import patch
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do
from content.mid_tier import _ROPE_STAYS


def _at(room, *flags):
    w, g = _make_world(cls="warrior")
    w.set_global("LIGHT-SPELL-ACTIVE", True)
    for flag in flags:
        w.set_global(flag, True)
    w.move_object(w.player, w.rooms[room])
    w.here = w.rooms[room]
    return w, g


def _give(w, name):
    obj = w.objects[name]
    obj.clear_flag("INVISIBLE")
    w.move_object(obj, w.player)


def test_cut_an_enemy_is_an_attack():
    w, g = _at("BACK-ALLEY", "MUGGER-SPOTTED")
    mugger = w.objects["MUGGER"]
    mugger.clear_flag("INVISIBLE")
    w.move_object(mugger, w.here)
    seen = []
    with patch("content.verbs._fight", lambda world, obj: seen.append((world.prsa, obj.name))):
        _do(g, "cut mugger")
    assert seen == [("V-MELEE", "MUGGER")]


@pytest.mark.parametrize("room,cmd,line", [
    ("BAR", "cut may", "May wouldn't appreciate that."),
    ("BAR", "slice may", "May wouldn't appreciate that."),
])
def test_cut_another_npc(room, cmd, line):
    w, g = _at(room)
    assert line in _do(g, cmd)


def test_cut_a_thing():
    w, g = _at("TOWN-SQUARE")
    _give(w, "CROWBAR")
    _give(w, "TORCH")
    moves = w.moves
    assert "Strange concept, cutting the crowbar..." in _do(g, "cut crowbar")
    assert "Strange concept, cutting the crowbar..." in _do(g, "cut crowbar with torch")
    assert w.moves == moves + 2


def test_cut_the_tied_rope_from_above():
    w, g = _at("STORED-ROOM", "STORED-ROOM-DUG", "ROPE-TIED")
    w.move_object(w.objects["ROPE"], w.here)
    assert _ROPE_STAYS in _do(g, "cut rope")
    assert w.get_global("ROPE-TIED")


def test_cut_the_rope_from_below():
    w, g = _at("PILE-OF-RUBBLE", "STORED-ROOM-DUG", "ROPE-TIED")
    assert _ROPE_STAYS in _do(g, "cut rope")


def test_cut_the_loose_rope():
    w, g = _at("TOWN-SQUARE")
    _give(w, "ROPE")
    assert "Strange concept, cutting the coil of rope..." in _do(g, "cut rope")


def test_attack_a_named_npc_has_no_the():
    w, g = _at("BAR")
    out = _do(g, "attack may")
    assert "You can't fight May." in out and "the May" not in out


def test_attack_a_thing_keeps_the():
    w, g = _at("TOWN-SQUARE")
    crowbar = w.objects["CROWBAR"]
    crowbar.clear_flag("INVISIBLE")
    w.move_object(crowbar, w.here)
    assert "You can't fight the crowbar." in _do(g, "attack crowbar")


def test_kick_an_enemy_is_an_attack():
    w, g = _at("BACK-ALLEY", "MUGGER-SPOTTED")
    mugger = w.objects["MUGGER"]
    mugger.clear_flag("INVISIBLE")
    w.move_object(mugger, w.here)
    seen = []
    with patch("content.verbs._fight", lambda world, obj: seen.append((world.prsa, obj.name))):
        _do(g, "kick mugger")
    assert seen == [("V-MELEE", "MUGGER")]


def test_kick_an_npc_and_a_thing():
    w, g = _at("BAR")
    _give(w, "CROWBAR")
    assert "May wouldn't appreciate that." in _do(g, "kick may")
    assert "Kicking the crowbar has no obvious effect." in _do(g, "kick crowbar")


def test_taunt_is_not_a_word():
    w, g = _at("BAR")
    assert 'I don\'t know the word "taunt".' in _do(g, "taunt may")


# --- RUB / TOUCH / FEEL / PAT / PET (mechanics.md — Parser Verbs) ---------------

@pytest.mark.parametrize("verb", ["rub", "touch", "feel", "pat", "pet"])
def test_rub_an_npc_and_a_thing(verb):
    w, g = _at("BAR")
    _give(w, "CROWBAR")
    assert "May wouldn't appreciate that." in _do(g, f"{verb} may")
    assert "Fiddling with the crowbar has no effect." in _do(g, f"{verb} crowbar")


@pytest.mark.parametrize("cmd", ["rub paper", "rub charcoal on paper", "rub engraving with charcoal"])
def test_the_rubbing_from_the_paper_or_charcoal(cmd):
    w, g = _at("INSCRIPTION-CHAMBER")
    _give(w, "THIN-PAPER")
    _give(w, "CHARCOAL")
    assert "You press the thin paper flat against the carved wall" in _do(g, cmd)


# --- SWING / THRUST (mechanics.md — Parser Verbs) -------------------------------

@pytest.mark.parametrize("verb", ["swing", "thrust"])
def test_swing_at_an_enemy_is_attack_with(verb):
    w, g = _at("BACK-ALLEY", "MUGGER-SPOTTED")
    _give(w, "CROWBAR")
    mugger = w.objects["MUGGER"]
    mugger.clear_flag("INVISIBLE")
    w.move_object(mugger, w.here)
    seen = []
    with patch("content.verbs._fight",
               lambda world, obj: seen.append((world.prsa, obj.name, world.prsi.name))):
        _do(g, f"{verb} crowbar at mugger")
    assert seen == [("V-MELEE", "MUGGER", "CROWBAR")]


def test_swing_alone_and_at_a_non_enemy():
    w, g = _at("BAR")
    _give(w, "CROWBAR")
    assert "Whoosh!" in _do(g, "swing crowbar")
    assert "You can't fight May." in _do(g, "swing crowbar at may")


# --- THROW (mechanics.md — Parser Verbs) ----------------------------------------

@pytest.mark.parametrize("verb", ["throw", "hurl", "chuck", "toss"])
def test_throw_alone_is_drop(verb):
    w, g = _at("TOWN-SQUARE")
    _give(w, "CROWBAR")
    assert "You drop the crowbar." in _do(g, f"{verb} crowbar")
    assert w.objects["CROWBAR"].location is w.here


@pytest.mark.parametrize("target", ["statue", "may"])
def test_throw_at_anything_keeps_it(target):
    w, g = _at("BAR" if target == "may" else "TOWN-SQUARE")
    _give(w, "CROWBAR")
    assert "You'd rather keep hold of the crowbar." in _do(g, f"throw crowbar at {target}")
    assert w.objects["CROWBAR"].location is w.player
