"""
Ty's Cargo table (mechanics.md — Ty's Casino Corner). Dice are fixed per test
by patching content.cargo._d6 with a sequence of faces.
Run with: pytest roundabout/test_cargo.py  (from c:\\zork_awt)
"""

import sys
import os
from unittest.mock import patch
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do
from content import cargo


def _table(zenni=20):
    w, g = _make_world(cls="warrior", zenni=zenni)
    w.move_object(w.player, w.rooms["CASINO-CORNER"])
    w.here = w.rooms["CASINO-CORNER"]
    return w, g


def _play(g, cmd, faces):
    """Run cmd with the dice coming up as `faces`, in order; all must be used."""
    it = iter(faces)
    with patch("content.cargo._d6", lambda: next(it)):
        out = _do(g, cmd)
    assert next(it, None) is None, "unused dice"
    return out


# Ty: 6 5 4 on the first roll, cargo 5 and 4 — keeps both, no reroll (9).
_TY_9 = [6, 5, 4, 5, 4]
# Ty fails: three rolls, never a six.
_TY_FAIL = [1, 2, 3, 1, 2, 1, 2, 3, 1, 2, 1, 2, 3, 1, 2]


# --- Talking and stakes --------------------------------------------------------

def test_talk_to_ty():
    w, g = _table()
    assert cargo._INTRO in _do(g, "talk to ty")


def test_stake_prompts():
    w, g = _table(zenni=5)
    assert cargo._STAKE_FIRST in _do(g, "play cargo")
    assert cargo._STAKE_FIRST in _do(g, "play")
    assert cargo._ZERO in _do(g, "bet 0")
    assert cargo._SHORT in _do(g, "bet 6")
    assert w.globals["zenni"] == 5


def test_not_at_the_table():
    w, g = _make_world(cls="warrior", zenni=20)
    out = _do(g, "bet 3")
    assert "Ty" not in out
    assert w.globals["zenni"] == 20


# --- Ty's turn -----------------------------------------------------------------

