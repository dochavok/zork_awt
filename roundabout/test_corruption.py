"""
Ring corruption (mechanics.md — The God-Forsaken Ring; ring-rituals.md — altar).

SACRED CONSTRAINT: corruption is never reduced, slowed or mitigated.

Every test plays real commands through game.do_turn(). Expected values are the
design's own numbers and text, written out here — not read from the code — so
a change to the code that breaks the design fails a test.

Run with: pytest roundabout/test_corruption.py  (from c:\\zork_awt)
"""

import sys
import os
from unittest.mock import patch
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do

# mechanics.md — Milestone messages, removal outcomes, game over
TICK_10 = ("The ring is warm. You hadn't noticed until just now. "
           "You're not sure when it started.")
TICK_25 = ("The ring is heavier than it was. Not in weight — in presence. It knows "
           "you're wearing it. You find yourself aware of it in a way you weren't before.")
TICK_40 = ("The ring is harder to ignore than it was. You are aware of it the way you're "
           "aware of a sound that hasn't stopped. You should take it off. You know you "
           "should take it off.")
CLEAN = "You remove the ring. Whatever it wants, it didn't get it this time."
NEAR_MISS = ("The ring comes off. It didn't want to. "
             "You're not sure you could have held out another moment.")
FAILED = "You try to take the ring off. Your fingers find it. They don't do what you ask."
GAME_OVER = ("You reach for the ring. Your hand doesn't move. You watch it not move. "
             "The ring is warm and patient and it has been waiting for exactly this. "
             "You are not going to take it off.")

# mechanics.md — Late-stage removal: target by tick
REMOVAL_TARGET = {41: 5, 42: 7, 43: 9, 44: 11, 45: 13, 46: 15, 47: 17, 48: 19, 49: 21}


def _ringed(room="TOWN-SQUARE", tick=0, **kw):
    """A game with the ring on (WEAR RING), corruption then set to `tick`."""
    w, g = _make_world(cls=kw.pop("cls", "warrior"), **kw)
    w.move_object(w.player, w.rooms[room])
    w.here = w.rooms[room]
    w.move_object(w.objects["RING"], w.player)
    _do(g, "wear ring")
    w.globals["ring_corruption"] = tick
    return w, g


def _tick(w):
    return w.globals["ring_corruption"]


def _removal_roll(value):
    """Fix the removal roll (level dice) at `value`."""
    return patch("content.player.roll", return_value=value)


# --- Ticking ------------------------------------------------------------------

def test_each_turn_worn_adds_exactly_one():
    w, g = _ringed(tick=5)
    for n in range(1, 6):
        _do(g, "wait")
        assert _tick(w) == 5 + n


def test_off_pauses_and_back_on_resumes_never_resets():
    w, g = _ringed(tick=12)
    _do(g, "remove ring")
    for _ in range(5):
        _do(g, "wait")
    assert _tick(w) == 12                      # paused while off
    _do(g, "wear ring")
    before = _tick(w)
    _do(g, "wait")
    assert before >= 12                        # resumed, not reset
    assert _tick(w) == before + 1


@pytest.mark.parametrize("tick,text", [(10, TICK_10), (25, TICK_25), (40, TICK_40)])
def test_milestone_lines(tick, text):
    w, g = _ringed(tick=tick - 1)
    assert text in _do(g, "wait")
    assert _tick(w) == tick
    assert text not in _do(g, "wait")          # once, at its tick only


def test_full_corruption_at_fifty_ends_the_game():
    w, g = _ringed(tick=48)
    assert GAME_OVER not in _do(g, "wait")     # 49: still playing
    out = _do(g, "wait")                       # 50
    assert GAME_OVER in out
    assert w.get_global("GAME-OVER") is True
    assert "The game is over." in _do(g, "remove ring")   # no roll offered, no resurrection


# --- Removal --------------------------------------------------------------------

