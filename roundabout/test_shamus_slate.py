"""
Shamus's slate and weapon sales (npcs.md — Shamus, The slate; locations.md —
Kitchen). Weapons are always on sale; a Mage or Rogue without Weapon Use gets
Shamus's warning.
Run with: pytest roundabout/test_shamus_slate.py  (from c:\\zork_awt)
"""

import sys
import os
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do
from content import verbs

_SLATE = """Chalked on the slate, in a square, heavy hand:
  Torch ........... 3 Zenni
  Thin paper ...... 2 Zenni
  Gunpowder ....... 5 Zenni
  Fishing rod ..... 8 Zenni
  Tip Journal ..... 5 Zenni
  Dagger .......... 5 Zenni
  Mace ............ 25 Zenni
  Battle axe ...... 100 Zenni
Under that, smaller: Ask about the stew.
Under that, smaller still: No refunds."""


def _kitchen(cls="warrior", zenni=200):
    w, g = _make_world(cls=cls, zenni=zenni)
    w.move_object(w.player, w.rooms["KITCHEN"])
    w.here = w.rooms["KITCHEN"]
    return w, g


def test_kitchen_mentions_the_slate():
    w, g = _kitchen()
    assert "Prices are chalked on a slate by the door." in _do(g, "look")


@pytest.mark.parametrize("cmd", ["read slate", "look at slate", "examine slate",
                                 "list", "wares", "prices"])
def test_slate_reads(cmd):
    w, g = _kitchen()
    assert _SLATE in _do(g, cmd)


def test_list_outside_the_kitchen_is_not_the_slate():
    w, g = _make_world(cls="warrior")
    assert "Chalked on the slate" not in _do(g, "list")


def test_bought_items_are_sold_but_torch_stays():
    w, g = _kitchen()
    _do(g, "buy mace")
    _do(g, "buy torch")
    out = _do(g, "read slate")
    assert "  Mace ............ (sold)" in out
    assert "  Torch ........... 3 Zenni" in out


def test_talk_points_at_the_slate():
    w, g = _kitchen()
    out = _do(g, "talk to shamus")
    assert ('Shamus wipes his hands on his apron. "What can I do for you?" He tips his '
            'head at the slate by the door. "Prices are up. Ask if you need something '
            'that isn\'t."') in out


@pytest.mark.parametrize("cmd,name,price", [
    ("buy dagger", "DAGGER", 5), ("buy mace", "MACE", 25),
    ("buy battle axe", "BATTLE-AXE", 100), ("buy axe", "BATTLE-AXE", 100),
    ("buy tip journal", "TIP-JOURNAL", 5),
])
def test_buying(cmd, name, price):
    w, g = _kitchen()
    out = _do(g, cmd)
    assert w.objects[name] in w.player.contents
    assert w.globals["zenni"] == 200 - price
    assert verbs._UNTRAINED not in out


@pytest.mark.parametrize("cls", ["mage", "rogue"])
def test_untrained_buyer_gets_the_warning(cls):
    w, g = _kitchen(cls=cls)
    w.globals.pop("skill_melee", None)
    out = _do(g, "buy dagger")
    assert "slides the dagger across the counter" in out and verbs._UNTRAINED in out
    assert w.objects["DAGGER"] in w.player.contents


def test_trained_mage_no_warning():
    w, g = _kitchen(cls="mage")
    w.globals["skill_melee"] = True
    assert verbs._UNTRAINED not in _do(g, "buy dagger")


def test_short_of_zenni():
    w, g = _kitchen(zenni=50)
    assert "(Need 100, have 50.)" in _do(g, "buy battle axe")
    assert w.objects["BATTLE-AXE"].location is None
