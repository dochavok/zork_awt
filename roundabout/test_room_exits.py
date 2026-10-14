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
    ("EMPTY-BEACH", ["Somewhere beyond them to the east", "The ship rides at anchor just offshore",
                     "content with that"]),
    ("KEVRYS-HOUSE", ["The beach is back out to the west", "a doorway to the east"]),
    ("ASSAY-ROOM", ["off the main shaft, which lies back to the north"]),
    ("RICKETY-BRIDGE", ["leads south to a heavy iron door",
                        "To the north, a carved doorway"]),
    ("MINE-TUNNELS", ["veins of ore", "fresh-cut rock", "run off to the north",
                      "the shaft climbs back up to the main level"]),
    ("RATS-NEST", ["raise questions on a dock", "The tunnel runs back south"]),
    ("HIDDEN-SECONDARY-ENTRANCE", ["assay room wall, to the west,",
                                  "runs east toward the tunnel network"]),
    ("FORGOTTEN-SHAFT", ["To the west, a rougher passage", "Southward, the passage widens again"]),
    ("UNDERCROFT", ["The passage runs north toward older, narrower stone",
                    "south to where the tunnels meet"]),
    ("JUNCTION", ["east toward the cellar", "north toward the old mine workings",
                  "south, where the floor drops away toward a ravine"]),
    ("BONE-PASSAGE", ["The passage runs south, and west toward the junction",
                      "a low door of black oak"]),
    ("CELLAR", ["Steps climb back up to the kitchen", "In the west wall is a low door"]),
    ("DUNGEON-ENTRANCE", ["the bridge back to the north, and a passage leading south"]),
    ("INK-CORRIDOR", ["west, east, and on to the south; the dungeon entrance is back to the north"]),
    ("SUPPLY-ROOM", ["something chemical underneath. The doorway back to the corridor is east."]),
    ("STORAGE-AREA", ["A passage leads south", "The corridor is back to the west."]),
    ("NARROW-PASSAGEWAY", ["the corridor to the north", "It goes south and ends at a doorway"]),
    ("PRAYER-ALCOVE", ["off a passage that runs north and south"]),
    ("INSCRIPTION-CHAMBER", ["wider than the passages running north and south from it"]),
    ("CAVE-CREATURES-LAIR", ["or it's only just left. The crawlspace leads back west."]),
    ("ECHO-ALCOVE", ["The passage runs north and south."]),
    ("SPILLWAY", ["The sluice deposited you here", "There's no way back up. The passage continues south."]),
    ("SUPPLY-CACHE", ["Passages lead north and south."]),
    ("FLOOD-SUMP", ["and it feels like it. The only way out is back north."]),
    ("LOWER-CRYPT", ["this is as far as he got. A passage leads on north; you see rubble to "
                     "the south."]),
    ("SEA-WEST", ["The beach stretches away to the west", "Eastward, the coast begins to fall away."]),
    ("SEA-MID", ["West is the way home, if you trust your bearings. Whatever's east, you'll find out."]),
    ("DESERT-ISLAND", ["The ship rides at anchor just offshore.",
                       "The island isn't telling."]),
    ("SEA-EAST", ["It sits quietly off the bow, waiting to be noticed.",
                  "East of it, the sea continues without comment. West, the swells run back toward town."]),
    ("WIZARDS-BEDROOM", ["long enough to matter.\nThe door back to the tower is south.\n"
                         "The rest of the room is Will's business"]),
    ("STACKS", ["The passage from the Main Hall, back to the west, opens into something"]),
    ("LOWER-ENCAMPMENT", ["no one saw it coming. The only way out is back north, to the rubble."]),
    ("PILE-OF-RUBBLE", ["Passages lead north, east, and south. Your rope hangs down through "
                        "the hole above."]),
    ("MAGNETIC-VAULT", ["on a low stone platform. Passages lead north and south. The room"]),
    ("KEY-DOOR-LANDING", ["The staircase ends in a rough cave", "The passage continues south, "
                          "and the stairs climb back north to the iron door."]),
    ("SHRINE-ROOM", ["A corridor leads north; to the south, the floor gives way to a "
                     "narrow stone bridge."]),
    ("CREATURE-DEN", ["A passage leads on to the north; the combat room is back through "
                      "the door to the west."]),
])
def test_the_description_names_the_exits(room, phrases):
    _, _, out = _look(room)
    for phrase in phrases:
        assert phrase in out


