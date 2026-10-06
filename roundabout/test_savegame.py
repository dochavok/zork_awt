"""
SAVE / RESTORE (engine/savegame.py; content/verbs.py V-SAVE / V-RESTORE).

The design says only that SAVE / RESTORE work (mechanics.md — Cargo: they still
work mid-round). The contract tested here: RESTORE puts the game back exactly
as it was at SAVE — in the same session, and in a fresh game (main.py builds a
new Game every launch, so a real restore always lands in a fresh one). Timers
keep running afterwards: ring corruption above all (sacred — mechanics.md).

Every test runs in a temporary directory, so no save file lands in the repo.
Run with: pytest roundabout/test_savegame.py  (from c:\\zork_awt)
"""

import sys
import os
import io
from unittest.mock import patch
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do
from content import light, quests


@pytest.fixture(autouse=True)
def _in_tmp(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)


def _goto(g, w, room):
    with patch("sys.stdout", io.StringIO()):
        g.enter_room(w.rooms[room])


def _mid_game():
    """A game with a little of everything changed."""
    w, g = _make_world(cls="rogue", level=3, hearts=4, zenni=17)
    w.globals["max_hearts"] = 6
    _goto(g, w, "TALE-AND-ALE")
    _goto(g, w, "KITCHEN")
    for name in ("ROPE", "SHOVEL"):
        w.move_object(w.objects[name], w.player)
    quests.discover(w, "22")
    with patch("sys.stdout", io.StringIO()):
        quests.complete(w, "41")
    w.set_global("MUGGER-DEAD", True)
    return w, g


def _state(w):
    return {
        "here": w.here.name,
        "carried": [o.name for o in w.player.contents],
        "hearts": w.globals["hearts"], "max": w.globals["max_hearts"],
        "zenni": w.globals["zenni"], "xp": w.globals["xp"], "level": w.globals["level"],
        "class": w.globals["player_class"], "name": w.globals["player_name"],
        "quests": dict(w.globals["quest_states"]),
        "mugger": w.get_global("MUGGER-DEAD"),
        "kitchen_visited": w.rooms["KITCHEN"].visited,
        "moves": w.moves,
    }


# --- Round trips -------------------------------------------------------------------

def test_save_line_and_restore_line():
    w, g = _mid_game()
    assert "Saved." in _do(g, "save")
    out = _do(g, "restore")
    assert "Restored." in out
    assert "Kitchen" in out                      # the room is described


def test_restore_undoes_everything_since_the_save():
    w, g = _mid_game()
    saved = _state(w)
    _do(g, "save")
    _do(g, "drop rope")
    _goto(g, w, "BAR")
    w.globals["zenni"] = 0
    w.globals["hearts"] = 1
    quests.discover(w, "40")
    _do(g, "restore")
    assert _state(w) == saved
    assert w.objects["ROPE"].location is w.player


def test_restore_into_a_fresh_game():
    w, g = _mid_game()
    saved = _state(w)
    _do(g, "save")
    w2, g2 = _make_world(cls="warrior", level=1)
    _do(g2, "restore")
    assert _state(w2) == saved


def test_object_text_and_flags_come_back():
    w, g = _mid_game()
    w.move_object(w.objects["TORCH"], w.player)
    light.light_torch(w)                         # ONBIT and "A lit torch."
    _do(g, "save")
    w2, g2 = _make_world()
    _do(g2, "restore")
    torch = w2.objects["TORCH"]
    assert torch.has_flag("ONBIT")
    assert torch.ldesc == "A lit torch."
    assert torch.location is w2.player


def test_room_xp_not_paid_twice_after_restore():
    w, g = _mid_game()
    _goto(g, w, "BAR")                           # paid on first entry
    _goto(g, w, "KITCHEN")
    _do(g, "save")
    w2, g2 = _make_world()
    _do(g2, "restore")
    xp = w2.globals["xp"]
    _goto(g2, w2, "BAR")
    assert w2.globals["xp"] == xp


def test_room_xp_not_paid_twice_for_a_room_that_forgets_its_visit():
    # The Dream Corridor clears its own visited flag on every entry until passed,
    # so only the room's saved XP value (paid = 0) stops a second payment.
    w, g = _mid_game()
    w.move_object(w.objects["TORCH"], w.player)
    light.light_torch(w)
    _goto(g, w, "DREAM-CORRIDOR")
    _do(g, "save")
    w2, g2 = _make_world()
    _do(g2, "restore")
    _goto(g2, w2, "SPILLWAY")                    # (its own first-visit XP)
    xp = w2.globals["xp"]
    _goto(g2, w2, "DREAM-CORRIDOR")
    assert w2.globals["xp"] == xp


