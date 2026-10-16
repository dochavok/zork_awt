"""
Quest 49 — ASSEMBLE BOWL and its synonyms (quests.md, mechanics.md): all
three pieces plus the clay adhesive become the Repaired Bowl.
Run with: pytest roundabout/test_assemble_bowl.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import pytest

from testkit import _make_world, _do, _carry
from content import shrine_bowl


@pytest.mark.parametrize("command", [
    "assemble bowl", "reassemble the bowl", "assemble",
    "repair bowl", "fix the bowl", "combine pieces", "combine bowl pieces",
])
def test_assembles_the_bowl(command):
    w, g = _make_world(cls="warrior")
    for name in shrine_bowl.PIECES + ("CLAY-ADHESIVE",):
        _carry(w, name)
    assert shrine_bowl._ASSEMBLED in _do(g, command)
    assert w.objects["REPAIRED-BOWL"].location is w.player
    assert all(w.objects[p].location is None for p in shrine_bowl.PIECES)


@pytest.mark.parametrize("command", ["repair bowl", "combine pieces"])
def test_synonyms_still_need_every_piece(command):
    w, g = _make_world(cls="warrior")
    _carry(w, "CLAY-ADHESIVE")
    assert shrine_bowl._MISSING_PIECES in _do(g, command)
