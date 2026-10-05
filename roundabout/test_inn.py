"""
The inn: food, drink, stew and rooms at the Bar (npcs.md — May), the guest
rooms (locations.md), and the bath that clears ink (traps.md — Trap 45).
Run with: pytest roundabout/test_inn.py  (from c:\\zork_awt)
"""

import sys
import os
from unittest.mock import patch
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do

_MAY_INKED = "Rooms are upstairs. That's all you're getting from me until you've used one."
_SHORT = '"You\'re short."'
_FULL = "You don't need it. Come back when you do."
_FULL_ROOM = "You're fine. Come back when you're not."
_SLEEP = "slides a key across the bar. \"Sleep well.\""
_RENT_INKED = "There's a bath up there. Use it."
_BATH = "The ink takes three changes of water and most of the soap. It comes off."
_WAKE3 = "You wake in the small room at the end of the hall."
_WAKE1 = "You come around slowly."


import pytest


@pytest.fixture(autouse=True)
def _room_three():
    """The guest-room roll at max, as under the always-max dice mock."""
    with patch("content.tavern.random.randint", return_value=3):
        yield


def _at_bar(hearts=3, max_hearts=5, zenni=10, **flags):
    w, g = _make_world(hearts=hearts, zenni=zenni)
    w.globals["max_hearts"] = max_hearts
    w.set_global("MAY-MET", True)
    for k, v in flags.items():
        w.set_global(k.replace("_", "-"), v)
    w.move_object(w.player, w.rooms["BAR"])
    w.here = w.rooms["BAR"]
    return w, g


# --- food, drink, stew ---------------------------------------------------------

def test_buy_drink():
    w, g = _at_bar()
    out = _do(g, "buy drink")
    assert "fills it without being asked what you want. Two Zenni." in out
    assert w.globals["hearts"] == 4 and w.globals["zenni"] == 8


def test_order_food():
    w, g = _at_bar()
    out = _do(g, "order food")
    assert 'She sets it in front of you. "Two Zenni."' in out
    assert w.globals["hearts"] == 4 and w.globals["zenni"] == 8


def test_purchase_drink():
    w, g = _at_bar()
    _do(g, "purchase a drink")
    assert w.globals["zenni"] == 8


def test_discount_after_quest_22():
    w, g = _at_bar(FOOD_DISCOUNT=True)
    assert "One Zenni." in _do(g, "buy drink")
    assert '"One Zenni."' in _do(g, "buy food")
    assert w.globals["zenni"] == 8


def test_stew_before_quest_40():
    w, g = _at_bar()
    assert '"Not on the menu," May says. "Ask Shamus."' in _do(g, "order stew")
    assert w.globals["zenni"] == 10


def test_stew_heals_two():
    w, g = _at_bar(hearts=2, HEARTY_STEW=True)
    out = _do(g, "buy hearty stew")
    assert 'sets it down without a word. "Two Zenni," May says.' in out
    assert w.globals["hearts"] == 4 and w.globals["zenni"] == 8


def test_stew_capped_at_max():
    w, g = _at_bar(hearts=4, HEARTY_STEW=True, FOOD_DISCOUNT=True)
    assert '"One Zenni," May says.' in _do(g, "order stew")
    assert w.globals["hearts"] == 5 and w.globals["zenni"] == 9


def test_full_hearts_no_charge():
    w, g = _at_bar(hearts=5, HEARTY_STEW=True)
    for cmd in ("buy drink", "buy food", "buy stew"):
        assert _FULL in _do(g, cmd)
    assert w.globals["zenni"] == 10


def test_short_of_zenni():
    w, g = _at_bar(zenni=1)
    assert _SHORT in _do(g, "buy drink")
    assert w.globals["hearts"] == 3 and w.globals["zenni"] == 1


def test_not_at_the_bar():
    w, g = _at_bar()
    w.move_object(w.player, w.rooms["TALE-AND-ALE"])
    w.here = w.rooms["TALE-AND-ALE"]
    for cmd in ("buy drink", "order food", "rent room"):
        assert "There's no one here to sell you that." in _do(g, cmd)
    assert w.globals["zenni"] == 10