def test_carried_order_preserved():
    w, g = _mid_game()
    before = [o.name for o in w.player.contents]
    _do(g, "save")
    w2, g2 = _make_world()
    _do(g2, "restore")
    assert [o.name for o in w2.player.contents] == before


# --- Nothing to restore --------------------------------------------------------------

def test_no_save_file():
    w, g = _mid_game()
    before = _state(w)
    assert "There's no saved game to restore." in _do(g, "restore")
    assert _state(w) == before


def test_damaged_save_file():
    w, g = _mid_game()
    before = _state(w)
    with open("Tess.sav", "wb") as fh:             # the character's own file
        fh.write(b"not a save file")
    assert "There's no saved game to restore." in _do(g, "restore")
    assert _state(w) == before


def test_no_restore_after_game_over():
    # GAME OVER refuses all further input (mechanics.md — death: no resurrection)
    w, g = _mid_game()
    _do(g, "save")
    w.set_global("GAME-OVER", True)
    assert "The game is over." in _do(g, "restore")


# --- Timers keep running after a restore ----------------------------------------------

def _ring_on(w, g, tick):
    w.move_object(w.objects["RING"], w.player)
    _do(g, "wear ring")
    w.globals["ring_corruption"] = tick


def test_corruption_keeps_ticking_after_restore_same_session():
    w, g = _mid_game()
    _ring_on(w, g, 20)
    _do(g, "save")
    _do(g, "restore")
    _do(g, "wait")
    assert w.globals["ring_corruption"] == 21


def test_corruption_keeps_ticking_after_restore_in_a_fresh_game():
    w, g = _mid_game()
    _ring_on(w, g, 20)
    _do(g, "save")
    w2, g2 = _make_world()
    _do(g2, "restore")
    assert w2.globals["ring_corruption"] == 20
    _do(g2, "wait")
    assert w2.globals["ring_corruption"] == 21


def test_torch_keeps_burning_after_restore_in_a_fresh_game():
    w, g = _mid_game()
    w.move_object(w.objects["TORCH"], w.player)
    light.light_torch(w)
    _goto(g, w, "MAUSOLEUM")                     # the timer starts
    _do(g, "wait")
    left = w.get_global("TORCH-LIT-TIMER")
    _do(g, "save")
    w2, g2 = _make_world()
    _do(g2, "restore")
    _do(g2, "wait")
    assert w2.get_global("TORCH-LIT-TIMER") == left - 1


def test_lit_fuse_still_goes_off_after_restore_in_a_fresh_game():
    w, g = _mid_game()
    _goto(g, w, "MINE-TUNNELS")
    w.set_global("WEAK-POINT-FOUND", True)
    w.set_global("GUNPOWDER-PLACED", True)
    w.move_object(w.objects["GUNPOWDER"], w.here)
    w.move_object(w.objects["FLINT-AND-STEEL"], w.player)
    _do(g, "light gunpowder")
    assert w.get_global("FUSE-LIT")
    _goto(g, w, "TOWN-SQUARE")                   # well clear of the mine
    _do(g, "save")
    w2, g2 = _make_world()
    _do(g2, "restore")
    for _ in range(6):
        _do(g2, "wait")
    assert w2.get_global("MINE-BLOWN")


def test_map_check_keeps_running_after_restore_in_a_fresh_game():
    w, g = _mid_game()
    _goto(g, w, "SHIP-DECK")                     # aboard: the map's check starts
    _do(g, "save")
    w2, g2 = _make_world()
    _do(g2, "restore")
    with patch("content.player.roll", return_value=14):     # Hard
        _do(g2, "wait")
    assert w2.get_global("MAP-FOUND")


def test_fuse_lit_after_the_save_is_out_after_restore():
    # Same session: RESTORE goes back to before the fuse was lit
    w, g = _mid_game()
    _goto(g, w, "MINE-TUNNELS")
    w.set_global("WEAK-POINT-FOUND", True)
    w.set_global("GUNPOWDER-PLACED", True)
    w.move_object(w.objects["GUNPOWDER"], w.here)
    w.move_object(w.objects["FLINT-AND-STEEL"], w.player)
    _goto(g, w, "TOWN-SQUARE")
    _do(g, "save")                               # nothing lit yet
    _goto(g, w, "MINE-TUNNELS")
    _do(g, "light gunpowder")
    assert w.get_global("FUSE-LIT")
    _do(g, "restore")
    for _ in range(8):
        _do(g, "wait")
    assert not w.get_global("FUSE-LIT")
    assert not w.get_global("MINE-BLOWN")


