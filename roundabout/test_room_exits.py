"""
Room descriptions name their exits (playtest theme 1; locations.md for each
room's text). The Church of All nave and Altar are in test_church_nave.py.
Run with: pytest roundabout/test_room_exits.py  (from c:\\zork_awt)
"""

import sys
import os
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do
from content.shrine_path import BRIDGE_WEST_SHUT
from content.mine import SHAFT_UP_OPEN, SHAFT_UP_BURIED


def _look(room, **globals_):
    w, g = _make_world()
    for k, v in globals_.items():
        w.set_global(k.replace("_", "-"), v)
    w.move_object(w.player, w.rooms[room])
    w.here = w.rooms[room]
    if not w.is_lit():                  # dark rooms: carry a lit torch
        torch = w.objects["TORCH"]
        w.move_object(torch, w.player)
        torch.clear_flag("INVISIBLE")
        from content import light
        import io, contextlib
        with contextlib.redirect_stdout(io.StringIO()):
            light.light_torch(w)
    return w, g, _do(g, "look")


@pytest.mark.parametrize("room, phrases", [
    ("ROUNDABOUT-BEACH", ["docks stretch east", "lighthouse stands to the northeast",
                          "Beach Road runs back north"]),
    ("TALE-AND-ALE", ["The bar is south", "A staircase climbs", "To the east, a doorway",
                      "far northwest corner", "street door opens north"]),
    ("UPPER-HALL", ["a narrower stair turns upward into the tower",
                    "the main staircase leads back down"]),
    ("MINE-PASSAGE", ["The stairs are back to the north", "runs on to the south",
                      "side passage opens to the east"]),
    ("MAIN-SHAFT", ["functional, not decorative", "A side room opens to the south",
                    "goes on down into the workings below"]),
    ("ARCHERY-RANGE", ["the encampment to the west", "The road back to town runs east",
                       "To the north, a footpath"]),
    ("LIBRARY", ["At the east end, one of the gaps", "The red doors to the street are south"]),
    ("ROUNDABOUT-WASTELAND", ["To the south, a volcano", "Eastward, a rutted road",
                              "the town is back to the west", "a matter of some local sensitivity"]),
    ("CHARNEL-WALK", ["worn steps climb up into the crypt", "tunnels running back to the north"]),
    ("CHUCKLE-ENTRANCE", ["a narrow passage leads south", "opens west onto the graveyard"]),
    ("LOWER-CROSSING", ["North, a short passage", "East, the walls close in",
                        "South, the dark is thicker", "antechamber is back to the west"]),
    ("TOWN-SQUARE", ["anchors the north end", "faces it from the south",
                     "Main Street runs off east and west", "to the southwest a gap"]),
    ("MAIN-EAST", ["the church standing apart to the south", "The wasteland begins to the east",
                   "Back to the west, the street opens into the town square"]),
    ("MAIN-WEST", ["The library stands to the north", "continues west toward the archery range",
                   "To the southeast, a gap", "The town square is back to the east"]),
    ("ALLEY", ["northeast back to the town square", "northwest to Main West",
               "Further south, the alley deepens"]),
    ("BACK-ALLEY", ["The only way out is back north"]),
    ("BAR", ["The kitchen is further south", "the main room is back to the north"]),
    ("KITCHEN", ["the door that leads back north to the bar", "set into the floor"]),
    ("PIPE-ROOM", ["Conversations here are conducted", "through the doorway to the west"]),
    ("CASINO-CORNER", ["from the main room, back to the southeast"]),
    ("TOWN-HALL", ["Council Chamber opens to the east", "Records Room to the west",
                   "a staircase climbs", "The heavy doors open south onto the square"]),
    ("COUNCIL-CHAMBER", ["The door back to the foyer is west"]),
    ("RECORDS-ROOM", ["The door back to the foyer is east"]),
    ("TOWN-HALL-TOWER", ["The narrow stair winds back down to the hall below"]),
    ("KEEPERS-CHAMBER", ["The door back to the nave is east. On the desk:"]),
    ("MAUSOLEUM", ["Steps descend inside toward the crypt below", "The graveyard lies back to the north"]),
    ("REJECTION-MIRROR", ["The doorway to the south", "The entrance hall is back to the north"]),
    ("SHATTER-TRAP-MIRROR", ["The way on is past it, to the south",
                             "The first mirror's room is back to the north"]),
    ("GHOSTS-ROOM", ["the one real doorway, back the way you came"]),
    ("VIKING-ENCAMPMENT", ["Paths lead north to a hut", "the archery range is back to the east"]),
    ("HAALVARS-HUT", ["The door flap opens south onto the encampment"]),
    ("RITUAL-CIRCLE", ["The path back to the encampment runs north"]),
    ("FIRE-PIT", ["The longhouses are back to the east"]),
    ("ROUNDABOUT-POND", ["the town path to the south and the bog to the north"]),
    ("BOG-SW", ["The pond lies back to the south"]),
    ("DANKHAUS-COMMON-ROOM", ["Doors lead off it to the north, south and east",
                              "the front door opens west onto the bog"]),
    ("DANKHAUS-HEARTH-ROOM", ["through the east door", "The common room is back to the west",
                              "a door to the south stands half open"]),
    ("LITLOCKS-ROOM", ["A narrower door in the east wall", "the common room is back to the south"]),
    ("LITLOCKS-STUDY", ["The only door is the one you came through, to the west"]),
    ("AURIX-ROOM", ["The common room is back through the door to the north"]),
    ("LYNDS-ROOM", ["The hearth room is back to the north"]),
    ("BEACH-ROAD", ["South, it runs down toward the beach", "North, it climbs toward a great old oak",
                    "The wasteland is back to the west"]),
    ("ROUNDABOUT-FOREST", ["Back to the south, the trees thin out", "a dark mouth leading down"]),
    ("MINE-ENTRANCE", ["NO, NOT YOU SLOTH", "the shaft drops down into the dark",
                       "the forest is back up the slope"]),
    ("VOLCANO", ["The wasteland is back to the north"]),
    ("PYRONICUS-FORGE", ["The uneven stairs climb back up into it"]),
    ("BEEKEEPERS-COTTAGE", ["The old oak's clearing is back to the east"]),
    ("DOCKS", ["sits in her berth to the east", "The beach is back to the west",
               "honest work"]),
    ("LIGHTHOUSE", ["a chain hung across its foot", "The door out to the beach is southwest"]),
    ("SEA-WEST", ["The beach stretches away to the west"]),
    ("EMPTY-BEACH", ["Somewhere beyond them to the east", "The ship rides at anchor just offshore",
                     "content with that"]),
    ("DESERT-ISLAND", ["The ship rides at anchor just offshore"]),
    ("KEVRYS-HOUSE", ["The beach is back out to the west", "a doorway to the east"]),
    ("ASSAY-ROOM", ["off the main shaft, which lies back to the north"]),
    ("RICKETY-BRIDGE", ["leads south to a heavy iron door",
                        "To the north, a carved doorway"]),
])
def test_the_description_names_the_exits(room, phrases):
    _, _, out = _look(room)
    for phrase in phrases:
        assert phrase in out


