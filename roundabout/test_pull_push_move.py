"""
PULL / MOVE / PUSH default lines (mechanics.md). PULL and MOVE follow Zork's
V-MOVE (gverbs.zil); PUSH has one fixed line. Rooms and objects with their
own lines (Flooding Room levers, wax seal) keep them.
Run with: pytest roundabout/test_pull_push_move.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do


def _world():
    w, g = _make_world(cls="warrior")
    w.move_object(w.objects["ROPE"], w.player)
    return w, g


def test_pull_and_move_fixed_object():
    w, g = _world()
    for verb in ("pull", "tug", "yank", "move"):
        assert "You can't move the fountain." in _do(g, f"{verb} fountain"), verb


def test_pull_and_move_takeable_object():
    w, g = _world()
    for verb in ("pull", "move"):
        assert "Moving the coil of rope reveals nothing." in _do(g, f"{verb} rope"), verb


def test_push_object():
    w, g = _world()
    assert "Pushing the fountain has no effect." in _do(g, "push fountain")
    assert "Pushing the coil of rope has no effect." in _do(g, "push rope")


def test_npc_line():
    w, g = _world()
    for verb in ("pull", "move", "push"):
        out = _do(g, f"{verb} knight")
        assert "The Redcrosse Knight wouldn't appreciate that." in out, verb


def test_wax_seal_keeps_its_line():
    from content import whispering_jar
    w, g = _world()
    seal = w.objects["WAX-SEAL"]
    seal.flags.discard("INVISIBLE")       # found in the Upper Hall cabinet
    w.move_object(seal, w.player)
    out = _do(g, "push seal")
    assert whispering_jar._NO_JAR_SEAL in out
    assert "has no effect" not in out


def test_flooding_levers_keep_their_lines():
    w, g = _world()
    w.move_object(w.player, w.rooms["FLOODING-ROOM"])
    w.here = w.rooms["FLOODING-ROOM"]
    w.set_global("LIGHT-SPELL-ACTIVE", True)
    from content import flooding
    assert flooding._LEFT in _do(g, "pull left lever")
