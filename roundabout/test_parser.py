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

from test_knight import _make_world, _do
from content.vocabulary import make_vocabulary

DIRECTIONS = [("n", "north"), ("s", "south"), ("e", "east"), ("w", "west"),
              ("u", "up"), ("d", "down"), ("ne", "northeast"), ("nw", "northwest"),
              ("se", "southeast"), ("sw", "southwest")]


def _goto(w, room):
    w.move_object(w.player, w.rooms[room])
    w.here = w.rooms[room]


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


@pytest.mark.parametrize("cmd", ["i", "inventory"])
def test_inventory_empty_handed_and_purse(cmd):
    w, g = _make_world(zenni=0)
    out = _do(g, cmd)
    assert "You are empty-handed." in out
    assert "You have no Zenni." in out


def test_inventory_purse_counts():
    w, g = _make_world(zenni=1)
    assert "You have 1 Zenni." in _do(g, "i")
    w.globals["zenni"] = 12
    assert "You have 12 Zenni." in _do(g, "i")


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
