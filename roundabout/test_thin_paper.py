"""
Thin paper is destroyed by the Flooding Room sweep (items.md — Thin Paper;
traps.md — Trap 41), and is back on Shamus's slate.
Run with: pytest roundabout/test_thin_paper.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do

RUINED = "The thin paper didn't survive the trip. What's left of it comes apart in your fingers."
SWEPT = "The water closes over your head and the floor drops away."


def _flooding(carry=("THIN-PAPER",)):
    w, g = _make_world()
    for name in carry:
        obj = w.objects[name]
        obj.flags.discard("INVISIBLE")
        w.move_object(obj, w.player)
    room = w.rooms["FLOODING-ROOM"]
    w.move_object(w.player, room)
    w.here = room
    w.set_global("FLOOD-PLATE", "fired")
    w.set_global("FLOOD-TURNS", 1)               # the warning has been given
    w.set_global("FLOOD-JUST-OPENED", False)
    return w, g


def test_sweep_ruins_the_paper():
    w, g = _flooding()
    out = _do(g, "wait")
    assert w.here.name == "SPILLWAY"
    assert out.index(SWEPT) < out.index(RUINED)    # then the (dark) Spillway
    assert w.objects["THIN-PAPER"].location is None


def test_paper_back_on_the_slate():
    w, g = _flooding()
    _do(g, "wait")
    w.move_object(w.player, w.rooms["KITCHEN"])
    w.here = w.rooms["KITCHEN"]
    out = _do(g, "read slate")
    assert "Thin paper" in out and "2 Zenni" in out.split("Thin paper")[1].split("\n")[0]
    _do(g, "buy paper")
    assert w.objects["THIN-PAPER"].location is w.player


def test_no_paper_no_line():
    w, g = _flooding(carry=())
    out = _do(g, "wait")
    assert w.here.name == "SPILLWAY" and RUINED not in out


def test_rubbing_and_scrolls_survive():
    w, g = _flooding(carry=("THIN-PAPER", "RUBBING", "INCANTATION-SCROLL"))
    _do(g, "wait")
    assert w.objects["RUBBING"].location is w.player
    assert w.objects["INCANTATION-SCROLL"].location is w.player


def test_knee_deep_water_is_harmless():
    w, g = _flooding()
    w.set_global("FLOOD-TURNS", 0)               # first turn of the flood
    _do(g, "wait")
    assert w.here.name == "FLOODING-ROOM"
    assert w.objects["THIN-PAPER"].location is w.player
