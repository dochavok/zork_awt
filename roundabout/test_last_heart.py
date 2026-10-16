"""
The last-heart line (mechanics.md — Hearts & Health, 2026-10-15): when damage
leaves the player on exactly 1 heart, right after the hit's own line.

Expected text is the design's, written out here.
Run with: pytest roundabout/test_last_heart.py  (from c:\\zork_awt)
"""

import sys
import os
import io
from unittest.mock import patch
sys.path.insert(0, os.path.dirname(__file__))

from testkit import _make_world
from test_traps import _world, _no_pause
from content import combat, back_alley

LAST_HEART = "You're hurting badly now. One more like that and you won't get up."
SHOCK = "Your hands close on the bars and the charge goes through you"
DEATH = "Your last heart gives out."
SWIM = "The moment you enter, the water is inside you somehow"
MUGGED_WAKE = "You come to in the Back Alley, lighter in the pocket and sore in the head."
FIGHT_LOST = "You come to on the cobbles. The mugger is gone"


def _out(fn, *a, **kw):
    buf = io.StringIO()
    with patch("sys.stdout", buf), _no_pause():
        fn(*a, **kw)
    return buf.getvalue()


def _touch_portcullis(hearts):
    w, g = _world()
    room = w.rooms["PORTCULLIS-CORRIDOR"]
    w.move_object(w.player, room)
    w.here = room
    w.globals["hearts"] = hearts
    return w, _out(g.do_turn, "touch portcullis")


def test_trap_hit_down_to_one_heart_warns_after_the_hit():
    w, out = _touch_portcullis(2)
    assert w.globals["hearts"] == 1
    assert SHOCK in out and LAST_HEART in out, out
    assert out.index(SHOCK) < out.index(LAST_HEART)


def test_no_warning_above_one_heart():
    w, out = _touch_portcullis(3)
    assert w.globals["hearts"] == 2
    assert LAST_HEART not in out, out


def test_no_warning_on_the_killing_blow():
    w, out = _touch_portcullis(1)
    assert DEATH in out
    assert LAST_HEART not in out, out


def test_warning_again_after_healing():
    w, out = _touch_portcullis(2)
    assert LAST_HEART in out
    w.globals["hearts"] = 2                     # healed
    assert LAST_HEART in _out(combat.take_damage, w, 1)


def _round_lost(w, **kw):
    with patch("content.combat.player_roll", return_value=1), \
            patch("content.combat._enemy_roll", return_value=10):
        return _out(combat.fight_round, w, (1, 6), "won", "lost", "tie", **kw)


def test_combat_round_down_to_one_heart_warns_after_the_round():
    w, g = _make_world(cls="warrior", hearts=2)
    out = _round_lost(w)
    assert w.globals["hearts"] == 1
    assert out.index("lost") < out.index(LAST_HEART)


def test_tied_round_warns_too():
    w, g = _make_world(cls="warrior", hearts=2)
    with patch("content.combat.player_roll", return_value=5), \
            patch("content.combat._enemy_roll", return_value=5):
        out = _out(combat.fight_round, w, (1, 6), "won", "lost", "tie")
    assert LAST_HEART in out, out


def test_no_warning_in_the_knights_trial():
    # finishing=False is the knight's trial: it stops at 1 heart by design
    w, g = _make_world(cls="mage", hearts=2)
    out = _round_lost(w, finishing=False)
    assert w.globals["hearts"] == 1
    assert LAST_HEART not in out, out


def test_no_warning_when_the_tunic_turns_the_blow():
    w, g = _make_world(cls="warrior", hearts=2)
    tunic = w.objects["IVANAAR-TUNIC"]
    w.move_object(tunic, w.player)
    tunic.set_flag("WEARBIT")
    with patch("content.combat.random.randint", return_value=10):
        out = _out(combat.take_damage, w, 1)
    assert w.globals["hearts"] == 2
    assert LAST_HEART not in out, out


def test_pool_swim_down_to_one_heart_warns():
    w, g = _make_world(cls="warrior", hearts=2)
    pool = w.rooms["FLOODED-PASSAGE"].exits["north"]
    out = _out(pool.resolve, w)
    assert w.globals["hearts"] == 1
    assert out.index(SWIM) < out.index(LAST_HEART)


def test_mugger_ambush_from_two_hearts_warns_after_waking():
    w, g = _make_world(cls="warrior", hearts=2)
    out = _out(back_alley._mugged, w)
    assert w.globals["hearts"] == 1
    assert out.index(MUGGED_WAKE) < out.index(LAST_HEART)


def test_mugger_ambush_at_one_heart_adds_nothing():
    w, g = _make_world(cls="warrior", hearts=1)
    out = _out(back_alley._mugged, w)
    assert w.globals["hearts"] == 1
    assert MUGGED_WAKE in out
    assert LAST_HEART not in out, out


def test_lost_mugger_fight_has_its_own_line():
    w, g = _make_world(cls="warrior", hearts=1)
    with patch("content.combat.player_roll", return_value=1), \
            patch("content.combat._enemy_roll", return_value=10):
        out = _out(back_alley.fight_round, w)
    assert w.globals["hearts"] == 1
    assert FIGHT_LOST in out
    assert LAST_HEART not in out, out
