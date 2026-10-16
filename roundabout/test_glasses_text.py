"""
The Enchanted Glasses' text (items.md — Enchanted Glasses): the nightstand
line only in Will's Bedroom, a plain floor line anywhere else, and examine
text of their own — regular and after Kevry's enchantment.
Run with: pytest roundabout/test_glasses_text.py  (from c:\\zork_awt)
"""

import sys
import os
import io
from unittest.mock import patch
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from testkit import _make_world, _do
from content.objects import GLASSES_EXAMINE, GLASSES_EXAMINE_ENCHANTED


def _carrying_glasses(room, enchanted=False):
    w, g = _make_world()
    w.move_object(w.player, w.rooms[room])
    w.here = w.rooms[room]
    w.move_object(w.objects["ENCHANTED-GLASSES"], w.player)
    if enchanted:
        from content import kevry
        with patch("sys.stdout", io.StringIO()):
            kevry.enchant(w)
    return w, g


@pytest.mark.parametrize("enchanted,line", [
    (False, "There is a pair of wire-rimmed glasses here."),
    (True, "There is a pair of slightly glowing wire-rimmed glasses here."),
])
def test_dropped_outside_the_bedroom(enchanted, line):
    w, g = _carrying_glasses("TOWN-SQUARE", enchanted)
    _do(g, "drop glasses")
    out = _do(g, "look")
    assert line in out
    assert "nightstand" not in out


@pytest.mark.parametrize("enchanted,line", [
    (False, "A pair of wire-rimmed glasses rests on the nightstand."),
    (True, "A pair of slightly glowing wire-rimmed glasses rests on the nightstand."),
])
def test_back_on_the_nightstand(enchanted, line):
    w, g = _carrying_glasses("WIZARDS-BEDROOM", enchanted)
    w.move_object(w.objects["ENCHANTED-GLASSES"], w.here)
    assert w.objects["ENCHANTED-GLASSES"].ldesc == line


@pytest.mark.parametrize("enchanted,text", [
    (False, GLASSES_EXAMINE), (True, GLASSES_EXAMINE_ENCHANTED),
])
def test_examine(enchanted, text):
    w, g = _carrying_glasses("TOWN-SQUARE", enchanted)
    out = _do(g, "examine glasses")
    assert text in out
    assert "nightstand" not in out