@pytest.mark.parametrize("room", ["ROUNDABOUT-BEACH", "EMPTY-BEACH"])
def test_beaches_dont_assume_the_way_in(room):
    _, _, out = _look(room)
    assert "behind you" not in out


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


# --- Bone Passage: the black oak door shows the flood until the cellar drains --

def test_bone_passage_door_seeps_before_the_drain():
    from content.cellar import _BONE_DOOR_SEEP
    w, g, out = _look("BONE-PASSAGE")
    assert _BONE_DOOR_SEEP not in out              # the room text gives no warning
    assert _BONE_DOOR_SEEP in _do(g, "examine door")


def test_bone_passage_door_is_plain_after_the_drain():
    from content.cellar import _BONE_DOOR_SEEP
    w, g, _ = _look("BONE-PASSAGE", CELLAR_DRAINED=True)
    out = _do(g, "examine door")
    assert _BONE_DOOR_SEEP not in out
    assert "nothing special about the black oak door" in out


def test_cellar_side_door_doesnt_seep():
    from content.cellar import _BONE_DOOR_SEEP
    w, g, _ = _look("CELLAR")
    assert _BONE_DOOR_SEEP not in _do(g, "examine door")


# --- Toll Bridge: the bridge and its exits, then the Boggart or what he left ---

@pytest.mark.parametrize("state, globals_", [
    ("_BRIDGE_BOGGART", {}),
    ("_BRIDGE_STRONGBOX", {"BOGGART_GONE": True}),
    ("_BRIDGE_LOOTED", {"BOGGART_GONE": True, "STRONGBOX_OPEN": True}),
])
def test_toll_bridge_names_its_exits_in_every_state(state, globals_):
    from content import tunnels
    from content.tunnels import _BRIDGE
    _, _, out = _look("TOLL-BRIDGE", **globals_)
    assert "Across it, the tunnel runs on south" in _BRIDGE
    assert out.index(_BRIDGE) < out.index(getattr(tunnels, state))
    for other in {"_BRIDGE_BOGGART", "_BRIDGE_STRONGBOX", "_BRIDGE_LOOTED"} - {state}:
        assert getattr(tunnels, other) not in out


# --- Collapsed Aqueduct: south, then north, in every repair state -------------

@pytest.mark.parametrize("globals_, south", [
    ({}, "away down the passage south."),
    ({"BLOCKS_PLACED": 3}, "away down the passage south."),
    ({"AQUEDUCT_SEALED": True}, "A passage leads on south."),
])
def test_aqueduct_names_its_exits_in_every_state(globals_, south):
    from content.aqueduct import _BACK_NORTH
    _, _, out = _look("COLLAPSED-AQUEDUCT", **globals_)
    assert out.index(south) < out.index(_BACK_NORTH)


# --- Collapsed Gallery: the state line, the flood, then the way north ---------

@pytest.mark.parametrize("globals_, east, flooded", [
    ({}, "Heavy timbers have come down across it", True),
    ({"TIMBERS_DOWN": 3}, "The timbers are down, but the rock overhead sags", True),
    ({"TIMBERS_CLEARED": True}, "toward an old bridge over a gap in the floor", True),
    ({"TIMBERS_CLEARED": True, "AQUEDUCT_SEALED": True},
     "toward an old bridge over a gap in the floor", False),
])
def test_gallery_names_its_exits_in_every_state(globals_, east, flooded):
    from content.aqueduct import _GALLERY_BACK_NORTH, _FLOOD
    _, _, out = _look("COLLAPSED-GALLERY", **globals_)
    assert out.index(east) < out.index(_GALLERY_BACK_NORTH)
    assert (_FLOOD in out) == flooded
    if flooded:
        assert out.index(_FLOOD) < out.index(_GALLERY_BACK_NORTH)
    assert "significant time" not in out


# --- Idol Room: both doorways; the slab blocks only the north one -------------

def test_idol_room_names_both_doorways():
    _, _, out = _look("IDOL-ROOM")
    assert "Doorways lead north and south." in out


def test_idol_slab_names_the_north_doorway_and_south_stays_open():
    w, g, _ = _look("IDOL-ROOM")
    out = _do(g, "take idol")
    assert "drops into the north doorway" in out and "The way back is gone." in out
    look = _do(g, "look")
    assert look.index("Doorways lead north and south.") < look.index("A stone slab fills the north doorway.")
    _do(g, "south")
    assert w.here.name == "COMBAT-ROOM"