def test_buy_drink_charges_with_free_drink_pending():
    w, g = _at_bar(FREE_DRINK_PENDING=True)
    _do(g, "buy drink")
    assert w.globals["zenni"] == 8
    assert w.get_global("FREE-DRINK-PENDING")


# --- rooms -----------------------------------------------------------------------

def test_rent_room_full_heal_and_wake():
    w, g = _at_bar(hearts=1)
    out = _do(g, "rent room")         # always-max: Guest Room 3
    assert w.here.name == "GUEST-ROOM-3"
    assert out.index(_SLEEP) < out.index("Guest Room 3") < out.index(_WAKE3)
    assert "narrow bed, a single candle" not in out
    assert _BATH not in out
    assert w.globals["hearts"] == 5 and w.globals["zenni"] == 5
    assert "narrow bed, a single candle" in _do(g, "look")


def test_buy_room_random_room():
    w, g = _at_bar(hearts=1)
    with patch("content.tavern.random.randint", return_value=1):
        out = _do(g, "buy room")
    assert w.here.name == "GUEST-ROOM-1" and _WAKE1 in out


def test_guest_room_one_way_out():
    w, g = _at_bar(hearts=1)
    _do(g, "rent room")
    _do(g, "south")
    assert w.here.name == "UPSTAIRS-HALL"
    assert "You can't go that way." in _do(g, "north")


def test_rent_room_full_hearts_refused():
    w, g = _at_bar(hearts=5)
    assert _FULL_ROOM in _do(g, "rent room")
    assert w.here.name == "BAR" and w.globals["zenni"] == 10


def test_rent_room_short():
    w, g = _at_bar(zenni=4)
    assert _SHORT in _do(g, "rent room")
    assert w.here.name == "BAR" and w.globals["zenni"] == 4


def test_guest_rooms_out_of_zenni_pool():
    from content.zenni_rooms import ELIGIBLE_ROOMS
    assert not [r for r in ELIGIBLE_ROOMS if r.startswith("GUEST-ROOM")]


# --- inked -------------------------------------------------------------------------

def test_inked_rent_at_full_hearts_bathes():
    w, g = _at_bar(hearts=5, INKED=True)
    out = _do(g, "rent room")
    assert _RENT_INKED in out and _SLEEP not in out
    assert out.index("Guest Room 3") < out.index(_BATH) < out.index(_WAKE3)
    assert not w.get_global("INKED")
    assert w.globals["zenni"] == 5


def test_inked_rent_heals_too():
    w, g = _at_bar(hearts=2, INKED=True)
    _do(g, "rent room")
    assert w.globals["hearts"] == 5 and not w.get_global("INKED")


def test_inked_short_stays_inked():
    w, g = _at_bar(zenni=4, INKED=True)
    assert _SHORT in _do(g, "rent room")
    assert w.get_global("INKED")


def test_inked_may_refuses_everything_else():
    w, g = _at_bar(INKED=True, HEARTY_STEW=True, FREE_DRINK_PENDING=True)
    for cmd in ("buy drink", "buy food", "buy stew", "talk to may", "tip may 3",
                "give 3 zenni to may"):
        assert _MAY_INKED in _do(g, cmd), cmd
    assert w.globals["zenni"] == 10 and w.globals["hearts"] == 3
    assert w.get_global("FREE-DRINK-PENDING")


def test_inked_quest_hand_overs_wait():
    w, g = _at_bar(INKED=True, CELLAR_DRAINED=True)
    _do(g, "talk to may")
    assert not w.get_global("BOOTS-GIVEN")
    _do(g, "rent room")
    _do(g, "south")
    _do(g, "down")
    _do(g, "south")
    assert w.here.name == "BAR"
    _do(g, "talk to may")
    assert w.get_global("BOOTS-GIVEN")
