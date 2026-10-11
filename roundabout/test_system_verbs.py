"""
System and flavor commands (mechanics.md — Parser Verbs): VERBOSE, BRIEF,
SUPERBRIEF, WAIT, PRAY, RESTART, EXIT / LEAVE — and a guard that every
command the parser accepts answers with something.
Run with: pytest roundabout/test_system_verbs.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import pytest

from test_knight import _make_world, _do
from test_quit_and_exit import _run, QUIT_PROMPT
from engine.game import VERBOSE, BRIEF, SUPER_BRIEF

RESTART_PROMPT = "Start over from the beginning? Anything you haven't saved will be lost. [yes/no] "


def _goto(w, name):
    w.move_object(w.player, w.rooms[name])
    w.here = w.rooms[name]


# --- Description modes ---------------------------------------------------------

@pytest.mark.parametrize("command,line,mode", [
    ("verbose", "Maximum verbosity.", VERBOSE),
    ("brief", "Brief descriptions.", BRIEF),
    ("superbrief", "Superbrief descriptions.", SUPER_BRIEF),
    ("super", "Superbrief descriptions.", SUPER_BRIEF),
])
def test_description_modes(command, line, mode):
    w, g = _make_world()
    g.desc_mode = VERBOSE if mode != VERBOSE else BRIEF
    moves = w.moves
    assert line in _do(g, command)
    assert g.desc_mode == mode
    assert w.moves == moves                         # no turn


def _describe(g):
    import io
    from unittest.mock import patch
    buf = io.StringIO()
    with patch("sys.stdout", buf):
        g.describe_room()
    return buf.getvalue()


def test_verbose_shows_the_full_room_on_return():
    w, g = _make_world()
    _goto(w, "CHURCH-NAVE")                         # a plain ldesc room
    room = w.rooms["CHURCH-NAVE"]
    room.visited = True
    assert "brass dial" not in _describe(g)         # BRIEF: name only on return
    _do(g, "verbose")
    assert "brass dial" in _describe(g)


def test_superbrief_shows_only_the_room_name_even_first_time():
    w, g = _make_world()
    _goto(w, "CHURCH-NAVE")
    w.rooms["CHURCH-NAVE"].visited = False
    _do(g, "superbrief")
    out = _describe(g)
    assert "Church of All" in out
    assert "brass dial" not in out


# --- WAIT, PRAY ----------------------------------------------------------------

@pytest.mark.parametrize("command", ["wait", "z"])
def test_wait_passes_a_turn(command):
    w, g = _make_world()
    moves = w.moves
    assert "Time passes..." in _do(g, command)
    assert w.moves == moves + 1


def test_pray_anywhere():
    w, g = _make_world()
    _goto(w, "TOWN-SQUARE")
    assert "If you pray enough, your prayers may be answered." in _do(g, "pray")


def test_pray_in_the_church_of_all():
    w, g = _make_world()
    _goto(w, "CHURCH-NAVE")
    out = _do(g, "pray")
    assert "The church receives it the way it receives everything" in out
    assert "If you pray enough" not in out


# --- EXIT / LEAVE --------------------------------------------------------------

@pytest.mark.parametrize("command", ["exit", "leave"])
def test_exit_and_leave_alone_are_quit(command):
    w, g = _make_world()
    moves = w.moves
    script, _ = _run(g, [command, "yes", "inventory"])
    assert QUIT_PROMPT in script.prompts
    assert script.lines == ["inventory"]
    assert w.moves == moves                         # no turn, like QUIT


def test_exit_no_plays_on():
    w, g = _make_world()
    script, out = _run(g, ["exit", "no", "inventory"])
    assert script.lines == []
    assert "empty-handed" in out.split(QUIT_PROMPT, 1)[1]


def test_leave_a_thing_drops_it():
    w, g = _make_world()
    shovel = w.objects["SHOVEL"]
    shovel.flags.discard("INVISIBLE")
    w.move_object(shovel, w.player)
    assert "You drop the shovel." in _do(g, "leave shovel")
    assert shovel.location is w.here


def test_exit_a_thing_goes_nowhere():
    w, g = _make_world()
    shovel = w.objects["SHOVEL"]
    w.move_object(shovel, w.player)
    assert "You can't go that way." in _do(g, "exit shovel")


# --- RESTART -------------------------------------------------------------------

def test_restart_yes_starts_a_new_game_at_west_of_house():
    import main
    script, out = _run(None, ["open mailbox", "yes", "", "warrior", "Tess", "",
                              "restart", "yes", "quit", "yes"], entry=main.main)
    assert RESTART_PROMPT in script.prompts
    assert script.lines == []
    after = out.split(RESTART_PROMPT, 1)[1]
    assert "West of House" in after                 # back at the very start


def test_restart_no_plays_on():
    w, g = _make_world()
    script, out = _run(g, ["restart", "no", "inventory"])
    assert script.lines == []
    assert not g.restart_requested
    assert "empty-handed" in out.split(RESTART_PROMPT, 1)[1]


def test_restart_uses_no_turn():
    w, g = _make_world()
    moves = w.moves
    _run(g, ["restart", "no"])
    assert w.moves == moves


def test_restart_with_input_closed_plays_on():
    w, g = _make_world()
    script, out = _run(g, ["restart"])
    assert not g.restart_requested
    assert "Traceback" not in out


# --- Every command answers -----------------------------------------------------
# A command the parser accepts but nothing handles used to print nothing at all
# (VERBOSE, WAIT...). Each one left here still does — remove it once it's built.

NOT_YET_BUILT = set()


def _bare_commands():
    from content.syntax import make_syntax_rules
    seen = []
    for r in make_syntax_rules():
        if r.obj1 is None and not r.prep and r.verb not in seen:
            seen.append(r.verb)
    return seen


@pytest.mark.parametrize("verb", _bare_commands())
def test_every_bare_command_answers(verb):
    if verb in ("quit", "q", "restart", "exit", "leave"):
        return                                      # prompts: covered above
    w, g = _make_world()
    _goto(w, "TOWN-SQUARE")
    silent = not _do(g, verb).strip()
    if verb in NOT_YET_BUILT:
        assert silent, f"{verb} answers now — take it off NOT_YET_BUILT"
    else:
        assert not silent, f"{verb} printed nothing"


# --- Removed words -------------------------------------------------------------

@pytest.mark.parametrize("word", [
    "answer", "reply", "hello", "hi", "say", "script", "unscript",
    "wake", "awake", "surprise", "startle",
])
def test_removed_words_are_unknown(word):
    w, g = _make_world()
    assert f'I don\'t know the word "{word}".' in _do(g, word)


# --- No-turn answers -----------------------------------------------------------

@pytest.mark.parametrize("command,line", [
    ("buy", "Buy what?"),
    ("find", "Find what?"),
    ("find shovel", "You'll have to look for it yourself."),
    ("back", "Sorry, my memory is poor. Please give a direction."),
    ("stand", "You are already standing, I think."),
])
def test_no_turn_answers(command, line):
    w, g = _make_world()
    w.move_object(w.objects["SHOVEL"], w.player)
    moves = w.moves
    assert line in _do(g, command)
    assert w.moves == moves


def test_diagnose_full_health():
    w, g = _make_world(hearts=5)
    moves = w.moves
    assert "You are in perfect health — 5 of 5 hearts." in _do(g, "diagnose")
    assert w.moves == moves


def test_diagnose_hurt():
    w, g = _make_world(hearts=5)
    w.globals["hearts"] = 3
    assert "You have 3 of 5 hearts." in _do(g, "diagnose")


# --- Flavor (one turn each) ----------------------------------------------------

@pytest.mark.parametrize("command,line", [
    ("blast", "You can't blast anything by using words."),
    ("exorcise", "What a bizarre concept!"),
    ("jump", "Wheeeeeeeeee!!!!!"),
    ("kiss", "I'd sooner kiss a pig."),
    ("play", "That's silly!"),
    ("wish", "With luck, your wish will come true."),
    ("yell", "Aaaarrrrgggghhhh!"),
    ("smell", "You smell nothing unusual."),
    ("smell shovel", "It smells like a shovel."),
    ("wave", "You wave. Nobody waves back."),
    ("wave shovel", "Waving the shovel has no effect."),
])
def test_flavor_lines(command, line):
    w, g = _make_world()
    _goto(w, "TOWN-SQUARE")
    w.move_object(w.objects["SHOVEL"], w.player)
    moves = w.moves
    assert line in _do(g, command)
    assert w.moves == moves + 1


@pytest.mark.parametrize("room", ["ROUNDABOUT-POND", "SEA-MID", "OPEN-OCEAN-40", "BOG-NE", "DOCKS"])
def test_swim_where_there_is_water(room):
    w, g = _make_world()
    _goto(w, room)
    assert "You don't want to swim in that!" in _do(g, "swim")


def test_swim_on_dry_land():
    w, g = _make_world()
    _goto(w, "TOWN-SQUARE")
    assert "There's nothing here to swim in." in _do(g, "swim")


def test_disembark_is_dock():
    w, g = _make_world()
    _goto(w, "TOWN-SQUARE")
    assert "You're not on a ship." in _do(g, "disembark")


# --- VERSION -------------------------------------------------------------------

def test_version_names_the_stamped_build(monkeypatch):
    import types
    stamp = types.ModuleType("content._version")
    stamp.VERSION = "v9.9-roundabout"
    monkeypatch.setitem(sys.modules, "content._version", stamp)
    w, g = _make_world()
    moves = w.moves
    assert "Roundabout: The God-Forsaken Ring — v9.9-roundabout" in _do(g, "version")
    assert w.moves == moves                         # no turn


def test_version_from_source_asks_git(monkeypatch):
    from content import version
    monkeypatch.setitem(sys.modules, "content._version", None)    # no stamp
    monkeypatch.setattr(version, "git_version", lambda: "v2.2-roundabout-3-gabc1234")
    w, g = _make_world()
    assert "— v2.2-roundabout-3-gabc1234" in _do(g, "version")


def test_version_without_git_or_stamp(monkeypatch):
    from content import version
    monkeypatch.setitem(sys.modules, "content._version", None)
    monkeypatch.setattr(version, "git_version", lambda: None)
    w, g = _make_world()
    assert "Roundabout: The God-Forsaken Ring — unknown version" in _do(g, "version")


def test_git_version_reads_the_real_tag():
    from content import version
    assert version.git_version().startswith("v")    # this checkout is tagged


def test_version_works_at_west_of_house():
    import main
    script, out = _run(None, ["version", "quit", "yes"], entry=main.main)
    assert "Roundabout: The God-Forsaken Ring — " in out
    assert "Great Underground Empire" not in out
