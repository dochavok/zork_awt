"""
Lights on and off (mechanics.md — Parser Verbs, "Lights on and off"), and the
Zork verbs Roundabout drops (BOARD <thing>, BLOW IN, BLOW UP … WITH, INFLATE, FOLLOW, OIL, PUMP, SHAKE, SQUEEZE, WIND,
RING), and a known non-verb word first: "There was no verb in that sentence!"
Run with: pytest roundabout/test_light_verbs.py  (from c:\\zork_awt)
"""

import sys
import os
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do
from content.verbs import (
    _ALREADY_LIT, _IVORY_HEAT, _TORCH_STAYS_LIT, _LANTERN_STAYS_LIT, _NOT_LIT,
    _LANTERN_NOT_HELD,
)

_UNKNOWN = "That sentence isn't one I recognize."


def _world(*names):
    w, g = _make_world()
    for name in names:
        obj = w.objects[name]
        obj.clear_flag("INVISIBLE")
        w.move_object(obj, w.player)
    return w, g


@pytest.mark.parametrize("cmd", ["turn off torch", "extinguish torch", "blow out torch"])
def test_torch_cannot_be_put_out(cmd):
    w, g = _world("TORCH")
    assert _TORCH_STAYS_LIT in _do(g, cmd)


@pytest.mark.parametrize("cmd", ["turn on torch", "light torch"])
def test_torch_is_already_lit(cmd):
    w, g = _world("TORCH")
    assert _ALREADY_LIT in _do(g, cmd)


def test_ivory_torch_needs_no_lighting():
    w, g = _world("IVORY-TORCH")
    assert _IVORY_HEAT in _do(g, "turn on ivory torch")


def test_anything_else_cannot_be_turned_on_or_off():
    w, g = _world("CROWBAR")
    assert "You can't turn that on." in _do(g, "turn on crowbar")
    assert "You can't turn that off." in _do(g, "turn off crowbar")
    assert "You can't turn that off." in _do(g, "extinguish crowbar")


def test_lantern_unlit_and_not_held():
    w, g = _world("GUARDIANS-LANTERN")
    assert _NOT_LIT in _do(g, "turn off lantern")
    _do(g, "drop lantern")
    assert _LANTERN_NOT_HELD in _do(g, "turn on lantern")


def test_lantern_once_hung_stays_lit():
    w, g = _make_world()
    lantern = w.objects["GUARDIANS-LANTERN"]
    lantern.clear_flag("INVISIBLE")
    w.move_object(lantern, w.here)
    w.set_global("LANTERN-HUNG", True)
    assert _LANTERN_STAYS_LIT in _do(g, "turn off lantern")
    assert _ALREADY_LIT in _do(g, "turn on lantern")


@pytest.mark.parametrize("cmd", [
    "board crowbar", "blow in crowbar", "blow up crowbar with torch",
])
def test_zork_boat_sentences_are_not_recognized(cmd):
    w, g = _world("CROWBAR", "TORCH")
    assert _UNKNOWN in _do(g, cmd)


def test_inflate_is_not_a_word():
    w, g = _world("CROWBAR")
    assert 'I don\'t know the word "inflate".' in _do(g, "inflate crowbar")


def test_board_ship_still_boards():
    w, g = _make_world()
    assert "There's no ship to board here." in _do(g, "board ship")
    assert "There's no ship to board here." in _do(g, "board")


@pytest.mark.parametrize("verb", ["burn", "ignite", "incinerate"])
def test_burn_is_light(verb):
    from content.mine import _LIT
    w, g = _world("TORCH", "CROWBAR", "FLINT-AND-STEEL")
    assert _ALREADY_LIT in _do(g, f"{verb} torch")
    assert "You can't light the crowbar." in _do(g, f"{verb} crowbar")
    w.move_object(w.player, w.rooms["MINE-TUNNELS"])
    w.here = w.rooms["MINE-TUNNELS"]
    w.set_global("WEAK-POINT-FOUND", True)
    w.set_global("GUNPOWDER-PLACED", True)
    w.move_object(w.objects["GUNPOWDER"], w.here)
    assert _LIT in _do(g, f"{verb} gunpowder")
    assert w.get_global("FUSE-LIT")


def test_lighting_the_lit_fuse_again():
    from content.mine import _FUSE_BURNING
    w, g = _world("FLINT-AND-STEEL")
    w.move_object(w.player, w.rooms["MINE-TUNNELS"])
    w.here = w.rooms["MINE-TUNNELS"]
    w.set_global("WEAK-POINT-FOUND", True)
    w.set_global("GUNPOWDER-PLACED", True)
    w.move_object(w.objects["GUNPOWDER"], w.here)
    _do(g, "light gunpowder")
    assert _FUSE_BURNING in _do(g, "burn gunpowder")


@pytest.mark.parametrize("word", ["follow", "pursue", "chase", "come", "lubricate", "oil", "grease", "pump", "shake", "squeeze", "wind"])
def test_follow_is_not_a_word(word):
    w, g = _make_world()
    assert f'I don\'t know the word "{word}".' in _do(g, f"{word} may")


def _at_weak_point(*carried):
    w, g = _world(*carried)
    w.move_object(w.player, w.rooms["MINE-TUNNELS"])
    w.here = w.rooms["MINE-TUNNELS"]
    w.set_global("WEAK-POINT-FOUND", True)
    w.set_global("GUNPOWDER-PLACED", True)
    w.move_object(w.objects["GUNPOWDER"], w.here)
    return w, g


@pytest.mark.parametrize("torch", ["TORCH", "IVORY-TORCH"])
@pytest.mark.parametrize("cmd", [
    "hold torch near gunpowder", "light gunpowder with torch", "light gunpowder",
])
def test_a_torch_will_not_light_the_gunpowder(torch, cmd):
    from content.mine import _TORCH_NO
    w, g = _at_weak_point(torch)
    assert _TORCH_NO in _do(g, cmd)
    assert not w.get_global("FUSE-LIT")


def test_torch_refused_even_with_flint_when_asked_for():
    from content.mine import _TORCH_NO, _LIT
    w, g = _at_weak_point("TORCH", "FLINT-AND-STEEL")
    assert _TORCH_NO in _do(g, "light gunpowder with torch")
    assert _LIT in _do(g, "light gunpowder")          # flint and steel does it


def test_no_torch_no_flint():
    from content.mine import _NO_FLINT
    w, g = _at_weak_point()
    assert _NO_FLINT in _do(g, "light gunpowder")


def test_hold_anything_else_near():
    w, g = _world("TORCH", "CROWBAR")
    assert "Nothing happens." in _do(g, "hold torch near crowbar")


@pytest.mark.parametrize("cmd", ["ring crowbar", "ring", "statue", "crowbar"])
def test_a_known_word_first_has_no_verb(cmd):
    w, g = _make_world()
    assert "There was no verb in that sentence!" in _do(g, cmd)


@pytest.mark.parametrize("word", ["peal", "xyzzy"])
def test_unknown_words_are_still_unknown(word):
    w, g = _make_world()
    assert f'I don\'t know the word "{word}".' in _do(g, f"{word} crowbar")