def test_ty_all_at_once_keeps_high_dice():
    w, g = _table()
    out = _play(g, "bet 3", _TY_9 + [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    assert cargo._TY_ALL_AT_ONCE in out
    assert "Ty keeps the" not in out and cargo._TY_REROLLS_BOTH not in out
    assert "Ty's cargo: 9." in out and cargo._TY_HIGH in out


def test_ty_keeps_one_rerolls_low():
    w, g = _table()
    # Ty: 6 5 4 2 6 → keeps 6, rerolls 2 → 1 (still low, one roll left) → 5: cargo 11.
    ty = [6, 5, 4, 2, 6, 1, 5]
    out = _play(g, "bet 3", ty + [1] * 15)
    assert out.count("Ty keeps the 6 and rolls the 2 again.") == 1
    assert "Ty keeps the 6 and rolls the 1 again." in out
    assert "Ty's cargo: 11." in out


def test_ty_rerolls_both_when_both_low():
    w, g = _table()
    ty = [6, 5, 4, 1, 3, 5, 6]          # both low → both rerolled → 5 and 6, keeps
    out = _play(g, "bet 3", ty + [1] * 15)
    assert cargo._TY_REROLLS_BOTH in out
    assert "Ty's cargo: 11." in out


def test_ty_six_on_second_roll():
    w, g = _table()
    ty = [1, 2, 3, 1, 2,  6, 5, 4, 5, 6]   # no six, then six five four and cargo 5 6
    out = _play(g, "bet 3", ty + [1] * 15)
    assert cargo._TY_SIX_ON_TWO in out
    assert "Ty's cargo: 11." in out


def test_ty_fails_scores_zero():
    w, g = _table()
    out = _play(g, "bet 3", _TY_FAIL + [1] * 15)
    assert cargo._TY_FAILS in out
    assert "Ty's cargo" not in out
    assert cargo._PUSH in out                    # both 0


# --- The player's turn -----------------------------------------------------------

def test_player_rolls_shown_and_no_slot():
    w, g = _table()
    out = _play(g, "bet 3", _TY_9 + [6, 1, 2, 3, 1,  5, 1, 2, 3,  1, 1, 2])
    assert "First roll: 6, 1, 2, 3, 1. You set aside the six." in out
    assert "Second roll: 5, 1, 2, 3. You set aside the five." in out
    assert "Third roll: 1, 1, 2. Nothing to set aside." in out
    assert "No crew. Your score: 0." in out
    assert cargo._LOSE in out
    assert w.globals["zenni"] == 17 and w.get_global("TY-BANKROLL") == 33


def test_sequence_on_last_roll_settles_at_once():
    w, g = _table()
    out = _play(g, "bet 3", _TY_9 + [1, 1, 1, 1, 1,  1, 1, 1, 1, 1,  6, 5, 4, 6, 6])
    assert "Ship, Captain and Crew. Your cargo: 6 and 6 — 12." in out
    assert cargo._CHOOSE not in out
    assert cargo._WIN in out
    assert w.globals["zenni"] == 23 and w.get_global("TY-BANKROLL") == 27


def test_choice_reroll_one_then_stand():
    w, g = _table()
    out = _play(g, "bet 3", _TY_9 + [6, 5, 4, 2, 6])
    assert "Ship, Captain and Crew. Your cargo: 2 and 6 — 8. Reroll one, both, or stand?" in out
    assert w.get_global("CARGO-ROUND") is not None
    out = _play(g, "reroll 2", [3])
    assert "You roll the 2 again: 3. Your cargo: 3 and 6 — 9." in out
    assert cargo._CHOOSE in out                  # one roll still left
    out = _do(g, "stand")
    assert cargo._PUSH in out                    # 9 against 9
    assert w.get_global("CARGO-ROUND") is None
    assert w.globals["zenni"] == 20


def test_choice_reroll_both_twice_must_keep():
    w, g = _table()
    _play(g, "bet 3", _TY_9 + [6, 5, 4, 6, 6])   # 12, two rolls left
    out = _play(g, "reroll both", [1, 1])
    assert "You roll the cargo again: 1 and 1 — 2." in out
    out = _play(g, "reroll both", [2, 1])
    assert "You roll the cargo again: 2 and 1 — 3." in out
    assert cargo._LOSE in out                    # no rolls left: settles on 3
    assert w.get_global("CARGO-ROUND") is None


def test_bare_reroll_and_other_commands_wait_without_a_turn():
    w, g = _table()
    _play(g, "bet 3", _TY_9 + [6, 5, 4, 2, 6])
    moves = w.moves
    assert 'Ty waits. "Both, or just the 2?" (REROLL BOTH, REROLL 2, or STAND)' in _do(g, "reroll")
    waiting = 'Ty waits. "Reroll or stand?" (REROLL BOTH, REROLL 2, or STAND)'
    assert waiting in _do(g, "reroll 5")
    assert waiting in _do(g, "north")
    assert waiting in _do(g, "cast light")
    assert w.moves == moves
    assert w.here.name == "CASINO-CORNER"


def test_reroll_matching_pair_rerolls_one():
    w, g = _table()
    _play(g, "bet 3", _TY_9 + [6, 5, 4, 3, 3])
    out = _play(g, "reroll 3", [6])
    assert "You roll the 3 again: 6. Your cargo: 6 and 3 — 9." in out


# --- Bankroll ------------------------------------------------------------------

def test_ty_matches_what_he_has_and_is_cleaned_out():
    w, g = _table(zenni=50)
    w.set_global("TY-BANKROLL", 4)
    out = _play(g, "bet 10", _TY_FAIL + [6, 5, 4, 6, 6])
    assert '"I can match 4."' in out
    assert "Ty's cargo" not in out
    out = _do(g, "stand")
    assert cargo._WIN in out and cargo._CLEANED_OUT in out
    assert w.globals["zenni"] == 54 and w.get_global("TY-BANKROLL") == 0
    assert cargo._CLOSED in _do(g, "bet 3")
    assert cargo._CLOSED in _do(g, "talk to ty")
    assert w.globals["zenni"] == 54


def test_play_again_right_away():
    w, g = _table()
    _play(g, "bet 3", _TY_FAIL + [1] * 15)
    out = _play(g, "play cargo 3", _TY_FAIL + [1] * 15)
    assert cargo._PUSH in out
