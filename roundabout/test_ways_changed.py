"""
When a room's ways change, its next description is full, even in BRIEF
(mechanics.md — Room Descriptions Name Their Exits; TODO #14).
Run with: pytest roundabout/test_ways_changed.py  (from c:\\zork_awt)
"""

import io
import os
import sys
import contextlib
from unittest.mock import patch

import pytest
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world
from engine.game import M_END


def _quiet(fn, *args):
    with contextlib.redirect_stdout(io.StringIO()):
        return fn(*args)


def _arrive(w, g, room, perceive=False):
    """Walk in as the game does (enter, describe, hooks), then end the turn."""
    out = io.StringIO()
    with contextlib.redirect_stdout(out), \
            patch("content.player.check_perception", return_value=perceive), \
            patch("content.perception.check_perception", return_value=perceive), \
            patch("random.randint", side_effect=lambda lo, hi: hi):
        g.enter_room(w.rooms[room])
        if w.rooms[room].action is not None:
            w.rooms[room].action(w, M_END)
    return out.getvalue()


def _lit(w):
    torch = w.objects["TORCH"]
    w.move_object(torch, w.player)
    torch.clear_flag("INVISIBLE")
    from content import light
    _quiet(light.light_torch, w)


# --- The rule, end to end in BRIEF ----------------------------------------------

def test_graveyard_after_litlocks_reveal_shows_the_chuckle_house_once():
    from content import dankhaus
    w, g = _make_world()
    _arrive(w, g, "GRAVEYARD")
    assert "east" not in _arrive(w, g, "GRAVEYARD").split("\n", 1)[1]   # BRIEF: the title only
    _quiet(dankhaus._bonk, w)
    out = _arrive(w, g, "GRAVEYARD")
    assert "east" in out.lower()                       # the full description, once
    assert _arrive(w, g, "GRAVEYARD").strip().splitlines()[0] == w.rooms["GRAVEYARD"].desc


def test_volcano_stairs_found_on_a_return_show_on_that_arrival():
    w, g = _make_world()
    _arrive(w, g, "VOLCANO")                           # first visit, not found
    out = _arrive(w, g, "VOLCANO", perceive=True)      # BRIEF return, found now
    assert "an uneven staircase leads down" in out
    assert "staircase" not in _arrive(w, g, "VOLCANO")  # and BRIEF again after


def test_mine_entrance_after_the_cave_in_says_so_on_the_next_arrival():
    from content import mine
    w, g = _make_world()
    _arrive(w, g, "MINE-ENTRANCE")
    w.move_object(w.player, w.rooms["ROUNDABOUT-FOREST"])
    w.here = w.rooms["ROUNDABOUT-FOREST"]
    _quiet(mine._explode, w)
    assert "The entrance is gone." in _arrive(w, g, "MINE-ENTRANCE")


# --- Every place a way changes marks its rooms -----------------------------------