def test_removal_at_forty_needs_no_roll():
    w, g = _ringed(tick=40)
    with _removal_roll(0):                     # a roll of 0 would fail any target
        _do(g, "remove ring")
    assert w.globals["ring_worn"] is False
    assert not w.objects["RING"].has_flag("WEARBIT")


@pytest.mark.parametrize("tick,target", sorted(REMOVAL_TARGET.items()))
def test_removal_target_by_tick(tick, target):
    w, g = _ringed(tick=tick)
    with _removal_roll(target - 1):
        out = _do(g, "remove ring")
    assert FAILED in out
    assert w.globals["ring_worn"] is True       # it stays on

    w, g = _ringed(tick=tick)
    with _removal_roll(target):
        _do(g, "remove ring")
    assert w.globals["ring_worn"] is False


def test_exactly_meeting_the_target_is_a_near_miss():
    w, g = _ringed(tick=45)
    with _removal_roll(13):
        out = _do(g, "remove ring")
    assert NEAR_MISS in out
    assert CLEAN not in out


def test_beating_the_target_easily_is_clean():
    w, g = _ringed(tick=41)
    with _removal_roll(25):
        out = _do(g, "remove ring")
    assert CLEAN in out
    assert NEAR_MISS not in out


def test_removal_roll_is_level_dice_only():
    # Level 2 is 2d6+1. Each die shows 2: the dice make 4 — one short of tick 41's
    # target of 5. The +1 level bonus, the Warrior's strength bonus, the gloves and
    # a weapon must not count, so the ring stays on.
    w, g = _ringed(tick=41, level=2)
    w.move_object(w.objects["APPRENTICE-GLOVES"], w.player)
    _do(g, "wear gloves")
    w.move_object(w.objects["BATTLE-AXE"], w.player)
    _do(g, "equip axe")
    w.globals["ring_corruption"] = 41
    with patch("random.randint", return_value=2):
        out = _do(g, "remove ring")
    assert FAILED in out
    assert w.globals["ring_worn"] is True


def test_failed_removal_never_lowers_corruption():
    w, g = _ringed(tick=45)
    for _ in range(3):
        with _removal_roll(1):
            _do(g, "remove ring")
    assert _tick(w) == 48                      # each failed attempt is a worn turn


# --- The altar (ring-rituals.md) ---------------------------------------------------

def test_altar_takes_the_worn_ring_without_a_tick():
    w, g = _ringed(room="ALTAR", tick=20)
    out = _do(g, "put ring on altar")
    assert _tick(w) == 20                      # placing it doesn't tick
    assert w.globals["ring_worn"] is False     # it came off automatically
    assert "Nothing happens. Something is missing from the ritual. You pick up the ring." in out
    assert w.objects["RING"].location is w.player
    _do(g, "wait")
    assert _tick(w) == 20                      # and stays off


# --- Healing never touches corruption (run where healing actually happens) -------

@pytest.mark.parametrize("cmd", ["buy drink", "rent room"])
def test_healing_at_the_bar_never_reduces_corruption(cmd):
    w, g = _ringed(room="BAR", tick=20, hearts=2, zenni=20)
    w.globals["max_hearts"] = 6
    _do(g, cmd)
    assert w.globals["hearts"] > 2             # the heal really happened
    assert _tick(w) > 20                       # and the worn turn still counted


def test_rest_heals_and_never_reduces_corruption():
    w, g = _ringed(tick=20, hearts=2, level=6)
    w.globals.update({"max_hearts": 6, "spell_rest": True})
    _do(g, "rest")
    assert w.globals["hearts"] == 3            # mechanics.md — REST recovers 1 heart
    assert _tick(w) == 21


def test_wear_ring_once_bound_refused():
    w, g = _ringed(tick=5)
    _do(g, "remove ring")
    w.globals["ring_bound"] = True
    assert "The ring won't go on. It simply won't." in _do(g, "wear ring")
    assert w.globals["ring_worn"] is False
