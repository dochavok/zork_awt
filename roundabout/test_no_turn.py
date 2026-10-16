"""
No turn means nothing moves (mechanics.md — Parser Verbs, No turn): a command
that uses no turn neither advances the clock nor ends the turn in the room — so
the werewolf in the Still Den gets no round from DIAGNOSE, SCORE, a refused
REST... A command that does use a turn (WAIT) still gives it one.
Run with: pytest roundabout/test_no_turn.py  (from c:\\zork_awt)
"""

import sys
import os
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from testkit import _make_world, _do

_CLAWS = "The werewolf's claws find you."


def _den():
    w, g = _make_world(hearts=5)
    w.set_global("LIGHT-SPELL-ACTIVE", True)
    w.move_object(w.player, w.rooms["STILL-DEN"])
    w.here = w.rooms["STILL-DEN"]
    w.set_global("WEREWOLF-RISEN", True)
    return w, g


@pytest.mark.parametrize("cmd", [
    "diagnose", "score", "verbose", "brief", "superbrief", "version",
    "rest", "cast", "count",
])
def test_no_turn_no_werewolf_round(cmd):
    w, g = _den()
    moves, hearts = w.moves, w.globals["hearts"]
    out = _do(g, cmd)
    assert _CLAWS not in out
    assert w.moves == moves and w.globals["hearts"] == hearts


def test_a_turn_still_gives_the_werewolf_its_round():
    from content.still_den import _MISSES
    w, g = _den()
    out = _do(g, "wait")
    assert _CLAWS in out or any(m in out for m in _MISSES)   # a round, hit or miss
    assert w.moves == 1


def test_rest_is_a_verb_refusals_take_no_turn_success_takes_one():
    from content.rest import _NOT_TIRED, _RESTED
    w, g = _make_world(hearts=5)
    moves = w.moves
    assert _NOT_TIRED in _do(g, "rest")
    assert w.moves == moves
    w.globals["spell_rest"] = True
    w.globals["hearts"] = 3
    assert _RESTED in _do(g, "rest")
    assert w.moves == moves + 1 and w.globals["hearts"] == 4