def _setup_and_act(case):
    """Returns (world, rooms that must be marked) after the real action."""
    from content import (aqueduct, cellar, chuckle, combat_room, dankhaus, dark_branch,
                         keeper, mine, shrine_path, still_den, trap_side, tunnels,
                         upper_tier, mid_tier, mine_branch, rooms)
    w, g = _make_world()
    for r in w.rooms.values():
        r.visited = True

    def at(room):
        w.move_object(w.player, w.rooms[room])
        w.here = w.rooms[room]

    def hold(*names):
        for n in names:
            o = w.objects[n]
            w.move_object(o, w.player)
            o.clear_flag("INVISIBLE")

    with contextlib.redirect_stdout(io.StringIO()), \
            patch("content.player.check_perception", return_value=True), \
            patch("content.perception.check_perception", return_value=True), \
            patch("content.player.roll_class_bonus", return_value=99), \
            patch("random.randint", side_effect=lambda lo, hi: hi):
        if case == "aqueduct seal":
            at("COLLAPSED-AQUEDUCT"); w.set_global("BLOCKS-PLACED", 3); hold("MORTAR")
            aqueduct.seal(w)
            return w, ["COLLAPSED-AQUEDUCT", "COLLAPSED-GALLERY", "RICKETY-BRIDGE"]
        if case == "gallery propped":
            at("COLLAPSED-GALLERY"); w.set_global("TIMBERS-DOWN", 3); hold("SUPPORT-BEAM")
            aqueduct.prop_passage(w)
            return w, ["COLLAPSED-GALLERY", "RICKETY-BRIDGE"]
        if case == "timbers down":
            at("COLLAPSED-GALLERY"); w.set_global("TIMBERS-DOWN", 2); hold("PICKAXE")
            aqueduct.strike_timber(w)
            return w, ["COLLAPSED-GALLERY"]
        if case == "cellar door":
            at("KITCHEN"); w.set_global("CELLAR-DOOR-UNLOCKED", True)
            cellar.open_cellar_door(w)
            return w, ["KITCHEN"]
        if case == "cellar drained":
            at("KITCHEN"); w.set_global("CELLAR-DOOR-OPEN", True); w.set_global("DRAIN-COVER-OFF", True)
            hold("CROWBAR")
            cellar.clear_drain(w)
            return w, ["KITCHEN"]
        if case == "tunnel door":
            at("CELLAR"); w.set_global("CELLAR-DRAINED", True)
            cellar.open_tunnel_door(w)
            return w, ["CELLAR", "BONE-PASSAGE"]
        if case == "ghost freed":
            at("GHOSTS-ROOM")
            chuckle.free_ghost(w)
            return w, ["CHUCKLE-ENTRANCE", "REJECTION-MIRROR", "SHATTER-TRAP-MIRROR"]
        if case == "plate fired":
            at("COMBAT-ROOM")
            with patch("content.char_create.input", lambda p="": ""):
                combat_room._fire_plate(w)     # its Press-ENTER pause
            return w, ["COMBAT-ROOM"]
        if case == "flooding slab":
            from content import flooding
            at("FLOODING-ROOM")
            flooding._fire(w)                  # the Den's way north is sealed
            return w, ["CREATURE-DEN"]
        if case == "dankhaus path":
            at("BOG-SE")
            dankhaus.path_check(w)
            return w, ["BOG-SE"]
        if case == "litlock's reveal":
            at("LITLOCKS-ROOM")
            dankhaus._bonk(w)
            return w, ["GRAVEYARD"]
        if case == "lantern hung":
            at("DARK-ROOM"); hold("GUARDIANS-LANTERN")
            dark_branch.light_lantern(w)
            return w, ["DARK-ROOM"]
        if case == "pool frozen":
            at("FLOODED-PASSAGE"); hold("GLACIER-MELT")
            w.prsa, w.prso, w.prsi = "V-POUR", w.objects["GLACIER-MELT"], None
            from engine.game import M_BEG
            w.rooms["FLOODED-PASSAGE"].action(w, M_BEG)
            return w, ["FLOODED-PASSAGE"]
        if case == "crawlspace spotted":
            at("INSCRIPTION-CHAMBER")
            from engine.game import M_ENTER
            w.rooms["INSCRIPTION-CHAMBER"].action(w, M_ENTER)
            return w, ["INSCRIPTION-CHAMBER"]
        if case == "keeper's door":
            at("CHURCH-NAVE"); hold("KEY-RING")
            keeper.unlock_door(w)
            return w, ["CHURCH-NAVE"]
        if case == "stored room dug":
            at("STORED-ROOM"); hold("SHOVEL")
            mid_tier._dig(w)
            return w, ["STORED-ROOM"]
        if case == "rope tied":
            at("STORED-ROOM"); w.set_global("STORED-ROOM-DUG", True); hold("ROPE")
            w.prsi = None
            mid_tier._tie_rope(w)
            return w, ["STORED-ROOM"]
        if case == "cave-in":
            at("ROUNDABOUT-FOREST")
            mine._explode(w)
            return w, ["MINE-ENTRANCE", "MAIN-SHAFT"]
        if case == "assay gap, mine side":
            mine_branch.on_enter(w, w.rooms["ASSAY-ROOM"])
            return w, ["ASSAY-ROOM"]
        if case == "assay gap, tunnel side":
            at("HIDDEN-SECONDARY-ENTRANCE")
            from engine.game import M_ENTER
            mine_branch.hidden_action(w, M_ENTER)
            return w, ["ASSAY-ROOM"]
        if case == "portcullis propped":
            at("PORTCULLIS-CORRIDOR"); w.set_global("PORTCULLIS", "discharged")
            w.set_global("PORTCULLIS-HELD", w.moves); hold("PORTCULLIS-BAR")
            shrine_path.use_bar(w)
            return w, ["PORTCULLIS-CORRIDOR"]
        if case == "key door":
            at("MID-TIER-KEY-DOOR"); hold("MIDDLE-TIER-KEY"); w.prsi = None
            shrine_path.unlock_key_door(w)
            return w, ["MID-TIER-KEY-DOOR"]
        if case == "bones cleared":
            at("ANTECHAMBER")
            still_den.clear_bones(w)
            return w, ["ANTECHAMBER"]
        if case == "alcove opened":
            at("TOOL-ALCOVE"); w.set_global("ALCOVE-FOUND", True); hold("INCANTATION-SCROLL")
            w.prsa, w.prso = "V-READ", w.objects["INCANTATION-SCROLL"]
            from engine.game import M_BEG
            w.rooms["TOOL-ALCOVE"].action(w, M_BEG)
            return w, ["TOOL-ALCOVE"]
        if case == "apprentice's tunnel":
            at("LOST-APPRENTICES-CELL"); w.set_global("APPRENTICE-FREED", True)
            with patch("content.char_create.input", lambda p="": ""):
                trap_side._digs_himself_out(w)     # he digs through himself
            return w, ["LOST-APPRENTICES-CELL"]
        if case == "boggart leaves":
            at("TOLL-BRIDGE"); hold("TOWN-CHARTER")
            tunnels.give_charter(w)
            return w, ["TOLL-BRIDGE"]
        if case == "idol slab drops":
            at("IDOL-ROOM")
            upper_tier.take_idol(w)
            return w, ["IDOL-ROOM"]
        if case == "idol slab pried":
            at("IDOL-ROOM"); w.set_global("IDOL-DOOR-SHUT", True); hold("CROWBAR")
            upper_tier.pry_idol_door(w)
            return w, ["IDOL-ROOM"]
        if case == "bedroom door":
            at("WIZARDS-TOWER")
            rooms.bedroom_door_check(w)
            return w, ["WIZARDS-TOWER"]
        if case == "volcano stairs":
            at("VOLCANO")
            rooms.volcano_stairs_check(w)
            return w, ["VOLCANO"]
        if case == "ship sails":
            from content import ship
            ship.on_enter(w, w.rooms["SEA-WEST"])
            return w, ["SHIP-DECK"]
    raise AssertionError(f"unknown case {case}")


