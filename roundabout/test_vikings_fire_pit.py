"""
Trial 3 — the Fire Pit (locations.md — The Fire Pit, Viking Encampment;
quests.md — Quest 57). Winning tells the player to bring Aylora back,
Ivanaar asks for her until they do, and DRAG AYLORA works like TAKE AYLORA.
Run with: pytest roundabout/test_vikings_fire_pit.py  (from c:\\zork_awt)
"""

import sys
import os
import pytest
from unittest.mock import patch
sys.path.insert(0, os.path.dirname(__file__))

from testkit import _make_world, _do

NUDGE = 'A nearby Viking stares at her, then at you. "Ivanaar won\'t believe that unless he sees it."'
NOT_HERE = ('"You\'re standing. That\'s something. But Aylora\'s not here to tell me '
            'how it went — and I\'ll believe it when I see it."')
TWO_DOWN = '"Two down. The fire pit is west. Don\'t embarrass yourself."'
DRAG = "You get her under the arms and start to drag."
HANDOFF = '"...Thornbrew?" he finally asks.'


def _fire_pit(cls="warrior"):
    w, g = _make_world(cls=cls)
    w.set_global("RIDDLE-DONE", True)
    w.set_global("CIRCLE-DONE", True)
    w.move_object(w.player, w.rooms["FIRE-PIT"])
    w.here = w.rooms["FIRE-PIT"]
    return w, g


def _drink(g, strength):
    with patch("content.player.roll_class_bonus", lambda w, skill: strength):
        return _do(g, "drink")


def test_winning_nudges_the_player_to_bring_her_back():
    w, g = _fire_pit()
    out = _drink(g, 20)
    assert "Aylora passes out." in out
    assert NUDGE in out
    assert out.index("Aylora passes out.") < out.index(NUDGE)


def test_losing_has_no_nudge():
    w, g = _fire_pit()
    out = _drink(g, 0)
    assert NUDGE not in out
    assert not w.get_global("AYLORA-OUT")


def test_ivanaar_points_west_before_the_contest():
    w, g = _fire_pit()
    _do(g, "east")
    assert TWO_DOWN in _do(g, "talk to ivanaar")


def test_ivanaar_asks_for_aylora_when_she_was_left_behind():
    w, g = _fire_pit()
    _drink(g, 20)
    _do(g, "east")
    out = _do(g, "talk to ivanaar")
    assert NOT_HERE in out
    assert TWO_DOWN not in out
    assert w.objects["RUNED-METAL"].location is not w.player


@pytest.mark.parametrize("cmd", ["take aylora", "drag aylora"])
def test_take_or_drag_aylora_back_triggers_the_handoff(cmd):
    w, g = _fire_pit()
    _drink(g, 20)
    assert DRAG in _do(g, cmd)
    out = _do(g, "east")
    assert HANDOFF in out
    assert "[Runed Metal added to inventory.]" in out
    assert w.objects["RUNED-METAL"].location is w.player


def test_drag_aylora_before_she_is_out():
    w, g = _fire_pit()
    out = _do(g, "drag aylora")
    assert "You can't take Aylora." in out
    assert not w.get_global("AYLORA-DRAGGED")


def test_drag_anything_else():
    w, g = _fire_pit()
    metal = w.objects["RUNED-METAL"]
    w.move_object(metal, w.player)
    assert "You can't drag that." in _do(g, "drag metal")
    assert metal.location is w.player


def test_drag_alone():
    w, g = _fire_pit()
    assert "Drag what?" in _do(g, "drag")
