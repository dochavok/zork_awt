"""
KNOCK [ON / AT] X, LOCK X and PICK X (mechanics.md — Parser Verbs): doors, the speaking wall
(locations.md — Tool Alcove), the Dankhaus door (Bog of Eternal Stench (SE)),
the White House door (West of House), and anything else.
Run with: pytest roundabout/test_knock.py  (from c:\\zork_awt)
"""

import sys
import os
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do
from content.verbs import _LITLOCK_UNKNOWN, _LITLOCK_OPEN
from content.ink import LITLOCK_DOOR
from content.tool_alcove import _ASKS
from content.init import WHITE_HOUSE_KNOCK

_JOKE = "What does this look like? A Great Underground Empire?"


def _at(room, *flags):
    w, g = _make_world()
    w.set_global("LIGHT-SPELL-ACTIVE", True)
    for flag in flags:
        w.set_global(flag, True)
    w.move_object(w.player, w.rooms[room])
    w.here = w.rooms[room]
    return w, g


@pytest.mark.parametrize("cmd", ["knock on door", "knock at door", "knock door", "rap on door"])
def test_a_door_nobody_home(cmd):
    w, g = _at("KITCHEN")
    assert "Nobody's home." in _do(g, cmd)


def test_anything_else():
    w, g = _at("TOWN-SQUARE")
    crowbar = w.objects["CROWBAR"]
    crowbar.clear_flag("INVISIBLE")
    w.move_object(crowbar, w.player)
    assert "Why knock on the crowbar?" in _do(g, "knock on crowbar")


def test_the_speaking_wall_asks_once_found():
    w, g = _at("TOOL-ALCOVE")
    w.set_global("ALCOVE-FOUND", True)
    assert _ASKS in _do(g, "knock on wall")
    w.set_global("ALCOVE-OPEN", True)
    assert _ASKS not in _do(g, "knock on wall")


@pytest.mark.parametrize("flags,line", [
    ((), _LITLOCK_UNKNOWN),
    (("DANKHAUS-INVITED",), _LITLOCK_OPEN),
    (("INKED",), LITLOCK_DOOR),
    (("DANKHAUS-INVITED", "INKED"), LITLOCK_DOOR),
])
def test_the_dankhaus_door(flags, line):
    w, g = _at("BOG-SE", "DANKHAUS-PATH-FOUND", *flags)
    w.objects["DANKHAUS"].clear_flag("INVISIBLE")
    for cmd in ("knock on door", "knock on yurt"):
        assert line in _do(g, cmd)
        assert w.here.name == "BOG-SE"


def test_the_dankhaus_door_before_the_path_gives_nothing_away():
    w, g = _at("BOG-SE")
    out = _do(g, "knock on door")
    assert "You can't see any door here!" in out
    assert "yurt" not in out


def _opening():
    w, g = _make_world()
    w.move_object(w.player, w.rooms["WHITE-HOUSE"])
    w.here = w.rooms["WHITE-HOUSE"]
    return w, g


@pytest.mark.parametrize("cmd", ["knock on door", "knock on house", "knock door", "rap on front door"])
def test_white_house_knock_is_rewarded(cmd):
    w, g = _opening()
    assert WHITE_HOUSE_KNOCK in _do(g, cmd)


@pytest.mark.parametrize("cmd", ["open door", "examine house", "take boards"])
def test_white_house_anything_else_is_the_joke(cmd):
    w, g = _opening()
    assert _JOKE in _do(g, cmd)


# --- LOCK (mechanics.md — Parser Verbs) ----------------------------------------

from content.verbs import _RELOCK


@pytest.mark.parametrize("room,flag", [
    ("KITCHEN", "CELLAR-DOOR-UNLOCKED"),
    ("MID-TIER-KEY-DOOR", "KEY-DOOR-UNLOCKED"),
])
def test_lock_a_door_you_unlocked(room, flag):
    w, g = _at(room)
    crowbar = w.objects["CROWBAR"]
    crowbar.clear_flag("INVISIBLE")
    w.move_object(crowbar, w.player)
    assert "You can't lock that." in _do(g, "lock door")       # still locked
    w.set_global(flag, True)
    assert _RELOCK in _do(g, "lock door")
    assert _RELOCK in _do(g, "lock door with crowbar")


def test_lock_anything_else():
    w, g = _at("TOWN-SQUARE")
    crowbar = w.objects["CROWBAR"]
    crowbar.clear_flag("INVISIBLE")
    w.move_object(crowbar, w.player)
    assert "You can't lock that." in _do(g, "lock crowbar")


# --- PICK (mechanics.md — Parser Verbs; locations.md — Mine Passage) ------------

from content.verbs import _UNPICKABLE
from content.mid_tier import _CHEST_LOCKED, _CHEST_PICKED


@pytest.mark.parametrize("cmd", ["pick lock", "pick chest"])
def test_pick_the_chest_with_the_lockpicks(cmd):
    w, g = _at("MINE-PASSAGE")
    picks = w.objects["LOCKPICKS"]
    picks.clear_flag("INVISIBLE")
    w.move_object(picks, w.player)
    zenni = w.globals["zenni"]
    assert _CHEST_PICKED in _do(g, cmd)
    assert w.globals["zenni"] == zenni + 20


def test_pick_the_chest_without_them():
    w, g = _at("MINE-PASSAGE")
    assert _CHEST_LOCKED in _do(g, "pick lock")


@pytest.mark.parametrize("room", ["MID-TIER-KEY-DOOR", "KITCHEN"])
def test_keyed_doors_cannot_be_picked(room):
    w, g = _at(room)
    assert _UNPICKABLE in _do(g, "pick lock")
    assert _UNPICKABLE in _do(g, "pick door")


def test_pick_a_takeable_thing_is_take():
    w, g = _at("TOWN-SQUARE")
    crowbar = w.objects["CROWBAR"]
    crowbar.clear_flag("INVISIBLE")
    w.move_object(crowbar, w.here)
    _do(g, "pick crowbar")
    assert crowbar.location is w.player


def test_pick_anything_else():
    w, g = _at("TOWN-SQUARE")
    assert "You can't pick that." in _do(g, "pick statue")
