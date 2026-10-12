"""
PLUG / PATCH / REPAIR / FIX / GLUE X [WITH Y] and SEAL X (mechanics.md — Parser
Verbs): the aqueduct is SEAL JOINTS (locations.md — Collapsed Aqueduct), the
Whispering Jar's seal step (items.md), the bowl is ASSEMBLE BOWL, anything else
gets a line.
Run with: pytest roundabout/test_fix.py  (from c:\\zork_awt)
"""

import sys
import os
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do
from content.aqueduct import _NO_MORTAR, _STILL_GAP
from content.whispering_jar import _PRESS, _NO_FILL, _ALREADY_SEALED


def _at(room, *carried):
    w, g = _make_world()
    w.set_global("LIGHT-SPELL-ACTIVE", True)
    w.move_object(w.player, w.rooms[room])
    w.here = w.rooms[room]
    for name in carried:
        obj = w.objects[name]
        obj.clear_flag("INVISIBLE")
        w.move_object(obj, w.player)
    return w, g


@pytest.mark.parametrize("cmd", ["repair aqueduct", "fix joints", "patch blocks", "plug joints", "glue aqueduct"])
def test_fixing_the_aqueduct_is_seal(cmd):
    w, g = _at("COLLAPSED-AQUEDUCT")
    assert _NO_MORTAR in _do(g, cmd)
    w, g = _at("COLLAPSED-AQUEDUCT", "MORTAR")
    assert _STILL_GAP in _do(g, cmd + " with mortar")


@pytest.mark.parametrize("cmd", ["fix jar", "repair crack", "patch jar", "plug crack", "glue jar", "seal jar"])
def test_fixing_the_jar_is_the_seal_step(cmd):
    w, g = _at("PIPE-ROOM")
    assert _NO_FILL in _do(g, cmd)
    w, g = _at("PIPE-ROOM", "WAX-SEAL")
    assert _PRESS[:40] in _do(g, cmd)
    assert w.get_global("JAR-SEALED")
    assert _ALREADY_SEALED in _do(g, cmd)


def test_fix_jar_with_seal():
    w, g = _at("PIPE-ROOM", "WAX-SEAL")
    _do(g, "fix jar with seal")
    assert w.get_global("JAR-SEALED")


@pytest.mark.parametrize("cmd", ["glue bowl", "patch bowl"])
def test_glue_bowl_is_assemble(cmd):
    from content.shrine_bowl import _MISSING_PIECES
    w, g = _at("TOWN-SQUARE")
    assert _MISSING_PIECES in _do(g, cmd)


def test_fix_and_seal_anything_else():
    w, g = _at("TOWN-SQUARE", "CROWBAR")
    for verb in ("repair", "fix", "patch", "plug", "glue"):
        assert "You can't fix that." in _do(g, f"{verb} crowbar")
    assert "You can't seal that." in _do(g, "seal crowbar")


# --- APPLY X TO / ON Y (mechanics.md — Parser Verbs) ---------------------------

@pytest.mark.parametrize("prep", ["to", "on"])
def test_apply_seal_and_dust_to_the_jar(prep):
    w, g = _at("PIPE-ROOM", "WAX-SEAL", "SILVER-DUST")
    _do(g, f"apply seal {prep} jar")
    assert w.get_global("JAR-SEALED")
    _do(g, f"apply dust {prep} jar")
    assert w.get_global("JAR-DUSTED")


def test_apply_mortar_is_seal():
    w, g = _at("COLLAPSED-AQUEDUCT", "MORTAR")
    assert _STILL_GAP in _do(g, "apply mortar to joints")


def test_apply_holy_water_is_pour():
    w, g = _at("TOWN-SQUARE", "HOLY-WATER", "SILVER-STAKE")
    _do(g, "apply holy water to stake")
    assert w.get_global("STAKE-CONSECRATED")


def test_apply_anything_else():
    w, g = _at("TOWN-SQUARE", "CROWBAR", "TORCH")
    assert "You can't apply the crowbar to the torch." in _do(g, "apply crowbar to torch")


# --- TAKE / REMOVE X FROM Y (mechanics.md — Parser Verbs) -----------------------

def test_take_from_where_it_is():
    w, g = _at("STORAGE-AREA")
    cart, crowbar = w.objects["HAND-CART"], w.objects["CROWBAR"]
    crowbar.clear_flag("INVISIBLE")
    w.move_object(crowbar, cart)
    _do(g, "take crowbar from cart")
    assert crowbar.location is w.player


@pytest.mark.parametrize("verb", ["take", "remove"])
def test_take_from_where_it_is_not(verb):
    w, g = _at("STORAGE-AREA")
    beam = w.objects["SUPPORT-BEAM"]
    assert "The support beam isn't in the hand cart." in _do(g, f"{verb} beam from cart")
    assert beam.location is w.here                     # not picked up on the way


# --- TIP (tip over) and TURN (mechanics.md — Parser Verbs) ----------------------

from content.verbs import _ONLY_MAY, _IDOL_NUDGED, _WHICH_WAY


@pytest.mark.parametrize("cmd", ["tip shamus", "tip shamus 5"])
def test_only_may_takes_tips(cmd):
    w, g = _at("KITCHEN")
    zenni = w.globals["zenni"]
    assert _ONLY_MAY in _do(g, cmd)
    assert w.globals["zenni"] == zenni


def test_tip_idol_only_nudges_it():
    w, g = _at("IDOL-ROOM")
    assert _IDOL_NUDGED in _do(g, "tip idol")
    assert w.objects["IDOL"].location is w.here
    assert not w.get_global("IDOL-DOOR-SHUT")


def test_tip_the_loaded_cart_is_unload():
    from content import gravestone
    w, g = _at("TOWN-SQUARE")
    cart, stone = w.objects["HAND-CART"], w.objects["GRAVESTONE"]
    w.move_object(cart, w.here)
    stone.clear_flag("INVISIBLE")
    w.move_object(stone, cart)
    assert gravestone.cart_loaded(w)
    assert gravestone._TIPPED_OFF in _do(g, "tip cart")
    assert stone.location is w.here


def test_tip_anything_else():
    w, g = _at("TOWN-SQUARE", "CROWBAR")
    assert "You can't tip that over." in _do(g, "tip crowbar")


@pytest.mark.parametrize("cmd", ["turn dial", "spin the dial"])
def test_turn_dial_asks_which_way(cmd):
    w, g = _at("ALTAR")
    moves = w.moves
    assert _WHICH_WAY in _do(g, cmd)
    assert w.moves == moves


@pytest.mark.parametrize("verb", ["turn", "spin", "flip"])
def test_turn_anything_else(verb):
    w, g = _at("TOWN-SQUARE", "CROWBAR")
    assert "You can't turn that." in _do(g, f"{verb} crowbar")


def test_shut_is_close():
    w, g = _at("KITCHEN")
    assert "You can't close that." in _do(g, "shut door")
