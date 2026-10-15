"""
Buildings and places you go into (mechanics.md — Parser Verbs, Stairs and
places; TODO #23, 2026-10-14): ENTER / GO INTO / GO THROUGH [place], EXAMINE /
LOOK AT / LOOK IN [place] ("Why not go in and look around?"), bare ENTER / IN
("Enter what?" where a room has several places).
Run with: pytest roundabout/test_places.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import pytest

from test_room_exits import _look, _do
from content import ways

LOOK_AROUND = "Why not go in and look around?"
ENTER_WHAT = "Enter what?"

# (room, noun, where it goes)
PLACES = [
    ("TOWN-SQUARE", "tavern", "TALE-AND-ALE"),
    ("TOWN-SQUARE", "inn", "TALE-AND-ALE"),
    ("TOWN-SQUARE", "pub", "TALE-AND-ALE"),
    ("TOWN-SQUARE", "tale and ale", "TALE-AND-ALE"),
    ("TOWN-SQUARE", "town hall", "TOWN-HALL"),
    ("TOWN-SQUARE", "hall", "TOWN-HALL"),
    ("TOWN-SQUARE", "townhall", "TOWN-HALL"),
    ("MAIN-WEST", "library", "LIBRARY"),
    ("MAIN-EAST", "church", "CHURCH-NAVE"),
    ("GRAVEYARD", "church", "CHURCH-NAVE"),
    ("GRAVEYARD", "mausoleum", "MAUSOLEUM"),
    ("GRAVEYARD", "tomb", "MAUSOLEUM"),
    ("ROUNDABOUT-BEACH", "lighthouse", "LIGHTHOUSE"),
    ("OLD-OAK", "cottage", "BEEKEEPERS-COTTAGE"),
    ("OLD-OAK", "beekeeper's cottage", "BEEKEEPERS-COTTAGE"),
    ("OLD-OAK", "house", "BEEKEEPERS-COTTAGE"),
    ("EMPTY-BEACH", "structure", "KEVRYS-HOUSE"),
    ("EMPTY-BEACH", "house", "KEVRYS-HOUSE"),
    ("EMPTY-BEACH", "building", "KEVRYS-HOUSE"),
    ("VIKING-ENCAMPMENT", "hut", "HAALVARS-HUT"),
]

# The ship and the yurt have their own gates (the Pie Rat; the path and ward)
SHIP_REFUSED = '"You don\'t even look like a pirate."'


def _go(room, command, lit=False, **globals_):
    w, g, _ = _look(room, **globals_)
    if lit:                                       # going into a dark place
        import io, contextlib
        from content import light
        torch = w.objects["TORCH"]
        w.move_object(torch, w.player)
        torch.clear_flag("INVISIBLE")
        with contextlib.redirect_stdout(io.StringIO()):
            light.light_torch(w)
    out = _do(g, command)
    return w, out


def test_the_lines_match_the_design():
    assert ways.LOOK_AROUND == LOOK_AROUND
    assert ways.ENTER_WHAT == ENTER_WHAT


@pytest.mark.parametrize("verb", ["enter", "go into", "go in", "go through"])
@pytest.mark.parametrize("room, noun, dest", PLACES)
def test_going_in(verb, room, noun, dest):
    w, _ = _go(room, f"{verb} {noun}", lit=True)  # the mausoleum is dark
    assert w.here.name == dest


def test_the_dark_mausoleum_is_still_dark():
    """ENTER is the exit: no light, no way in (as SOUTH)."""
    w, out = _go("GRAVEYARD", "enter mausoleum")
    assert "too dark to go any further" in out
    assert w.here.name == "GRAVEYARD"


@pytest.mark.parametrize("verb", ["examine", "look at", "look in", "x"])
@pytest.mark.parametrize("room, noun, _dest", PLACES)
def test_look_around(verb, room, noun, _dest):
    w, out = _go(room, f"{verb} {noun}")
    assert LOOK_AROUND in out
    assert w.here.name == room


@pytest.mark.parametrize("noun", ["", " statue", " fountain"])
def test_x_is_examine(noun):
    """X is EXAMINE (mechanics.md — Parser Verbs; 2026-10-12 playtest)."""
    _w, examined = _go("TOWN-SQUARE", f"examine{noun}")
    _w, x = _go("TOWN-SQUARE", f"x{noun}")
    assert x == examined


@pytest.mark.parametrize("command", ["enter", "in", "go in"])
@pytest.mark.parametrize("room, globals_", [
    ("TOWN-SQUARE", {}),
    ("GRAVEYARD", {}),
    ("GRAVEYARD", {"CHUCKLE_HOUSE_VISIBLE": True}),
])
def test_several_places_asks_without_a_turn(room, globals_, command):
    w, g, _ = _look(room, **globals_)
    moves = w.moves
    out = _do(g, command)
    assert ENTER_WHAT in out
    assert w.here.name == room
    assert w.moves == moves                      # no turn, as "Up or down?"


@pytest.mark.parametrize("command", ["enter", "in"])
@pytest.mark.parametrize("room, dest", [
    ("MAIN-WEST", "LIBRARY"), ("MAIN-EAST", "CHURCH-NAVE"),
    ("ROUNDABOUT-BEACH", "LIGHTHOUSE"), ("OLD-OAK", "BEEKEEPERS-COTTAGE"),
    ("EMPTY-BEACH", "KEVRYS-HOUSE"), ("VIKING-ENCAMPMENT", "HAALVARS-HUT"),
])
def test_one_place_goes_in(room, dest, command):
    w, _ = _go(room, command)
    assert w.here.name == dest


# --- The Chuckle House: only once Litlock's bonk has shown it ---------------------

CHUCKLE_NOUNS = ["building", "house", "structure", "facade", "chuckle house", "low building"]


@pytest.mark.parametrize("noun", CHUCKLE_NOUNS)
def test_the_chuckle_house_once_shown(noun):
    w, _ = _go("GRAVEYARD", f"enter {noun}", CHUCKLE_HOUSE_VISIBLE=True)
    assert w.here.name == "CHUCKLE-ENTRANCE"
    w, out = _go("GRAVEYARD", f"examine {noun}", CHUCKLE_HOUSE_VISIBLE=True)
    assert LOOK_AROUND in out


@pytest.mark.parametrize("noun", ["building", "house"])
def test_no_chuckle_house_before_the_bonk(noun):
    w, out = _go("GRAVEYARD", f"enter {noun}")
    assert f"You can't see any {noun} here!" in out
    assert w.here.name == "GRAVEYARD"


def test_entering_the_chuckle_house_is_going_east():
    """ENTER walks the exit: the same arrival as EAST."""
    w1, by_enter = _go("GRAVEYARD", "enter house", CHUCKLE_HOUSE_VISIBLE=True)
    w2, by_east = _go("GRAVEYARD", "east", CHUCKLE_HOUSE_VISIBLE=True)
    assert by_enter == by_east
    assert w1.here is not None and w1.here.name == w2.here.name


# --- The Pie Rat Ship ---------------------------------------------------------------

@pytest.mark.parametrize("command", ["enter ship", "enter", "in", "go into ship", "board ship"])
def test_the_ship_is_going_east(command):
    """Every way in meets the Pie Rat, as EAST does."""
    _w, by_east = _go("DOCKS", "east")
    w, out = _go("DOCKS", command)
    assert out == by_east and SHIP_REFUSED in out
    assert w.here.name == "DOCKS"


@pytest.mark.parametrize("noun", ["ship", "pie rat ship", "vessel", "boat"])
def test_examine_the_ship(noun):
    _w, out = _go("DOCKS", f"examine {noun}")
    assert LOOK_AROUND in out


# --- The Dankhaus yurt: only once the path is found ------------------------------

def _bog(command, found=True, invited=True):
    w, g, _ = _look("BOG-SE", DANKHAUS_PATH_FOUND=found, DANKHAUS_INVITED=invited)
    if found:
        w.objects["DANKHAUS"].clear_flag("INVISIBLE")   # as path_check does
    return w, _do(g, command)


@pytest.mark.parametrize("command", ["enter", "in", "enter yurt", "enter dankhaus", "go into yurt"])
def test_into_the_yurt(command):
    w, _ = _bog(command)
    assert w.here.name == "DANKHAUS-COMMON-ROOM"


@pytest.mark.parametrize("noun", ["yurt", "dankhaus"])
def test_examine_the_yurt(noun):
    w, out = _bog(f"examine {noun}")
    assert LOOK_AROUND in out


def test_no_yurt_before_the_path():
    w, out = _bog("enter", found=False)
    assert "You can't go in there." in out
    w, out = _bog("enter yurt", found=False)
    assert "You can't see any yurt here!" in out
    assert w.here.name == "BOG-SE"


def test_the_ward_still_turns_you_back():
    _w, by_east = _bog("east", invited=False)
    w, out = _bog("enter yurt", invited=False)
    assert out == by_east
    assert w.here.name == "BOG-SE"


# --- The longhouses: scenery, not a way in ---------------------------------------

LONGHOUSES = ("Timber halls with turf roofs, each long enough to sleep a ship's crew. "
              "Nobody has invited you in, and nobody looks likely to.")


@pytest.mark.parametrize("noun", ["longhouses", "longhouse", "halls"])
def test_examine_the_longhouses(noun):
    _w, out = _go("VIKING-ENCAMPMENT", f"examine {noun}")
    assert LONGHOUSES in out


def test_no_way_into_the_longhouses():
    w, out = _go("VIKING-ENCAMPMENT", "enter longhouse")
    assert "You can't go in there." in out
    assert w.here.name == "VIKING-ENCAMPMENT"


# --- Apostrophes join a word, they don't split it (mechanics.md — Synonym Policy) --

@pytest.mark.parametrize("room, command, expect", [
    ("LIGHTHOUSE", "examine keeper's desk", "A plain desk under the window"),
    ("WIZARDS-TOWER", "examine will's desk", None),
    ("TOWN-SQUARE", "what's the statue", None),
    ("OLD-OAK", "examine beekeeper’s cottage", LOOK_AROUND),      # a curly apostrophe
    ("VIKING-ENCAMPMENT", "examine haalvar's hut", LOOK_AROUND),
])
def test_possessives(room, command, expect):
    _w, out = _go(room, command)
    _w, plain = _go(room, command.replace("'", "").replace("’", ""))
    assert out == plain and "You can't see any" not in out
    if expect:
        assert expect in out


@pytest.mark.parametrize("room, noun", [
    ("MAIN-WEST", "church"), ("MAIN-EAST", "library"), ("TOWN-SQUARE", "library"),
])
def test_a_building_only_where_the_room_names_it(room, noun):
    w, out = _go(room, f"enter {noun}")
    assert f"You can't see any {noun} here!" in out
    assert w.here.name == room


# --- OUT / LEAVE (mechanics.md — EXIT / LEAVE / OUT; TODO #23) -----------------------

WHICH_DIRECTION = "Which direction?"
NO_PLACE_TO_LAND = "There's no place to land here."
LAND_PROMPT = "Do you wish to land? [yes/no] "


def test_the_leaving_lines_match_the_design():
    from content import verbs
    assert verbs._WHICH_DIRECTION == WHICH_DIRECTION
    assert verbs._NO_PLACE_TO_LAND == NO_PLACE_TO_LAND
    assert verbs._LAND_PROMPT == LAND_PROMPT


@pytest.mark.parametrize("command", [
    "out", "go out", "leave", "leave bar", "leave the bar", "leave tavern", "leave room",
])
def test_leaving_asks_which_direction(command):
    w, g, _ = _look("BAR")
    moves = w.moves
    out = _do(g, command)
    assert out.strip() == WHICH_DIRECTION
    assert w.here.name == "BAR" and w.moves == moves     # no turn


@pytest.mark.parametrize("room, command", [
    ("LIBRARY", "leave library"), ("CHURCH-NAVE", "leave church"), ("KITCHEN", "leave kitchen"),
    ("TOWN-SQUARE", "out"),
])
def test_leaving_anywhere_ashore(room, command):
    _w, out = _go(room, command)
    assert out.strip() == WHICH_DIRECTION


def _holding(room, name):
    w, g, _ = _look(room)
    obj = w.objects[name]
    obj.clear_flag("INVISIBLE")
    w.move_object(obj, w.player)
    return w, g, obj


def test_leave_a_thing_is_still_drop():
    w, g, crowbar = _holding("BAR", "CROWBAR")
    assert "You drop the crowbar." in _do(g, "leave crowbar")
    assert crowbar.location is w.here
    _w, not_held = _go("BAR", "leave crowbar")
    _w, dropped = _go("BAR", "drop crowbar")
    assert not_held == dropped


def test_leave_bar_holding_the_portcullis_bar_drops_it():
    w, g, bar = _holding("BAR", "PORTCULLIS-BAR")
    assert "You drop the portcullis bar." in _do(g, "leave bar")
    assert bar.location is w.here


# --- Aboard: "Do you wish to land?" -------------------------------------------------

def _aboard(room, answer, command="out", **globals_):
    from unittest.mock import patch
    w, g, _ = _look(room, **globals_)
    prompts = []

    def _input(prompt=""):
        prompts.append(prompt)
        return answer

    moves = w.moves
    with patch("builtins.input", _input):
        out = _do(g, command)
    return w, out, prompts, w.moves != moves


@pytest.mark.parametrize("command", ["out", "go out", "leave", "leave ship"])
@pytest.mark.parametrize("room, globals_, dest", [
    ("SHIP-DECK", {}, "DOCKS"),                          # moored in harbor
    ("SEA-WEST", {"AT_SEA": True}, "DOCKS"),
    ("SEA-EAST", {"AT_SEA": True}, "DESERT-ISLAND"),
    ("LAND-HO", {"AT_SEA": True}, "EMPTY-BEACH"),
])
def test_yes_lands(room, globals_, dest, command):
    w, _out, prompts, turned = _aboard(room, "yes", command, **globals_)
    assert prompts == [LAND_PROMPT]
    assert w.here.name == dest and turned


@pytest.mark.parametrize("answer", ["no", "n", "", "maybe"])
def test_anything_else_stays_aboard(answer):
    w, out, prompts, turned = _aboard("LAND-HO", answer, AT_SEA=True)
    assert prompts == [LAND_PROMPT]
    assert w.here.name == "LAND-HO" and not turned


@pytest.mark.parametrize("command", ["out", "leave", "leave ship"])
@pytest.mark.parametrize("room", ["SEA-MID", "OPEN-OCEAN-5"])
def test_no_place_to_land_at_sea(room, command):
    w, out, prompts, turned = _aboard(room, "yes", command, AT_SEA=True)
    assert prompts == []                                 # no question to refuse
    assert out.strip() == NO_PLACE_TO_LAND
    assert w.here.name == room and not turned


@pytest.mark.parametrize("command", ["land", "dock", "disembark"])
def test_landing_from_the_deck_in_harbor(command):
    """The deck moored at the Docks lands on the Docks (it used to be "no place")."""
    w, _ = _go("SHIP-DECK", command)
    assert w.here.name == "DOCKS"
