"""
The dragon-nip under Will's nightstand: a silent Level 4 (18) perception check,
or LOOK UNDER NIGHTSTAND with no roll; LOOK IN / LOOK UNDER defaults (mechanics.md)
(locations.md — Will Passion's Bedroom; quests.md — Quest 58).
Run with: pytest roundabout/test_sprig_check.py  (from c:\\zork_awt)
"""

import sys
import os
from unittest.mock import patch
sys.path.insert(0, os.path.dirname(__file__))

from testkit import _make_world
from content import bedroom
from engine.world import INVISIBLE


def _check(total):
    """Run the check with the perception roll (class bonus included) fixed."""
    w, g = _make_world(cls="mage", level=3)
    w.move_object(w.player, w.rooms[bedroom.BEDROOM])
    w.here = w.rooms[bedroom.BEDROOM]
    with patch("content.player.roll_class_bonus", return_value=total):
        bedroom.check_sprig(w)
    return not w.objects["DRAGON-NIP"].has_flag(INVISIBLE)


def test_seventeen_misses():
    assert not _check(17)


def test_eighteen_finds_it():
    assert _check(18)


# LOOK UNDER NIGHTSTAND finds it outright, no roll (locations.md)

def _bedroom():
    from test_knight import _do
    w, g = _make_world(cls="mage", level=3)
    w.move_object(w.player, w.rooms[bedroom.BEDROOM])
    w.here = w.rooms[bedroom.BEDROOM]
    return w, g, _do


def test_look_under_nightstand_finds_it_without_a_roll():
    w, g, _do = _bedroom()
    with patch("content.player.roll_class_bonus", return_value=1):
        out = _do(g, "look under nightstand")
    assert bedroom.SPRIG_FOUND in out
    assert not w.objects["DRAGON-NIP"].has_flag(INVISIBLE)
    assert bedroom.SPRIG_LDESC in _do(g, "look under nightstand")    # still there


def test_look_under_nightstand_once_taken():
    w, g, _do = _bedroom()
    _do(g, "look under nightstand")
    _do(g, "take sprig")
    assert w.objects["DRAGON-NIP"].location is w.player
    assert bedroom.NOTHING_UNDER in _do(g, "look under nightstand")
    _do(g, "drop sprig")                                              # on the floor now
    assert bedroom.NOTHING_UNDER in _do(g, "look under nightstand")


def test_look_in_is_examine_and_under_is_dust():
    w, g, _do = _bedroom()
    nightstand_examine = w.objects["NIGHTSTAND"].examine
    assert nightstand_examine and nightstand_examine[:30] in _do(g, "look in nightstand")
    crowbar = w.objects["CROWBAR"]
    crowbar.clear_flag(INVISIBLE)
    w.move_object(crowbar, w.player)
    assert bedroom.NOTHING_UNDER in _do(g, "look under crowbar")


def test_the_bed():
    w, g, _do = _bedroom()
    assert "made with the perfunctory neatness" in _do(g, "examine bed")
    assert bedroom.UNDER_BED in _do(g, "look under bed")
    assert w.objects["DRAGON-NIP"].has_flag(INVISIBLE)        # not a way to find it
