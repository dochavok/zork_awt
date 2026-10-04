"""
Quest 54 — Fight the Knight. The full-score walkthrough is a Warrior, so it
only sees the Warrior line; these play the trial as a Mage and a Rogue.
Run with: pytest roundabout/test_knight.py  (from c:\\zork_awt)
"""

import sys
import os
import io
from unittest.mock import patch
sys.path.insert(0, os.path.dirname(__file__))

from engine.world import World
from engine.clock import Clock
from engine.game import Game
from content.init import initialize_world


def _make_world(cls="mage", level=3, hearts=5, zenni=10):
    from engine.parser import Parser
    from content.vocabulary import make_vocabulary
    from content.syntax import make_syntax_rules
    w = World()
    p = Parser(make_vocabulary(), make_syntax_rules())
    g = Game(w, p, Clock())
    initialize_world(w, g)
    w.globals.update({
        "hearts": hearts, "max_hearts": hearts, "level": level, "xp": 0, "zenni": zenni,
        "player_class": cls, "player_name": "Tess", "ring_corruption": 0,
        "ring_worn": False, "quest_states": {},
    })
    w.move_object(w.player, w.rooms["TOWN-SQUARE"])
    w.here = w.rooms["TOWN-SQUARE"]
    return w, g


def _do(g, cmd):
    buf = io.StringIO()
    with patch("sys.stdout", buf):
        g.do_turn(cmd)
    return buf.getvalue()


def _rolls(player, knight):
    """Fix one round: the player's roll and the knight's 2d8 total."""
    return (patch("content.player.roll", return_value=player),
            patch("content.knight.random.randint", side_effect=[knight, 0]))


def _round(g, player, knight):
    a, b = _rolls(player, knight)
    with a, b:
        return _do(g, "kill knight")


def test_warrior_is_waved_off():
    from content.quests import get_state
    w, g = _make_world(cls="warrior")
    assert "already know what I teach" in _do(g, "talk to knight")
    assert "don't need me for that" in _do(g, "fight knight")
    assert get_state(w, "54") == "undiscovered"


def test_below_level_three_turned_away():
    from content.quests import get_state
    w, g = _make_world(level=2)
    assert "I teach one thing" in _do(g, "talk to knight")
    assert get_state(w, "54") == "undiscovered"
    assert "Not yet" in _do(g, "challenge knight")
    assert not w.get_global("KNIGHT-FIGHTING")


def test_one_heart_refused():
    w, g = _make_world(hearts=1)
    assert "Rest first" in _do(g, "fight knight")


def test_mage_loses_then_wins_and_pays():
    from content.quests import get_state
    w, g = _make_world(cls="mage", hearts=3)
    out = _do(g, "fight knight")
    assert "I'm Tess, and I'm ready." in out and "draws his weapon" in out
    assert get_state(w, "54") == "discovered"
    assert "flat of his blade" in _round(g, 2, 9)
    out = _round(g, 2, 9)
    assert "keep your feet" in out
    assert w.globals["hearts"] == 1 and not w.get_global("KNIGHT-FIGHTING")
    assert "Ready to try again" in _do(g, "talk to knight")

    w.globals["hearts"] = 3
    assert _do(g, "fight knight").strip() == "He draws his weapon."
    w.globals["spell_fireball"] = True
    assert "Not that" in _do(g, "cast fireball at knight")
    for _ in range(2):
        assert "clean blow" in _round(g, 15, 3)
    out = _round(g, 15, 3)
    assert "Good, Tess," in out
    assert w.get_global("KNIGHT-WON") and not w.get_global("KNIGHT-FIGHTING")
    assert "Three Zenni, Tess" in _do(g, "talk to knight")

    w.globals["zenni"] = 2
    assert "Come back when you have it" in _do(g, "pay knight")
    w.globals["zenni"] = 5
    xp = w.globals["xp"]
    out = _do(g, "give knight three zenni")
    assert "arms ache" in out and "Shamus, at the inn" in out
    assert w.globals["skill_melee"] and w.globals["zenni"] == 2
    assert get_state(w, "54") == "complete"
    assert w.globals["xp"] == xp + 8
    assert "Keep your guard up" in _do(g, "talk to knight")
    assert "done with that" in _do(g, "kill knight")


def test_rogue_tie_to_one_heart_each_is_a_win():
    w, g = _make_world(cls="rogue", hearts=2)
    _do(g, "fight knight")
    w.globals["KNIGHT-HEARTS"] = 2
    out = _round(g, 7, 7)
    assert "both of you land one" in out and "Good, Tess," in out
    assert w.globals["hearts"] == 1 and w.get_global("KNIGHT-WON")


def test_leaving_abandons_trial():
    w, g = _make_world()
    _do(g, "fight knight")
    _round(g, 15, 3)
    _do(g, "east")
    _do(g, "west")
    assert not w.get_global("KNIGHT-FIGHTING")
    assert _do(g, "fight knight").strip() == "He draws his weapon."
    assert w.globals["KNIGHT-HEARTS"] == 4
