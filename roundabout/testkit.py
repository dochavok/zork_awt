"""
Shared test helpers: a fresh world, one turn's output, moving the player,
carrying things. Not a test file, so pytest doesn't collect it.
"""

import sys
import os
import io
import contextlib
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


def _quiet(fn, *a, **kw):
    with patch("sys.stdout", io.StringIO()):
        return fn(*a, **kw)


def _goto(w, room):
    """Put the player in a room without a turn or its arrival text."""
    w.move_object(w.player, w.rooms[room])
    w.here = w.rooms[room]


def _carry(w, name):
    obj = w.objects[name]
    obj.flags.discard("INVISIBLE")   # hidden until found in play
    w.move_object(obj, w.player)
    return obj


def _at(room, *flags):
    """A Mage in a room, lit by the light spell, with the given flags set."""
    w, g = _make_world()
    w.set_global("LIGHT-SPELL-ACTIVE", True)
    for flag in flags:
        w.set_global(flag, True)
    _goto(w, room)
    return w, g


def _look(room, **globals_):
    w, g = _make_world()
    for k, v in globals_.items():
        w.set_global(k.replace("_", "-"), v)
    _goto(w, room)
    if not w.is_lit():                  # dark rooms: carry a lit torch
        torch = w.objects["TORCH"]
        w.move_object(torch, w.player)
        torch.clear_flag("INVISIBLE")
        from content import light
        with contextlib.redirect_stdout(io.StringIO()):
            light.light_torch(w)
    return w, g, _do(g, "look")