CASES = [
    "aqueduct seal", "gallery propped", "timbers down", "cellar door", "cellar drained",
    "tunnel door", "ghost freed", "plate fired", "flooding slab", "dankhaus path", "litlock's reveal",
    "lantern hung", "pool frozen", "crawlspace spotted", "keeper's door", "stored room dug",
    "rope tied", "cave-in", "assay gap, mine side", "assay gap, tunnel side",
    "portcullis propped", "key door", "bones cleared", "alcove opened",
    "apprentice's tunnel", "boggart leaves", "idol slab drops", "idol slab pried",
    "bedroom door", "volcano stairs", "ship sails",
]


@pytest.mark.parametrize("case", CASES)
def test_the_change_marks_its_rooms_for_a_full_description(case):
    w, marked = _setup_and_act(case)
    for name in marked:
        assert w.rooms[name].visited is False, f"{case}: {name} not marked"


def test_passing_the_hidden_entrance_again_doesnt_remark_the_assay_room():
    from content import mine_branch
    from engine.game import M_ENTER
    w, g = _make_world()
    w.set_global("ASSAY-GAP-FOUND", True)
    w.rooms["ASSAY-ROOM"].visited = True
    _quiet(mine_branch.hidden_action, w, M_ENTER)
    assert w.rooms["ASSAY-ROOM"].visited is True