# --- Combat Room: north and south, whether the Den door is shut or open --------

@pytest.mark.parametrize("plate, door", [(None, "door is set into the stone, shut. "),
                                         ("fired", "the heavy door stands open. ")])
def test_combat_room_names_its_doorways(plate, door):
    _, _, out = _look("COMBAT-ROOM", PLATE_STATE=plate)
    assert door + "Doorways lead north and south. Whatever happened" in out


def test_prayer_alcove_no_longer_calls_itself_a_dead_end():
    _, _, out = _look("PRAYER-ALCOVE")
    assert "dead end" not in out


# --- Portcullis Corridor: the exit line follows the portcullis -----------------

@pytest.mark.parametrize("state, propped", [(None, False), ("discharged", False), ("propped", True)])
def test_portcullis_corridor_names_its_exits(state, propped):
    from content.shrine_path import _PORT_EXITS_OPEN, _PORT_EXITS_SHUT
    _, _, out = _look("PORTCULLIS-CORRIDOR", PORTCULLIS=state)
    assert (_PORT_EXITS_OPEN in out) == propped
    assert (_PORT_EXITS_SHUT in out) != propped


def test_walking_off_while_holding_the_portcullis_drops_it_on_the_way_out():
    from content.shrine_path import _DROPS
    w, g, _ = _look("PORTCULLIS-CORRIDOR", PORTCULLIS="discharged", PORTCULLIS_SIDE="north",
                    TRAP19_CHECKED=True)
    w.set_global("PORTCULLIS-HELD", w.moves)       # as LIFT PORTCULLIS leaves it
    out = _do(g, "north")
    assert w.here.name == "PRAYER-ALCOVE"
    assert out.index(_DROPS) < out.index("Prayer Alcove")
    out = _do(g, "south")
    assert w.here.name == "PORTCULLIS-CORRIDOR"
    assert _DROPS not in out
    assert w.get_global("PORTCULLIS-HELD") is None


# --- Mid-Tier Key Door: the bridge line on LOOK, not in the locked refusal ----

@pytest.mark.parametrize("unlocked, door", [(False, "It wants a key."),
                                            (True, "Stone stairs lead down to the south.")])
def test_key_door_names_the_bridge(unlocked, door):
    from content.shrine_path import _KEY_DOOR_BACK
    _, _, out = _look("MID-TIER-KEY-DOOR", KEY_DOOR_UNLOCKED=unlocked)
    assert door + " " + _KEY_DOOR_BACK in out


def test_key_door_refusal_doesnt_mention_the_bridge():
    from content.shrine_path import _KEY_DOOR_BACK
    w, g, _ = _look("MID-TIER-KEY-DOOR")
    out = _do(g, "south")
    assert "It wants a key." in out and _KEY_DOOR_BACK not in out


# --- Stored Room / Hole to Below: east before the dig, out of reach after ------

def test_stored_room_names_east_before_the_dig():
    from content.mid_tier import _HOLE_EXITS
    _, _, out = _look("STORED-ROOM")
    assert "A narrow passage carries on east beyond it; the mine passage is back to the west." in out
    assert _HOLE_EXITS not in out


@pytest.mark.parametrize("rope", [False, True])
def test_hole_to_below_exit_line_comes_last(rope):
    from content.mid_tier import _HOLE_EXITS
    _, _, out = _look("STORED-ROOM", STORED_ROOM_DUG=True, ROPE_TIED=rope)
    assert out.rstrip().endswith(_HOLE_EXITS)
    assert ("A rope is knotted around the timber" in out) == rope


def test_crevice_names_the_way_out_with_or_without_the_watch():
    w, g, out = _look("THE-CREVICE")
    assert out.rstrip().endswith("dangles a gold pocket watch on a chain. The only way out is back west.")
    w.move_object(w.objects["GOLD-WATCH"], w.player)
    out = _do(g, "look")
    assert out.rstrip().endswith("the finger empty now. The only way out is back west.")


# --- Deep Lock Door: a dead end, and every answer says so ----------------------

def test_deep_lock_door_names_the_way_back():
    _, _, out = _look("DEEP-LOCK-DOOR")
    assert "The passage ends here; the only way is back north." in out


