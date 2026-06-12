"""
Smoke tests: world init, room/object instantiation, flag checks.
Run with: pytest roundabout/test_world.py  (from c:\\zork_awt)
or: python test_world.py  (from c:\\zork_awt\\roundabout)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from engine.world import World, Room, GameObject, Exit, TAKEBIT, ACTORBIT, ONBIT
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
    room = Room(name="test-room", desc="A room.", flags=frozenset({ONBIT}))
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


# ---------------------------------------------------------------------------
# Full world init
# ---------------------------------------------------------------------------

def test_world_init_room_count():
    w, g = _make_world()
    assert len(w.rooms) >= 150, f"Expected >= 150 rooms, got {len(w.rooms)}"


def test_world_init_object_count():
    w, g = _make_world()
    # Objects excluding player
    objs = [o for o in w.objects.values() if o.name != "player"]
    assert len(objs) >= 80, f"Expected >= 80 objects, got {len(objs)}"


def test_player_created():
    w, g = _make_world()
    assert w.player is not None
    assert w.player.name == "player"


def test_player_in_starting_room():
    w, g = _make_world()
    assert w.here is not None
    assert w.player in w.here.contents


def test_globals_initialized():
    w, g = _make_world()
    assert "hearts" in w.globals
    assert w.globals["hearts"] == 5
    assert "zenni" in w.globals
    assert "ring_corruption" in w.globals
    assert w.globals["ring_corruption"] == 0


# ---------------------------------------------------------------------------
# Key rooms exist
# ---------------------------------------------------------------------------

def test_key_rooms_present():
    w, g = _make_world()
    expected = [
        "tale-and-ale-main",
        "wills-tower-main",
        "portcullis-corridor",
        "idol-room",
        "flooding-room",
        "ink-corridor",
        "bone-passage",
        "skeleton-room",
        "ghosts-room",
        "church-nave",     # Church of All — nave room
        "the-altar",       # Church of All — altar sub-room
        "combat-room",
    ]
    for name in expected:
        assert name in w.rooms, f"Room missing: {name}"


# ---------------------------------------------------------------------------
# Key objects exist and have correct flags
# ---------------------------------------------------------------------------

def test_ring_object_exists():
    w, g = _make_world()
    ring = w.objects.get("ring")
    assert ring is not None
    assert ring.has_flag("WEARBIT") or "WEARBIT" in str(ring.flags)


def test_pale_blade_object_exists():
    w, g = _make_world()
    blade = w.objects.get("pale-blade")
    assert blade is not None
    assert blade.has_flag("TAKEBIT") or "TAKEBIT" in str(blade.flags)


def test_npc_objects_present():
    w, g = _make_world()
    # Core NPCs: will, may, shamus, litlock, archivist, beekeeper, knight, warden
    expected_npcs = ["may", "will", "shamus", "litlock", "archivist", "beekeeper",
                     "knight", "warden", "ivanaar"]
    for name in expected_npcs:
        assert name in w.objects, f"NPC missing: {name}"
        npc = w.objects[name]
        assert npc.has_flag("ACTORBIT"), f"NPC {name} missing ACTORBIT"


def test_objects_have_locations():
    w, g = _make_world()
    unplaced = [
        o.name for o in w.objects.values()
        if o.location is None and o.name != "player"
        and not o.name.startswith("_")
    ]
    # Many items are unplaced at start (reward items, quest-spawned, locked room items).
    # Threshold is 55 to account for them all; if this grows much larger investigate.
    assert len(unplaced) <= 55, f"Too many unplaced objects ({len(unplaced)}): {unplaced[:10]}"


# ---------------------------------------------------------------------------
# GameObject flag helpers
# ---------------------------------------------------------------------------

def test_set_flag_and_has_flag():
    obj = GameObject(name="test", desc="Test", flags=set())
    obj.set_flag("CUSTOM")
    assert obj.has_flag("CUSTOM")


def test_clear_flag():
    obj = GameObject(name="test2", desc="Test", flags=set({"MYBIT"}))
    assert obj.has_flag("MYBIT")
    obj.clear_flag("MYBIT")
    assert not obj.has_flag("MYBIT")


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