def test_the_mailbox_is_still_in_the_tavern_description():
    _, _, out = _look("TALE-AND-ALE")
    assert "stands a mailbox" in out


# --- Rickety Bridge: the west line follows the Quest 38 shortcut ---------------

def test_bridge_west_shut_before_the_shortcut_opens():
    w, g, out = _look("RICKETY-BRIDGE")
    assert BRIDGE_WEST_SHUT in out
    assert BRIDGE_WEST_SHUT in _do(g, "west")
    assert w.here.name == "RICKETY-BRIDGE"


def test_bridge_west_shut_with_only_the_timbers_cleared():
    w, g, out = _look("RICKETY-BRIDGE", TIMBERS_CLEARED=True)
    assert BRIDGE_WEST_SHUT in out
    assert BRIDGE_WEST_SHUT in _do(g, "west")


def test_bridge_west_open_once_timbers_and_flood_are_done():
    w, g, out = _look("RICKETY-BRIDGE", TIMBERS_CLEARED=True, AQUEDUCT_SEALED=True)
    assert "To the west, a side passage leads back toward the Collapsed Gallery." in out
    assert BRIDGE_WEST_SHUT not in out
    _do(g, "west")
    assert w.here.name == "COLLAPSED-GALLERY"


# --- Main Shaft: the way up is buried after the cave-in ------------------------

def test_shaft_up_open_before_the_cave_in():
    _, _, out = _look("MAIN-SHAFT")
    assert SHAFT_UP_OPEN in out
    assert SHAFT_UP_BURIED not in out


def test_shaft_up_buried_after_the_cave_in():
    _, _, out = _look("MAIN-SHAFT", MINE_BLOWN=True)
    assert SHAFT_UP_BURIED in out
    assert SHAFT_UP_OPEN not in out


def test_the_bar_description_doesnt_name_may_before_she_introduces_herself():
    _, _, out = _look("BAR")
    room_text = out.split("A woman behind the bar")[0]
    assert "May" not in room_text
    assert "a system only the bartender understands" in room_text


# --- Guest rooms: the door out; from the hall, the doors are rented -------------

@pytest.mark.parametrize("n, way", [(1, "east"), (2, "west"), (3, "south")])
def test_guest_room_names_its_door(n, way):
    from content.tavern import DOOR_OUT
    _, _, out = _look(f"GUEST-ROOM-{n}")
    assert DOOR_OUT.format(way) in out


@pytest.mark.parametrize("n, way", [(1, "east"), (2, "west"), (3, "south")])
def test_guest_room_door_line_follows_the_wake_up_text(n, way):
    from content.tavern import DOOR_OUT
    w, g, _ = _look(f"GUEST-ROOM-{n}")
    w.set_global("GUEST-WAKING", True)
    out = _do(g, "look")
    assert out.rstrip().endswith(DOOR_OUT.format(way))


