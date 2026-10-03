"""
Room definitions for Roundabout: The God-Forsaken Ring.
Sourced from AWT_story_line/locations.md.
Built incrementally — rooms added as walkthrough sections require them.
"""

from __future__ import annotations
import random
from engine.world import Room, Exit, ONBIT, RLANDBIT


def make_rooms(world) -> None:
    _make_opening(world)
    _make_tower(world)
    _make_tale_and_ale(world)
    _make_town(world)
    _make_volcano(world)
    _make_west_town(world)
    _make_mine(world)
    _make_beach_and_sea(world)
    _make_kevrys_island(world)


# ---------------------------------------------------------------------------
# Opening area
# ---------------------------------------------------------------------------

def _make_opening(world) -> None:
    r = Room(
        name="WHITE-HOUSE",
        desc="West of House",
        ldesc=(
            "You are standing in an open field west of a white house, "
            "with a boarded front door.\n"
            "There is a small mailbox here."
        ),
        value=1,
    )
    r.set_flag(ONBIT)
    r.set_flag(RLANDBIT)
    r.global_objects = ["MAILBOX-WHITE-HOUSE"]
    world.register_room(r)


# ---------------------------------------------------------------------------
# Will's Wizard Tower
# ---------------------------------------------------------------------------

def _make_tower(world) -> None:
    main = Room(
        name="WIZARDS-TOWER",
        desc="Will's Wizard Tower",
        ldesc=(
            "The tower doesn't announce itself. It simply is — books, firelight, "
            "the low hum of something you can't quite locate. A desk dominates one "
            "end, buried under papers that somehow manage to look organized. A "
            "painting hangs on the wall, slightly crooked. The room has the feeling "
            "of a place where important things happen without any particular fuss."
        ),
        value=1,
    )
    main.set_flag(ONBIT)
    main.global_objects = ["PAINTING", "MAILBOX-TOWER"]
    world.register_room(main)

    bedroom = Room(
        name="WIZARDS-BEDROOM",
        desc="Will Passion's Bedroom",
        ldesc=(
            "This is, apparently, where the magic happens. The bedroom is smaller "
            "than the main room and considerably more honest about its occupant.\n"
            "Books here are not organized — they are stacked, wedged, balanced, "
            "and in at least one case load-bearing.\n"
            "A narrow bed sits against the far wall, made with the perfunctory "
            "neatness of someone who knows they'll be up again soon.\n"
            "A nightstand holds a pair of wire-rimmed glasses, a half-melted "
            "candle, and a ring left by a cup that was never there long enough "
            "to matter.\n"
            "The rest of the room is Will's business and clearly has been for "
            "a very long time."
        ),
        value=1,
    )
    bedroom.set_flag(ONBIT)
    bedroom.exits["south"] = Exit(destination="WIZARDS-TOWER")
    bedroom.global_objects = ["ENCHANTED-GLASSES", "PAINTING"]
    world.register_room(bedroom)

    # North exit is perception-gated; condition checks world global set by room action
    main.exits["north"] = Exit(
        destination="WIZARDS-BEDROOM",
        condition=lambda w: bool(w.get_global("BEDROOM-DOOR-VISIBLE")),
        fail_message="You can't go that way.",
        message="You push open the bedroom door and step inside.",
    )

    from engine.game import M_NOT_HANDLED, M_ENTER, M_END
    from content.perception import EASY

    def tower_action(w, msg=M_NOT_HANDLED):
        if msg == M_END:
            from content.will import glasses_seen
            glasses_seen(w)
            return M_NOT_HANDLED
        if msg == M_ENTER:
            # Silent Easy perception check fires every visit until bedroom found
            if not w.get_global("BEDROOM-DOOR-VISIBLE"):
                from content.player import check_perception
                if check_perception(w, EASY):
                    w.set_global("BEDROOM-DOOR-VISIBLE", True)
                    print("You notice a door to the north you hadn't seen before.")
        return M_NOT_HANDLED

    main.action = tower_action


# ---------------------------------------------------------------------------
# Tale and Ale (Main Room only — enough for the painting portal landing)
# ---------------------------------------------------------------------------

