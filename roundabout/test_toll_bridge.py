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
from content.tunnels import _TOLL, _PAY_REFUSED


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
