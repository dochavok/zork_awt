"""
The Pie Rat Ship gangplank (locations.md — Pie Rat Ship — Deck, The gangplank).
BOARD SHIP and EAST from the Docks are the same action: the disguise and the
explosion, or the Pie Rat Coin.
Run with: pytest roundabout/test_gangplank.py  (from c:\\zork_awt)
"""

import sys
import os
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do
from content import ship

_ENTRIES = ["board ship", "east"]


def _docks(disguise=False, blown=False, returned=False, coin=False):
    w, g = _make_world(cls="warrior")
    w.move_object(w.player, w.rooms["DOCKS"])
    w.here = w.rooms["DOCKS"]
    if disguise:
        w.move_object(w.objects["PIE-RAT-DISGUISE"], w.player)
    if blown:
        w.set_global("PIE-RATS-GONE", True)
    if returned:
        w.set_global("SHIP-RETURNED", True)
    if coin:
        w.move_object(w.objects["PIE-RAT-COIN"], w.player)
    return w, g


@pytest.mark.parametrize("cmd", _ENTRIES)
def test_no_disguise_before_explosion(cmd):
    w, g = _docks()
    assert ship._NO_DISGUISE in _do(g, cmd)
    assert w.here.name == "DOCKS"


@pytest.mark.parametrize("cmd", _ENTRIES)
def test_no_disguise_after_explosion(cmd):
    w, g = _docks(blown=True)
    assert ship._NO_DISGUISE in _do(g, cmd)
    assert w.here.name == "DOCKS"


@pytest.mark.parametrize("cmd", _ENTRIES)
def test_disguise_but_crew_aboard(cmd):
    w, g = _docks(disguise=True)
    assert ship._CREW_ABOARD in _do(g, cmd)
    assert w.here.name == "DOCKS"


@pytest.mark.parametrize("cmd", _ENTRIES)
def test_disguise_after_explosion_boards(cmd):
    w, g = _docks(disguise=True, blown=True)
    _do(g, cmd)
    assert w.here.name == "SHIP-DECK"


@pytest.mark.parametrize("cmd", _ENTRIES)
def test_returned_without_coin_refused(cmd):
    w, g = _docks(disguise=True, blown=True, returned=True)
    assert ship._NO_COIN in _do(g, cmd)
    assert w.here.name == "DOCKS"


@pytest.mark.parametrize("cmd", _ENTRIES)
@pytest.mark.parametrize("disguise", [False, True])
def test_coin_boards_with_or_without_disguise(cmd, disguise):
    w, g = _docks(disguise=disguise, blown=True, returned=True, coin=True)
    _do(g, cmd)
    assert w.here.name == "SHIP-DECK"


@pytest.mark.parametrize("cmd", _ENTRIES)
def test_coin_boards_even_before_explosion(cmd):
    w, g = _docks(coin=True)
    _do(g, cmd)
    assert w.here.name == "SHIP-DECK"


def test_west_off_the_deck_unchecked():
    w, g = _docks(disguise=True, blown=True)
    _do(g, "east")
    w.move_object(w.objects["PIE-RAT-DISGUISE"], None)
    _do(g, "west")
    assert w.here.name == "DOCKS"
