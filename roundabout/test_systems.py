"""
Timed and weighed systems (mechanics.md — Torch, Shamus swap tiers, Weight
System; quests.md — Quest 51; locations.md — The Back Alley, Rickety Bridge).

Expected numbers and text are the design's, written out here.
Run with: pytest roundabout/test_systems.py  (from c:\\zork_awt)
"""

import sys
import os
import io
from unittest.mock import patch
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do
from content import light

IGNITION = "The torch catches the dark and pushes it back. Good thinking, getting one of these."
WARN_50 = "The torch burns a little lower than it did."
WARN_30 = "The torch is noticeably dimmer now. It won't last forever."
WARN_15 = "The torch gutters. You don't have much time left on it."
GUTTERS_OUT = "The torch gutters and goes out."
SWAP_REFUSED = ('Shamus glances at the torch. "That one\'s got plenty of life left." '
                'He hands it back. "Come see me when it\'s lower."')
SWAP = {
    "getting": 'Shamus glances at the torch. "Getting there." He hands you a fresh one. "Three Zenni."',
    "short": 'Shamus glances at the torch. "That one\'s running short." He hands you a fresh one. "Three Zenni."',
    "had it": 'Shamus glances at the torch. "That one\'s had it." He hands you a fresh one. "Three Zenni."',
}
OVERWEIGHT = ("The bridge groans under your load — a deep, unhappy sound from somewhere in "
              "the stone. It isn't going to hold. You'll need to lighten what you're carrying.")
MUGGED = "Something hits you from behind. The alley tilts, then goes away."
MUGGED_WAKE = "You come to in the Back Alley, lighter in the pocket and sore in the head."
BOUNTY = ("BOUNTY: someone's been robbing people in the back alley. Whoever puts a stop "
          "to it drinks free. — May")


def _quiet(fn, *a, **kw):
    with patch("sys.stdout", io.StringIO()):
        return fn(*a, **kw)


def _goto(w, room):
    w.move_object(w.player, w.rooms[room])
    w.here = w.rooms[room]


# --- Torch: 100 turns from the first dark room; warnings at 50 / 30 / 15 left -------

def test_torch_life_and_warnings_over_real_turns():
    w, g = _make_world(cls="warrior")
    w.move_object(w.objects["TORCH"], w.player)
    light.light_torch(w)                           # as bought: lit, timer not started
    for _ in range(10):
        _do(g, "wait")                             # in town, the torch doesn't burn
    buf = io.StringIO()
    with patch("sys.stdout", buf):
        g.enter_room(w.rooms["MAUSOLEUM"])         # dark; one step from the lit Graveyard
    assert IGNITION in buf.getvalue()

    seen = {}
    for turn in range(1, 101):
        out = _do(g, "wait")
        for line in (WARN_50, WARN_30, WARN_15, GUTTERS_OUT):
            if line in out:
                seen.setdefault(line, turn)
    assert seen == {WARN_50: 50, WARN_30: 70, WARN_15: 85, GUTTERS_OUT: 100}
    assert not w.get_global("GAME-OVER")           # an exit leads straight to light


# --- Shamus's swap tiers: BUY TORCH while carrying one ------------------------------

def _swap(turns_left):
    w, g = _make_world(cls="warrior", zenni=10)
    _goto(w, "KITCHEN")
    w.move_object(w.objects["TORCH"], w.player)
    light.light_torch(w)
    w.set_global("TORCH-LIT-TIMER", turns_left)
    out = _do(g, "buy torch")
    return w, out


@pytest.mark.parametrize("left", [100, 70])
def test_swap_refused_while_plenty_left(left):
    w, out = _swap(left)
    assert SWAP_REFUSED in out
    assert w.globals["zenni"] == 10


@pytest.mark.parametrize("left,tier", [(69, "getting"), (30, "getting"), (29, "short"),
                                       (15, "short"), (14, "had it"), (1, "had it")])
def test_swap_tiers(left, tier):
    w, out = _swap(left)
    assert SWAP[tier] in out
    assert w.globals["zenni"] == 7
    assert light.turns_left(w) == 100              # fresh torch; waits for the next dark room


# --- Rickety Bridge: carry limit 12, either way ------------------------------------------

def _loaded(room, *items):
    w, g = _make_world(cls="warrior")
    w.move_object(w.objects["TORCH"], w.player)            # 2 — the dungeon is dark
    light.light_torch(w)
    for name in items:
        w.move_object(w.objects[name], w.player)
    _quiet(g.enter_room, w.rooms[room])
    return w, g


# torch 2 + rope 3 + shovel 3 + pickaxe 3 = 11; + scroll 1 = 12; + map 1 = 13
AT_LIMIT = ("ROPE", "SHOVEL", "PICKAXE", "THIN-PAPER")
OVER = AT_LIMIT + ("TREASURE-MAP",)


def test_bridge_crossable_at_twelve():
    w, g = _loaded("RICKETY-BRIDGE", *AT_LIMIT)
    _do(g, "south")
    assert w.here.name == "MID-TIER-KEY-DOOR"
    _do(g, "north")
    assert w.here.name == "RICKETY-BRIDGE"


def test_bridge_refuses_thirteen_either_way():
    w, g = _loaded("RICKETY-BRIDGE", *OVER)
    assert OVERWEIGHT in _do(g, "south")
    assert w.here.name == "RICKETY-BRIDGE"
    w, g = _loaded("MID-TIER-KEY-DOOR", *OVER)
    assert OVERWEIGHT in _do(g, "north")
    assert w.here.name == "MID-TIER-KEY-DOOR"


# --- Back Alley mugging: 1 heart and 2-3 Zenni, never below 1 heart ----------------------

def _mugging(theft_face, zenni=10, hearts=5):
    w, g = _make_world(cls="warrior", zenni=zenni, hearts=hearts)
    buf = io.StringIO()
    with patch("content.player.roll", return_value=1), \
         patch("content.back_alley.random.randint", lambda a, b: a if theft_face == "low" else b), \
         patch("sys.stdout", buf):
        g.enter_room(w.rooms["BACK-ALLEY"])
        g.do_turn("look")
    return w, buf.getvalue()


def test_mugging_takes_two_to_three_zenni_and_a_heart():
    w, out = _mugging("low")
    assert MUGGED in out and MUGGED_WAKE in out
    assert w.globals["zenni"] == 8
    assert w.globals["hearts"] == 4
    w, out = _mugging("high")
    assert w.globals["zenni"] == 7


def test_mugging_never_kills_or_overdraws():
    w, out = _mugging("high", zenni=0, hearts=1)
    assert w.globals["zenni"] == 0
    assert w.globals["hearts"] == 1
    assert not w.get_global("GAME-OVER")


# --- Quest 51 bounty: posted at 100 turns while the mugger lives -------------------------

def test_bounty_goes_up_at_turn_100():
    w, g = _make_world(cls="warrior")
    _goto(w, "BAR")
    while w.moves < 99:
        _do(g, "wait")
    assert BOUNTY not in _do(g, "read board")       # read board is turn 100's command
    _do(g, "wait")
    assert BOUNTY in _do(g, "read board")
