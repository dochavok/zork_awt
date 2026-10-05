"""
Mage class XP bonus (experience.md — Class XP Adjustments): +1 XP the first
time a Mage enters each of the 43 dungeon rooms. The walkthroughs play a
Warrior, so these enter the rooms directly.
Run with: pytest roundabout/test_mage_bonus.py  (from c:\\zork_awt)
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
from content.experience import DUNGEON_ROOMS


def _make_world(cls="mage"):
    from engine.parser import Parser
    from content.vocabulary import make_vocabulary
    from content.syntax import make_syntax_rules
    w = World()
    p = Parser(make_vocabulary(), make_syntax_rules())
    g = Game(w, p, Clock())
    initialize_world(w, g)
    w.globals.update({
        "hearts": 5, "max_hearts": 5, "level": 1, "xp": 0, "zenni": 0,
        "player_class": cls, "player_name": "Tess", "ring_corruption": 0,
        "ring_worn": False, "quest_states": {},
    })
    # Room XP is paid on first entry too; zero it so only the bonus counts.
    for r in w.rooms.values():
        r.value = 0
    return w, g


def _enter(w, g, name):
    # Minimum dice: entry checks (e.g. the Inscription Chamber snare) fail
    # and pay nothing, so only the bonus moves XP.
    with patch("sys.stdout", io.StringIO()), \
            patch("random.randint", lambda a, b: a):
        g.enter_room(w.rooms[name])
    return w.globals["xp"]


def test_dungeon_rooms_exist_and_number_43():
    w, _ = _make_world()
    assert len(DUNGEON_ROOMS) == 43
    assert DUNGEON_ROOMS <= set(w.rooms)


def test_mage_earns_one_per_dungeon_room():
    for name in sorted(DUNGEON_ROOMS):
        w, g = _make_world()
        assert _enter(w, g, name) == 1, name


def test_mage_is_credited_once_per_room():
    w, g = _make_world()
    _enter(w, g, "INK-CORRIDOR")
    _enter(w, g, "SUPPLY-ROOM")
    # Some rooms reset room.visited; the bonus must not pay again.
    w.rooms["INK-CORRIDOR"].visited = False
    assert _enter(w, g, "INK-CORRIDOR") == 2


def test_no_bonus_outside_the_dungeon():
    w, g = _make_world()
    for name in ("TOWN-SQUARE", "DUNGEON-ENTRANCE", "CRYPT", "TOLL-BRIDGE",
                 "MINE-TUNNELS", "ASSAY-ROOM", "BONE-PASSAGE", "SEA-WEST"):
        assert _enter(w, g, name) == 0, name


def test_warrior_and_rogue_get_no_room_bonus():
    for cls in ("warrior", "rogue"):
        w, g = _make_world(cls)
        assert _enter(w, g, "INK-CORRIDOR") == 0, cls


def test_no_bonus_when_darkness_blocks_the_move():
    # The dark-room walk check refuses the move before the room is entered.
    w, g = _make_world()
    w.move_object(w.player, w.rooms["DUNGEON-ENTRANCE"])
    w.here = w.rooms["DUNGEON-ENTRANCE"]
    buf = io.StringIO()
    with patch("sys.stdout", buf):
        g.do_turn("south")
    assert "too dark to go any further" in buf.getvalue()
    assert w.here.name == "DUNGEON-ENTRANCE"
    assert w.globals["xp"] == 0
    assert "MAGE-ROOMS-CREDITED" not in w.globals


def test_bonus_survives_save_and_restore():
    from engine.savegame import snapshot
    w, g = _make_world()
    _enter(w, g, "INK-CORRIDOR")
    assert "INK-CORRIDOR" in snapshot(g)["globals"]["MAGE-ROOMS-CREDITED"]
