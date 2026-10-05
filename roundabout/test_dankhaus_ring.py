"""
The ring vs. the Dankhaus wards (npcs.md — Litlock, invisible entry).
Run with: pytest roundabout/test_dankhaus_ring.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do

_WARD = "a house that knows you haven't been introduced yet"
_UNSEEN = "Then he waits. He does not speak."
_INCITING = "Entertain me."
_NO_ENGAGE = "Litlock glances toward where you are, and waits. He does not speak."
_THERE = '"There you are," Litlock says'
_FAINT = 'From inside, faintly: "...and there you go."'


def _at_bog_se(invited=False, ring_on=False, inked=False):
    w, g = _make_world()
    w.set_global("DANKHAUS-PATH-FOUND", True)
    w.set_global("GRAVESTONE-FOUND", True)      # keep Bog-SE quiet
    w.objects["DANKHAUS"].clear_flag("INVISIBLE")
    if invited:
        w.set_global("DANKHAUS-INVITED", True)
    if inked:
        w.set_global("INKED", True)
    w.move_object(w.objects["RING"], w.player)
    w.move_object(w.player, w.rooms["BOG-SE"])
    w.here = w.rooms["BOG-SE"]
    if ring_on:
        _do(g, "wear ring")
    return w, g


def test_ward_stops_visible_uninvited_player():
    w, g = _at_bog_se()
    assert _WARD in _do(g, "east")
    assert w.here.name == "BOG-SE"


def test_ink_cancels_the_ring_at_the_ward():
    # Inked: Litlock's line turns the player away, ring or not (traps.md — Trap 45)
    w, g = _at_bog_se(ring_on=True, inked=True)
    out = _do(g, "east")
    assert 'Litlock\'s voice: "Not like that, you\'re not."' in out
    assert _WARD not in out
    assert w.here.name == "BOG-SE"


def test_ring_slips_past_the_ward():
    from content.quests import get_state
    w, g = _at_bog_se(ring_on=True)
    out = _do(g, "east")
    assert w.here.name == "DANKHAUS-COMMON-ROOM"
    assert _UNSEEN in out
    assert "He looks up." not in out
    assert _INCITING not in out
    assert get_state(w, "52") == "undiscovered"
    assert _UNSEEN in _do(g, "look")
    assert _NO_ENGAGE in _do(g, "talk to litlock")


def test_unseen_rooms_are_open():
    w, g = _at_bog_se(ring_on=True)
    _do(g, "east")
    _do(g, "east")
    assert w.here.name == "DANKHAUS-HEARTH-ROOM"


def test_ring_off_in_common_room_ejects():
    w, g = _at_bog_se(ring_on=True)
    _do(g, "east")
    out = _do(g, "remove ring")
    assert w.here.name == "BOG-SE"
    assert out.index(_THERE) < out.index("Bog of Eternal Stench") < out.index(_FAINT)
    assert _WARD not in out
    assert not w.get_global("LITLOCK-MET")


def test_ring_off_elsewhere_ejects_with_ward_line():
    w, g = _at_bog_se(ring_on=True)
    _do(g, "east")
    _do(g, "east")
    out = _do(g, "remove ring")
    assert w.here.name == "BOG-SE"
    assert out.index(_WARD) < out.index("Bog of Eternal Stench")
    assert _THERE not in out and _FAINT not in out


def test_dropped_ring_stays_inside():
    w, g = _at_bog_se(ring_on=True)
    _do(g, "east")
    _do(g, "east")
    _do(g, "drop ring")
    assert w.here.name == "BOG-SE"
    assert w.objects["RING"].location is w.rooms["DANKHAUS-HEARTH-ROOM"]


def test_invited_unseen_entry_holds_inciting_moment():
    from content.quests import get_state
    w, g = _at_bog_se(invited=True, ring_on=True)
    out = _do(g, "east")
    assert _UNSEEN in out and _INCITING not in out
    out = _do(g, "remove ring")
    assert w.here.name == "DANKHAUS-COMMON-ROOM"
    assert out.index(_THERE) < out.index(_INCITING)
    assert _FAINT not in out
    assert get_state(w, "52") != "undiscovered"


def test_invited_visible_entry_unchanged():
    w, g = _at_bog_se(invited=True)
    out = _do(g, "east")
    assert "He looks up." in out and _INCITING in out
    assert _UNSEEN not in out


def test_unseen_player_cannot_answer_the_tree():
    w, g = _at_bog_se(invited=True)
    _do(g, "east")
    assert w.get_global("LITLOCK-TIER") == "1"
    assert "There you are" not in _do(g, "wear ring")
    assert _NO_ENGAGE in _do(g, "1")
    assert w.get_global("LITLOCK-TIER") == "1"


def test_invited_ring_off_elsewhere_is_quiet():
    w, g = _at_bog_se(invited=True)
    _do(g, "east")
    _do(g, "east")
    _do(g, "wear ring")
    out = _do(g, "remove ring")
    assert w.here.name == "DANKHAUS-HEARTH-ROOM"
    assert _THERE not in out and _WARD not in out