def _make_tale_and_ale(world) -> None:
    main = Room(
        name="TALE-AND-ALE",
        desc="Tale and Ale — Main Room",
        ldesc=(
            "The Tale and Ale announces itself with warmth before you're fully "
            "through the door — woodsmoke, something cooking, the low sound "
            "of people who have decided their evening is going well.\n"
            "Tables fill most of the floor, a mix of occupied and merely claimed. "
            "The bar is south. A staircase climbs to the upper floor. A mailbox "
            "sits near the door, entirely out of place and acknowledged by no one."
        ),
        value=1,
    )
    main.set_flag(ONBIT)
    main.set_flag(RLANDBIT)
    main.global_objects = ["MAILBOX-TOWER"]
    world.register_room(main)

    bar = Room(
        name="BAR",
        desc="Bar",
        ldesc=(
            "The bar runs the length of the south wall — solid oak, worn smooth "
            "at the elbows. Bottles line the shelf behind it in an arrangement "
            "that suggests a system only May understands.\n"
            "She works the bar with the efficiency of someone who has answered "
            "every question before and will answer them all again without complaint.\n"
            "A board on the wall to one side holds notices. The kitchen is further south."
        ),
        value=1,
    )
    bar.set_flag(ONBIT)
    world.register_room(bar)
    from content.tavern import bar_action
    bar.action = bar_action

    kitchen = Room(
        name="KITCHEN",
        desc="Kitchen",
        ldesc=(
            "The kitchen is warm and loud in the way that working kitchens are — "
            "pots, fire, the particular authority of someone who knows exactly what "
            "they're doing.\n"
            "Shamus moves through it without wasted motion, cooking and selling in "
            "equal measure — if you need something, he's worth asking.\n"
            "Dried herbs hang from the ceiling in loose bundles."
        ),
        value=1,
    )
    kitchen.set_flag(ONBIT)
    world.register_room(kitchen)

    pipe_room = Room(
        name="PIPE-ROOM",
        desc="Pipe Room",
        ldesc=(
            "The pipe room is quieter than the rest of the tavern, which appears "
            "to be the point.\n"
            "A few low chairs, a side table, the particular haze of an evening's "
            "worth of smoke that has nowhere urgent to be."
        ),
        value=1,
    )
    pipe_room.set_flag(ONBIT)
    world.register_room(pipe_room)

    # Wire exits after all rooms registered
    main.exits["south"] = Exit(destination="BAR")
    main.exits["east"]  = Exit(destination="PIPE-ROOM")
    bar.exits["north"]  = Exit(destination="TALE-AND-ALE")
    bar.exits["south"]  = Exit(destination="KITCHEN")
    kitchen.exits["north"] = Exit(destination="BAR")
    pipe_room.exits["west"] = Exit(destination="TALE-AND-ALE")


# ---------------------------------------------------------------------------
# Town — overworld from Tale and Ale to Docks
# ---------------------------------------------------------------------------

