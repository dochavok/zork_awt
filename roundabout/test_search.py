"""
SEARCH — one extra look per visit (mechanics.md — Perception: SEARCH).
Room checks fire on arrival; SEARCH re-runs the ones still unfound, once per
visit, for a turn.
Run with: pytest roundabout/test_search.py  (from c:\\zork_awt)
"""

import sys
import os
import io
from unittest.mock import patch
sys.path.insert(0, os.path.dirname(__file__))

import pytest

from test_traps import _world, _arrive, _rolls, LOW, HIGH
from content import search
from content.pond import BOTTLE_IN_POND

LEAD_IN = "Searching carefully, you notice something you missed."
NOTHING = "You search carefully but find nothing unusual."


def _search(g, total, command="search"):
    buf = io.StringIO()
    with _rolls(total), patch("sys.stdout", buf):
        g.do_turn(command)
    return buf.getvalue()


def _missed(room):
    """Arrive with every roll failing, so the room's checks all miss."""
    w, g = _world()
    w.set_global("ZENNI-ROOMS", {})             # no hidden-Zenni rolls in the way
    _arrive(w, g, room, LOW)
    return w, g


# --- Finds ---------------------------------------------------------------------

def test_search_finds_what_arrival_missed():
    w, g = _missed("ROUNDABOUT-POND")
    assert not w.get_global("POND-BOTTLE-SEEN")
    out = _search(g, HIGH)
    assert BOTTLE_IN_POND in out                    # the check's own line
    assert w.get_global("POND-BOTTLE-SEEN")
    assert LEAD_IN not in out


def test_search_shows_a_quiet_find_with_the_room():
    w, g = _missed("SHRINE-ROOM")
    piece = w.objects["BOWL-PIECE-SHRINE"]
    assert piece.has_flag("INVISIBLE")
    out = _search(g, HIGH)
    assert not piece.has_flag("INVISIBLE")
    assert LEAD_IN in out
    assert "Shrine Room" in out.split(LEAD_IN, 1)[1]    # the room, described in full


def test_search_find_announced_at_end_of_turn():
    w, g = _missed("TOLL-BRIDGE")
    out = _search(g, HIGH)
    assert w.get_global("SEAL-FOUND") is True       # the M_END line ran this turn
    assert NOTHING not in out


def test_search_finds_hidden_zenni():
    w, g = _world()
    w.set_global("ZENNI-ROOMS", {"TOWN-SQUARE": {"difficulty": 9, "zenni": 2, "found": False}})
    _arrive(w, g, "TOWN-SQUARE", LOW)
    zenni = w.globals["zenni"]
    out = _search(g, HIGH)
    assert "Something catches your eye" in out
    assert w.globals["zenni"] == zenni + 2


def test_search_gives_the_alcove_a_second_roll():
    w, g = _missed("PRAYER-ALCOVE")
    assert not w.get_global("NICHE-FOUND")
    _search(g, HIGH)
    assert w.get_global("NICHE-FOUND")


def test_search_spots_the_idol_plate():
    w, g = _missed("IDOL-ROOM")
    _search(g, HIGH)
    assert w.get_global("IDOL-PLATE-SPOTTED")


# --- Nothing -------------------------------------------------------------------

def test_search_with_nothing_to_find():
    w, g = _missed("TOWN-SQUARE")
    moves = w.moves
    assert NOTHING in _search(g, HIGH)
    assert w.moves == moves + 1                     # a turn


def test_search_that_fails_reads_the_same():
    w, g = _missed("ROUNDABOUT-POND")
    out = _search(g, LOW)
    assert NOTHING in out
    assert not w.get_global("POND-BOTTLE-SEEN")


def test_once_per_visit():
    w, g = _missed("ROUNDABOUT-POND")
    _search(g, LOW)
    out = _search(g, HIGH)                          # same visit: no second roll
    assert NOTHING in out
    assert not w.get_global("POND-BOTTLE-SEEN")
    _arrive(w, g, "ARCHERY-RANGE", LOW)             # leave...
    _arrive(w, g, "ROUNDABOUT-POND", LOW)           # ...come back: a new visit
    assert BOTTLE_IN_POND in _search(g, HIGH)


def test_search_a_thing_searches_the_room():
    w, g = _missed("ROUNDABOUT-POND")
    w.move_object(w.objects["SHOVEL"], w.player)
    assert BOTTLE_IN_POND in _search(g, HIGH, "search shovel")


def test_search_in_the_dark():
    w, g = _missed("TOWN-SQUARE")
    with patch.object(type(w), "is_lit", lambda self: False):
        out = _search(g, HIGH)
    assert "It's too dark to see!" in out


# --- Not re-run ----------------------------------------------------------------

def test_arrival_traps_are_not_rerun():
    from test_traps import _arrive as arrive
    w, g = _world()
    w.set_global("ZENNI-ROOMS", {})
    arrive(w, g, "INK-CORRIDOR", LOW)               # Trap 45 fires on the way in
    inked = w.get_global("INKED")
    assert NOTHING in _search(g, HIGH)
    assert w.get_global("INKED") == inked


def test_every_listed_check_exists():
    for room, checks in search._CHECKS.items():
        assert room in _world()[0].rooms, room
        for module, name, _shows in checks:
            assert callable(search._fn(module, name)), (module, name)
