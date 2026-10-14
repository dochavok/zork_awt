"""
Stairs and places (mechanics.md — Parser Verbs, Stairs and places; TODO #15,
2026-10-14): CLIMB / GO UP / DOWN STAIRS, ASCEND / DESCEND, UPSTAIRS /
DOWNSTAIRS, "Up or down?", the wrong way, EXAMINE STAIRS, the stairs only
where the room shows them; ENTER MINE, ENTER CRYPT, GO THROUGH ARCH, bare
ENTER / IN.
Run with: pytest roundabout/test_stairs_and_places.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import pytest

from test_room_exits import _look, _do
from content import ways

LEAD_UP, LEAD_DOWN, LEAD_BOTH = "The stairs lead up.", "The stairs lead down.", "The stairs lead up and down."
ONLY_UP, ONLY_DOWN = "The stairs only go up.", "The stairs only go down."
CANT_SEE = "You can't see any stairs here!"


def _go(room, command, **globals_):
    w, g, _ = _look(room, **globals_)
    out = _do(g, command)
    return w, out


# --- Stairs ------------------------------------------------------------------------

@pytest.mark.parametrize("command", [
    "climb stairs", "climb up stairs", "go up stairs", "walk up stairs", "ascend",
    "ascend stairs", "upstairs", "go upstairs", "take stairs", "use stairs", "climb steps",
    "climb staircase",
])
def test_up_the_tavern_stairs(command):
    w, _ = _go("TALE-AND-ALE", command)
    assert w.here.name == "UPSTAIRS-HALL"


@pytest.mark.parametrize("command", ["climb down stairs", "go down stairs", "descend stairs",
                                     "descend"])
def test_the_wrong_way(command):
    w, out = _go("TALE-AND-ALE", command)
    assert ONLY_UP in out
    assert w.here.name == "TALE-AND-ALE"


@pytest.mark.parametrize("command", ["climb stairs", "take stairs", "climb staircase"])
def test_both_ways_asks_without_a_turn(command):
    w, g, _ = _look("UPPER-HALL")
    moves = w.moves
    out = _do(g, command)
    assert ways.UP_OR_DOWN in out
    assert w.here.name == "UPPER-HALL"
    assert w.moves == moves                      # no turn, as TURN DIAL
    _do(g, "up")                                 # the answer is a command
    assert w.here.name == "TOWN-HALL-TOWER"


@pytest.mark.parametrize("command, dest", [
    ("climb up stairs", "TOWN-HALL-TOWER"), ("go down stairs", "TOWN-HALL"),
    ("upstairs", "TOWN-HALL-TOWER"), ("downstairs", "TOWN-HALL"),
])
def test_both_ways_with_a_direction(command, dest):
    w, _ = _go("UPPER-HALL", command)
    assert w.here.name == dest


@pytest.mark.parametrize("room, dest", [
    ("UPSTAIRS-HALL", "TALE-AND-ALE"), ("TOWN-HALL", "UPPER-HALL"),
    ("TOWN-HALL-TOWER", "UPPER-HALL"), ("MAUSOLEUM", "CRYPT"), ("CRYPT", "MAUSOLEUM"),
    ("CHARNEL-WALK", "CRYPT"), ("CELLAR", "KITCHEN"), ("PYRONICUS-FORGE", "VOLCANO"),
    ("KEY-DOOR-LANDING", "MID-TIER-KEY-DOOR"),
])
def test_climb_stairs_goes_the_only_way(room, dest):
    w, _ = _go(room, "climb stairs")
    assert w.here.name == dest


def test_the_crypts_way_down_is_not_stairs():
    w, out = _go("CRYPT", "climb down stairs")
    assert ONLY_UP in out
    w, _ = _go("CRYPT", "descend")                # the sloping passage is still DOWN
    assert w.here.name == "CHARNEL-WALK"


def test_the_landing_stairs_go_north():
    w, _ = _go("KEY-DOOR-LANDING", "ascend")
    assert w.here.name == "MID-TIER-KEY-DOOR"
    w, _ = _go("KEY-DOOR-LANDING", "climb up stairs")
    assert w.here.name == "MID-TIER-KEY-DOOR"


def test_the_lighthouse_stair_is_chained():
    w, out = _go("LIGHTHOUSE", "climb stairs")
    assert "KEEPER ONLY" in out
    assert w.here.name == "LIGHTHOUSE"


@pytest.mark.parametrize("room, globals_, text", [
    ("TALE-AND-ALE", {}, LEAD_UP), ("UPSTAIRS-HALL", {}, LEAD_DOWN), ("UPPER-HALL", {}, LEAD_BOTH),
    ("MID-TIER-KEY-DOOR", {"KEY_DOOR_UNLOCKED": True}, LEAD_DOWN),
])
def test_examine_stairs(room, globals_, text):
    _, out = _go(room, "examine stairs", **globals_)
    assert text in out


@pytest.mark.parametrize("room, globals_", [
    ("KITCHEN", {}), ("VOLCANO", {}), ("MID-TIER-KEY-DOOR", {}), ("TOWN-SQUARE", {}),
])
def test_no_stairs_where_the_room_shows_none(room, globals_):
    _, out = _go(room, "climb stairs", **globals_)
    assert CANT_SEE in out


@pytest.mark.parametrize("globals_, dest", [
    ({"CELLAR_DOOR_UNLOCKED": True, "CELLAR_DOOR_OPEN": True, "CELLAR_DRAINED": True}, "CELLAR"),
])
def test_the_cellar_steps_once_the_door_is_open(globals_, dest):
    w, _ = _go("KITCHEN", "climb stairs", **globals_)
    assert w.here.name == dest


def test_the_volcano_stairs_once_found():
    w, _ = _go("VOLCANO", "descend stairs", VOLCANO_STAIRS_FOUND=True)
    assert w.here.name == "PYRONICUS-FORGE"


# --- Places ------------------------------------------------------------------------

@pytest.mark.parametrize("command", ["enter mine", "enter mine entrance", "go into mine",
                                     "go in mine", "enter", "in", "go in"])
def test_enter_the_mine(command):
    w, _ = _go("ROUNDABOUT-FOREST", command)
    assert w.here.name == "MINE-ENTRANCE"


def test_examine_mine():
    _, out = _go("ROUNDABOUT-FOREST", "examine mine")
    assert "a dark mouth leading down into the ground" in out


@pytest.mark.parametrize("command", ["enter crypt", "go through arch", "go into crypt",
                                     "enter arch", "enter", "in"])
def test_into_the_crypt(command):
    w, _ = _go("CHARNEL-WALK", command)
    assert w.here.name == "CRYPT"


def test_examine_arch():
    _, out = _go("CHARNEL-WALK", "examine arch")
    assert ways.ARCH in out


def test_bare_enter_with_no_place_is_unchanged():
    w, out = _go("TOWN-SQUARE", "enter")
    assert "You can't go in there." in out
    w, out = _go("TOWN-SQUARE", "in")
    assert "You can't go that way." in out