def _make_town(world) -> None:
    town_sq = Room(
        name="TOWN-SQUARE",
        desc="Roundabout Town Square",
        ldesc="",   # stateful — see town_square_action
        value=1,
    )
    town_sq.set_flag(ONBIT)
    town_sq.set_flag(RLANDBIT)
    world.register_room(town_sq)

    # locations.md — Town Square: fountain and statue states are independent
    _SQUARE_BASE = (
        "The square is the kind of place a town organizes itself around "
        "without quite deciding to. Cobblestones, worn smooth at the center.\n"
        "The Town Hall anchors the north end with the authority of a building "
        "that has never doubted its own importance. The tavern faces it from "
        "the south, which seems about right."
    )
    _FOUNTAIN_DRY = (
        "A fountain stands in the middle — dry, the basin cracked at one edge, "
        "the stonework patient in the way of things that have been waiting a "
        "long time."
    )
    _FOUNTAIN_RUNNING = (
        "The fountain has been running long enough now that people have "
        "stopped remarking on it. The square sounds different with water in it."
    )
    _STATUE = {
        "unexamined": (
            "A stone statue stands to one side — a civic figure of some kind, "
            "the plaque below it worn to illegibility."
        ),
        "examined": (
            "A stone statue stands to one side. The plaque below it is worn to "
            "illegibility, but the base has a seam around it — visible now that "
            "you're looking. Something with leverage could open it."
        ),
        "looted": (
            "The statue stands to one side, its base pried open and empty. "
            "Whatever was inside is gone."
        ),
    }

    from engine.game import M_NOT_HANDLED, M_HANDLED, M_LOOK

    def town_square_action(w, msg=M_NOT_HANDLED):
        if msg != M_LOOK:
            return M_NOT_HANDLED
        print(_SQUARE_BASE)
        print(_FOUNTAIN_RUNNING if w.get_global("FOUNTAIN-RUNNING") else _FOUNTAIN_DRY)
        if w.get_global("STATUE-LOOTED"):
            print(_STATUE["looted"])
        elif w.get_global("STATUE-EXAMINED"):
            print(_STATUE["examined"])
        else:
            print(_STATUE["unexamined"])
        return M_HANDLED

    town_sq.action = town_square_action

    main_east = Room(
        name="MAIN-EAST",
        desc="Main East",
        ldesc=(
            "Main Street ends here, or nearly does. The buildings thin out toward "
            "the east — a few shuttered fronts, a sign that's lost its lettering, "
            "the church standing apart to the south as though it chose its distance "
            "deliberately. The wasteland begins where the cobblestones stop."
        ),
        value=1,
    )
    main_east.set_flag(ONBIT)
    main_east.set_flag(RLANDBIT)
    world.register_room(main_east)

    wasteland = Room(
        name="ROUNDABOUT-WASTELAND",
        desc="Roundabout Wasteland",
        ldesc=(
            "The wasteland sits at the edge of Roundabout like an embarrassing "
            "relative. Something went very wrong here, and not recently.\n"
            "The ground doesn't grow anything. The structures that remain are shells. "
            "Whatever happened, it happened thoroughly.\n"
            "To the south, a volcano rises against the sky — large, dark, and "
            "entirely convincing."
        ),
        value=1,
    )
    wasteland.set_flag(ONBIT)
    wasteland.set_flag(RLANDBIT)
    world.register_room(wasteland)

    beach_road = Room(
        name="BEACH-ROAD",
        desc="Beach Road",
        ldesc=(
            "A road that forks — south toward Roundabout Beach, north toward "
            "Roundabout Forest via The Old Oak."
        ),
        value=1,
    )
    beach_road.set_flag(ONBIT)
    beach_road.set_flag(RLANDBIT)
    world.register_room(beach_road)

    old_oak = Room(
        name="OLD-OAK",
        desc="The Old Oak",
        ldesc="",   # stateful (kite) — content/old_oak.py
        value=1,
    )
    old_oak.set_flag(ONBIT)
    old_oak.set_flag(RLANDBIT)
    world.register_room(old_oak)

    r_forest = Room(
        name="ROUNDABOUT-FOREST",
        desc="Roundabout Forest",
        ldesc=(
            "You wouldn't know, walking through here, that the ground beneath you "
            "is hollow. The forest is peaceful — birdsong, dappled light, the smell "
            "of pine.\n"
            "The mine entrance sits somewhere among the roots and undergrowth, easy "
            "to miss if you don't know to look.\n"
            "A stone shrine stands at the edge of the trees — old enough that the "
            "forest has started to take it back. A carved pedestal, still solid.\n"
            "On it, the remains of a ceramic bowl, smashed at some point and not "
            "recently. Three or four pieces visible here; others have clearly gone "
            "elsewhere.\n"
            "The symbol on the pedestal is a sprouting seed inside a circle of leaves."
        ),
        value=1,
    )
    r_forest.set_flag(ONBIT)
    r_forest.set_flag(RLANDBIT)
    world.register_room(r_forest)

    roundabout_beach = Room(
        name="ROUNDABOUT-BEACH",
        desc="Roundabout Beach",
        ldesc=(
            "Roundabout Beach opens up as the town falls behind you — a generous "
            "sweep of sand, the water catching whatever light the sky offers. The "
            "docks stretch east to where the Pie Rat Ship is moored, close enough "
            "to read the name on its hull."
        ),
        value=1,
    )
    roundabout_beach.set_flag(ONBIT)
    roundabout_beach.set_flag(RLANDBIT)
    world.register_room(roundabout_beach)

    docks = Room(
        name="DOCKS",
        desc="The Docks",
        ldesc=(
            "The boards flex slightly underfoot, worn smooth by years of boots "
            "and cargo. Bollards thick with rope line the edge. A coil of rope "
            "sits loose on the nearest bollard. The Pie Rat Ship sits in her "
            "berth like she owns it."
        ),
        value=1,
    )
    docks.set_flag(ONBIT)
    docks.set_flag(RLANDBIT)
    world.register_room(docks)

    lighthouse = Room(
        name="LIGHTHOUSE",
        desc="The Lighthouse",
        ldesc=(
            "The keeper's room is small and round, the walls curving with the "
            "tower. A narrow stair spirals up toward the lamp. A desk sits under "
            "the one window, papers stacked with more care than anything else in "
            "the room — whoever works here left in the middle of something and "
            "meant to come back."
        ),
        value=1,
    )
    lighthouse.set_flag(ONBIT)
    lighthouse.set_flag(RLANDBIT)
    world.register_room(lighthouse)

    # Wire town exits
    # Town Square: south→Tale and Ale, east→Main East, west→Main West (not yet built)
    town_sq.exits["south"] = Exit(destination="TALE-AND-ALE")
    town_sq.exits["east"]  = Exit(destination="MAIN-EAST")
    main_east.exits["west"] = Exit(destination="TOWN-SQUARE")
    main_east.exits["east"] = Exit(destination="ROUNDABOUT-WASTELAND")
    wasteland.exits["west"] = Exit(destination="MAIN-EAST")
    wasteland.exits["east"] = Exit(destination="BEACH-ROAD")
    beach_road.exits["west"]  = Exit(destination="ROUNDABOUT-WASTELAND")
    beach_road.exits["south"] = Exit(destination="ROUNDABOUT-BEACH")
    beach_road.exits["north"] = Exit(destination="OLD-OAK")
    old_oak.exits["south"] = Exit(destination="BEACH-ROAD")
    old_oak.exits["west"]  = Exit(destination="BEEKEEPERS-COTTAGE")
    old_oak.exits["east"]  = Exit(destination="SWARM-TREE")
    old_oak.exits["north"] = Exit(destination="ROUNDABOUT-FOREST")
    r_forest.exits["south"] = Exit(destination="OLD-OAK")
    roundabout_beach.exits["north"] = Exit(destination="BEACH-ROAD")
    roundabout_beach.exits["east"]  = Exit(destination="DOCKS")
    roundabout_beach.exits["northeast"] = Exit(destination="LIGHTHOUSE")
    lighthouse.exits["southwest"] = Exit(destination="ROUNDABOUT-BEACH")
    docks.exits["west"] = Exit(destination="ROUNDABOUT-BEACH")

    cottage = Room(
        name="BEEKEEPERS-COTTAGE",
        desc="Beekeeper's Cottage",
        ldesc=(
            "A low wooden cottage sits at the edge of the trees, almost part of "
            "the forest. Stacked hive boxes line the south wall, painted in fading "
            "colours. The smell of beeswax and woodsmoke is pleasant in a specific, "
            "unhurried way. The beekeeper is here — a broad woman with patience in "
            "her posture and a concerning number of sting marks on her forearms."
        ),
        value=1,
    )
    swarm_tree = Room(
        name="SWARM-TREE",
        desc="Swarm Tree",
        ldesc=(
            "A broad-trunked tree at the forest edge, older than the others around "
            "it. A low drone comes from a dark gap in the bark at chest height. The "
            "air nearby has a quality that suggests strongly you should not approach "
            "without a plan."
        ),
        value=1,
    )
    for r in (cottage, swarm_tree):
        r.set_flag(ONBIT)
        r.set_flag(RLANDBIT)
        world.register_room(r)
    cottage.exits["east"]    = Exit(destination="OLD-OAK")
    swarm_tree.exits["west"] = Exit(destination="OLD-OAK")

    from content import old_oak as _oak
    old_oak.action    = _oak.oak_action
    cottage.action    = _oak.cottage_action
    swarm_tree.action = _oak.swarm_action
    r_forest.action   = _oak.forest_action

    # Tale and Ale: north→Town Square (east→Pipe Room already wired in _make_tale_and_ale)
    world.rooms["TALE-AND-ALE"].exits["north"] = Exit(destination="TOWN-SQUARE")


