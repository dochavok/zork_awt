"""
Quest 50: Will is shaken on the first tower arrival after the apprentice
comes home (npcs.md — Will Passion; quests.md — Quest 50).
Run with: pytest roundabout/test_will_shaken.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do

SHAKEN = ('Will is standing at the window when you arrive. He doesn\'t turn around. '
          '"Thank you," he says, to the glass. Then he sits back down, and that\'s the end of it.')


def _at_tavern(q50_done=True, inked=False):
    from content import quests
    w, g = _make_world()
    w.set_global("BEDROOM-DOOR-VISIBLE", True)      # keep the arrival quiet
    if q50_done:
        quests.complete(w, "50")
    if inked:
        w.set_global("INKED", True)
    w.move_object(w.player, w.rooms["TALE-AND-ALE"])
    w.here = w.rooms["TALE-AND-ALE"]
    return w, g


def test_shaken_on_first_arrival_before_room():
    w, g = _at_tavern()
    out = _do(g, "open mailbox")
    assert w.here.name == "WIZARDS-TOWER"
    assert out.index(SHAKEN) < out.index("Will's Wizard Tower") \
        < out.index("Will Passion sits at his desk, pen in hand.")


def test_only_once():
    w, g = _at_tavern()
    _do(g, "open mailbox")
    _do(g, "look at painting")                      # back to the Tale and Ale
    w.move_object(w.player, w.rooms["TALE-AND-ALE"])
    w.here = w.rooms["TALE-AND-ALE"]
    assert SHAKEN not in _do(g, "open mailbox")


def test_not_before_quest_50():
    w, g = _at_tavern(q50_done=False)
    assert SHAKEN not in _do(g, "open mailbox")
    assert not w.get_global("WILL-SHAKEN-SHOWN")


def test_fires_when_inked():
    w, g = _at_tavern(inked=True)
    assert SHAKEN in _do(g, "open mailbox")