@pytest.mark.parametrize("cmd, expected", [
    ("south", "DEEP_LOCK_SOUTH"),
    ("examine door", "DEEP_LOCK_EXAMINE"),
    ("pick lock", "_DEEP_LOCK_PICK"),
    ("pick door", "_DEEP_LOCK_PICK"),
    ("open door", "_DOOR_SHUT"),
])
def test_deep_lock_door_answers(cmd, expected):
    from content import inscription
    w, g, _ = _look("DEEP-LOCK-DOOR")
    assert getattr(inscription, expected) in _do(g, cmd)
    assert w.here.name == "DEEP-LOCK-DOOR"


# --- Lost Apprentice's Cell: the tunnel stops short until it's dug -------------

@pytest.mark.parametrize("dug, shown, hidden", [
    (False, "_CELL", "_CELL_DUG"),
    (True, "_CELL_DUG", "_CELL"),
])
def test_cell_tunnel_follows_the_dig(dug, shown, hidden):
    from content import trap_side
    _, _, out = _look("LOST-APPRENTICES-CELL", TUNNEL_DUG=dug)
    assert getattr(trap_side, shown) in out
    assert getattr(trap_side, hidden) not in out
    assert "west wall" not in out


# --- Antechamber: doorways named in both states; the warning names the door ----

@pytest.mark.parametrize("cleared", [False, True])
def test_antechamber_names_its_doorways_and_the_deadly_one(cleared):
    _, _, out = _look("ANTECHAMBER", BONES_CLEARED=cleared)
    assert "Doorways lead east and south, and the rubble lies to the west." in out
    assert ("narrow path of bare stone" in out) == cleared
    assert "beyond the south doorway" in out
    assert "the way you came" not in out


# --- The Narrow Pass: the breathing stops when the werewolf does ---------------

@pytest.mark.parametrize("dead, shown, hidden", [
    (False, "_NARROW_PASS", "_NARROW_PASS_QUIET"),
    (True, "_NARROW_PASS_QUIET", "_NARROW_PASS"),
])
def test_narrow_pass_follows_the_werewolf(dead, shown, hidden):
    from content import still_den
    _, _, out = _look("NARROW-PASS", WEREWOLF_DEAD=dead)
    assert getattr(still_den, shown) in out
    assert getattr(still_den, hidden) not in out
    assert "The crossing is back to the west." in out


# --- The Still Den: the way back once the werewolf is up, and after ------------

@pytest.mark.parametrize("globals_", [{"WEREWOLF_RISEN": True}, {"WEREWOLF_DEAD": True}])
def test_still_den_names_the_way_back(globals_):
    _, _, out = _look("STILL-DEN", **globals_)
    assert "The narrow pass is back to the west." in out


def test_still_den_first_visit_has_no_exit_line():
    _, _, out = _look("STILL-DEN")
    assert "That changes the moment you enter." in out
    assert "The narrow pass is back to the west." not in out


# --- Tool Alcove: south in every state, north once open; not in EXAMINE WALL ---

@pytest.mark.parametrize("globals_", [{}, {"ALCOVE_FOUND": True}, {"ALCOVE_OPEN": True}])
def test_tool_alcove_names_the_way_back(globals_):
    from content.tool_alcove import _BACK_SOUTH, _ASKS
    _, _, out = _look("TOOL-ALCOVE", **globals_)
    assert _BACK_SOUTH in out
    assert ("onto a passage north" in out) == ("ALCOVE_OPEN" in globals_)
    if "ALCOVE_FOUND" in globals_:
        assert out.index(_BACK_SOUTH) < out.index(_ASKS)


@pytest.mark.parametrize("globals_", [{}, {"ALCOVE_OPEN": True}])
def test_tool_alcove_examine_wall_has_no_exit_line(globals_):
    from content.tool_alcove import _BACK_SOUTH
    w, g, _ = _look("TOOL-ALCOVE", **globals_)
    assert _BACK_SOUTH not in _do(g, "examine wall")


@pytest.mark.parametrize("frozen", [False, True])
def test_flooded_passage_names_both_ways(frozen):
    _, _, out = _look("FLOODED-PASSAGE", POOL_FROZEN=frozen)
    assert "The passage north" in out
    assert out.rstrip().endswith("The alcove is back to the south.")
    assert ("frozen solid" in out) == frozen


def test_fountain_room_frozen_names_south_and_still_ends_on_the_figure():
    _, _, out = _look("FOUNTAIN-ROOM")
    assert "settled and absolute. The flooded passage is back to the south." in out
    assert out.rstrip().endswith("A person. Standing. Composed.")


