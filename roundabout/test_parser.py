"""
Parser (mechanics.md — Parser Verbs, Synonym Policy, Inventory Display).

Commands are played in the Town Square: at the White House every command but
OPEN MAILBOX gets the opening's joke, so tests there can't tell anything apart.
Run with: pytest roundabout/test_parser.py  (from c:\\zork_awt)
"""

import sys
import os
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from testkit import _make_world, _do, _goto, _carry
from content.vocabulary import make_vocabulary

DIRECTIONS = [("n", "north"), ("s", "south"), ("e", "east"), ("w", "west"),
              ("u", "up"), ("d", "down"), ("ne", "northeast"), ("nw", "northwest"),
              ("se", "southeast"), ("sw", "southwest")]


# --- Synonym Policy ---------------------------------------------------------------

@pytest.mark.parametrize("word,canonical", [
    ("incant", "cast"), ("chant", "cast"),           # 5. cast owns incant / chant
    ("banish", "exorcise"), ("begone", "exorcise"),  # 5. exorcise keeps banish / begone
    ("moor", "dock"), ("angle", "fish"),
    ("trade", "swap"), ("exchange", "swap"),
    ("order", "buy"), ("purchase", "buy"), ("rent", "buy"),
    ("lever", "pry"), ("jimmy", "pry"),
    ("drive", "drive"), ("tip", "tip"), ("load", "load"), ("clear", "clear"),
])
def test_verb_synonyms(word, canonical):
    assert make_vocabulary().canonical_verb(word) == canonical


def test_set_belongs_to_sail_not_turn():
    v = make_vocabulary()
    assert v.canonical_verb("turn") == "turn"
    assert v.canonical_verb("set") != "turn"          # 6. SET SAIL -> sail


@pytest.mark.parametrize("short,full", DIRECTIONS)
def test_direction_abbreviations(short, full):
    v = make_vocabulary()
    assert v.canonical_direction(short) == v.canonical_direction(full) is not None


def test_abbreviation_moves_like_the_full_word():
    w, g = _make_world()
    _goto(w, "TOWN-SQUARE")
    _do(g, "n")
    via_short = w.here.name
    _goto(w, "TOWN-SQUARE")
    _do(g, "north")
    assert w.here.name == via_short != "TOWN-SQUARE"


# --- Responses -----------------------------------------------------------------------

def test_unknown_word():
    w, g = _make_world()
    assert 'I don\'t know the word "xyzzy".' in _do(g, "xyzzy")


# --- Object lists (Synonym Policy 7) -----------------------------------------------------

def test_take_a_list_one_line_each():
    w, g = _make_world()
    _goto(w, "TOWN-SQUARE")
    for name in ("ROPE", "SHOVEL"):
        w.move_object(w.objects[name], w.here)
    out = _do(g, "take rope and shovel")
    assert w.objects["ROPE"].location is w.player
    assert w.objects["SHOVEL"].location is w.player
    assert len([l for l in out.splitlines() if l.strip()]) == 2


def test_get_is_take():
    w, g = _make_world()
    _goto(w, "TOWN-SQUARE")
    w.move_object(w.objects["ROPE"], w.here)
    _do(g, "get rope")
    assert w.objects["ROPE"].location is w.player


# --- The default examine line: no "the" before a name (mechanics.md — Object descriptions; TODO #32)

@pytest.mark.parametrize("room,noun,line", [
    ("COUNCIL-CHAMBER", "man", "You see nothing special about Councilman Rowan Finch."),
    ("BAR", "may", "You see nothing special about May."),
])
def test_nothing_special_about_a_named_npc(room, noun, line):
    w, g = _make_world()
    _goto(w, room)
    assert line in _do(g, f"look at {noun}")


def test_nothing_special_keeps_the_for_a_title():
    w, g = _make_world()
    _goto(w, "COUNCIL-CHAMBER")
    w.move_object(w.objects["ROWAN-FINCH"], None)
    w.move_object(w.objects["ARCHIVIST"], w.here)
    assert "You see nothing special about the Archivist." in _do(g, "x archivist")


# --- TODO #28: possessives, the burnt-out torch, READ, the riddle's answers --------

@pytest.mark.parametrize("cmd", ["x shamus's slate", "x shamus' slate", "x the slate"])
def test_an_owners_name_is_dropped(cmd):
    w, g = _make_world()
    _goto(w, "KITCHEN")
    assert "Chalked on the slate" in _do(g, cmd)


def test_an_owner_on_a_carried_thing_and_on_nothing():
    w, g = _make_world()
    _goto(w, "TOWN-SQUARE")
    _carry(w, "KITE")
    assert "You can't see" not in _do(g, "x child's kite")
    assert "You can't see any banana here!" in _do(g, "x shamus's banana")


def test_a_possessive_adjective_still_matches():
    w, g = _make_world()
    _goto(w, "LIGHTHOUSE")
    assert "You can't see" not in _do(g, "x keeper's desk")


def test_burnt_out_torch_by_its_name():
    from content import light
    w, g = _make_world()
    _goto(w, "TOWN-SQUARE")
    torch = _carry(w, "TORCH")
    light._go_out(w)
    assert "You toss the burnt-out torch aside." in _do(g, "drop burnt-out torch")
    assert torch.location is None
    light.light_torch(w)                                   # a fresh one isn't "burnt"
    assert torch.adjectives == []


@pytest.mark.parametrize("name,line", [
    ("GRAVESTONE", "You tip up one edge far enough to read it: CALDER FINCH — EXPLORER."),
    ("POCKET-WATCH", "You can't read that."),
])
def test_read_text(name, line):
    w, g = _make_world()
    _goto(w, "TOWN-SQUARE")
    obj = _carry(w, name)
    assert line in _do(g, f"read {obj.synonyms[0]}")


def test_read_banner_stays_nothing_written():
    w, g = _make_world()
    _goto(w, "VIKING-ENCAMPMENT")
    assert "There's nothing written on the banner." in _do(g, "read banner")


@pytest.mark.parametrize("answer", ["the sea", "it's the sea", "it is the sea", "a sea"])
def test_riddle_takes_the_sea(answer):
    w, g = _make_world()
    _goto(w, "HAALVARS-HUT")
    assert '"The stone is satisfied.' in _do(g, answer)          # locations.md — Haalvar's Hut
    assert w.get_global("RIDDLE-DONE")


def test_riddle_wrong_with_an_article():
    w, g = _make_world()
    _goto(w, "HAALVARS-HUT")
    assert '"Impressive. Wrong, but impressive in its wrongness."' in _do(g, "the ocean")
    assert not w.get_global("RIDDLE-DONE")
