"""
The Lost Apprentice's Cell (Quest 50; redesigned 2026-10-14, TODO #22):
he isn't digging when the player arrives; freed, he finishes his own tunnel,
hands over his gloves and climbs out, and Quest 50 completes there. An
invisible player he doesn't see.

Design: npcs.md (The Afflicted Apprentice), locations.md (Lost Apprentice's
Cell), quests.md (Quest 50), experience.md (Afflicted Apprentice 12 XP).
Run with: pytest roundabout/test_apprentice.py  (from c:\\zork_awt)
"""

import sys
import os
import io
import contextlib
from unittest.mock import patch
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do
from content import trap_side, quests
from content.trap_side import (APPRENTICE_ATTACKS, APPRENTICE_AFFLICTED, APPRENTICE_UNSEEING,
                               APPRENTICE_UNAWARE, _FREED, _DIGS_THROUGH, _FAREWELL,
                               _GLOVES_ADDED, _DIG_BLOCKED, _DUG, _NOT_THROUGH, _SURFACE)
from content.char_create import _PAUSE_CUE


def _cell(cls="rogue", **globals_):
    """In the cell with a lit torch; no room pays exploration XP."""
    from content import light
    w, g = _make_world(cls=cls, level=5, hearts=5)
    w.globals["skill_melee"] = True
    w.globals.update(globals_)
    for room in w.rooms.values():
        room.value = 0
    torch = w.objects["TORCH"]
    w.move_object(torch, w.player)
    torch.clear_flag("INVISIBLE")
    with contextlib.redirect_stdout(io.StringIO()):
        light.light_torch(w)
    cell = w.rooms["LOST-APPRENTICES-CELL"]
    w.move_object(w.player, cell)
    w.here = cell
    return w, g


def _free(w, g):
    """Three winning rounds; the pause answered and shown as <cue>."""
    buf = io.StringIO()

    def pause(prompt=""):
        buf.write("<" + prompt + ">")
        return ""
    with patch("sys.stdout", buf), patch("content.char_create.input", pause), \
         patch("content.player.roll", return_value=99), \
         patch("content.combat.random.randint", return_value=1):
        for _ in range(3):
            g.do_turn("kill apprentice")
    return buf.getvalue()


# --- He isn't digging; seen or unseen ---------------------------------------

def test_first_sight_then_presence():
    w, g = _cell()
    assert APPRENTICE_ATTACKS in _do(g, "look")
    out = _do(g, "look")
    assert APPRENTICE_AFFLICTED in out and APPRENTICE_ATTACKS not in out


def test_he_is_not_digging():
    # npcs.md — the affliction has stopped his progress
    assert "scraping" not in APPRENTICE_ATTACKS
    assert "stopped mid-scrape" in APPRENTICE_ATTACKS


def test_invisible_he_doesnt_see_you():
    w, g = _cell(ring_worn=True)
    out = _do(g, "look")
    assert APPRENTICE_UNSEEING in out and APPRENTICE_ATTACKS not in out
    assert APPRENTICE_UNAWARE in _do(g, "look")


def test_taking_the_ring_off_he_sees_you_and_attacks():
    w, g = _cell(ring_worn=True)
    _do(g, "look")
    w.globals["ring_worn"] = False
    assert APPRENTICE_ATTACKS in _do(g, "look")
    assert APPRENTICE_AFFLICTED in _do(g, "look")


def test_inked_he_sees_you():
    # Ink (Trap 45) cancels the ring's invisibility — the Chuckle House rule
    w, g = _cell(ring_worn=True, INKED=True)
    assert APPRENTICE_ATTACKS in _do(g, "look")


def test_invisible_attacking_him_is_a_normal_fight():
    w, g = _cell(ring_worn=True)
    out = _free(w, g)
    assert _FREED in out and w.get_global("APPRENTICE-FREED")


# --- Freed: he digs himself out ---------------------------------------------

def test_freed_he_digs_through_hands_over_the_gloves_and_leaves():
    w, g = _cell()
    out = _free(w, g)
    cue = "<" + _PAUSE_CUE + ">"
    assert out.count(cue) == 1
    assert (out.index(_FREED) < out.index(_DIGS_THROUGH) < out.index(cue)
            < out.index(_FAREWELL) < out.index(_GLOVES_ADDED))
    assert w.objects["APPRENTICE-GLOVES"].location is w.player
    assert w.objects["APPRENTICE"].location is None
    assert w.get_global("TUNNEL-DUG")


def test_quest_50_completes_at_the_handover():
    # quests.md — Quest 50: 12 XP, 5 Zenni; experience.md — the apprentice 12 XP
    w, g = _cell(cls="rogue")
    zenni = w.globals["zenni"]
    _free(w, g)
    assert quests.is_complete(w, "50")
    assert w.here.name == "LOST-APPRENTICES-CELL"       # not on reaching the bog
    assert w.globals["xp"] == 12 + 12
    assert w.globals["zenni"] == zenni + 5


def test_no_shovel_needed_to_get_out():
    w, g = _cell()
    assert w.objects["SHOVEL"].location is not w.player
    _free(w, g)
    out = _do(g, "up")
    assert _SURFACE in out
    assert w.here.name == "BOG-NW"


def test_dig_before_and_after():
    w, g = _cell()
    _do(g, "look")
    assert _DIG_BLOCKED in _do(g, "dig")
    assert _NOT_THROUGH in _do(g, "up")
    _free(w, g)
    assert _DUG in _do(g, "dig")
    w.move_object(w.objects["SHOVEL"], w.player)
    w.objects["SHOVEL"].clear_flag("INVISIBLE")
    assert _DUG in _do(g, "use shovel")


def test_an_old_save_with_him_freed_in_the_cell():
    # Before 2026-10-14 a freed apprentice waited for the shovel
    w, g = _cell()
    w.set_global("APPRENTICE-FREED", True)
    with patch("content.char_create.input", lambda p="": ""):
        out = _do(g, "wait")
    assert _FAREWELL in out
    assert quests.is_complete(w, "50")
