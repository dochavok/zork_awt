"""
MELT X [WITH Y] (mechanics.md — Parser Verbs) and the Fountain Room ice
(locations.md — The Fountain Room): MELT ICE with no tool uses a carried torch.
Run with: pytest roundabout/test_melt.py  (from c:\\zork_awt)
"""

import sys
import os
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from testkit import _make_world, _do
from content.frozen_soldier import _THAW_1, _PLAIN_TORCH_LIT, _NO_HEAT


def _fountain(*carried):
    w, g = _make_world()
    w.set_global("LIGHT-SPELL-ACTIVE", True)
    w.move_object(w.player, w.rooms["FOUNTAIN-ROOM"])
    w.here = w.rooms["FOUNTAIN-ROOM"]
    for name in carried:
        obj = w.objects[name]
        obj.clear_flag("INVISIBLE")
        w.move_object(obj, w.player)
    return w, g


@pytest.mark.parametrize("cmd", ["melt ice", "thaw ice"])
def test_melt_ice_uses_the_ivory_torch(cmd):
    w, g = _fountain("IVORY-TORCH", "TORCH")
    assert _THAW_1 in _do(g, cmd)
    assert w.get_global("ICE-THAW") == 1


def test_melt_ice_with_only_the_ordinary_torch():
    w, g = _fountain("TORCH")
    from content import light
    import io, contextlib
    with contextlib.redirect_stdout(io.StringIO()):
        light.light_torch(w)
    assert _PLAIN_TORCH_LIT in _do(g, "melt ice")
    assert not w.get_global("ICE-THAW")


def test_melt_ice_with_no_torch():
    w, g = _fountain()
    assert _NO_HEAT in _do(g, "melt ice")


def test_melt_ice_with_the_wrong_thing():
    w, g = _fountain("CROWBAR")
    assert "The crowbar won't melt anything." in _do(g, "melt ice with crowbar")
    assert not w.get_global("ICE-THAW")


def test_melt_anything_else():
    w, g = _make_world()
    crowbar = w.objects["CROWBAR"]
    crowbar.clear_flag("INVISIBLE")
    w.move_object(crowbar, w.player)
    assert "It's not clear that the crowbar can be melted." in _do(g, "melt crowbar")
