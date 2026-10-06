"""
REST — Level 6 (mechanics.md — Spell Mechanics: REST notes).

Expected text and numbers are the design's, written out here.
Run with: pytest roundabout/test_rest.py  (from c:\\zork_awt)
"""

import sys
import os
import io
from unittest.mock import patch
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do
from content.experience import award_xp

RESTED = ("You sit with your back to the nearest wall and let your breathing slow. "
          "When you get up, some of the ache has gone with it.")
NOT_TIRED = "You're not tired."
FIGHTING = "You can't rest now, there's fighting to be done!"
TOO_SOON = "What are you sitting around for, there's a dungeon to explore!"
FULL = "You're as rested as you're going to get."


def _rester(room="TOWN-SQUARE", hearts=2, max_hearts=6, level=6):
    w, g = _make_world(cls="warrior", level=level, hearts=hearts)
    w.globals["max_hearts"] = max_hearts
    if level >= 6:
        w.globals["spell_rest"] = True
    w.move_object(w.player, w.rooms[room])
    w.here = w.rooms[room]
    return w, g


def test_rest_heals_one_heart_and_uses_a_turn():
    w, g = _rester()
    moves = w.moves
    assert RESTED in _do(g, "rest")
    assert w.globals["hearts"] == 3
    assert w.moves == moves + 1


def test_earned_at_level_six():
    w, g = _rester(level=1)
    assert NOT_TIRED in _do(g, "rest")
    with patch("sys.stdout", io.StringIO()):
        award_xp(w, 225)                       # experience.md — Level 6 at 225 XP
    assert RESTED in _do(g, "rest")


def test_before_level_six_not_tired_no_turn():
    w, g = _rester(level=5)
    moves = w.moves
    assert NOT_TIRED in _do(g, "rest")
    assert w.globals["hearts"] == 2
    assert w.moves == moves


def test_fifty_turn_reuse_timer():
    w, g = _rester(hearts=1)
    _do(g, "rest")
    rested_at = w.moves - 1                    # the move REST was taken on
    while w.moves < rested_at + 49:
        _do(g, "wait")
    moves = w.moves
    assert TOO_SOON in _do(g, "rest")          # 49 turns on: not yet, no turn used
    assert w.moves == moves
    assert w.globals["hearts"] == 2
    _do(g, "wait")
    assert RESTED in _do(g, "rest")            # 50 turns on: ready
    assert w.globals["hearts"] == 3


def test_full_hearts_refused_without_starting_the_timer():
    w, g = _rester(hearts=6)
    moves = w.moves
    assert FULL in _do(g, "rest")
    assert w.moves == moves
    w.globals["hearts"] = 5
    assert RESTED in _do(g, "rest")            # the timer wasn't started


def test_works_while_inked():
    w, g = _rester()
    w.set_global("INKED", True)
    assert RESTED in _do(g, "rest")
    assert w.globals["hearts"] == 3


# --- Not in a fight: a live enemy in the room -------------------------------------------

def _mugger_spotted(w):
    w.set_global("MUGGER-SPOTTED", True)


def _warden_out(w):
    w.set_global("WARDEN-OUT", True)


def _knight_trial(w):
    w.set_global("KNIGHT-FIGHTING", True)


@pytest.mark.parametrize("room,setup", [
    ("BACK-ALLEY", _mugger_spotted),
    ("COMBAT-ROOM", _warden_out),
    ("LOST-APPRENTICES-CELL", None),           # the apprentice, not yet freed
    ("STILL-DEN", None),                       # the werewolf, alive
    ("TOWN-SQUARE", _knight_trial),
])
def test_refused_with_a_live_enemy_here(room, setup):
    w, g = _rester(room=room)
    if setup:
        setup(w)
    moves = w.moves
    assert FIGHTING in _do(g, "rest")
    assert w.globals["hearts"] == 2
    assert w.moves == moves


@pytest.mark.parametrize("room,flag", [
    ("BACK-ALLEY", "MUGGER-DEAD"),
    ("COMBAT-ROOM", "WARDEN-DEAD"),
    ("LOST-APPRENTICES-CELL", "APPRENTICE-FREED"),
    ("STILL-DEN", "WEREWOLF-DEAD"),
])
def test_allowed_once_the_enemy_is_done(room, flag):
    w, g = _rester(room=room)
    w.set_global(flag, True)
    assert RESTED in _do(g, "rest")


def test_unspotted_mugger_does_not_block():
    w, g = _rester(room="BACK-ALLEY")
    assert RESTED in _do(g, "rest")