def test_fountain_room_after_the_thaw_names_south():
    _, _, out = _look("FOUNTAIN-ROOM", ICE_THAW=2)
    assert out.rstrip().endswith("melting at its edges. The flooded passage is back to the south.")


def test_dark_room_names_no_exit_before_the_lantern_and_both_after():
    _, _, out = _look("DARK-ROOM")
    assert "something the dark is doing on purpose" in out
    assert not any(d in out for d in ("north", "south"))      # absolute, by design
    _, _, out = _look("DARK-ROOM", LANTERN_HUNG=True)
    assert "passages north and south" in out


def test_spirit_room_names_both_passages_seen_or_unseen():
    from test_spirit_room import _walk_in
    w, g, out = _walk_in()                         # visible, working ring carried
    assert "The passages north and south are visible." in out
    _do(g, "wear ring")
    assert "Passages lead north and south." in _do(g, "look")


@pytest.mark.parametrize("moved", [False, True])
def test_burial_chamber_names_the_way_back_past_the_shapes(moved):
    _, _, out = _look("BURIAL-CHAMBER", MASK_MOVED=moved)
    assert ("The only way out is north, back through the shapes. Whatever they were, they let "
            "you pass once — unseen. You'd like to keep it that way.") in out


# --- Wizard Tower: the painting's subject; the bedroom door found, then kept ---

def test_tower_painting_says_what_it_shows():
    _, _, out = _look("WIZARDS-TOWER", BEDROOM_DOOR_VISIBLE=True)
    assert "A painting of a tavern hangs on the wall, slightly crooked." in out


@pytest.mark.parametrize("visited", [False, True])
def test_tower_door_found_line_follows_the_room(visited):
    import io, contextlib
    from unittest.mock import patch
    from content.rooms import BEDROOM_DOOR_FOUND, BEDROOM_DOOR_STAYS
    w, g = _make_world()
    tower = w.rooms["WIZARDS-TOWER"]
    tower.visited = visited                       # first visit, or BRIEF return
    w.move_object(w.player, w.rooms["WIZARDS-BEDROOM"])
    w.here = w.rooms["WIZARDS-BEDROOM"]
    with patch("content.player.check_perception", return_value=True):
        out = _do(g, "south")
    assert w.here is tower
    assert out.index("Will's Wizard Tower") < out.index(BEDROOM_DOOR_FOUND)
    assert BEDROOM_DOOR_STAYS not in out            # the find turn: announced, not yet kept
    assert BEDROOM_DOOR_STAYS in _do(g, "look")
    assert w.get_global("BEDROOM-DOOR-VISIBLE") is True


def test_tower_door_not_mentioned_before_it_is_found():
    from content.rooms import BEDROOM_DOOR_STAYS
    _, _, out = _look("WIZARDS-TOWER")
    assert BEDROOM_DOOR_STAYS not in out


# --- Every room: each exit usable now is named (mechanics.md — Room
# Descriptions Name Their Exits). Default state only; state-dependent text has
# its own tests above. Exits are tried on a throwaway world, since some end the
# game or move things.

_DIRECTION_WORDS = {
    "north": r"\bnorth(ward)?\b", "south": r"\bsouth(ward)?\b",
    "east": r"\beast(ward)?\b", "west": r"\bwest(ward)?\b",
    "northeast": r"\bnortheast\b", "northwest": r"\bnorthwest\b",
    "southeast": r"\bsoutheast\b", "southwest": r"\bsouthwest\b",
    "up": r"\bup\b|climb|above|upward", "down": r"\bdown\b|below|descend",
    "in": r"\bin\b|inside|enter", "out": r"\bout\b|outside",
}
# Deliberate exceptions (mechanics.md), each with its reason
_NO_EXIT_LINE = {
    "BOG-NE": "the Bog's interior — navigation is the puzzle",
    "BOG-NW": "the Bog's interior — navigation is the puzzle",
    "BOG-SE": "the Bog's interior — navigation is the puzzle",
    "BOG-SW": "the Bog's interior — navigation is the puzzle",
    "LAND-HO": "the end of the Open Ocean run",
    "DARK-ROOM": "the dark is absolute before the lantern",
    "DREAM-CORRIDOR": "its numbered choices are the navigation",
    "STILL-DEN": "first visit — the rising is the moment",
    "GHOSTS-ROOM": "the mirror maze — 'the one real doorway, back the way you came'",
}