@pytest.mark.parametrize("way", ["west", "east", "north"])
def test_the_guest_rooms_cant_be_walked_into_from_the_hall(way):
    from content.tavern import ROOMS_RENTED
    w, g, _ = _look("UPSTAIRS-HALL")
    assert ROOMS_RENTED in _do(g, way)
    assert w.here.name == "UPSTAIRS-HALL"


@pytest.mark.parametrize("visits", [1, 2, 3])
def test_the_crypt_passage_goes_down_and_the_steps_go_up(visits):
    w, g, _ = _look("CRYPT")
    w.set_global("CRYPT-VISITS", visits)
    out = _do(g, "look")
    assert "slopes down" in out
    assert "Steps climb up to the mausoleum." in out


def test_swarm_tree_names_the_way_back_with_the_smoke_jar():
    w, g = _make_world()
    jar = w.objects["SMOKE-JAR"]
    w.move_object(jar, w.player)
    jar.clear_flag("INVISIBLE")
    w.move_object(w.player, w.rooms["OLD-OAK"])
    w.here = w.rooms["OLD-OAK"]
    out = _do(g, "east")
    assert w.here.name == "SWARM-TREE"
    assert "The oak's clearing is back to the west" in out


def test_mine_entrance_after_the_cave_in_names_the_way_up():
    _, _, out = _look("MINE-ENTRANCE", MINE_BLOWN=True)
    assert "The entrance is gone." in out
    assert "The forest is back up the slope." in out
    assert "drops down into the dark" not in out


def test_docks_rope_is_described_once_and_goes_when_taken():
    w, g, out = _look("DOCKS")
    assert out.count("coil of rope") == 1          # its own listing only
    _do(g, "take rope")
    assert "rope sits loose" not in _do(g, "look")


def test_lighthouse_stair_is_chained_off():
    from content.rooms import LIGHTHOUSE_CHAIN
    w, g, _ = _look("LIGHTHOUSE")
    assert LIGHTHOUSE_CHAIN in _do(g, "up")
    assert w.here.name == "LIGHTHOUSE"


# --- Pie Rat Ship deck: the way off depends on where she lies -----------------

def test_deck_at_the_docks():
    from content.ship import DECK_AT_DOCKS, DECK_OFF_ISLAND
    _, _, out = _look("SHIP-DECK")
    assert DECK_AT_DOCKS in out and DECK_OFF_ISLAND not in out


@pytest.mark.parametrize("island", ["DESERT-ISLAND", "EMPTY-BEACH"])
def test_deck_after_reboarding_off_an_island(island):
    from content.ship import DECK_AT_DOCKS, DECK_OFF_ISLAND
    w, g = _make_world()
    w.set_global("SHIP-AWAY", True)
    w.move_object(w.player, w.rooms[island])
    w.here = w.rooms[island]
    _do(g, "board ship")
    out = _do(g, "look")
    assert w.here.name == "SHIP-DECK"
    assert DECK_OFF_ISLAND in out and DECK_AT_DOCKS not in out


# --- Captain's Quarters: the room, then Kevry's line ---------------------------

def _to_kevry(glasses):
    from engine.world import WEARBIT
    w, g = _make_world()
    gl = w.objects["ENCHANTED-GLASSES"]
    if glasses != "none":
        w.move_object(gl, w.player)
        gl.clear_flag("INVISIBLE")
        if glasses == "worn":
            gl.set_flag(WEARBIT)
    w.move_object(w.player, w.rooms["KEVRYS-HOUSE"])
    w.here = w.rooms["KEVRYS-HOUSE"]
    return w, g, _do(g, "east")


@pytest.mark.parametrize("glasses", ["none", "carried", "worn"])
def test_kevry_introduces_himself_after_the_room(glasses):
    from content.kevry import _QUARTERS, _FIRST_SEEN
    w, g, out = _to_kevry(glasses)
    assert out.index(_QUARTERS) < out.index(_FIRST_SEEN)
    assert w.get_global("KEVRY-MET")             # A House is now Kevry's House


def test_kevry_carried_line_follows_the_greeting():
    from content.kevry import _FIRST_SEEN, _CARRIED
    _, _, out = _to_kevry("carried")
    assert out.index(_FIRST_SEEN) < out.index(_CARRIED)
    assert "not looking up" not in out


def test_kevry_first_meeting_plays_once():
    from content.kevry import _FIRST_SEEN, _SEEN_AGAIN, _SEEN_ENCHANTED
    _, g, _ = _to_kevry("none")
    out = _do(g, "look")
    assert _FIRST_SEEN not in out and _SEEN_AGAIN in out
    _, g, _ = _to_kevry("worn")
    out = _do(g, "look")
    assert _FIRST_SEEN not in out and _SEEN_ENCHANTED in out