# ---------------------------------------------------------------------------
# Volcano & Pyronicus's Forge
# ---------------------------------------------------------------------------

_VOLCANO_LDESC = (
    "The volcano fills the sky above you — black rock streaked with old flows, "
    "a thread of smoke rising from the summit, heat rolling down the slope in "
    "slow waves. It is large, dark, and entirely convincing. There is no way in "
    "that you can see."
)

_VOLCANO_STAIRS = (
    "Something about the heat is wrong — it rises, but it doesn't burn. Where "
    "the rock meets the ground, an uneven staircase leads down into the dark."
)


def _make_volcano(world) -> None:
    from engine.game import M_NOT_HANDLED, M_HANDLED, M_ENTER, M_LOOK
    from content.perception import HARD, reveal_exit_if_found

    volcano = Room(name="VOLCANO", desc="The Volcano", ldesc="", value=1)
    volcano.set_flag(ONBIT)
    volcano.set_flag(RLANDBIT)
    world.register_room(volcano)

    forge = Room(
        name="PYRONICUS-FORGE",
        desc="Pyronicus's Forge",
        ldesc=(
            "The room is large enough that the walls at the far end are "
            "suggestion rather than certainty.\n"
            "Obsidian everywhere — floor, walls, ceiling — smooth and black and "
            "catching the forge light in brief amber before giving it back to "
            "the dark.\n"
            "The forge itself dominates the center: enormous, ancient, burning "
            "with the steady purpose of something that has never been allowed "
            "to go out.\n"
            "The heat it produces rises through the rock above, feeding an "
            "illusion so convincing that even the smoke smells right.\n"
            "Pyronicus built this room first. The volcano came after."
        ),
        value=2,
    )
    forge.set_flag(ONBIT)   # lit by the forge
    world.register_room(forge)

    world.rooms["ROUNDABOUT-WASTELAND"].exits["south"] = Exit(destination="VOLCANO")
    volcano.exits["north"] = Exit(destination="ROUNDABOUT-WASTELAND")
    # Down is hidden until a Hard perception check sees through the illusion
    volcano.exits["down"] = Exit(
        destination="PYRONICUS-FORGE",
        condition=lambda w: bool(w.get_global("VOLCANO-STAIRS-FOUND")),
        fail_message="You can't go that way.",
    )
    forge.exits["up"] = Exit(destination="VOLCANO")

    def volcano_action(w, msg=M_NOT_HANDLED):
        if msg == M_ENTER:
            # Silent check every visit until the staircase is found
            reveal_exit_if_found(w, "VOLCANO", "down", HARD, "VOLCANO-STAIRS-FOUND")
            return M_NOT_HANDLED
        if msg == M_LOOK:
            print(_VOLCANO_LDESC)
            if w.get_global("VOLCANO-STAIRS-FOUND"):
                print(_VOLCANO_STAIRS)
            return M_HANDLED
        return M_NOT_HANDLED

    volcano.action = volcano_action