def _all_rooms():
    w, _ = _make_world()
    return sorted(n for n in w.rooms
                  if n not in _NO_EXIT_LINE and not n.startswith("OPEN-OCEAN-"))


def _leads_somewhere(room, direction):
    """Highest rolls, so a random refusal (the Ghost's Room) doesn't count."""
    import io, contextlib
    from unittest.mock import patch
    w, _ = _make_world()
    w.move_object(w.player, w.rooms[room])
    w.here = w.rooms[room]
    with contextlib.redirect_stdout(io.StringIO()), \
            patch("random.randint", side_effect=lambda lo, hi: hi):
        dest, _msg = w.rooms[room].exits[direction].resolve(w)
    return dest is not None


@pytest.mark.parametrize("room", _all_rooms())
def test_every_room_names_its_usable_exits(room):
    import re
    w, _, out = _look(room)
    text = out.lower()
    missing = [d for d in w.rooms[room].exits
               if _leads_somewhere(room, d)
               and not re.search(_DIRECTION_WORDS.get(d, re.escape(d)), text)]
    assert not missing, f"{room}: the description never names {missing}"


# --- The reverse: every direction a room's text names is a way, or has its own
# refusal (never the generic one), or is a listed descriptive mention.

_GENERIC_REFUSAL = "You can't go that way."
_COMPASS = ("northeast", "northwest", "southeast", "southwest", "north", "south", "east", "west")
_DESCRIPTIVE = {
    ("ALLEY", "west"): "'Main West' is the street's name",
    ("BEEKEEPERS-COTTAGE", "south"): "the south wall",
    ("FLOODING-ROOM", "north"): "the levers on the north wall",
    ("CASINO-CORNER", "northwest"): "the tavern's northwest corner",
    ("WHITE-HOUSE", "west"): "'west of a white house' — the opening",
}
_CANT_STAY = {"SWARM-TREE": "the swarm drives you off without the smoke jar (tested above)"}


def _refusal(room, direction):
    """What trying `direction` here says, or None if it leads somewhere."""
    import io, contextlib
    from unittest.mock import patch
    w, _ = _make_world()
    w.move_object(w.player, w.rooms[room])
    w.here = w.rooms[room]
    exit_ = w.rooms[room].exits.get(direction)
    if exit_ is None:
        return _GENERIC_REFUSAL
    out = io.StringIO()
    with contextlib.redirect_stdout(out), \
            patch("random.randint", side_effect=lambda lo, hi: hi):
        dest, msg = exit_.resolve(w)
    return None if dest is not None else (msg or out.getvalue().strip())


def _reverse_rooms():
    w, _ = _make_world()
    return sorted(n for n in w.rooms if n not in _CANT_STAY and not n.startswith("OPEN-OCEAN-"))


@pytest.mark.parametrize("room", _reverse_rooms())
def test_every_direction_named_is_a_way_or_refused(room):
    import re
    _, _, out = _look(room)
    text = out.split("\n", 1)[-1].lower()            # the room's text, not its title
    named = {d for d in _COMPASS if re.search(rf"\b{d}(ward)?\b", text)}
    generic = [d for d in sorted(named)
               if (room, d) not in _DESCRIPTIVE
               and (_refusal(room, d) or "").strip() == _GENERIC_REFUSAL]
    assert not generic, f"{room}: names {generic} but going there says {_GENERIC_REFUSAL!r}"


def test_the_new_refusals():
    from content.rooms import ALLEY_NORTH, BACK_ALLEY_SOUTH, SEA_WEST_NORTH
    from content.upper_tier import STORAGE_EAST
    from content.aqueduct import CHANNEL_ENDS
    from content.mid_tier import CREVICE_EAST
    for room, d, line in (("ALLEY", "north", ALLEY_NORTH), ("BACK-ALLEY", "south", BACK_ALLEY_SOUTH),
                          ("SEA-WEST", "north", SEA_WEST_NORTH), ("STORAGE-AREA", "east", STORAGE_EAST),
                          ("COLLAPSED-AQUEDUCT", "east", CHANNEL_ENDS),
                          ("COLLAPSED-AQUEDUCT", "west", CHANNEL_ENDS), ("THE-CREVICE", "east", CREVICE_EAST)):
        w, g, _ = _look(room)
        assert line in _do(g, d)
        assert w.here.name == room


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
