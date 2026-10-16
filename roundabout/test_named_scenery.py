"""
Nouns the room text names (TODO #28, 2026-10-15; locations.md under each room):
the plain ones answer with the default line; the volcano, the Idol Room's
pedestal, the Ritual Circle's stones and symbol have their own; the drain's
sacking is the drain.
Run with: pytest roundabout/test_named_scenery.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import pytest

from test_room_exits import _look, _do
from content.scenery import VOLCANO, VOLCANO_FOUND, PEDESTAL, PEDESTAL_EMPTY, RING_STONES, CIRCLE_SYMBOL
from content.upper_tier import SALT_ON_PEDESTAL, _IDOL_SPOTTED
from content.cellar import _EX_COVER_OFF


def _say(room, command, **globals_):
    w, g, _ = _look(room, LIGHT_SPELL_ACTIVE=True, **globals_)
    return w, _do(g, command)


@pytest.mark.parametrize("room, noun, desc", [
    ("BACK-ALLEY", "crates", "crates"), ("BACK-ALLEY", "barrels", "crates"),
    ("ARCHERY-RANGE", "targets", "targets"),
    ("CHURCH-NAVE", "pews", "pews"),
    ("MAUSOLEUM", "iron door", "iron door"),
    ("CRYPT", "alcoves", "alcoves"), ("CRYPT", "passage", "passage"),
    ("CREATURE-DEN", "bones", "bones"),
])
def test_plain_scenery(room, noun, desc):
    _, out = _say(room, f"x {noun}")
    assert f"You see nothing special about the {desc}." in out


def test_footprints_only_once_the_text_names_them():
    _, out = _say("CRYPT", "x footprints")
    assert "You can't see any footprints here!" in out              # first visit: undisturbed dust
    _, out = _say("CRYPT", "x footprints", CRYPT_VISITS=2)
    assert "You see nothing special about the footprints." in out


@pytest.mark.parametrize("room", ["VOLCANO", "ROUNDABOUT-WASTELAND"])
def test_volcano(room):
    _, out = _say(room, "x volcano")
    assert VOLCANO in out
    _, out = _say(room, "x volcano", VOLCANO_STAIRS_FOUND=True)
    assert VOLCANO_FOUND in out and VOLCANO not in out


@pytest.mark.parametrize("verb", ["touch", "press", "push", "activate"])
def test_rune_stones_answer_to_touch_press_push(verb):
    w, g, _ = _look("RITUAL-CIRCLE")
    assert "The Earth stone hums and lights from within." in _do(g, f"{verb} earth stone")
    assert '"The child looks disappointed in you."' in _do(g, f"{verb} heart stone")


def test_push_elsewhere_unchanged():
    w, g, _ = _look("RITUAL-CIRCLE")
    assert "Pushing the stones has no effect." in _do(g, "push stones")


def test_pedestal_by_state():
    w, g, _ = _look("IDOL-ROOM")
    assert PEDESTAL in _do(g, "x pedestal")
    w.set_global("IDOL-PLATE-SPOTTED", True)
    assert PEDESTAL + " " + _IDOL_SPOTTED in _do(g, "x pedestal")
    w.move_object(w.objects["IDOL"], None)
    w.set_global("IDOL-PLATE-SPOTTED", False)
    assert PEDESTAL_EMPTY in _do(g, "x pedestal")
    w.set_global("IDOL-SWAPPED", True)
    assert SALT_ON_PEDESTAL in _do(g, "x pedestal")


def test_ritual_circle():
    _, out = _say("RITUAL-CIRCLE", "x stones")
    assert RING_STONES in out
    _, out = _say("RITUAL-CIRCLE", "x stone")
    assert "Which stone do you mean" in out                       # one stone: still asks
    _, out = _say("RITUAL-CIRCLE", "x symbol")
    assert CIRCLE_SYMBOL in out


def test_sacking_is_the_drain():
    w, g, _ = _look("KITCHEN", CELLAR_DOOR_OPEN=True, DRAIN_COVER_OFF=True)
    out = _do(g, "x sacking")
    assert _EX_COVER_OFF in out and out == _do(g, "x drain")
