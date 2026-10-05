"""
Smoke tests: the engine's core object/room operations and the world's
starting state. Content (rooms, NPCs, items) is covered by the walkthroughs
and the feature tests.
Run with: pytest roundabout/test_world.py  (from c:\\zork_awt)
or: py test_world.py  (from c:\\zork_awt\\roundabout)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from engine.world import World, Room, GameObject, TAKEBIT
from engine.clock import Clock
from engine.game import Game
from content.init import initialize_world


def _make_world():
    w = World()
    c = Clock()
    g = Game(w, w, c)
    initialize_world(w, g)
    return w, g


# ---------------------------------------------------------------------------
# Basic engine
# ---------------------------------------------------------------------------

def test_basic_room_and_object():
    w = World()
    room = Room(name="test-room", desc="A room.", flags=frozenset())
    w.register_room(room)
    obj = GameObject(name="widget", desc="A widget.", flags=frozenset({TAKEBIT}))
    w.register_object(obj)
    w.move_object(obj, room)
    assert obj in room.contents
    assert obj.location is room


def test_move_object_updates_location():
    w = World()
    r1 = Room(name="r1", desc="R1.", flags=frozenset())
    r2 = Room(name="r2", desc="R2.", flags=frozenset())
    w.register_room(r1)
    w.register_room(r2)
    obj = GameObject(name="coin", desc="Coin.", flags=frozenset({TAKEBIT}))
    w.register_object(obj)
    w.move_object(obj, r1)
    assert obj in r1.contents
    w.move_object(obj, r2)
    assert obj not in r1.contents
    assert obj in r2.contents


def test_move_object_to_none_removes():
    w = World()
    r = Room(name="rm", desc="Room.", flags=frozenset())
    w.register_room(r)
    obj = GameObject(name="x", desc="X", flags=frozenset({TAKEBIT}))
    w.register_object(obj)
    w.move_object(obj, r)
    w.move_object(obj, None)
    assert obj not in r.contents
    assert obj.location is None


def test_set_flag_and_has_flag():
    obj = GameObject(name="test", desc="Test", flags=set())
    obj.set_flag("CUSTOM")
    assert obj.has_flag("CUSTOM")


def test_clear_flag():
    obj = GameObject(name="test2", desc="Test", flags=set({"MYBIT"}))
    assert obj.has_flag("MYBIT")
    obj.clear_flag("MYBIT")
    assert not obj.has_flag("MYBIT")


# ---------------------------------------------------------------------------
# Starting state
# ---------------------------------------------------------------------------

def test_player_in_starting_room():
    w, g = _make_world()
    assert w.here is w.rooms["WHITE-HOUSE"]
    assert w.player in w.here.contents
    assert w.player.location is w.here


def test_globals_initialized():
    w, g = _make_world()
    assert "hearts" in w.globals
    assert w.globals["hearts"] == 5
    assert "zenni" in w.globals
    assert "ring_corruption" in w.globals
    assert w.globals["ring_corruption"] == 0


if __name__ == "__main__":
    import traceback
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    passed = failed = 0
    for fn in tests:
        try:
            fn()
            print(f"PASS  {fn.__name__}")
            passed += 1
        except Exception as e:
            print(f"FAIL  {fn.__name__}: {e}")
            traceback.print_exc()
            failed += 1
    print(f"\n{passed} passed, {failed} failed")
