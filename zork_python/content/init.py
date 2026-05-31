"""
World initialization for Zork I.

Creates the player, places all objects in their initial locations, sets up
all global state flags, and registers verb handlers.  Call
initialize_world(world, game) once at startup before running the game loop.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from engine.world import GameObject, INVISIBLE, ACTORBIT, SACREDBIT, ONBIT, TAKEBIT, NDESCBIT, CONTBIT, OPENBIT

if TYPE_CHECKING:
    from engine.game import Game
    from engine.world import World


def initialize_world(world: "World", game: "Game") -> None:
    """
    Populate world with all rooms, objects, and initial state.

    Call order:
      1. Register objects (make_objects)
      2. Register rooms (make_rooms)
      3. Place objects
      4. Create and place player
      5. Initialize global flags
      6. Register verb handlers
    """
    from content.objects import make_objects
    from content.rooms import make_rooms
    from content.verbs import register_verbs
    from content.actions import i_lantern, i_thief, i_maint_room, i_river

    make_objects(world)
    make_rooms(world)

    _place_objects(world)
    _create_player(world)
    _init_globals(world)
    register_verbs(game)
    _init_clock(world, game, i_lantern, i_thief, i_maint_room, i_river)


# ---------------------------------------------------------------------------
# Object placement (ZIL (IN ...) clauses)
# ---------------------------------------------------------------------------

def _place_objects(world: "World") -> None:
    """Move every object to its initial location per 1dungeon.zil."""

    def mv(obj_name: str, loc_name: str) -> None:
        obj = world.objects.get(obj_name)
        if obj is None:
            return
        room = world.rooms.get(loc_name)
        if room is not None:
            world.move_object(obj, room)
            return
        container = world.objects.get(loc_name)
        if container is not None:
            world.move_object(obj, container)

    # Objects that start in LOCAL-GLOBALS (scenery, no placement needed):
    # BOARD, SONGBIRD, WHITE-HOUSE, FOREST, TREE, GLOBAL-WATER, KITCHEN-WINDOW,
    # CHIMNEY, SLIDE, LADDER
    # Objects that start in GLOBAL-OBJECTS (global scenery, no placement):
    # TEETH, WALL, GRANITE-WALL

    # MOUNTAIN-RANGE in MOUNTAINS
    mv("MOUNTAIN-RANGE", "MOUNTAINS")

    # GHOSTS in ENTRANCE-TO-HADES
    mv("GHOSTS", "ENTRANCE-TO-HADES")

    # SKULL in LAND-OF-LIVING-DEAD
    mv("SKULL", "LAND-OF-LIVING-DEAD")

    # LOWERED-BASKET in LOWER-SHAFT
    mv("LOWERED-BASKET", "LOWER-SHAFT")

    # RAISED-BASKET in SHAFT-ROOM
    mv("RAISED-BASKET", "SHAFT-ROOM")

    # BAT in BAT-ROOM
    mv("BAT", "BAT-ROOM")

    # BELL in NORTH-TEMPLE
    mv("BELL", "NORTH-TEMPLE")

    # AXE in TROLL (troll's inventory)
    mv("AXE", "TROLL")

    # BOLT in DAM-ROOM
    mv("BOLT", "DAM-ROOM")

    # BUBBLE in DAM-ROOM
    mv("BUBBLE", "DAM-ROOM")

    # ALTAR in SOUTH-TEMPLE
    mv("ALTAR", "SOUTH-TEMPLE")

    # BOOK in ALTAR
    mv("BOOK", "ALTAR")

    # SCEPTRE in COFFIN
    mv("SCEPTRE", "COFFIN")

    # TIMBERS in TIMBER-ROOM
    mv("TIMBERS", "TIMBER-ROOM")

    # KITCHEN-TABLE in KITCHEN
    mv("KITCHEN-TABLE", "KITCHEN")

    # ATTIC-TABLE in ATTIC
    mv("ATTIC-TABLE", "ATTIC")

    # SANDWICH-BAG in KITCHEN-TABLE (initially on table)
    mv("SANDWICH-BAG", "KITCHEN-TABLE")

    # LUNCH in SANDWICH-BAG
    mv("LUNCH", "SANDWICH-BAG")

    # TOOL-CHEST in MAINTENANCE-ROOM
    mv("TOOL-CHEST", "MAINTENANCE-ROOM")

    # YELLOW-BUTTON in MAINTENANCE-ROOM
    mv("YELLOW-BUTTON", "MAINTENANCE-ROOM")

    # BROWN-BUTTON in MAINTENANCE-ROOM
    mv("BROWN-BUTTON", "MAINTENANCE-ROOM")

    # RED-BUTTON in MAINTENANCE-ROOM
    mv("RED-BUTTON", "MAINTENANCE-ROOM")

    # BLUE-BUTTON in MAINTENANCE-ROOM
    mv("BLUE-BUTTON", "MAINTENANCE-ROOM")

    # TROPHY-CASE in LIVING-ROOM
    mv("TROPHY-CASE", "LIVING-ROOM")

    # RUG in LIVING-ROOM
    mv("RUG", "LIVING-ROOM")

    # TRAP-DOOR in LIVING-ROOM
    mv("TRAP-DOOR", "LIVING-ROOM")

    # WOODEN-DOOR in LIVING-ROOM
    mv("WOODEN-DOOR", "LIVING-ROOM")

    # SWORD in LIVING-ROOM
    mv("SWORD", "LIVING-ROOM")

    # MAP in TROPHY-CASE
    mv("MAP", "TROPHY-CASE")

    # BOAT-LABEL in INFLATED-BOAT
    mv("BOAT-LABEL", "INFLATED-BOAT")

    # THIEF in ROUND-ROOM
    mv("THIEF", "ROUND-ROOM")

    # LARGE-BAG in THIEF
    mv("LARGE-BAG", "THIEF")

    # STILETTO in THIEF
    mv("STILETTO", "THIEF")

    # PEDESTAL in TORCH-ROOM
    mv("PEDESTAL", "TORCH-ROOM")

    # TORCH in PEDESTAL
    mv("TORCH", "PEDESTAL")

    # GUIDE in DAM-LOBBY
    mv("GUIDE", "DAM-LOBBY")

    # TROLL in TROLL-ROOM
    mv("TROLL", "TROLL-ROOM")

    # TRUNK in RESERVOIR (per ZIL source; INVISIBLE flag set on object)
    mv("TRUNK", "RESERVOIR")

    # TUBE in MAINTENANCE-ROOM
    mv("TUBE", "MAINTENANCE-ROOM")

    # ENGRAVINGS in ENGRAVINGS-CAVE
    mv("ENGRAVINGS", "ENGRAVINGS-CAVE")

    # PAINTING in GALLERY
    mv("PAINTING", "GALLERY")

    # CANDLES in SOUTH-TEMPLE
    mv("CANDLES", "SOUTH-TEMPLE")

    # CHALICE in TREASURE-ROOM (per ZIL source)
    mv("CHALICE", "TREASURE-ROOM")

    # COFFIN in EGYPT-ROOM
    mv("COFFIN", "EGYPT-ROOM")

    # CYCLOPS in CYCLOPS-ROOM
    mv("CYCLOPS", "CYCLOPS-ROOM")

    # DAM in DAM-ROOM
    mv("DAM", "DAM-ROOM")

    # MIRROR-1 in MIRROR-ROOM-1
    mv("MIRROR-1", "MIRROR-ROOM-1")

    # MIRROR-2 in MIRROR-ROOM-2
    mv("MIRROR-2", "MIRROR-ROOM-2")

    # DIAMOND in MACHINE-ROOM (initially absent, added by machine)
    # Leave DIAMOND unplaced - it appears via machine action

    # JADE in BAT-ROOM
    mv("JADE", "BAT-ROOM")

    # KNIFE in ATTIC-TABLE
    mv("KNIFE", "ATTIC-TABLE")

    # BONES in MAZE-5 (per ZIL source)
    mv("BONES", "MAZE-5")

    # BURNED-OUT-LANTERN in MAZE-5
    mv("BURNED-OUT-LANTERN", "MAZE-5")

    # BAG-OF-COINS in MAZE-5
    mv("BAG-OF-COINS", "MAZE-5")

    # LAMP in LIVING-ROOM (on trophy case)
    mv("LAMP", "LIVING-ROOM")

    # EMERALD in BUOY (per ZIL source; BUOY is a container, EMERALD starts inside)
    mv("EMERALD", "BUOY")

    # ADVERTISEMENT in WEST-OF-HOUSE
    mv("ADVERTISEMENT", "WEST-OF-HOUSE")

    # MACHINE in MACHINE-ROOM
    mv("MACHINE", "MACHINE-ROOM")

    # MACHINE-SWITCH in MACHINE-ROOM
    mv("MACHINE-SWITCH", "MACHINE-ROOM")

    # INFLATED-BOAT: unplaced initially (appears when INFLATABLE-BOAT is inflated)
    # mv("INFLATED-BOAT", ...)  — do not place; created by pump action

    # MAILBOX in WEST-OF-HOUSE
    mv("MAILBOX", "WEST-OF-HOUSE")

    # MATCH in DAM-LOBBY (ZIL: (IN DAM-LOBBY))
    mv("MATCH", "DAM-LOBBY")

    # ROPE in ATTIC (ZIL: (IN ATTIC))
    mv("ROPE", "ATTIC")

    # RUSTY-KNIFE in MAZE-5
    mv("RUSTY-KNIFE", "MAZE-5")

    # SAND in SANDY-CAVE
    mv("SAND", "SANDY-CAVE")

    # SCARAB in SANDY-CAVE (invisible)
    mv("SCARAB", "SANDY-CAVE")

    # BRACELET in GAS-ROOM
    mv("BRACELET", "GAS-ROOM")

    # SCREWDRIVER in MAINTENANCE-ROOM
    mv("SCREWDRIVER", "MAINTENANCE-ROOM")

    # KEYS in MAZE-5
    mv("KEYS", "MAZE-5")

    # SHOVEL in SANDY-BEACH
    mv("SHOVEL", "SANDY-BEACH")

    # COAL in DEAD-END-5
    mv("COAL", "DEAD-END-5")

    # LARGE-BAG already placed in THIEF above

    # GRATE in GRATING-CLEARING (invisible until leaves moved)
    mv("GRATE", "GRATING-CLEARING")

    # LEAVES in GRATING-CLEARING
    mv("LEAVES", "GRATING-CLEARING")

    # PUMP in RESERVOIR-NORTH (per ZIL source)
    mv("PUMP", "RESERVOIR-NORTH")

    # BODIES in ENTRANCE-TO-HADES
    mv("BODIES", "ENTRANCE-TO-HADES")

    # INFLATABLE-BOAT in DAM-BASE (per ZIL source)
    mv("INFLATABLE-BOAT", "DAM-BASE")

    # BAR in LOUD-ROOM (with SACREDBIT; removed by echo)
    mv("BAR", "LOUD-ROOM")

    # POT-OF-GOLD in END-OF-RAINBOW (invisible until rainbow)
    mv("POT-OF-GOLD", "END-OF-RAINBOW")

    # PRAYER in NORTH-TEMPLE
    mv("PRAYER", "NORTH-TEMPLE")

    # RAILING in DOME-ROOM
    mv("RAILING", "DOME-ROOM")

    # RAINBOW in FALLS area (global)
    mv("RAINBOW", "ARAGAIN-FALLS")

    # RIVER in RIVER-1 (global in multiple rooms — just a reference)
    mv("RIVER", "RIVER-1")

    # BUOY in RIVER-4 (per ZIL source)
    mv("BUOY", "RIVER-4")

    # TRIDENT in ATLANTIS-ROOM (per ZIL source)
    mv("TRIDENT", "ATLANTIS-ROOM")

    # NEST in UP-A-TREE
    mv("NEST", "UP-A-TREE")

    # EGG in NEST
    mv("EGG", "NEST")

    # CANARY in EGG
    mv("CANARY", "EGG")

    # BAUBLE: unplaced initially; appears via canary winding action in the forest

    # GARLIC in SANDWICH-BAG (inside kitchen sack)
    mv("GARLIC", "SANDWICH-BAG")

    # BOTTLE in KITCHEN-TABLE
    mv("BOTTLE", "KITCHEN-TABLE")

    # WATER in BOTTLE
    mv("WATER", "BOTTLE")

    # BOARDED-WINDOW — LOCAL-GLOBALS, no placement
    # FRONT-DOOR in WEST-OF-HOUSE
    mv("FRONT-DOOR", "WEST-OF-HOUSE")

    # BARROW-DOOR in STONE-BARROW
    mv("BARROW-DOOR", "STONE-BARROW")

    # BARROW in STONE-BARROW
    mv("BARROW", "STONE-BARROW")

    # CRACK in DAMP-CAVE
    mv("CRACK", "DAMP-CAVE")

    # WRENCH in MAINTENANCE-ROOM
    mv("WRENCH", "MAINTENANCE-ROOM")

    # CONTROL-PANEL in DAM-ROOM (per ZIL source)
    mv("CONTROL-PANEL", "DAM-ROOM")

    # OWNERS-MANUAL in STUDIO (per ZIL source)
    mv("OWNERS-MANUAL", "STUDIO")

    # LEAK in MAINTENANCE-ROOM (per ZIL source; INVISIBLE flag set on object)
    mv("LEAK", "MAINTENANCE-ROOM")

    # CLIMBABLE-CLIFF in CANYON-BOTTOM
    mv("CLIMBABLE-CLIFF", "CANYON-BOTTOM")

    # WHITE-CLIFF in WHITE-CLIFFS-NORTH
    mv("WHITE-CLIFF", "WHITE-CLIFFS-NORTH")

    # PUTTY in TUBE (per ZIL source; TUBE is a container in MAINTENANCE-ROOM)
    mv("PUTTY", "TUBE")

    # GUNK in GRATING-ROOM (result of putty use; starts unplaced)

    # ENGRAVINGS in ENGRAVINGS-CAVE already done

    # ADVERTISEMENT in mailbox in original; put in MAILBOX
    advert = world.objects.get("ADVERTISEMENT")
    mailbox = world.objects.get("MAILBOX")
    if advert and mailbox:
        world.move_object(advert, mailbox)

    # GARLIC: actually starts in WEST-OF-HOUSE per ZIL
    # Already set above; no change needed.


# ---------------------------------------------------------------------------
# Player creation
# ---------------------------------------------------------------------------

def _create_player(world: "World") -> None:
    """Create the ADVENTURER player object and place them in WEST-OF-HOUSE."""
    adventurer = world.objects.get("ADVENTURER")
    if adventurer is None:
        adventurer = GameObject(
            name="ADVENTURER",
            synonyms=["adventurer"],
            desc="cretin",
            flags={NDESCBIT, INVISIBLE, SACREDBIT, ACTORBIT, CONTBIT, OPENBIT},
            strength=0,
            capacity=100,
        )
        world.register_object(adventurer)

    start = world.rooms.get("WEST-OF-HOUSE") or world.rooms.get("LIVING-ROOM")
    if start:
        world.move_object(adventurer, start)
        world.here = start

    world.player = adventurer
    world.winner = adventurer


# ---------------------------------------------------------------------------
# Global flags
# ---------------------------------------------------------------------------

def _init_globals(world: "World") -> None:
    """Initialize all ZIL global flags to their starting values."""

    # Conditional exit flags
    world.set_global("CYCLOPS-FLAG",  False)
    world.set_global("DEFLATE",       False)
    world.set_global("DOME-FLAG",     False)
    world.set_global("EMPTY-HANDED",  False)
    world.set_global("LLD-FLAG",      False)
    world.set_global("LOW-TIDE",      False)
    world.set_global("MAGIC-FLAG",    False)
    world.set_global("RAINBOW-FLAG",  False)
    world.set_global("TROLL-FLAG",    False)
    world.set_global("WON-FLAG",      False)
    world.set_global("COFFIN-CURE",   False)

    # Other gameplay globals
    world.set_global("GRATE-REVEALED", False)
    world.set_global("GRUNLOCK",       False)
    world.set_global("RUG-MOVED",      False)
    world.set_global("CAGE-TOP",       True)
    world.set_global("MIRROR-MUNG",    False)
    world.set_global("LUCKY",          True)
    world.set_global("KITCHEN-WINDOW-FLAG", False)
    world.set_global("TIDE-TURNED",    False)
    world.set_global("THIEF-HERE",     False)
    world.set_global("THIEF-ENGROSSED", False)

    # Scoring
    world.set_global("SCORE",         0)
    world.set_global("SCORE-MAX",     350)
    world.set_global("BASE-SCORE",    0)
    world.set_global("MOVES",         0)

    # Misc
    world.set_global("FALSE-FLAG",    False)
    world.set_global("VERBOSE",       False)
    world.set_global("SUPER-BRIEF",   False)

    # Hades ceremony state (XB=bell rung, XC=candles relit)
    world.set_global("XB",            False)
    world.set_global("XC",            False)

    # Match count
    world.set_global("MATCH-COUNT",   6)

    # Dam / water system
    world.set_global("GATE-FLAG",     False)
    world.set_global("GATES-OPEN",    False)
    world.set_global("WATER-LEVEL",   0)

    # Canary song (True after canary has been wound and sung)
    world.set_global("SING-SONG",     False)

    # LIGHT-SHAFT bonus: 13 points when player first sees shaft lit from below
    world.set_global("LIGHT-SHAFT",   13)


# ---------------------------------------------------------------------------
# Clock initialization (mirrors GO() in 1dungeon.zil)
# ---------------------------------------------------------------------------

def _init_clock(world: "World", game, i_lantern_handler, i_thief_handler, i_maint_handler, i_river_handler) -> None:
    """Pre-queue the lamp and other clock events at game start."""
    world.set_global("LAMP-STAGE", 0)
    # Lamp: 200 ticks queued but disabled until player turns it on
    game.clock.queue("I-LANTERN", i_lantern_handler, 200)
    game.clock.disable("I-LANTERN")
    # Thief: demon, fires every turn (re-queues itself)
    game.clock.queue("I-THIEF", i_thief_handler, 1, is_demon=True)
    # Maintenance room flood: registered but quiescent until blue button pressed
    game.clock.add_demon("I-MAINT-ROOM", i_maint_handler)
    # River current: interrupt, quiescent until player launches boat
    game.clock.queue("I-RIVER", i_river_handler, 0)
