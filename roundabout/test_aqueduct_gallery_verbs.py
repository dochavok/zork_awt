"""
Quest 22 / Quest 38 phrasings (locations.md — Collapsed Aqueduct and Collapsed
Gallery; TODO #15, 2026-10-14): every way of saying PLACE BLOCKS, EXAMINE on the
aqueduct, PRY TIMBER with the pickaxe, the crowbar's near-miss line and
EXAMINE TIMBERS.
Run with: pytest roundabout/test_aqueduct_gallery_verbs.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from unittest.mock import patch
import pytest

from test_room_exits import _look, _do
from content import aqueduct


def _strong():
    return patch("content.player.roll", return_value=99)


def _give(w, *names):
    for n in names:
        o = w.objects[n]
        o.flags.discard("INVISIBLE")
        w.move_object(o, w.player)


# --- Collapsed Aqueduct ---------------------------------------------------------------

@pytest.mark.parametrize("command", [
    "place block", "put block", "lift block", "lift blocks", "raise block", "heave block",
    "replace block", "move block", "push block", "put block in gap", "put block in channel",
    "put block on aqueduct", "push block into gap",
])
def test_every_way_of_placing_a_block(command):
    w, g, _ = _look("COLLAPSED-AQUEDUCT")
    with _strong():
        assert aqueduct._PLACED[0] in _do(g, command)
    assert w.get_global("BLOCKS-PLACED") == 1


def test_a_weak_lift_still_slips():
    w, g, _ = _look("COLLAPSED-AQUEDUCT")
    with patch("content.player.roll", return_value=1):
        assert aqueduct._SLIPS in _do(g, "lift block")
    assert not w.get_global("BLOCKS-PLACED")


def test_take_block_is_still_too_heavy():
    w, g, _ = _look("COLLAPSED-AQUEDUCT")
    assert aqueduct._TOO_HEAVY in _do(g, "take block")


@pytest.mark.parametrize("command", ["examine blocks", "examine gap", "examine aqueduct",
                                     "examine channel"])
def test_examine_follows_the_blocks(command):
    w, g, _ = _look("COLLAPSED-AQUEDUCT")
    for n in range(4):
        w.set_global("BLOCKS-PLACED", n)
        assert aqueduct._BLOCKS_STATE[n] in _do(g, command)
    w.set_global("AQUEDUCT-SEALED", True)
    assert aqueduct._WHOLE in _do(g, command)


# --- Collapsed Gallery ----------------------------------------------------------------

@pytest.mark.parametrize("command", ["pry timber", "pry timber with pickaxe",
                                     "lever timber with pickaxe"])
def test_prying_with_the_pickaxe_is_a_swing(command):
    w, g, _ = _look("COLLAPSED-GALLERY")
    _give(w, "PICKAXE", "CROWBAR")
    with _strong():
        assert aqueduct._TIMBER_DOWN[0] in _do(g, command)
    assert w.get_global("TIMBERS-DOWN") == 1


@pytest.mark.parametrize("command", ["pry timber", "pry timber with crowbar",
                                     "lever timber with crowbar", "use crowbar on timber"])
def test_the_crowbar_points_to_breaking(command):
    w, g, _ = _look("COLLAPSED-GALLERY")
    _give(w, "CROWBAR")
    with _strong():
        out = _do(g, command)
    assert aqueduct._CROWBAR_WONT in out
    assert "leverage" not in out
    assert not w.get_global("TIMBERS-DOWN")


def test_the_crowbar_named_with_the_pickaxe_held_still_fails():
    w, g, _ = _look("COLLAPSED-GALLERY")
    _give(w, "PICKAXE", "CROWBAR")
    assert aqueduct._CROWBAR_WONT in _do(g, "pry timber with crowbar")


def test_examine_timbers():
    w, g, _ = _look("COLLAPSED-GALLERY")
    assert aqueduct._TIMBERS in _do(g, "examine timbers")
    w.set_global("TIMBERS-DOWN", 3)
    assert aqueduct._NO_TIMBERS in _do(g, "examine timbers")


def test_prying_after_all_three_are_down():
    w, g, _ = _look("COLLAPSED-GALLERY")
    _give(w, "CROWBAR")
    w.set_global("TIMBERS-DOWN", 3)
    assert aqueduct._NO_TIMBERS in _do(g, "pry timber")
