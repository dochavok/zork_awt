"""
The Tale and Ale mailbox is the way into Will's Tower; there is no mailbox in
the Tower itself (locations.md — Will's Wizard Tower, Connections).
Run with: pytest roundabout/test_tower_mailbox.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do


def _at(room):
    w, g = _make_world(cls="warrior")
    w.move_object(w.player, w.rooms[room])
    w.here = w.rooms[room]
    return w, g


def test_open_mailbox_in_tower_does_nothing():
    w, g = _at("WIZARDS-TOWER")
    out = _do(g, "open mailbox")
    assert "familiar warmth" not in out
    assert w.here.name == "WIZARDS-TOWER"


def test_open_mailbox_in_tavern_still_teleports():
    w, g = _at("TALE-AND-ALE")
    out = _do(g, "open mailbox")
    assert "familiar warmth" in out
    assert w.here.name == "WIZARDS-TOWER"