# ---------------------------------------------------------------------------
# Main West, Archery Range & Viking Encampment
# Trial logic lives in content/vikings.py.
# ---------------------------------------------------------------------------

def _make_west_town(world) -> None:
    from content import vikings

    def room(name, desc, ldesc, value=1):
        r = Room(name=name, desc=desc, ldesc=ldesc, value=value)
        r.set_flag(ONBIT)
        r.set_flag(RLANDBIT)
        world.register_room(r)
        return r

    main_west = room(
        "MAIN-WEST", "Main West",
        "Main Street narrows toward the west end, the buildings pulling back "
        "slightly as if making room for something that never arrived. The "
        "library stands to the north, solid and unhurried. The road continues "
        "west toward the archery range. To the southeast, a gap between "
        "buildings leads into the alley.",
    )
    archery = room(
        "ARCHERY-RANGE", "Archery Range",
        "Straw targets line the far end of a long cleared field, bristling "
        "with arrows. The range is well-used.\n"
        "The Vikings from the encampment to the west use it freely — and "
        "apparently consider the entire field fair game, including the parts "
        "you're standing in.",
    )
    encampment = room(
        "VIKING-ENCAMPMENT", "Viking Encampment",
        "Longhouses ring a wide clearing, smoke rising from their roof-holes. "
        "A banner hangs from a pole near the largest one, its runes stitched "
        "in thread gone dark with weather.\n"
        "Vikings go about their business — mending, sharpening, arguing — and "
        "keep half an eye on you while they do it. Paths lead north to a hut, "
        "south to a ring of stones, and west toward the glow of a fire pit.",
    )
    hut = room(
        "HAALVARS-HUT", "Haalvar's Hut",
        "The hut is close and warm and smells of tallow. In the center sits a "
        "stone carved with runes — solid to the touch, but its surface moves "
        "like dark water, as if something underneath is breathing.",
    )
    circle = room(
        "RITUAL-CIRCLE", "The Ritual Circle",
        "Five rune stones stand in a ring around a carved symbol in the earth: "
        "Earth, Air, Fire, Water, and one marked with a heart. The ground "
        "inside the ring is swept clean.",
    )
    fire_pit = room(
        "FIRE-PIT", "The Fire Pit",
        "A great fire burns in a stone-lined pit, benches drawn up close "
        "around it. Cups, a barrel, and a smell that could strip paint. This "
        "is where the encampment settles its arguments.",
    )

    # Main West: north → Library, southeast → The Alley (not yet built)
    world.rooms["TOWN-SQUARE"].exits["west"] = Exit(destination="MAIN-WEST")
    main_west.exits["east"] = Exit(destination="TOWN-SQUARE")
    main_west.exits["west"] = Exit(destination="ARCHERY-RANGE")

    # The Alley & Back Alley (locations.md). Alley exits go back the way the
    # player came: northeast to Town Square, northwest to Main West.
    alley = room(
        "ALLEY", "The Alley",
        "The gap between buildings is narrow enough that the sky above is just "
        "a strip. Cobblestones give way to packed dirt underfoot. The tavern's "
        "back wall runs along the south side. It smells like kitchen waste and "
        "something less identifiable. Further south, the alley deepens.",
    )
    back_alley = room(
        "BACK-ALLEY", "The Back Alley",
        "Darker than the alley, smaller, and considerably less welcoming. The "
        "tavern's back wall seals the south end. Broken crates and barrels have "
        "accumulated here the way things do when no one is watching. The ground "
        "is stained. The air is close. This is where things happen that don't "
        "happen on Main Street.",
    )
    world.rooms["TOWN-SQUARE"].exits["southwest"] = Exit(destination="ALLEY")
    main_west.exits["southeast"] = Exit(destination="ALLEY")
    alley.exits["northeast"] = Exit(destination="TOWN-SQUARE")
    alley.exits["northwest"] = Exit(destination="MAIN-WEST")
    alley.exits["south"]     = Exit(destination="BACK-ALLEY")
    back_alley.exits["north"] = Exit(destination="ALLEY")
    from content.back_alley import back_alley_action
    back_alley.action = back_alley_action
    # Archery Range: north → Roundabout Pond (not yet built)
    archery.exits["east"] = Exit(destination="MAIN-WEST")
    archery.exits["west"] = Exit(destination="VIKING-ENCAMPMENT")
    encampment.exits["east"]  = Exit(destination="ARCHERY-RANGE")
    encampment.exits["north"] = Exit(destination="HAALVARS-HUT")
    encampment.exits["south"] = Exit(destination="RITUAL-CIRCLE")
    encampment.exits["west"]  = Exit(destination="FIRE-PIT")
    hut.exits["south"]      = Exit(destination="VIKING-ENCAMPMENT")
    circle.exits["north"]   = Exit(destination="VIKING-ENCAMPMENT")
    fire_pit.exits["east"]  = Exit(destination="VIKING-ENCAMPMENT")

    _make_pond_and_bog(world, archery)

    archery.action    = vikings.archery_action
    encampment.action = vikings.encampment_action
    hut.action        = vikings.hut_action


