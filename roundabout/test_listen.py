"""
LISTEN default lines (mechanics.md): plain LISTEN, LISTEN TO an object, and
LISTEN TO an NPC — passive, never a stand-in for TALK TO. The Whispering
Jar and the Tool Alcove keep their own lines.
Run with: pytest roundabout/test_listen.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do


def _goto(w, name):
    w.move_object(w.player, w.rooms[name])
    w.here = w.rooms[name]


def test_plain_listen():
    w, g = _make_world(cls="warrior")
    assert "You hear nothing out of the ordinary." in _do(g, "listen")


def test_listen_to_object():
    w, g = _make_world(cls="warrior")
    assert "The fountain makes no sound." in _do(g, "listen to fountain")


def test_listen_to_npc_is_passive():
    from content.quests import get_state
    w, g = _make_world(cls="mage")
    before = get_state(w, "54")
    out = _do(g, "listen to knight")
    assert "The Redcrosse Knight isn't saying anything right now." in out
    assert get_state(w, "54") == before


def test_listen_to_named_npc():
    w, g = _make_world(cls="warrior")
    _goto(w, "KITCHEN")
    assert "Shamus isn't saying anything right now." in _do(g, "listen to shamus")


def test_jar_keeps_its_hum():
    w, g = _make_world(cls="warrior")
    _goto(w, "PIPE-ROOM")
    out = _do(g, "listen")
    assert "low, steady hum" in out
    assert "nothing out of the ordinary" not in out


def test_tool_alcove_keeps_its_line_once_found():
    w, g = _make_world(cls="warrior")
    _goto(w, "TOOL-ALCOVE")
    w.set_global("ALCOVE-FOUND", True)
    w.set_global("LIGHT-SPELL-ACTIVE", True)
    out = _do(g, "listen")
    assert out.strip()
    assert "nothing out of the ordinary" not in out
