"""
Quest state machine and cascades (quests.md). Rewards (XP, Zenni) for every
quest: test_progression.py. Discovery triggers: test_quest_discovery.py.

Run with: pytest roundabout/test_quests.py  (from c:\\zork_awt)
"""

import sys
import os
from unittest.mock import patch
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do
from content import quests

FOUNTAIN_DRY = "The fountain is dry. You'll need clean running water."
ADHESIVE = ("You work the clay in your hands under the fountain's spill until it softens, "
            "then keeps softening, into something smooth and tacky that holds whatever it "
            "touches. Clay adhesive — enough for one careful job.")


def _goto(w, room):
    w.move_object(w.player, w.rooms[room])
    w.here = w.rooms[room]


# --- State machine ---------------------------------------------------------------

def test_quest_lifecycle():
    w, g = _make_world()
    assert quests.get_state(w, "51") == "undiscovered"
    quests.discover(w, "51")
    assert quests.get_state(w, "51") == "discovered"
    quests.start(w, "51")
    assert quests.get_state(w, "51") == "in_progress"
    with patch("sys.stdout"):
        quests.complete(w, "51")
    assert quests.is_complete(w, "51")


def test_completion_is_permanent():
    w, g = _make_world()
    with patch("sys.stdout"):
        quests.complete(w, "40")
    quests.discover(w, "40")                   # a later trigger can't reopen it
    assert quests.get_state(w, "40") == "complete"


# --- Quest 22 cascade: the aqueduct sealed, the fountain runs (Quest 49's water) -------

def _clay(w):
    clay = w.objects["FIRE-CLAY"]
    clay.flags.discard("INVISIBLE")            # LOOK UP in the Thermal Vent Room finds it
    w.move_object(clay, w.player)


def test_fountain_dry_until_the_aqueduct_is_sealed():
    w, g = _make_world(cls="warrior")
    _clay(w)
    _goto(w, "TOWN-SQUARE")
    assert FOUNTAIN_DRY in _do(g, "mix clay with water")
    assert w.objects["FIRE-CLAY"].location is w.player


def test_sealing_the_aqueduct_completes_22_and_runs_the_fountain():
    w, g = _make_world(cls="warrior")
    _clay(w)
    _goto(w, "COLLAPSED-AQUEDUCT")
    w.move_object(w.objects["MORTAR"], w.player)
    with patch("content.player.roll", return_value=20):
        for _ in range(3):
            _do(g, "place blocks")
    _do(g, "seal joints with mortar")
    assert quests.is_complete(w, "22")
    assert w.objects["MORTAR"].location is not w.player       # used up

    _goto(w, "TOWN-SQUARE")
    assert ADHESIVE in _do(g, "mix clay with water")
    assert w.objects["FIRE-CLAY"].location is not w.player    # clay used up


# --- Quest 41: the kite, and the rune stone for Quest 42 ----------------------------

def test_kite_quest_end_to_end():
    w, g = _make_world(cls="warrior")
    _goto(w, "OLD-OAK")
    _do(g, "climb tree")
    _do(g, "take rune stone")
    _do(g, "give kite to child")
    assert quests.is_complete(w, "41")
    assert w.objects["OLD-OAK-RUNE-STONE"].location is w.player
    assert w.objects["KITE"].location is not w.player
