"""
Surface scenery and windows (TODO #15, 2026-10-14; locations.md under each
room, mechanics.md — Windows): the Altar and its dial, Will's desk and papers,
the library's catalogue, shelves and ledger, the fountain, the Upstairs Hall's
doors, floorboards and window, and the other windows' views.
Run with: pytest roundabout/test_surface_scenery.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import pytest

from testkit import _do, _look
from content import scenery as sc
from content.scenery import (TOWER_DESK, TOWER_PAPERS_WILL, TOWER_PAPERS_ALONE, CATALOGUE,
                             CATALOGUE_CARD, SHELVES, LEDGER, FOUNTAIN_DRY, FOUNTAIN_RUNNING,
                             ALTAR_EXAMINE, DIAL, HALL_DOORS, FLOORBOARDS, WINDOW_SHUT,
                             ALLEY_MUGGER, ALLEY_QUIET)
from content.tavern import ROOMS_RENTED


def _say(room, command, **globals_):
    w, g, _ = _look(room, **globals_)
    return w, g, _do(g, command)


# --- The Altar -----------------------------------------------------------------------

def test_examine_altar():
    _, _, out = _say("ALTAR", "examine altar")
    assert ALTAR_EXAMINE in out and "nothing special" not in out


@pytest.mark.parametrize("command", ["examine dial", "examine symbols", "examine marks"])
def test_examine_dial_names_the_glowing_symbol(command):
    w, g, out = _say("ALTAR", command)
    assert DIAL in out
    assert "The glow sits on the lantern — The Keepers of the Lantern." in out
    _do(g, "turn dial left")
    assert "The glow sits on the coin — The House of the Coin." in _do(g, command)


def test_the_nave_still_points_east():
    _, _, out = _say("CHURCH-NAVE", "examine altar")
    assert "The altar is through the archway to the east." in out


# --- Will's tower --------------------------------------------------------------------

def test_desk():
    _, _, out = _say("WIZARDS-TOWER", "examine desk")
    assert TOWER_DESK in out


@pytest.mark.parametrize("command", ["read papers", "examine papers", "search desk"])
def test_papers_with_and_without_will(command):
    _, _, out = _say("WIZARDS-TOWER", command)
    assert TOWER_PAPERS_WILL in out
    w, g, _ = _look("WIZARDS-TOWER")
    w.move_object(w.objects["WILL"], None)
    assert TOWER_PAPERS_ALONE in _do(g, command)


def test_search_desk_leaves_the_rooms_search():
    w, g, _ = _look("WIZARDS-TOWER")
    _do(g, "search desk")
    assert not w.get_global("SEARCHED-HERE")


# --- The library ---------------------------------------------------------------------

@pytest.mark.parametrize("command, text", [
    ("examine catalogue", CATALOGUE), ("examine card catalogue", CATALOGUE),
    ("search catalogue", CATALOGUE_CARD), ("open drawer", CATALOGUE_CARD),
    ("examine shelves", SHELVES), ("examine books", SHELVES),
])
def test_library_scenery(command, text):
    _, _, out = _say("LIBRARY", command)
    assert text in out


def test_the_ledger_only_after_her_scene():
    _, _, out = _say("LIBRARY", "read ledger")
    assert "You can't see any ledger here!" in out
    for command in ("read ledger", "examine ledger"):
        _, _, out = _say("LIBRARY", command, LIBRARIAN_MET=True)
        assert LEDGER in out


def test_the_ledger_is_not_a_pickup():
    w, g, _ = _say("LIBRARY", "take ledger", LIBRARIAN_MET=True)
    assert w.objects["LIBRARY-LEDGER"] not in w.player.contents


# --- The fountain --------------------------------------------------------------------

@pytest.mark.parametrize("command", ["examine fountain", "examine basin"])
def test_fountain(command):
    _, _, out = _say("TOWN-SQUARE", command)
    assert FOUNTAIN_DRY in out
    _, _, out = _say("TOWN-SQUARE", command, FOUNTAIN_RUNNING=True)
    assert FOUNTAIN_RUNNING in out


# --- Upstairs Hall and windows -------------------------------------------------------

@pytest.mark.parametrize("command", ["look out window", "look out of window",
                                     "look through window", "examine window"])
def test_the_hall_window_shows_the_alley(command):
    _, _, out = _say("UPSTAIRS-HALL", command)
    assert ALLEY_MUGGER in out
    _, _, out = _say("UPSTAIRS-HALL", command, MUGGER_DEAD=True)
    assert ALLEY_QUIET in out


@pytest.mark.parametrize("command", ["open window", "break window", "climb out window"])
def test_the_window_doesnt_open(command):
    _, _, out = _say("UPSTAIRS-HALL", command)
    assert WINDOW_SHUT in out


@pytest.mark.parametrize("room", list(sc.VIEWS))
def test_every_window_has_its_view(room):
    _, _, out = _say(room, "look out window")
    assert sc.VIEWS[room] in out


def test_no_window_where_there_is_none():
    _, _, out = _say("TALE-AND-ALE", "look out window")
    assert "You can't see any window here!" in out


def test_hall_doors_and_floorboards():
    _, _, out = _say("UPSTAIRS-HALL", "examine doors")
    assert HALL_DOORS in out
    for command in ("open door", "knock on door"):
        _, _, out = _say("UPSTAIRS-HALL", command)
        assert ROOMS_RENTED in out
    _, _, out = _say("UPSTAIRS-HALL", "examine floorboards")
    assert FLOORBOARDS in out