def test_every_mid_game_clock_event_can_be_rebuilt():
    # Replay the full-score walkthrough; any clock event created after setup
    # needs a factory (content/init.py), or a fresh-game RESTORE drops it.
    import test_walkthrough_fullscore_v2 as fullscore
    with patch("random.randint", fullscore._always_max),             patch("content.char_create.input", fullscore._make_input_feed()),             patch("sys.stdout", io.StringIO()):
        g, w = fullscore._make_game()
        at_setup = set(g.clock._events)
        for section in fullscore.parse_walkthrough(fullscore._WALKTHROUGH_PATH):
            for cmd, _frag in section.steps:
                g.do_turn(cmd)
    created = set(g.clock._events) - at_setup
    assert created, "the walkthrough should create some mid-game events"
    assert created <= set(g.clock_factories), sorted(created - set(g.clock_factories))


# --- The file is named after the character (mechanics.md — Save and Restore) -----------

def test_save_file_is_named_after_the_character():
    w, g = _mid_game()                           # player_name "Tess"
    _do(g, "save")
    assert os.listdir(".") == ["Tess.sav"]


def test_restore_finds_your_own_file_only():
    w, g = _mid_game()
    w.globals["player_name"] = "Arwen"
    _do(g, "save")                               # Arwen.sav
    w2, g2 = _make_world()                       # Tess
    assert "There's no saved game to restore." in _do(g2, "restore")


def test_restore_by_name_loads_another_characters_save():
    w, g = _mid_game()
    w.globals["player_name"] = "Arwen"
    saved = _state(w)
    _do(g, "save")
    w2, g2 = _make_world()                       # a new character, Tess
    out = _do(g2, "restore arwen")               # any case
    assert "Restored." in out
    assert _state(w2) == saved
    assert w2.globals["player_name"] == "Arwen"  # later SAVEs go to Arwen.sav
    _do(g2, "save")
    assert sorted(os.listdir(".")) == ["Arwen.sav"]


def test_restore_by_name_uses_no_turn():
    # The worn ring ticks every turn: a turn spent restoring would show
    w, g = _mid_game()
    _ring_on(w, g, 20)
    _do(g, "save")
    _do(g, "wait")
    _do(g, "RESTORE TESS")
    assert w.globals["ring_corruption"] == 20


def test_restore_unknown_name():
    w, g = _mid_game()
    before = _state(w)
    moves = w.moves
    assert "There's no saved game for Boromir." in _do(g, "restore BOROMIR")
    assert _state(w) == before
    assert w.moves == moves


@pytest.mark.parametrize("name,path", [
    ("Tess", "Tess.sav"),
    ("Mary Jane", "Mary Jane.sav"),
    ("O'Brien", "O'Brien.sav"),
    ("../evil", "evil.sav"),                     # no path parts
    ("Ar:we*n?", "Arwen.sav"),                   # nothing Windows refuses
    ("***", "roundabout.sav"),                   # nothing left: the fallback
    (None, "roundabout.sav"),
])
def test_save_file_names(name, path):
    from engine import savegame
    assert savegame.path_for(name) == path


# --- The turn count (cooldowns and turn-based notices store turn numbers) -------------

def test_rest_cooldown_holds_across_a_fresh_restore():
    from test_rest import RESTED, TOO_SOON
    w, g = _mid_game()
    w.globals.update({"spell_rest": True, "hearts": 2})
    for _ in range(30):
        _do(g, "wait")
    _do(g, "rest")                               # ready again 50 turns from here
    rested_at = w.moves - 1
    _do(g, "save")
    w2, g2 = _make_world()
    _do(g2, "restore")
    assert w2.moves == w.moves
    assert TOO_SOON in _do(g2, "rest")
    while w2.moves < rested_at + 50:
        _do(g2, "wait")
    assert RESTED in _do(g2, "rest")


def test_bounty_still_goes_up_at_turn_100_after_a_fresh_restore():
    from test_systems import BOUNTY
    w, g = _mid_game()
    w.set_global("MUGGER-DEAD", False)           # the bounty is only for a live mugger
    _goto(g, w, "BAR")
    while w.moves < 90:
        _do(g, "wait")
    _do(g, "save")
    w2, g2 = _make_world()
    _do(g2, "restore")
    while w2.moves < 99:
        _do(g2, "wait")
    assert BOUNTY not in _do(g2, "read board")
    _do(g2, "wait")
    assert BOUNTY in _do(g2, "read board")


def test_save_without_a_turn_count_loads_at_zero():
    import pickle
    w, g = _mid_game()
    for _ in range(5):
        _do(g, "wait")
    _do(g, "save")
    with open("Tess.sav", "rb") as fh:
        data = pickle.load(fh)
    del data["moves"]                            # as saved before the count was kept
    with open("Tess.sav", "wb") as fh:
        pickle.dump(data, fh)
    w2, g2 = _make_world()
    assert "Restored." in _do(g2, "restore")
    assert w2.moves == 0
