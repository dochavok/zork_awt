"""
Full sentences naming a missing tool get the designed line, not the parser's
"You can't see any X here!": SEAL JOINTS WITH MORTAR without the mortar, MIX
CLAY WITH WATER away from the fountain (SyntaxRule.obj2_optional). Other
rules still report a missing object.
Run with: pytest roundabout/test_optional_with.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do
from content import aqueduct, shrine_bowl


def _goto(w, name):
    w.move_object(w.player, w.rooms[name])
    w.here = w.rooms[name]


def _aqueduct():
    w, g = _make_world(cls="warrior")
    _goto(w, "COLLAPSED-AQUEDUCT")
    w.set_global("LIGHT-SPELL-ACTIVE", True)
    return w, g


def _hold(w, name):
    obj = w.objects[name]
    obj.flags.discard("INVISIBLE")
    w.move_object(obj, w.player)
    return obj


def test_seal_with_mortar_without_mortar():
    w, g = _aqueduct()
    out = _do(g, "seal joints with mortar")
    assert aqueduct._NO_MORTAR in out
    assert "can't see" not in out


def test_seal_with_mortar_still_works():
    w, g = _aqueduct()
    _hold(w, "MORTAR")
    w.set_global("BLOCKS-PLACED", 3)
    out = _do(g, "seal joints with mortar")
    assert aqueduct._SEALED in out
    assert w.get_global("AQUEDUCT-SEALED")


def test_mix_with_water_away_from_fountain():
    w, g = _make_world(cls="warrior")
    _hold(w, "FIRE-CLAY")
    _goto(w, "KITCHEN")
    out = _do(g, "mix clay with water")
    assert shrine_bowl._NO_WATER in out
    assert "can't see" not in out


def test_mix_with_water_at_running_fountain_still_works():
    w, g = _make_world(cls="warrior")
    _hold(w, "FIRE-CLAY")
    w.set_global("FOUNTAIN-RUNNING", True)
    out = _do(g, "mix clay with water")
    assert shrine_bowl._MIXED in out
    assert w.objects["CLAY-ADHESIVE"].location is w.player


def test_other_rules_still_report_a_missing_object():
    w, g = _make_world(cls="warrior")
    assert "You can't see any crowbar here!" in _do(g, "unlock statue with crowbar")
