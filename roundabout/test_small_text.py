"""
Small text fixes from the v2.7 playtest (TODO #32, 2026-10-15): the Bone
Passage's door once open (locations.md — The Bone Passage), the gravestone
back at the Graveyard (items.md — Gravestone), the heart necklace's lines
(items.md — Heart Necklace).
Run with: pytest roundabout/test_small_text.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from testkit import _do, _look
from content.tunnels import _BONE_DOOR_SHUT, _BONE_DOOR_OPEN
from content.gravestone import EXAMINE_STONE, _GRAVEYARD_STONE
from content.verbs import _NECKLACE_ON, _NECKLACE_OFF


def test_bone_passage_door_open_or_shut():
    w, g, _ = _look("BONE-PASSAGE", LIGHT_SPELL_ACTIVE=True)
    out = _do(g, "look")
    assert _BONE_DOOR_SHUT in out and _BONE_DOOR_OPEN not in out
    w.set_global("TUNNEL-DOOR-OPEN", True)
    out = _do(g, "look")
    assert _BONE_DOOR_OPEN in out and _BONE_DOOR_SHUT not in out


def test_gravestone_back_at_the_graveyard_reads_standing():
    w, g, _ = _look("BOG-SE")
    w.objects["GRAVESTONE"].flags.discard("INVISIBLE")
    w.move_object(w.objects["HAND-CART"], w.player)
    assert EXAMINE_STONE in _do(g, "x gravestone")
    _do(g, "load stone onto cart")
    w.move_object(w.player, w.rooms["GRAVEYARD"])
    w.here = w.rooms["GRAVEYARD"]
    _do(g, "unload stone")
    for cmd in ("x gravestone", "read gravestone"):
        out = _do(g, cmd)
        assert _GRAVEYARD_STONE in out and "tip up one edge" not in out


def test_heart_necklace_names_the_heart():
    w, g, _ = _look("TOWN-SQUARE")
    w.globals.update({"hearts": 5, "max_hearts": 5})
    necklace = w.objects["HEART-NECKLACE"]
    necklace.flags.discard("INVISIBLE")
    w.move_object(necklace, w.player)
    assert _NECKLACE_ON in _do(g, "wear necklace")
    assert w.globals["max_hearts"] == 6
    out = _do(g, "remove necklace")
    assert _NECKLACE_OFF in out and "removed." not in out
    assert w.globals["max_hearts"] == 5
