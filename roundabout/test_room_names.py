"""
Rooms renamed in play keep their names through SAVE / RESTORE (mechanics.md —
Save and Restore). A renamed room's name follows a game flag, so a restore
gets it right from any save, old ones included:
- Stored Room → Hole to Below once dug (locations.md — dungeon mid tier)
- A House → Kevry's House once Kevry is met (locations.md — Kevry's Island)

Run with: pytest roundabout/test_room_names.py  (from c:\\zork_awt)
"""

import ast
import glob
import io
import os
import sys
from unittest.mock import patch
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do
from engine import savegame

_HERE = os.path.dirname(os.path.abspath(__file__))


def _at(w, room):
    w.move_object(w.player, w.rooms[room])
    w.here = w.rooms[room]


def _title(g):
    """The room title LOOK prints (its first line)."""
    return _do(g, "look").strip().splitlines()[0]


def _stored_room():
    from content import light
    w, g = _make_world(cls="warrior")
    w.move_object(w.objects["TORCH"], w.player)
    with patch("sys.stdout", io.StringIO()):
        light.light_torch(w)
    w.move_object(w.objects["SHOVEL"], w.player)
    _at(w, "STORED-ROOM")
    return w, g


def _dug():
    w, g = _stored_room()
    assert _title(g) == "Stored Room"
    with patch("content.mid_tier.random.randint", return_value=20):   # no Will note
        _do(g, "dig")
    assert w.get_global("STORED-ROOM-DUG")
    return w, g


def _met_kevry():
    w, g = _make_world(cls="warrior")
    _at(w, "KEVRYS-HOUSE")
    assert _title(g) == "A House"
    _at(w, "CAPTAINS-QUARTERS")
    _do(g, "talk to kevry")
    assert w.get_global("KEVRY-MET")
    return w, g


def _restored(g, tmp_path):
    path = str(tmp_path / "game.sav")
    savegame.save(g, path)
    w2, g2 = _make_world(cls="warrior")
    assert savegame.restore(g2, path)
    return w2, g2


# --- In play -------------------------------------------------------------------

def test_digging_renames_the_stored_room():
    w, g = _dug()
    assert _title(g) == "Hole to Below"


def test_meeting_kevry_names_his_house():
    w, g = _met_kevry()
    _at(w, "KEVRYS-HOUSE")
    assert _title(g) == "Kevry's House"


# --- Through a restore ---------------------------------------------------------

def test_hole_to_below_survives_restore(tmp_path):
    w, g = _dug()
    w2, g2 = _restored(g, tmp_path)
    assert w2.here.name == "STORED-ROOM"
    assert _title(g2) == "Hole to Below"


def test_kevrys_house_survives_restore(tmp_path):
    w, g = _met_kevry()
    w2, g2 = _restored(g, tmp_path)
    _at(w2, "KEVRYS-HOUSE")
    assert _title(g2) == "Kevry's House"


def test_a_save_holding_only_the_flags_restores_the_names(tmp_path):
    # Saves from before this fix carry the flags and no room names
    w, g = _make_world(cls="warrior")
    w.set_global("STORED-ROOM-DUG", True)
    w.set_global("KEVRY-MET", True)
    w2, g2 = _restored(g, tmp_path)
    assert w2.rooms["STORED-ROOM"].desc == "Hole to Below"
    assert w2.rooms["KEVRYS-HOUSE"].desc == "Kevry's House"


def test_restoring_an_earlier_save_brings_the_old_name_back(tmp_path):
    w, g = _stored_room()
    path = str(tmp_path / "before.sav")
    savegame.save(g, path)                         # before digging
    with patch("content.mid_tier.random.randint", return_value=20):
        _do(g, "dig")
    assert _title(g) == "Hole to Below"
    assert savegame.restore(g, path)               # same game, earlier save
    assert _title(g) == "Stored Room"


def test_unchanged_rooms_keep_their_names_through_restore(tmp_path):
    w, g = _dug()
    w2, g2 = _restored(g, tmp_path)
    renamed = {"STORED-ROOM", "KEVRYS-HOUSE"}
    fresh, _ = _make_world(cls="warrior")
    for name, room in w2.rooms.items():
        if name not in renamed:
            assert room.desc == fresh.rooms[name].desc, name


# --- Guard: every rename goes through the rules --------------------------------

def test_content_never_renames_a_room_directly():
    """A room's name may only change through Game.register_room_name, so a
    restore can rebuild it. Direct `<room>.desc = ...` in content is refused."""
    found = []
    for path in glob.glob(os.path.join(_HERE, "content", "*.py")):
        tree = ast.parse(open(path, encoding="utf-8").read())
        for node in ast.walk(tree):
            if not isinstance(node, ast.Assign):
                continue
            for t in node.targets:
                if isinstance(t, ast.Attribute) and t.attr == "desc":
                    owner = ast.unparse(t.value).lower()
                    if "room" in owner or "here" in owner:
                        found.append(f"{os.path.basename(path)}:{node.lineno} {ast.unparse(node)}")
    assert found == [], "rooms renamed directly:\n  " + "\n  ".join(found)