# ---------------------------------------------------------------------------
# Roundabout Pond & the Bog of Eternal Stench (locations.md)
# All four bog rooms share one player-facing title; SE/NE/SW/NW are internal.
# ---------------------------------------------------------------------------

_BOG_TITLE = "The Bog of Eternal Stench"


def _make_pond_and_bog(world, archery) -> None:
    def room(name, desc, ldesc):
        r = Room(name=name, desc=desc, ldesc=ldesc, value=1)
        r.set_flag(ONBIT)
        r.set_flag(RLANDBIT)
        world.register_room(r)
        return r

    pond = room(
        "ROUNDABOUT-POND", "Roundabout Pond",
        "The pond is easy to walk past without noticing. It sits low between the "
        "town path and the bog, ringed with reeds and the occasional frog. The "
        "water is dark and calm.",
    )
    bog_se = room(
        "BOG-SE", _BOG_TITLE,
        "The bog stretches in every direction, dark water between clumps of "
        "soggy earth. The smell is comprehensive and personal. Reeds crowd the "
        "edges of every dry patch. Something is moving just out of sight, or was.",
    )
    bog_ne = room(
        "BOG-NE", _BOG_TITLE,
        "The ground here is technically solid. Technically. Dark water pools "
        "between tufts of coarse grass. The smell has layers. You have stopped "
        "trying to identify them, and don't really want to.",
    )
    bog_sw = room(
        "BOG-SW", _BOG_TITLE,
        "A flat expanse of bog, grey-green and indifferent. The water is still "
        "except where it isn't. The smell arrived before you did and will be "
        "here long after you leave.",
    )
    bog_nw = room(
        "BOG-NW", _BOG_TITLE,
        "The reeds are taller here, crowding in from the edges. The water is "
        "darker. The smell is worse. This part of the bog feels less visited, "
        "which is saying something.",
    )

    archery.exits["north"] = Exit(destination="ROUNDABOUT-POND")
    pond.exits["south"] = Exit(destination="ARCHERY-RANGE")
    pond.exits["west"]  = Exit(destination="BOG-SE")
    # 2×2 grid, diagonals allowed. Bog-SE south → Dankhaus: built with H2.
    bog_se.exits.update(east=Exit(destination="ROUNDABOUT-POND"), north=Exit(destination="BOG-NE"),
                        west=Exit(destination="BOG-SW"), northwest=Exit(destination="BOG-NW"))
    bog_ne.exits.update(south=Exit(destination="BOG-SE"), west=Exit(destination="BOG-NW"),
                        southwest=Exit(destination="BOG-SW"))
    bog_sw.exits.update(east=Exit(destination="BOG-SE"), north=Exit(destination="BOG-NW"),
                        northeast=Exit(destination="BOG-NE"))
    bog_nw.exits.update(east=Exit(destination="BOG-NE"), south=Exit(destination="BOG-SW"),
                        southeast=Exit(destination="BOG-SE"))

    from engine.game import M_NOT_HANDLED, M_ENTER

    def bog_sw_action(w, msg=M_NOT_HANDLED):
        if msg == M_ENTER:
            # Shrine bowl piece — Easy perception, every visit until found
            from content.perception import EASY, reveal_if_found
            reveal_if_found(w, "BOWL-PIECE-BOG", EASY)
        return M_NOT_HANDLED

    bog_sw.action = bog_sw_action


# ---------------------------------------------------------------------------
# Mine — Pie Rats Mining Inc.
# ---------------------------------------------------------------------------

