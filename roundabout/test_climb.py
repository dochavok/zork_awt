"""
CLIMB UP / CLIMB DOWN [X] are UP / DOWN, whatever X is (as Zork) — exits
check as usual; CLIMB UP TREE at the Old Oak is CLIMB TREE
(mechanics.md — Parser Verbs).
Run with: pytest roundabout/test_climb.py  (from c:\\zork_awt)
"""

import sys
import os
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do


def _at(room, *flags):
    w, g = _make_world()
    w.set_global("LIGHT-SPELL-ACTIVE", True)
    for flag in flags:
        w.set_global(flag, True)
    w.move_object(w.player, w.rooms[room])
    w.here = w.rooms[room]
    return w, g


@pytest.mark.parametrize("cmd", ["climb down", "climb down rope"])
def test_climb_down_the_roped_hole(cmd):
    w, g = _at("STORED-ROOM", "STORED-ROOM-DUG", "ROPE-TIED")
    w.move_object(w.objects["ROPE"], w.here)
    _do(g, cmd)
    assert w.here.name == "PILE-OF-RUBBLE"


def test_climb_down_checks_the_exit():
    w, g = _at("STORED-ROOM")
    assert "You can't go that way." in _do(g, "climb down")
    assert w.here.name == "STORED-ROOM"


def test_climb_up_from_the_rubble():
    w, g = _at("PILE-OF-RUBBLE", "STORED-ROOM-DUG", "ROPE-TIED")
    _do(g, "climb up")
    assert w.here.name == "STORED-ROOM"


def test_climb_with_nowhere_to_go():
    w, g = _at("TOWN-SQUARE")
    w.objects["CROWBAR"].clear_flag("INVISIBLE")
    w.move_object(w.objects["CROWBAR"], w.player)
    assert "You can't go that way." in _do(g, "climb up crowbar")
    assert "You can't go that way." in _do(g, "climb down")


@pytest.mark.parametrize("cmd", ["climb up tree", "climb tree"])
def test_climb_up_tree_is_climb_tree(cmd):
    w, g = _at("OLD-OAK")
    assert "You haul yourself up through the branches" in _do(g, cmd)


def test_the_rope_from_below():
    from content.objects import HANGING_ROPE_EXAMINE
    from content.mid_tier import _ROPE_STAYS
    w, g = _at("PILE-OF-RUBBLE", "STORED-ROOM-DUG", "ROPE-TIED")
    assert HANGING_ROPE_EXAMINE in _do(g, "examine rope")
    assert _ROPE_STAYS in _do(g, "take rope")
    assert _ROPE_STAYS in _do(g, "untie rope")
    _do(g, "climb up rope")
    assert w.here.name == "STORED-ROOM"


def test_climb_rope_from_below_goes_up():
    w, g = _at("PILE-OF-RUBBLE", "STORED-ROOM-DUG", "ROPE-TIED")
    _do(g, "climb rope")
    assert w.here.name == "STORED-ROOM"


def test_climb_tied_rope_from_above_goes_down():
    w, g = _at("STORED-ROOM", "STORED-ROOM-DUG", "ROPE-TIED")
    w.move_object(w.objects["ROPE"], w.here)
    _do(g, "climb rope")
    assert w.here.name == "PILE-OF-RUBBLE"


# --- LOWER ROPE (locations.md — Stored Room) and LOWER defaults ----------------

def test_lower_rope_before_it_is_tied():
    from content.verbs import _LOWER_UNTIED
    w, g = _at("STORED-ROOM", "STORED-ROOM-DUG")
    rope = w.objects["ROPE"]
    w.move_object(rope, w.player)
    assert _LOWER_UNTIED in _do(g, "lower rope")
    assert not w.get_global("ROPE-TIED")


@pytest.mark.parametrize("room", ["STORED-ROOM", "PILE-OF-RUBBLE"])
def test_lower_rope_once_tied(room):
    from content.verbs import _LOWER_TIED
    w, g = _at(room, "STORED-ROOM-DUG", "ROPE-TIED")
    w.move_object(w.objects["ROPE"], w.rooms["STORED-ROOM"])
    assert _LOWER_TIED in _do(g, "lower rope")


def test_lower_anything_else():
    w, g = _at("TOWN-SQUARE")
    w.move_object(w.objects["ROPE"], w.player)
    assert "Playing in this way with the coil of rope has no obvious effect." in _do(g, "lower rope")


# --- TIE / UNTIE away from the hole (mechanics.md — Parser Verbs) ---------------

def test_tie_and_untie_elsewhere():
    from content.mid_tier import _NOTHING_TO_TIE
    w, g = _at("TOWN-SQUARE")
    for name in ("ROPE", "CROWBAR"):
        obj = w.objects[name]
        obj.clear_flag("INVISIBLE")
        w.move_object(obj, w.player)
    assert _NOTHING_TO_TIE in _do(g, "tie rope to statue")
    assert "You can't tie the crowbar." in _do(g, "tie crowbar")
    assert "You can't tie the crowbar to that." in _do(g, "tie crowbar to statue")
    assert "It isn't tied to anything." in _do(g, "untie rope")
    assert "This cannot be tied, so it cannot be untied!" in _do(g, "untie crowbar")


@pytest.mark.parametrize("verb", ["untie", "free", "release"])
def test_untie_an_npc(verb):
    w, g = _at("BAR")
    assert "May isn't tied up." in _do(g, f"{verb} may")
