"""
Perception (mechanics.md — Perception mechanic, Difficulty tiers, Enchanted
Glasses; experience.md — Second Glance at Level 5). Checks are played through
real room entries; the player's level roll is fixed per check.

Design tiers used here: Easy 5 (Prayer Alcove niche), Medium 9 (Back Alley
mugger; Tool Alcove door), Hard 14 (the volcano's staircase).
Run with: pytest roundabout/test_perception.py  (from c:\\zork_awt)
"""

import sys
import os
import io
from unittest.mock import patch
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do


def _enter(g, w, room, rolls):
    """Walk into `room` (M_ENTER fires) with the level rolls fixed in order."""
    with patch("content.player.roll", side_effect=list(rolls) + [0] * 5), \
         patch("sys.stdout", io.StringIO()):
        g.enter_room(w.rooms[room])


def _world(cls="warrior", level=1):
    w, g = _make_world(cls=cls, level=level, zenni=10)
    w.move_object(w.objects["TORCH"], w.player)        # light for the dungeon rooms
    from content import light
    light.light_torch(w)
    return w, g


def _spotted(w):
    return bool(w.get_global("MUGGER-SPOTTED"))


# --- Difficulty tiers through real checks ------------------------------------------

@pytest.mark.parametrize("room,flag,target", [
    ("PRAYER-ALCOVE", "NICHE-FOUND", 5),               # Easy
    ("TOOL-ALCOVE", "ALCOVE-FOUND", 9),                # Medium
    ("VOLCANO", "VOLCANO-STAIRS-FOUND", 14),           # Hard
])
def test_tier_targets(room, flag, target):
    w, g = _world()
    _enter(g, w, room, [target - 1])
    assert not w.get_global(flag)
    w, g = _world()
    _enter(g, w, room, [target])
    assert w.get_global(flag)


# --- Repeating vs once-per-visit ---------------------------------------------------

def test_repeating_check_fires_every_visit_until_found():
    w, g = _world()
    for _ in range(3):
        _enter(g, w, "TOWN-SQUARE", [])
        _enter(g, w, "BACK-ALLEY", [1])
        assert not _spotted(w)
    _enter(g, w, "TOWN-SQUARE", [])
    _enter(g, w, "BACK-ALLEY", [9])
    assert _spotted(w)


@pytest.mark.parametrize("room,flag,target", [
    ("TOOL-ALCOVE", "ALCOVE-FOUND", 9),
    ("PRAYER-ALCOVE", "NICHE-FOUND", 5),
])
def test_once_per_visit_needs_a_return(room, flag, target):
    w, g = _world()
    _enter(g, w, room, [1])                                    # missed on arrival
    with patch("content.player.roll", return_value=99):
        _do(g, "look")
        _do(g, "wait")
    assert not w.get_global(flag)                              # no second try this visit
    _enter(g, w, "TOWN-SQUARE", [])
    _enter(g, w, room, [target])                               # back again: a fresh roll
    assert w.get_global(flag)


def test_found_is_permanent():
    w, g = _world()
    _enter(g, w, "VOLCANO", [14])
    assert w.get_global("VOLCANO-STAIRS-FOUND")
    _enter(g, w, "TOWN-SQUARE", [])
    _enter(g, w, "VOLCANO", [1])                               # a failed roll later
    with patch("content.player.roll", return_value=1):
        _do(g, "down")
    assert w.here.name == "PYRONICUS-FORGE"


def test_hidden_exit_blocked_until_found():
    w, g = _world()
    _enter(g, w, "VOLCANO", [1])
    with patch("content.player.roll", return_value=1):
        assert "You can't go that way." in _do(g, "down")
    assert w.here.name == "VOLCANO"


# --- Second Glance (Level 5): one silent second roll on a failure --------------------

def test_second_glance_from_level_five():
    w, g = _world(level=5)
    _enter(g, w, "BACK-ALLEY", [1, 9])
    assert _spotted(w)


def test_no_second_glance_below_level_five():
    w, g = _world(level=4)
    _enter(g, w, "BACK-ALLEY", [1, 9])
    assert not _spotted(w)


def test_second_glance_is_only_one_reroll():
    w, g = _world(level=5)
    _enter(g, w, "BACK-ALLEY", [1, 1, 9])
    assert not _spotted(w)


# --- Class bonus: Mages and Rogues, not Warriors ---------------------------------------

@pytest.mark.parametrize("cls,spots", [("warrior", False), ("mage", True), ("rogue", True)])
def test_class_perception_bonus(cls, spots):
    w, g = _world(cls=cls)
    _enter(g, w, "BACK-ALLEY", [8])                            # one short of Medium 9
    assert _spotted(w) is spots


# --- The glasses ---------------------------------------------------------------------

def _wearing_glasses(enchanted):
    w, g = _world()
    glasses = w.objects["ENCHANTED-GLASSES"]
    glasses.flags.discard("INVISIBLE")
    w.move_object(glasses, w.player)
    if enchanted:
        w.set_global("GLASSES-ENCHANTED", True)
    _do(g, "wear glasses")
    return w, g


def test_enchanted_glasses_small_bonus():
    w, g = _wearing_glasses(enchanted=False)
    _enter(g, w, "BACK-ALLEY", [8])                            # one short without them
    assert _spotted(w)


def test_glasses_only_while_worn():
    w, g = _wearing_glasses(enchanted=False)
    _do(g, "remove glasses")
    _enter(g, w, "BACK-ALLEY", [8])
    assert not _spotted(w)


def test_actually_enchanted_glasses_pass_everything():
    w, g = _wearing_glasses(enchanted=True)
    _enter(g, w, "VOLCANO", [0])                               # Hard, with a roll of 0
    assert w.get_global("VOLCANO-STAIRS-FOUND")