def _make_mine(world) -> None:
    mine_entrance = Room(
        name="MINE-ENTRANCE",
        desc="Mine Entrance",
        ldesc=(
            "The entrance to Pie Rats Mining Inc. is a ragged wound in the earth, "
            "shored up with timber and optimism. A sign above the opening reads: "
            "PIE RATS MINING INC. — AUTHORIZED PERSONNEL ONLY."
        ),
        value=1,
    )
    mine_entrance.set_flag(ONBIT)
    world.register_room(mine_entrance)

    main_shaft = Room(
        name="MAIN-SHAFT",
        desc="Main Shaft",
        ldesc=(
            "The main shaft drops away from the entrance in a single rough-cut "
            "passage, wide enough for two men and a cart. Timber supports run at "
            "intervals. The smell of rock dust and old torchsmoke is thick here."
        ),
        value=1,
    )
    main_shaft.set_flag(ONBIT)
    world.register_room(main_shaft)

    assay_room = Room(
        name="ASSAY-ROOM",
        desc="Assay Room",
        ldesc=(
            "A side room off the main shaft, fitted out for testing ore samples. "
            "A long workbench runs the length of one wall, scarred with acid burns "
            "and impact marks. The far wall has a gap in it that doesn't look "
            "entirely accidental."
        ),
        value=1,
    )
    assay_room.set_flag(ONBIT)
    world.register_room(assay_room)

    mine_tunnels = Room(
        name="MINE-TUNNELS",
        desc="Mine Tunnels",
        ldesc=(
            "The working tunnels branch off the main shaft. Torch sconces are fixed "
            "to the walls at intervals — the torches in them are real and lit. "
            "The floor is rutted with cart tracks."
        ),
        value=1,
    )
    mine_tunnels.set_flag(ONBIT)
    world.register_room(mine_tunnels)

    rats_nest = Room(
        name="RATS-NEST",
        desc="The Rat's Nest",
        ldesc=(
            "A widening in the tunnel that someone has decided is a room. Crates "
            "and barrels are stacked with more care than the surroundings suggest — "
            "this is storage, not clutter. The Pie Rats keep their surplus here."
        ),
        value=1,
    )
    rats_nest.set_flag(ONBIT)
    world.register_room(rats_nest)

    # Wire mine exits
    world.rooms["ROUNDABOUT-FOREST"].exits["down"] = Exit(destination="MINE-ENTRANCE")
    mine_entrance.exits["up"]   = Exit(destination="ROUNDABOUT-FOREST")
    mine_entrance.exits["down"] = Exit(destination="MAIN-SHAFT")
    main_shaft.exits["up"]    = Exit(destination="MINE-ENTRANCE")
    main_shaft.exits["south"] = Exit(destination="ASSAY-ROOM")
    main_shaft.exits["down"]  = Exit(destination="MINE-TUNNELS")
    assay_room.exits["north"] = Exit(destination="MAIN-SHAFT")
    mine_tunnels.exits["up"]    = Exit(destination="MAIN-SHAFT")
    mine_tunnels.exits["north"] = Exit(destination="RATS-NEST")
    rats_nest.exits["south"] = Exit(destination="MINE-TUNNELS")

    # Cave-in fires on entry to Mine Entrance or Forest after fuse is lit
    from engine.game import M_NOT_HANDLED, M_ENTER

    def _cave_in_check(w, msg=M_NOT_HANDLED):
        if msg == M_ENTER:
            from content.verbs import _check_mine_cave_in
            _check_mine_cave_in(w)
        return M_NOT_HANDLED

    mine_entrance.action = _cave_in_check
    # Roundabout Forest runs the same check from content/old_oak.forest_action


# ---------------------------------------------------------------------------
# Beach, sea, and Kevry's island
# ---------------------------------------------------------------------------

