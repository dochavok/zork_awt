"""
TODO #15 item 4 (2026-10-14): text that misled the player.
- Supply Room: the line after Trap 17 says how it was resolved (locations.md —
  Supply Room); the disarm line reads cleanly (traps.md — Trap 17 descriptor).
- READ CHARTER gives the clause the Boggart reads (items.md — Town Charter).
- The Lighthouse: the smooth stone, the desk and the keeper's log
  (locations.md — The Lighthouse).
Run with: pytest roundabout/test_misleading_text.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from unittest.mock import patch
import pytest

from test_room_exits import _look, _do
from content.upper_tier import _SUPPLY_DISARMED, _SUPPLY_FIRED
from content.objects import (CHARTER_TEXT, LIGHTHOUSE_STONE, LIGHTHOUSE_STONE_STAYS,
                             LIGHTHOUSE_DESK, LIGHTHOUSE_LOG)

DISARM_LINE = ("You spot a trigger hidden among an unstable arrangement of clay pots. You "
               "disarm it before it can do anything.")
BOTCH_LINE = ("You see a trigger hidden among an unstable arrangement of clay pots. You try "
              "to disarm it, and fail miserably.")
OLD_SPOTTED = "Whatever it triggers, it isn't subtle."


def _enter_supply(spotted, disarmed):
    w, g, _ = _look("INK-CORRIDOR")
    with patch("content.player.check_perception", lambda w, d: spotted), \
         patch("content.player.roll_class_bonus", lambda w, k: 99 if disarmed else 1):
        first = _do(g, "west")
    return w, g, first


# --- Supply Room, Trap 17 ----------------------------------------------------------

def test_disarmed_trap_leaves_the_wedged_mechanism():
    w, g, first = _enter_supply(spotted=True, disarmed=True)
    assert DISARM_LINE in first
    out = _do(g, "look")
    assert _SUPPLY_DISARMED in out
    assert _SUPPLY_FIRED not in out and OLD_SPOTTED not in out


@pytest.mark.parametrize("spotted", [True, False])
def test_fired_trap_leaves_shards(spotted):
    w, g, first = _enter_supply(spotted=spotted, disarmed=False)
    if spotted:
        assert BOTCH_LINE in first
    out = _do(g, "look")
    assert _SUPPLY_FIRED in out
    assert _SUPPLY_DISARMED not in out and OLD_SPOTTED not in out


def test_a_save_from_before_shows_neither_line():
    w, g, _ = _look("SUPPLY-ROOM", TRAP17_DONE=True, TRAP17_SPOTTED=True)
    out = _do(g, "look")
    assert _SUPPLY_DISARMED not in out and _SUPPLY_FIRED not in out and OLD_SPOTTED not in out


# --- The town charter ---------------------------------------------------------------

def test_read_charter_gives_the_clause():
    w, g, _ = _look("RECORDS-ROOM")
    w.move_object(w.objects["TOWN-CHARTER"], w.player)
    out = _do(g, "read charter")
    assert CHARTER_TEXT in out
    assert "nothing written" not in out


# --- The Lighthouse -----------------------------------------------------------------

def _lighthouse(rune_stone=False):
    w, g, out = _look("LIGHTHOUSE")
    if rune_stone:
        o = w.objects["OLD-OAK-RUNE-STONE"]
        o.flags.discard("INVISIBLE")
        w.move_object(o, w.player)
    return w, g, out


@pytest.mark.parametrize("rune_stone", [False, True])
def test_the_stone_is_on_the_desk_and_stays(rune_stone):
    w, g, _ = _lighthouse(rune_stone)
    assert LIGHTHOUSE_STONE in _do(g, "examine stone")
    assert LIGHTHOUSE_STONE_STAYS in _do(g, "take stone")
    assert w.objects["LIGHTHOUSE-STONE"].location is w.here


def test_the_stone_gets_its_own_listing_once_the_scroll_is_gone():
    w, g, out = _lighthouse()
    listing = "A smooth stone sits on the desk where the scroll was."
    assert "weighted at one corner with a smooth stone" in out
    assert listing not in out
    _do(g, "take scroll")
    assert listing in _do(g, "look")


def test_take_all_leaves_the_stone():
    w, g, _ = _lighthouse()
    out = _do(g, "take all")
    assert LIGHTHOUSE_STONE_STAYS in out
    assert w.objects["SCROLL-UNBIND-UNDEAD"].location is w.player
    assert w.objects["LIGHTHOUSE-STONE"].location is w.here


def test_take_rune_stone_still_means_the_rune_stone():
    w, g, _ = _lighthouse(rune_stone=True)
    assert "already have the flat rune stone" in _do(g, "take rune stone")


def test_desk_and_log():
    w, g, _ = _lighthouse()
    assert LIGHTHOUSE_DESK in _do(g, "examine desk")
    for command in ("read papers", "read log", "examine papers"):
        assert LIGHTHOUSE_LOG in _do(g, command)
