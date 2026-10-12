"""
The Toll Bridge Boggart's toll (npcs.md — Boggart; locations.md — The Toll
Bridge): he asks for "two hundred" of something he never names, and no amount
of Zenni pays it.
Run with: pytest roundabout/test_toll_bridge.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do
from content.tunnels import _TOLL, _PAY_REFUSED, _BLOCKED
from content.verbs import _JUST_GO


def _at_bridge(zenni=10):
    w, g = _make_world(zenni=zenni)
    w.set_global("SEAL-FOUND", True)   # keep the seal discovery out of the output
    w.move_object(w.player, w.rooms["TOLL-BRIDGE"])
    w.here = w.rooms["TOLL-BRIDGE"]
    return w, g


def test_talk_names_no_currency():
    w, g = _at_bridge()
    out = _do(g, "talk to boggart")
    assert _TOLL in out
    assert "Zenni" not in out


def test_pay_refused_even_with_200_zenni():
    w, g = _at_bridge(zenni=250)
    out = _do(g, "pay boggart")
    assert _PAY_REFUSED in out
    assert w.globals["zenni"] == 250
    assert not w.get_global("BOGGART-GONE")


def test_cross_with_the_boggart_there_is_his_refusal():
    w, g = _at_bridge()
    moves = w.moves
    for cmd in ("cross", "cross bridge"):
        out = _do(g, cmd)
        assert _BLOCKED in out and _JUST_GO not in out
    assert w.here.name == "TOLL-BRIDGE"
    assert w.moves == moves + 2          # as walking south would


def test_cross_with_the_boggart_gone_points_the_way():
    w, g = _at_bridge()
    w.set_global("BOGGART-GONE", True)
    moves = w.moves
    assert _JUST_GO in _do(g, "cross bridge")
    assert w.moves == moves and w.here.name == "TOLL-BRIDGE"


def test_cross_on_the_rickety_bridge_points_the_way():
    w, g = _make_world()
    w.set_global("LIGHT-SPELL-ACTIVE", True)
    w.move_object(w.player, w.rooms["RICKETY-BRIDGE"])
    w.here = w.rooms["RICKETY-BRIDGE"]
    assert _JUST_GO in _do(g, "cross")