def _make_beach_and_sea(world) -> None:
    # Pie Rat Ship Deck
    ship_deck = Room(
        name="SHIP-DECK",
        desc="Pie Rat Ship — Deck",
        ldesc=(
            "The deck is cluttered in the way of a working vessel — coils of line, "
            "barrels lashed to the rail, a general smell of fish and salt and "
            "something that has been at sea too long. This is a ship that wants to move."
        ),
        value=1,
    )
    ship_deck.set_flag(ONBIT)
    world.register_room(ship_deck)

    # Sea rooms
    sea_west = Room(
        name="SEA-WEST",
        desc="Western Roundabout Sea",
        ldesc=(
            "The smell of the town still reaches you here — smoke and bread "
            "underneath the salt. The beach stretches behind you, the lighthouse "
            "standing watch to the north. The water is choppier than it looked "
            "from shore."
        ),
        value=1,
    )
    sea_west.set_flag(ONBIT)
    world.register_room(sea_west)

    sea_mid = Room(
        name="SEA-MID",
        desc="Roundabout Sea",
        ldesc=(
            "The coast is gone. There is nothing in any direction but open water "
            "and sky. The sea moves in long slow swells that lift and drop the hull "
            "with a steady indifference. You are very small out here."
        ),
        value=1,
    )
    sea_mid.set_flag(ONBIT)
    world.register_room(sea_mid)

    sea_east = Room(
        name="SEA-EAST",
        desc="Eastern Roundabout Sea",
        ldesc=(
            "Is that — yes. An island. Small, tree-lined, a beach curving around "
            "the side facing you. The water around it is shallow and clear. East "
            "of it, the sea continues without comment."
        ),
        value=1,
    )
    sea_east.set_flag(ONBIT)
    world.register_room(sea_east)

    # 69 Open Ocean rooms
    _OCEAN_DESCS = [
        "Open ocean in every direction. Nothing else.",
        "The ocean does not vary its presentation.",
        "No land. No landmarks. Just the creak of the hull and the indifferent sea.",
        "The ocean offers nothing in any direction. It does not apologize for this.",
        "Sea. Sky. Nothing else to report.",
    ]

    ocean_rooms = []
    for i in range(1, 70):
        oc = Room(
            name=f"OPEN-OCEAN-{i}",
            desc="Open Ocean",
            ldesc=_OCEAN_DESCS[(i - 1) % len(_OCEAN_DESCS)],
            value=0,
        )
        oc.set_flag(ONBIT)
        world.register_room(oc)
        ocean_rooms.append(oc)

    # Desert Island (spur south of sea_east, not on main east axis)
    desert_island = Room(
        name="DESERT-ISLAND",
        desc="Desert Island",
        ldesc=(
            "The sand on the beach is undisturbed. That fact, for some reason, "
            "does not comfort you.\n"
            "Nothing here is threatening and nothing here is welcoming. The island "
            "feels like a place that has been waiting — not for you specifically, "
            "but for someone."
        ),
        value=1,
    )
    desert_island.set_flag(ONBIT)
    desert_island.set_flag(RLANDBIT)
    world.register_room(desert_island)

    # Wire ship and sea exits
    world.rooms["DOCKS"].exits["east"] = Exit(destination="SHIP-DECK")
    ship_deck.exits["west"] = Exit(destination="DOCKS")
    ship_deck.exits["east"] = Exit(destination="SEA-WEST")

    sea_west.exits["west"] = Exit(destination="SHIP-DECK")
    sea_west.exits["east"] = Exit(destination="SEA-MID")
    sea_mid.exits["west"]  = Exit(destination="SEA-WEST")
    sea_mid.exits["east"]  = Exit(destination="SEA-EAST")
    sea_east.exits["west"] = Exit(destination="SEA-MID")
    sea_east.exits["east"] = Exit(destination="OPEN-OCEAN-1")
    sea_east.exits["south"] = Exit(destination="DESERT-ISLAND")
    desert_island.exits["north"] = Exit(destination="SEA-EAST")

    # Chain ocean rooms east/west
    for idx, oc in enumerate(ocean_rooms):
        if idx == 0:
            oc.exits["west"] = Exit(destination="SEA-EAST")
        else:
            oc.exits["west"] = Exit(destination=ocean_rooms[idx - 1].name)
        if idx < len(ocean_rooms) - 1:
            oc.exits["east"] = Exit(destination=ocean_rooms[idx + 1].name)
        # Square 69 east exit → Land, Ho! (wired after that room is registered)


def _make_kevrys_island(world) -> None:
    land_ho = Room(
        name="LAND-HO",
        desc="Land, Ho!",
        ldesc=(
            "The island resolves out of the horizon slowly, then all at once. "
            "Sand, trees, solid ground. You've earned this. The beach curves "
            "invitingly ahead."
        ),
        value=5,
    )
    land_ho.set_flag(ONBIT)
    land_ho.set_flag(RLANDBIT)
    world.register_room(land_ho)

    empty_beach = Room(
        name="EMPTY-BEACH",
        desc="Empty Beach",
        ldesc=(
            "The beach is long and quiet, the sand unmarked. A line of scrubby "
            "trees runs along the inland edge. Somewhere beyond them, half-hidden, "
            "a small structure."
        ),
        value=5,
    )
    empty_beach.set_flag(ONBIT)
    empty_beach.set_flag(RLANDBIT)
    world.register_room(empty_beach)

    kevry_house = Room(
        name="KEVRYS-HOUSE",
        desc="A House",
        ldesc=(
            "The interior is cluttered in the way that only makes sense to its "
            "owner. Charts pinned to every surface, ropes coiled with obsessive "
            "care, a hammock in the corner."
        ),
        value=5,
    )
    kevry_house.set_flag(ONBIT)
    world.register_room(kevry_house)

    captains_quarters = Room(
        name="CAPTAINS-QUARTERS",
        desc="Captain's Quarters",
        ldesc=(
            "A small back room, all table and charts and the smell of ink. "
            "A weathered man sits hunched over a map, muttering."
        ),
        value=5,
    )
    captains_quarters.set_flag(ONBIT)
    world.register_room(captains_quarters)

    # Wire Kevry's island exits
    world.rooms["OPEN-OCEAN-69"].exits["east"] = Exit(destination="LAND-HO")
    land_ho.exits["west"]  = Exit(destination="OPEN-OCEAN-69")
    land_ho.exits["east"]  = Exit(destination="EMPTY-BEACH")
    empty_beach.exits["west"] = Exit(destination="LAND-HO")
    empty_beach.exits["east"] = Exit(destination="KEVRYS-HOUSE")
    kevry_house.exits["west"] = Exit(destination="EMPTY-BEACH")
    kevry_house.exits["east"] = Exit(destination="CAPTAINS-QUARTERS")
    captains_quarters.exits["west"] = Exit(destination="KEVRYS-HOUSE")
