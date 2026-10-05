"""
The dragon-nip under Will's nightstand: a silent Very Hard (18) perception
check (locations.md — Will Passion's Bedroom; quests.md — Quest 58).
Run with: pytest roundabout/test_sprig_check.py  (from c:\\zork_awt)
"""

import sys
import os
from unittest.mock import patch
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world
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
