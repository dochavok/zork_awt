"""
Quest 49 — the forest shrine pedestal and the Shrine Room plinth (quests.md
Quest 49 steps 6–7; locations.md Roundabout Forest and Shrine Room; mechanics.md
PRAY). TODO #15, 2026-10-14: IN works as ON, the in-bowl and bare offerings,
PRAY and EXAMINE at the shrine, and no implicit "(Taken)" off the pedestal.
Run with: pytest roundabout/test_shrine_pedestal.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import pytest

from test_room_exits import _look, _do
from content import shrine_bowl


def _forest(placed=False):
    w, g, _ = _look("ROUNDABOUT-FOREST")
    w.move_object(w.objects["REPAIRED-BOWL"], w.player)
    w.globals["zenni"] = 10
    if placed:
        _do(g, "put bowl on pedestal")
    return w, g


@pytest.mark.parametrize("command", [
    "put bowl on pedestal", "put bowl in shrine", "put bowl in pedestal", "put bowl on shrine",
])
def test_placing_the_bowl(command):
    w, g = _forest()
    assert shrine_bowl._BOWL_PLACED in _do(g, command)
    assert w.objects["REPAIRED-BOWL"].location is w.here
    assert w.get_global("BOWL-ON-PEDESTAL")


@pytest.mark.parametrize("command", ["put bowl in shrine", "put bowl on pedestal"])
def test_placed_bowl_is_not_auto_taken(command):
    """The old bug: PUT BOWL IN SHRINE auto-took the bowl and left the flag set."""
    w, g = _forest(placed=True)
    out = _do(g, command)
    assert "(Taken)" not in out
    assert shrine_bowl._ALREADY_PLACED in out
    assert w.objects["REPAIRED-BOWL"].location is w.here


def test_taken_bowl_is_listed_where_dropped():
    w, g = _forest(placed=True)
    _do(g, "take bowl")
    assert not w.get_global("BOWL-ON-PEDESTAL")
    assert shrine_bowl._BARE in _do(g, "look")         # mended: no remains left there
    _do(g, "south")
    _do(g, "drop bowl")
    assert "repaired bowl" in _do(g, "look")


def test_stale_flag_from_an_old_save_reads_correctly():
    """A save where the flag outlived the bowl: the bowl in hand is not on the pedestal."""
    w, g = _forest()
    w.set_global("BOWL-ON-PEDESTAL", True)
    out = _do(g, "look")
    assert shrine_bowl._ON_PEDESTAL_REPAIRED not in out
    assert shrine_bowl._BARE in out
    assert shrine_bowl._JUST_A_COIN in _do(g, "put zenni on pedestal")
    assert w.objects["REPAIRED-BOWL"].location is w.player


@pytest.mark.parametrize("command", [
    "put zenni on pedestal", "put zenni in bowl", "put zenni in shrine", "put zenni in pedestal",
    "offer zenni", "donate zenni", "give zenni to shrine", "offer", "donate",
])
def test_the_offering(command):
    w, g = _forest(placed=True)
    assert shrine_bowl._TRANSFORMED in _do(g, command)
    assert w.get_global("BOWL-TRANSFORMED")


def test_zenni_in_a_held_bowl_is_not_an_offering():
    w, g = _forest()
    assert "won't fit in the repaired bowl" in _do(g, "put zenni in bowl")
    assert w.globals["zenni"] == 10


def test_bare_offer_away_from_the_shrine_is_unchanged():
    w, g, _ = _look("TOWN-SQUARE")
    w.globals["zenni"] = 10
    assert "isn't one I recognize" in _do(g, "offer")
    assert w.globals["zenni"] == 10


def test_pray_follows_the_quest():
    w, g = _forest()
    assert shrine_bowl._PRAY_BROKEN in _do(g, "pray")
    _do(g, "put bowl on pedestal")
    assert shrine_bowl._PRAY_PLACED in _do(g, "pray")
    _do(g, "put zenni on pedestal")
    assert shrine_bowl._PRAY_DONE in _do(g, "pray")


def test_the_remains_stay_until_the_bowl_is_mended():
    """locations.md — Pedestal states (2026-10-14): remains until repaired, then bare."""
    w, g, out = _look("ROUNDABOUT-FOREST")
    assert shrine_bowl._REMAINS in out
    assert shrine_bowl._REMAINS in _do(g, "examine pedestal")
    w.move_object(w.objects["REPAIRED-BOWL"], w.player)      # as ASSEMBLE BOWL leaves it
    out = _do(g, "look")
    assert shrine_bowl._BARE in out and shrine_bowl._REMAINS not in out


@pytest.mark.parametrize("command", ["examine pedestal", "examine shrine"])
def test_examine_pedestal_shows_its_state(command):
    w, g = _forest()
    out = _do(g, command)
    assert shrine_bowl._PEDESTAL in out and shrine_bowl._BARE in out   # bowl in hand
    _do(g, "put bowl on pedestal")
    assert shrine_bowl._ON_PEDESTAL_REPAIRED in _do(g, command)
    _do(g, "put zenni on pedestal")
    assert shrine_bowl._ON_PEDESTAL_CRYSTAL in _do(g, command)
    _do(g, "take bowl")
    assert shrine_bowl._BARE in _do(g, command)


@pytest.mark.parametrize("command", ["examine plinth", "examine depression", "examine stone plinth"])
def test_shrine_room_plinth(command):
    w, g, _ = _look("SHRINE-ROOM")
    assert shrine_bowl.PLINTH in _do(g, command)


@pytest.mark.parametrize("command", ["put bowl in depression", "put bowl on plinth"])
def test_bowl_does_not_go_on_the_plinth(command):
    w, g, _ = _look("SHRINE-ROOM")
    w.move_object(w.objects["REPAIRED-BOWL"], w.player)
    assert shrine_bowl._NOT_THIS_SHRINE in _do(g, command)
    assert w.objects["REPAIRED-BOWL"].location is w.player
