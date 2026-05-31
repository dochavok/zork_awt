"""
Room definitions for Zork I.

Translates all <ROOM> declarations from 1dungeon.zil into Room instances
registered with the World.
"""

from __future__ import annotations

from engine.world import (
    World, Room, Exit,
    ONBIT, RLANDBIT, SACREDBIT, DOORBIT, OPENBIT, TOUCHBIT,
)

# Additional flags not in engine/world.py
MAZEBIT    = "MAZEBIT"
NONLANDBIT = "NONLANDBIT"


def _cond(flag_name: str):
    """Return a condition lambda that checks a world global flag."""
    return lambda w: bool(w.get_global(flag_name))


def _obj_open(obj_name: str):
    """Return a condition lambda that checks if a named object has OPENBIT."""
    return lambda w: w.flag_set(obj_name, OPENBIT)


def make_rooms(world: World) -> None:
    """Create all Rooms and register them with the world."""
    from content.actions import ROOM_ACTION_HANDLERS

    def act(name):
        return ROOM_ACTION_HANDLERS.get(name)

    def room(name, desc, *, ldesc="", flags=None, exits=None,
             global_objects=None, action_name=None, value=0):
        r = Room(
            name=name,
            desc=desc,
            ldesc=ldesc,
            exits=exits or {},
            flags=set(flags or []),
            global_objects=global_objects or [],
            action=act(action_name) if action_name else None,
            value=value,
        )
        world.register_room(r)
        return r

    # ---- Forest and outside of house ----

    room("WEST-OF-HOUSE", "West of House",
         flags=[RLANDBIT, ONBIT, SACREDBIT],
         exits={
             "north": Exit(destination="NORTH-OF-HOUSE"),
             "south": Exit(destination="SOUTH-OF-HOUSE"),
             "northeast": Exit(destination="NORTH-OF-HOUSE"),
             "southeast": Exit(destination="SOUTH-OF-HOUSE"),
             "west": Exit(destination="FOREST-1"),
             "east": Exit(message="The door is boarded and you can't remove the boards."),
             "southwest": Exit(destination="STONE-BARROW",
                               condition=_cond("WON-FLAG"),
                               fail_message="You can't go that way."),
             "in": Exit(destination="STONE-BARROW",
                        condition=_cond("WON-FLAG"),
                        fail_message="You can't go that way."),
         },
         action_name="WEST-HOUSE",
         global_objects=["WHITE-HOUSE", "BOARD", "FOREST"])

    room("STONE-BARROW", "Stone Barrow",
         ldesc="You are standing in front of a massive barrow of stone. In the east face\nis a huge stone door which is open. You cannot see into the dark of the tomb.",
         flags=[RLANDBIT, ONBIT, SACREDBIT],
         exits={
             "northeast": Exit(destination="WEST-OF-HOUSE"),
         },
         action_name="STONE-BARROW-FCN")

    room("NORTH-OF-HOUSE", "North of House",
         ldesc="You are facing the north side of a white house. There is no door here,\nand all the windows are boarded up. To the north a narrow path winds through\nthe trees.",
         flags=[RLANDBIT, ONBIT, SACREDBIT],
         exits={
             "southwest": Exit(destination="WEST-OF-HOUSE"),
             "southeast": Exit(destination="EAST-OF-HOUSE"),
             "west": Exit(destination="WEST-OF-HOUSE"),
             "east": Exit(destination="EAST-OF-HOUSE"),
             "north": Exit(destination="PATH"),
             "south": Exit(message="The windows are all boarded."),
         },
         global_objects=["BOARDED-WINDOW", "BOARD", "WHITE-HOUSE", "FOREST"])

    room("SOUTH-OF-HOUSE", "South of House",
         ldesc="You are facing the south side of a white house. There is no door here,\nand all the windows are boarded.",
         flags=[RLANDBIT, ONBIT, SACREDBIT],
         exits={
             "west": Exit(destination="WEST-OF-HOUSE"),
             "east": Exit(destination="EAST-OF-HOUSE"),
             "northeast": Exit(destination="EAST-OF-HOUSE"),
             "northwest": Exit(destination="WEST-OF-HOUSE"),
             "south": Exit(destination="FOREST-3"),
             "north": Exit(message="The windows are all boarded."),
         },
         global_objects=["BOARDED-WINDOW", "BOARD", "WHITE-HOUSE", "FOREST"])

    room("EAST-OF-HOUSE", "Behind House",
         flags=[RLANDBIT, ONBIT, SACREDBIT],
         exits={
             "north": Exit(destination="NORTH-OF-HOUSE"),
             "south": Exit(destination="SOUTH-OF-HOUSE"),
             "southwest": Exit(destination="SOUTH-OF-HOUSE"),
             "northwest": Exit(destination="NORTH-OF-HOUSE"),
             "east": Exit(destination="CLEARING"),
             "west": Exit(destination="KITCHEN",
                          condition=_obj_open("KITCHEN-WINDOW"),
                          fail_message="The window is not open."),
             "in": Exit(destination="KITCHEN",
                        condition=_obj_open("KITCHEN-WINDOW"),
                        fail_message="The window is not open."),
         },
         action_name="EAST-HOUSE",
         global_objects=["WHITE-HOUSE", "KITCHEN-WINDOW", "FOREST"])

    room("FOREST-1", "Forest",
         ldesc="This is a forest, with trees in all directions. To the east,\nthere appears to be sunlight.",
         flags=[RLANDBIT, ONBIT, SACREDBIT],
         exits={
             "up": Exit(message="There is no tree here suitable for climbing."),
             "north": Exit(destination="GRATING-CLEARING"),
             "east": Exit(destination="PATH"),
             "south": Exit(destination="FOREST-3"),
             "west": Exit(message="You would need a machete to go further west."),
         },
         action_name="FOREST-ROOM",
         global_objects=["TREE", "SONGBIRD", "WHITE-HOUSE", "FOREST"])

    room("FOREST-2", "Forest",
         ldesc="This is a dimly lit forest, with large trees all around.",
         flags=[RLANDBIT, ONBIT, SACREDBIT],
         exits={
             "up": Exit(message="There is no tree here suitable for climbing."),
             "north": Exit(message="The forest becomes impenetrable to the north."),
             "east": Exit(destination="MOUNTAINS"),
             "south": Exit(destination="CLEARING"),
             "west": Exit(destination="PATH"),
         },
         action_name="FOREST-ROOM",
         global_objects=["TREE", "SONGBIRD", "WHITE-HOUSE", "FOREST"])

    room("MOUNTAINS", "Forest",
         ldesc="The forest thins out, revealing impassable mountains.",
         flags=[RLANDBIT, ONBIT, SACREDBIT],
         exits={
             "up": Exit(message="The mountains are impassable."),
             "north": Exit(destination="FOREST-2"),
             "east": Exit(message="The mountains are impassable."),
             "south": Exit(destination="FOREST-2"),
             "west": Exit(destination="FOREST-2"),
         },
         global_objects=["TREE", "WHITE-HOUSE"])

    room("FOREST-3", "Forest",
         ldesc="This is a dimly lit forest, with large trees all around.",
         flags=[RLANDBIT, ONBIT, SACREDBIT],
         exits={
             "up": Exit(message="There is no tree here suitable for climbing."),
             "north": Exit(destination="CLEARING"),
             "east": Exit(message="The rank undergrowth prevents eastward movement."),
             "south": Exit(message="Storm-tossed trees block your way."),
             "west": Exit(destination="FOREST-1"),
             "northwest": Exit(destination="SOUTH-OF-HOUSE"),
         },
         action_name="FOREST-ROOM",
         global_objects=["TREE", "SONGBIRD", "WHITE-HOUSE", "FOREST"])

    room("PATH", "Forest Path",
         ldesc="This is a path winding through a dimly lit forest. The path heads\nnorth-south here. One particularly large tree with some low branches\nstands at the edge of the path.",
         flags=[RLANDBIT, ONBIT, SACREDBIT],
         exits={
             "up": Exit(destination="UP-A-TREE"),
             "north": Exit(destination="GRATING-CLEARING"),
             "east": Exit(destination="FOREST-2"),
             "south": Exit(destination="NORTH-OF-HOUSE"),
             "west": Exit(destination="FOREST-1"),
         },
         action_name="FOREST-ROOM",
         global_objects=["TREE", "SONGBIRD", "WHITE-HOUSE", "FOREST"])

    room("UP-A-TREE", "Up a Tree",
         flags=[RLANDBIT, ONBIT, SACREDBIT],
         exits={
             "down": Exit(destination="PATH"),
             "up": Exit(message="You cannot climb any higher."),
         },
         action_name="TREE-ROOM",
         global_objects=["TREE", "FOREST", "SONGBIRD", "WHITE-HOUSE"])

    room("GRATING-CLEARING", "Clearing",
         flags=[RLANDBIT, ONBIT, SACREDBIT],
         exits={
             "north": Exit(message="The forest becomes impenetrable to the north."),
             "east": Exit(destination="FOREST-2"),
             "west": Exit(destination="FOREST-1"),
             "south": Exit(destination="PATH"),
             "down": Exit(destination="GRATING-ROOM",
                          condition=lambda w: _grating_cond(w),
                          fail_message="You can't go that way."),
         },
         action_name="CLEARING-FCN",
         global_objects=["WHITE-HOUSE", "GRATE"])

    room("CLEARING", "Clearing",
         ldesc="You are in a small clearing in a well marked forest path that\nextends to the east and west.",
         flags=[RLANDBIT, ONBIT, SACREDBIT],
         exits={
             "up": Exit(message="There is no tree here suitable for climbing."),
             "east": Exit(destination="CANYON-VIEW"),
             "north": Exit(destination="FOREST-2"),
             "south": Exit(destination="FOREST-3"),
             "west": Exit(destination="EAST-OF-HOUSE"),
         },
         action_name="FOREST-ROOM",
         global_objects=["TREE", "SONGBIRD", "WHITE-HOUSE", "FOREST"])

    # ---- House ----

    room("KITCHEN", "Kitchen",
         flags=[RLANDBIT, ONBIT, SACREDBIT],
         exits={
             "east": Exit(destination="EAST-OF-HOUSE",
                          condition=_obj_open("KITCHEN-WINDOW"),
                          fail_message="The window is not open."),
             "west": Exit(destination="LIVING-ROOM"),
             "out": Exit(destination="EAST-OF-HOUSE",
                         condition=_obj_open("KITCHEN-WINDOW"),
                         fail_message="The window is not open."),
             "up": Exit(destination="ATTIC"),
             "down": Exit(destination="STUDIO",
                          condition=_cond("FALSE-FLAG"),
                          fail_message="Only Santa Claus climbs down chimneys."),
         },
         action_name="KITCHEN-FCN",
         global_objects=["KITCHEN-WINDOW", "CHIMNEY", "STAIRS"],
         value=10)

    room("ATTIC", "Attic",
         ldesc="This is the attic. The only exit is a stairway leading down.",
         flags=[RLANDBIT, SACREDBIT],
         exits={
             "down": Exit(destination="KITCHEN"),
         },
         global_objects=["STAIRS"])

    room("LIVING-ROOM", "Living Room",
         flags=[RLANDBIT, ONBIT, SACREDBIT],
         exits={
             "east": Exit(destination="KITCHEN"),
             "west": Exit(destination="STRANGE-PASSAGE",
                          condition=_cond("MAGIC-FLAG"),
                          fail_message="The door is nailed shut."),
             "down": Exit(destination="CELLAR",
                          condition=lambda w: _trap_door_cond(w),
                          fail_message="You can't go that way."),
         },
         action_name="LIVING-ROOM-FCN",
         global_objects=["STAIRS"])

    # ---- Cellar and vicinity ----

    room("CELLAR", "Cellar",
         flags=[RLANDBIT],
         exits={
             "north": Exit(destination="TROLL-ROOM"),
             "south": Exit(destination="EAST-OF-CHASM"),
             "up": Exit(destination="LIVING-ROOM",
                        condition=_obj_open("TRAP-DOOR"),
                        fail_message="The trap door is closed."),
             "west": Exit(message="You try to ascend the ramp, but it is impossible, and you slide back down."),
         },
         action_name="CELLAR-FCN",
         global_objects=["TRAP-DOOR", "SLIDE", "STAIRS"],
         value=25)

    room("TROLL-ROOM", "The Troll Room",
         ldesc="This is a small room with passages to the east and south and a\nforbidding hole leading west. Bloodstains and deep scratches\n(perhaps made by an axe) mar the walls.",
         flags=[RLANDBIT],
         exits={
             "south": Exit(destination="CELLAR"),
             "east": Exit(destination="EW-PASSAGE",
                          condition=_cond("TROLL-FLAG"),
                          fail_message="The troll fends you off with a menacing gesture."),
             "west": Exit(destination="MAZE-1",
                          condition=_cond("TROLL-FLAG"),
                          fail_message="The troll fends you off with a menacing gesture."),
         },
         action_name="TROLL-ROOM-F")

    room("EAST-OF-CHASM", "East of Chasm",
         ldesc="You are on the east edge of a chasm, the bottom of which cannot be\nseen. A narrow passage goes north, and the path you are on continues\nto the east.",
         flags=[RLANDBIT],
         exits={
             "north": Exit(destination="CELLAR"),
             "east": Exit(destination="GALLERY"),
             "down": Exit(message="The chasm probably leads straight to the infernal regions."),
         })

    room("GALLERY", "Gallery",
         ldesc="This is an art gallery. Most of the paintings have been stolen by\nvandals with exceptional taste. The vandals left through either the\nnorth or west exits.",
         flags=[RLANDBIT, ONBIT],
         exits={
             "west": Exit(destination="EAST-OF-CHASM"),
             "north": Exit(destination="STUDIO"),
         })

    room("STUDIO", "Studio",
         ldesc="This appears to have been an artist's studio. The walls and floors are\nsplattered with paints of 69 different colors. Strangely enough, nothing\nof value is hanging here. At the south end of the room is an open door\n(also covered with paint). A dark and narrow chimney leads up from a\nfireplace; although you might be able to get up it, it seems unlikely\nyou could get back down.",
         flags=[RLANDBIT],
         exits={
             "south": Exit(destination="GALLERY"),
             "up": Exit(destination="KITCHEN",
                        condition=lambda w: _up_chimney(w),
                        fail_message="You can't get up there."),
         },
         global_objects=["CHIMNEY"])

    # ---- Maze ----

    room("MAZE-1", "Maze",
         ldesc="This is part of a maze of twisty little passages, all alike.",
         flags=[RLANDBIT, MAZEBIT],
         exits={
             "east": Exit(destination="TROLL-ROOM"),
             "north": Exit(destination="MAZE-1"),
             "south": Exit(destination="MAZE-2"),
             "west": Exit(destination="MAZE-4"),
         })

    room("MAZE-2", "Maze",
         ldesc="This is part of a maze of twisty little passages, all alike.",
         flags=[RLANDBIT, MAZEBIT],
         exits={
             "south": Exit(destination="MAZE-1"),
             "down": Exit(destination="MAZE-4",
                          condition=lambda w: _maze_diode_warn(w)),
             "east": Exit(destination="MAZE-3"),
         })

    room("MAZE-3", "Maze",
         ldesc="This is part of a maze of twisty little passages, all alike.",
         flags=[RLANDBIT, MAZEBIT],
         exits={
             "west": Exit(destination="MAZE-2"),
             "north": Exit(destination="MAZE-4"),
             "up": Exit(destination="MAZE-5"),
         })

    room("MAZE-4", "Maze",
         ldesc="This is part of a maze of twisty little passages, all alike.",
         flags=[RLANDBIT, MAZEBIT],
         exits={
             "west": Exit(destination="MAZE-3"),
             "north": Exit(destination="MAZE-1"),
             "east": Exit(destination="DEAD-END-1"),
         })

    room("DEAD-END-1", "Dead End",
         ldesc="You have come to a dead end in the maze.",
         flags=[RLANDBIT, MAZEBIT],
         exits={
             "south": Exit(destination="MAZE-4"),
         })

    room("MAZE-5", "Maze",
         ldesc="This is part of a maze of twisty little passages, all alike.\nA skeleton, probably the remains of a luckless adventurer, lies here.",
         flags=[RLANDBIT, MAZEBIT],
         exits={
             "east": Exit(destination="DEAD-END-2"),
             "north": Exit(destination="MAZE-3"),
             "southwest": Exit(destination="MAZE-6"),
         })

    room("DEAD-END-2", "Dead End",
         ldesc="You have come to a dead end in the maze.",
         flags=[RLANDBIT, MAZEBIT],
         exits={
             "west": Exit(destination="MAZE-5"),
         })

    room("MAZE-6", "Maze",
         ldesc="This is part of a maze of twisty little passages, all alike.",
         flags=[RLANDBIT, MAZEBIT],
         exits={
             "down": Exit(destination="MAZE-5"),
             "east": Exit(destination="MAZE-7"),
             "west": Exit(destination="MAZE-6"),
             "up": Exit(destination="MAZE-9"),
         })

    room("MAZE-7", "Maze",
         ldesc="This is part of a maze of twisty little passages, all alike.",
         flags=[RLANDBIT, MAZEBIT],
         exits={
             "up": Exit(destination="MAZE-14"),
             "west": Exit(destination="MAZE-6"),
             "down": Exit(destination="DEAD-END-1",
                          condition=lambda w: _maze_diode_warn(w)),
             "east": Exit(destination="MAZE-8"),
             "south": Exit(destination="MAZE-15"),
         })

    room("MAZE-8", "Maze",
         ldesc="This is part of a maze of twisty little passages, all alike.",
         flags=[RLANDBIT, MAZEBIT],
         exits={
             "northeast": Exit(destination="MAZE-7"),
             "west": Exit(destination="MAZE-8"),
             "southeast": Exit(destination="DEAD-END-3"),
         })

    room("DEAD-END-3", "Dead End",
         ldesc="You have come to a dead end in the maze.",
         flags=[RLANDBIT, MAZEBIT],
         exits={
             "north": Exit(destination="MAZE-8"),
         })

    room("MAZE-9", "Maze",
         ldesc="This is part of a maze of twisty little passages, all alike.",
         flags=[RLANDBIT, MAZEBIT],
         exits={
             "north": Exit(destination="MAZE-6"),
             "down": Exit(destination="MAZE-11",
                          condition=lambda w: _maze_diode_warn(w)),
             "east": Exit(destination="MAZE-10"),
             "south": Exit(destination="MAZE-13"),
             "west": Exit(destination="MAZE-12"),
             "northwest": Exit(destination="MAZE-9"),
         })

    room("MAZE-10", "Maze",
         ldesc="This is part of a maze of twisty little passages, all alike.",
         flags=[RLANDBIT, MAZEBIT],
         exits={
             "east": Exit(destination="MAZE-9"),
             "west": Exit(destination="MAZE-13"),
             "up": Exit(destination="MAZE-11"),
         })

    room("MAZE-11", "Maze",
         ldesc="This is part of a maze of twisty little passages, all alike.",
         flags=[RLANDBIT, MAZEBIT],
         exits={
             "northeast": Exit(destination="GRATING-ROOM"),
             "down": Exit(destination="MAZE-10"),
             "northwest": Exit(destination="MAZE-13"),
             "southwest": Exit(destination="MAZE-12"),
         })

    room("GRATING-ROOM", "Grating Room",
         flags=[RLANDBIT],
         exits={
             "southwest": Exit(destination="MAZE-11"),
             "up": Exit(destination="GRATING-CLEARING",
                        condition=_obj_open("GRATE"),
                        fail_message="The grating is closed."),
         },
         action_name="MAZE-11-FCN",
         global_objects=["GRATE"])

    room("MAZE-12", "Maze",
         ldesc="This is part of a maze of twisty little passages, all alike.",
         flags=[RLANDBIT, MAZEBIT],
         exits={
             "down": Exit(destination="MAZE-5",
                          condition=lambda w: _maze_diode_warn(w)),
             "southwest": Exit(destination="MAZE-11"),
             "east": Exit(destination="MAZE-13"),
             "up": Exit(destination="MAZE-9"),
             "north": Exit(destination="DEAD-END-4"),
         })

    room("DEAD-END-4", "Dead End",
         ldesc="You have come to a dead end in the maze.",
         flags=[RLANDBIT, MAZEBIT],
         exits={
             "south": Exit(destination="MAZE-12"),
         })

    room("MAZE-13", "Maze",
         ldesc="This is part of a maze of twisty little passages, all alike.",
         flags=[RLANDBIT, MAZEBIT],
         exits={
             "east": Exit(destination="MAZE-9"),
             "down": Exit(destination="MAZE-12"),
             "south": Exit(destination="MAZE-10"),
             "west": Exit(destination="MAZE-11"),
         })

    room("MAZE-14", "Maze",
         ldesc="This is part of a maze of twisty little passages, all alike.",
         flags=[RLANDBIT, MAZEBIT],
         exits={
             "west": Exit(destination="MAZE-15"),
             "northwest": Exit(destination="MAZE-14"),
             "northeast": Exit(destination="MAZE-7"),
             "south": Exit(destination="MAZE-7"),
         })

    room("MAZE-15", "Maze",
         ldesc="This is part of a maze of twisty little passages, all alike.",
         flags=[RLANDBIT, MAZEBIT],
         exits={
             "west": Exit(destination="MAZE-14"),
             "south": Exit(destination="MAZE-7"),
             "southeast": Exit(destination="CYCLOPS-ROOM"),
         })

    # ---- Cyclops and Hideaway ----

    room("CYCLOPS-ROOM", "Cyclops Room",
         flags=[RLANDBIT],
         exits={
             "northwest": Exit(destination="MAZE-15"),
             "east": Exit(destination="STRANGE-PASSAGE",
                          condition=_cond("MAGIC-FLAG"),
                          fail_message="The east wall is solid rock."),
             "up": Exit(destination="TREASURE-ROOM",
                        condition=_cond("CYCLOPS-FLAG"),
                        fail_message="The cyclops doesn't look like he'll let you past."),
         },
         action_name="CYCLOPS-ROOM-FCN",
         global_objects=["STAIRS"])

    room("STRANGE-PASSAGE", "Strange Passage",
         ldesc="This is a long passage. To the west is one entrance. On the\neast there is an old wooden door, with a large opening in it (about\ncyclops sized).",
         flags=[RLANDBIT],
         exits={
             "west": Exit(destination="CYCLOPS-ROOM"),
             "in": Exit(destination="CYCLOPS-ROOM"),
             "east": Exit(destination="LIVING-ROOM"),
         })

    room("TREASURE-ROOM", "Treasure Room",
         ldesc="This is a large room, whose east wall is solid granite. A number\nof discarded bags, which crumble at your touch, are scattered about\non the floor. There is an exit down a staircase.",
         flags=[RLANDBIT],
         exits={
             "down": Exit(destination="CYCLOPS-ROOM"),
         },
         action_name="TREASURE-ROOM-FCN",
         global_objects=["STAIRS"],
         value=25)

    # ---- Reservoir area ----

    room("RESERVOIR-SOUTH", "Reservoir South",
         flags=[RLANDBIT],
         exits={
             "southeast": Exit(destination="DEEP-CANYON"),
             "southwest": Exit(destination="CHASM-ROOM"),
             "east": Exit(destination="DAM-ROOM"),
             "west": Exit(destination="STREAM-VIEW"),
             "north": Exit(destination="RESERVOIR",
                           condition=_cond("LOW-TIDE"),
                           fail_message="You would drown."),
         },
         action_name="RESERVOIR-SOUTH-FCN",
         global_objects=["GLOBAL-WATER"])

    room("RESERVOIR", "Reservoir",
         flags=[NONLANDBIT],
         exits={
             "north": Exit(destination="RESERVOIR-NORTH"),
             "south": Exit(destination="RESERVOIR-SOUTH"),
             "up": Exit(destination="IN-STREAM"),
             "west": Exit(destination="IN-STREAM"),
             "down": Exit(message="The dam blocks your way."),
         },
         action_name="RESERVOIR-FCN",
         global_objects=["GLOBAL-WATER"])

    room("RESERVOIR-NORTH", "Reservoir North",
         flags=[RLANDBIT],
         exits={
             "north": Exit(destination="ATLANTIS-ROOM"),
             "south": Exit(destination="RESERVOIR",
                           condition=_cond("LOW-TIDE"),
                           fail_message="You would drown."),
         },
         action_name="RESERVOIR-NORTH-FCN",
         global_objects=["GLOBAL-WATER", "STAIRS"])

    room("STREAM-VIEW", "Stream View",
         ldesc="You are standing on a path beside a gently flowing stream. The path\nfollows the stream, which flows from west to east.",
         flags=[RLANDBIT],
         exits={
             "east": Exit(destination="RESERVOIR-SOUTH"),
             "west": Exit(message="The stream emerges from a spot too small for you to enter."),
         },
         global_objects=["GLOBAL-WATER"])

    room("IN-STREAM", "Stream",
         ldesc="You are on the gently flowing stream. The upstream route is too narrow\nto navigate, and the downstream route is invisible due to twisting\nwalls. There is a narrow beach to land on.",
         flags=[NONLANDBIT],
         exits={
             "up": Exit(message="The channel is too narrow."),
             "west": Exit(message="The channel is too narrow."),
             "land": Exit(destination="STREAM-VIEW"),
             "down": Exit(destination="RESERVOIR"),
             "east": Exit(destination="RESERVOIR"),
         },
         global_objects=["GLOBAL-WATER"])

    # ---- Mirror rooms ----

    room("MIRROR-ROOM-1", "Mirror Room",
         flags=[RLANDBIT],
         exits={
             "north": Exit(destination="COLD-PASSAGE"),
             "west": Exit(destination="TWISTING-PASSAGE"),
             "east": Exit(destination="SMALL-CAVE"),
         },
         action_name="MIRROR-ROOM")

    room("MIRROR-ROOM-2", "Mirror Room",
         flags=[RLANDBIT, ONBIT],
         exits={
             "west": Exit(destination="WINDING-PASSAGE"),
             "north": Exit(destination="NARROW-PASSAGE"),
             "east": Exit(destination="TINY-CAVE"),
         },
         action_name="MIRROR-ROOM")

    room("SMALL-CAVE", "Cave",
         ldesc="This is a tiny cave with entrances west and north, and a staircase\nleading down.",
         flags=[RLANDBIT],
         exits={
             "north": Exit(destination="MIRROR-ROOM-1"),
             "down": Exit(destination="ATLANTIS-ROOM"),
             "south": Exit(destination="ATLANTIS-ROOM"),
             "west": Exit(destination="TWISTING-PASSAGE"),
         },
         global_objects=["STAIRS"])

    room("TINY-CAVE", "Cave",
         ldesc="This is a tiny cave with entrances west and north, and a dark,\nforbidding staircase leading down.",
         flags=[RLANDBIT],
         exits={
             "north": Exit(destination="MIRROR-ROOM-2"),
             "west": Exit(destination="WINDING-PASSAGE"),
             "down": Exit(destination="ENTRANCE-TO-HADES"),
         },
         action_name="CAVE2-ROOM",
         global_objects=["STAIRS"])

    room("COLD-PASSAGE", "Cold Passage",
         ldesc="This is a cold and damp corridor where a long east-west passageway\nturns into a southward path.",
         flags=[RLANDBIT],
         exits={
             "south": Exit(destination="MIRROR-ROOM-1"),
             "west": Exit(destination="SLIDE-ROOM"),
         })

    room("NARROW-PASSAGE", "Narrow Passage",
         ldesc="This is a long and narrow corridor where a long north-south passageway\nbriefly narrows even further.",
         flags=[RLANDBIT],
         exits={
             "north": Exit(destination="ROUND-ROOM"),
             "south": Exit(destination="MIRROR-ROOM-2"),
         })

    room("WINDING-PASSAGE", "Winding Passage",
         ldesc="This is a winding passage. It seems that there are only exits\non the east and north.",
         flags=[RLANDBIT],
         exits={
             "north": Exit(destination="MIRROR-ROOM-2"),
             "east": Exit(destination="TINY-CAVE"),
         })

    room("TWISTING-PASSAGE", "Twisting Passage",
         ldesc="This is a winding passage. It seems that there are only exits\non the east and north.",
         flags=[RLANDBIT],
         exits={
             "north": Exit(destination="MIRROR-ROOM-1"),
             "east": Exit(destination="SMALL-CAVE"),
         })

    room("ATLANTIS-ROOM", "Atlantis Room",
         ldesc="This is an ancient room, long under water. There is an exit to\nthe south and a staircase leading up.",
         flags=[RLANDBIT],
         exits={
             "up": Exit(destination="SMALL-CAVE"),
             "south": Exit(destination="RESERVOIR-NORTH"),
         },
         global_objects=["STAIRS"])

    # ---- Round room and vicinity ----

    room("EW-PASSAGE", "East-West Passage",
         ldesc="This is a narrow east-west passageway. There is a narrow stairway\nleading down at the north end of the room.",
         flags=[RLANDBIT],
         exits={
             "east": Exit(destination="ROUND-ROOM"),
             "west": Exit(destination="TROLL-ROOM"),
             "down": Exit(destination="CHASM-ROOM"),
             "north": Exit(destination="CHASM-ROOM"),
         },
         global_objects=["STAIRS"],
         value=5)

    room("ROUND-ROOM", "Round Room",
         ldesc="This is a circular stone room with passages in all directions. Several\nof them have unfortunately been blocked by cave-ins.",
         flags=[RLANDBIT],
         exits={
             "east": Exit(destination="LOUD-ROOM"),
             "west": Exit(destination="EW-PASSAGE"),
             "north": Exit(destination="NS-PASSAGE"),
             "south": Exit(destination="NARROW-PASSAGE"),
             "southeast": Exit(destination="ENGRAVINGS-CAVE"),
         })

    room("DEEP-CANYON", "Deep Canyon",
         flags=[RLANDBIT],
         exits={
             "northwest": Exit(destination="RESERVOIR-SOUTH"),
             "east": Exit(destination="DAM-ROOM"),
             "southwest": Exit(destination="NS-PASSAGE"),
             "down": Exit(destination="LOUD-ROOM"),
         },
         action_name="DEEP-CANYON-F",
         global_objects=["STAIRS"])

    room("DAMP-CAVE", "Damp Cave",
         ldesc="This cave has exits to the west and east, and narrows to a crack toward\nthe south. The earth is particularly damp here.",
         flags=[RLANDBIT],
         exits={
             "west": Exit(destination="LOUD-ROOM"),
             "east": Exit(destination="WHITE-CLIFFS-NORTH"),
             "south": Exit(message="It is too narrow for most insects."),
         },
         global_objects=["CRACK"])

    room("LOUD-ROOM", "Loud Room",
         flags=[RLANDBIT],
         exits={
             "east": Exit(destination="DAMP-CAVE"),
             "west": Exit(destination="ROUND-ROOM"),
             "up": Exit(destination="DEEP-CANYON"),
         },
         action_name="LOUD-ROOM-FCN",
         global_objects=["STAIRS"])

    room("NS-PASSAGE", "North-South Passage",
         ldesc="This is a high north-south passage, which forks to the northeast.",
         flags=[RLANDBIT],
         exits={
             "north": Exit(destination="CHASM-ROOM"),
             "northeast": Exit(destination="DEEP-CANYON"),
             "south": Exit(destination="ROUND-ROOM"),
         })

    room("CHASM-ROOM", "Chasm",
         ldesc="A chasm runs southwest to northeast and the path follows it. You are\non the south side of the chasm, where a crack opens into a passage.",
         flags=[RLANDBIT],
         exits={
             "northeast": Exit(destination="RESERVOIR-SOUTH"),
             "southwest": Exit(destination="EW-PASSAGE"),
             "up": Exit(destination="EW-PASSAGE"),
             "south": Exit(destination="NS-PASSAGE"),
             "down": Exit(message="Are you out of your mind?"),
         },
         global_objects=["CRACK", "STAIRS"])

    # ---- Hades ----

    room("ENTRANCE-TO-HADES", "Entrance to Hades",
         flags=[RLANDBIT, ONBIT],
         exits={
             "up": Exit(destination="TINY-CAVE"),
             "in": Exit(destination="LAND-OF-LIVING-DEAD",
                        condition=_cond("LLD-FLAG"),
                        fail_message="Some invisible force prevents you from passing through the gate."),
             "south": Exit(destination="LAND-OF-LIVING-DEAD",
                           condition=_cond("LLD-FLAG"),
                           fail_message="Some invisible force prevents you from passing through the gate."),
         },
         action_name="LLD-ROOM",
         global_objects=["BODIES"])

    room("LAND-OF-LIVING-DEAD", "Land of the Dead",
         ldesc="You have entered the Land of the Living Dead. Thousands of lost souls\ncan be heard weeping and moaning. In the corner are stacked the remains\nof dozens of previous adventurers less fortunate than yourself.\nA passage exits to the north.",
         flags=[RLANDBIT, ONBIT],
         exits={
             "out": Exit(destination="ENTRANCE-TO-HADES"),
             "north": Exit(destination="ENTRANCE-TO-HADES"),
         },
         global_objects=["BODIES"])

    # ---- Dome, Temple, Egypt ----

    room("ENGRAVINGS-CAVE", "Engravings Cave",
         ldesc="You have entered a low cave with passages leading northwest and east.",
         flags=[RLANDBIT],
         exits={
             "northwest": Exit(destination="ROUND-ROOM"),
             "east": Exit(destination="DOME-ROOM"),
         })

    room("EGYPT-ROOM", "Egyptian Room",
         ldesc="This is a room which looks like an Egyptian tomb. There is an\nascending staircase to the west.",
         flags=[RLANDBIT],
         exits={
             "west": Exit(destination="NORTH-TEMPLE"),
             "up": Exit(destination="NORTH-TEMPLE"),
         },
         global_objects=["STAIRS"])

    room("DOME-ROOM", "Dome Room",
         flags=[RLANDBIT],
         exits={
             "west": Exit(destination="ENGRAVINGS-CAVE"),
             "down": Exit(destination="TORCH-ROOM",
                          condition=_cond("DOME-FLAG"),
                          fail_message="You cannot go down without fracturing many bones."),
         },
         action_name="DOME-ROOM-FCN")

    room("TORCH-ROOM", "Torch Room",
         flags=[RLANDBIT],
         exits={
             "up": Exit(message="You cannot reach the rope."),
             "south": Exit(destination="NORTH-TEMPLE"),
             "down": Exit(destination="NORTH-TEMPLE"),
         },
         action_name="TORCH-ROOM-FCN",
         global_objects=["STAIRS"])

    room("NORTH-TEMPLE", "Temple",
         ldesc="This is the north end of a large temple. On the east wall is an\nancient inscription, probably a prayer in a long-forgotten language.\nBelow the prayer is a staircase leading down. The west wall is solid\ngranite. The exit to the north end of the room is through huge\nmarble pillars.",
         flags=[RLANDBIT, ONBIT, SACREDBIT],
         exits={
             "down": Exit(destination="EGYPT-ROOM"),
             "east": Exit(destination="EGYPT-ROOM"),
             "north": Exit(destination="TORCH-ROOM"),
             "out": Exit(destination="TORCH-ROOM"),
             "up": Exit(destination="TORCH-ROOM"),
             "south": Exit(destination="SOUTH-TEMPLE"),
         },
         global_objects=["STAIRS"])

    room("SOUTH-TEMPLE", "Altar",
         ldesc="This is the south end of a large temple. In front of you is what\nappears to be an altar. In one corner is a small hole in the floor\nwhich leads into darkness. You probably could not get back up it.",
         flags=[RLANDBIT, ONBIT, SACREDBIT],
         exits={
             "north": Exit(destination="NORTH-TEMPLE"),
             "down": Exit(destination="TINY-CAVE",
                          condition=_cond("COFFIN-CURE"),
                          fail_message="You haven't a prayer of getting the coffin down there."),
         },
         action_name="SOUTH-TEMPLE-FCN")

    # ---- Flood Control Dam #3 ----

    room("DAM-ROOM", "Dam",
         flags=[RLANDBIT, ONBIT],
         exits={
             "south": Exit(destination="DEEP-CANYON"),
             "down": Exit(destination="DAM-BASE"),
             "east": Exit(destination="DAM-BASE"),
             "north": Exit(destination="DAM-LOBBY"),
             "west": Exit(destination="RESERVOIR-SOUTH"),
         },
         action_name="DAM-ROOM-FCN",
         global_objects=["GLOBAL-WATER"])

    room("DAM-LOBBY", "Dam Lobby",
         ldesc="This room appears to have been the waiting room for groups touring\nthe dam. There are open doorways here to the north and east marked\n\"Private\", and there is a path leading south over the top of the dam.",
         flags=[RLANDBIT, ONBIT],
         exits={
             "south": Exit(destination="DAM-ROOM"),
             "north": Exit(destination="MAINTENANCE-ROOM"),
             "east": Exit(destination="MAINTENANCE-ROOM"),
         })

    room("MAINTENANCE-ROOM", "Maintenance Room",
         ldesc="This is what appears to have been the maintenance room for Flood\nControl Dam #3. Apparently, this room has been ransacked recently, for\nmost of the valuable equipment is gone. On the wall in front of you is a\ngroup of buttons colored blue, yellow, brown, and red. There are doorways to\nthe west and south.",
         flags=[RLANDBIT],
         exits={
             "south": Exit(destination="DAM-LOBBY"),
             "west": Exit(destination="DAM-LOBBY"),
         })

    # ---- River area ----

    room("DAM-BASE", "Dam Base",
         ldesc="You are at the base of Flood Control Dam #3, which looms above you\nand to the north. The river Frigid is flowing by here. Along the\nriver are the White Cliffs which seem to form giant walls stretching\nfrom north to south along the shores of the river as it winds its\nway downstream.",
         flags=[RLANDBIT, ONBIT, SACREDBIT],
         exits={
             "north": Exit(destination="DAM-ROOM"),
             "up": Exit(destination="DAM-ROOM"),
         },
         global_objects=["GLOBAL-WATER", "RIVER"])

    room("RIVER-1", "Frigid River",
         ldesc="You are on the Frigid River in the vicinity of the Dam. The river\nflows quietly here. There is a landing on the west shore.",
         flags=[NONLANDBIT, SACREDBIT, ONBIT],
         exits={
             "up": Exit(message="You cannot go upstream due to strong currents."),
             "west": Exit(destination="DAM-BASE"),
             "land": Exit(destination="DAM-BASE"),
             "down": Exit(destination="RIVER-2"),
             "east": Exit(message="The White Cliffs prevent your landing here."),
         },
         global_objects=["GLOBAL-WATER", "RIVER"])

    room("RIVER-2", "Frigid River",
         ldesc="The river turns a corner here making it impossible to see the\nDam. The White Cliffs loom on the east bank and large rocks prevent\nlanding on the west.",
         flags=[NONLANDBIT, SACREDBIT],
         exits={
             "up": Exit(message="You cannot go upstream due to strong currents."),
             "down": Exit(destination="RIVER-3"),
             "land": Exit(message="There is no safe landing spot here."),
             "east": Exit(message="The White Cliffs prevent your landing here."),
             "west": Exit(message="Just in time you steer away from the rocks."),
         },
         global_objects=["GLOBAL-WATER", "RIVER"])

    room("RIVER-3", "Frigid River",
         ldesc="The river descends here into a valley. There is a narrow beach on the\nwest shore below the cliffs. In the distance a faint rumbling can be\nheard.",
         flags=[NONLANDBIT, SACREDBIT],
         exits={
             "up": Exit(message="You cannot go upstream due to strong currents."),
             "down": Exit(destination="RIVER-4"),
             "land": Exit(destination="WHITE-CLIFFS-NORTH"),
             "west": Exit(destination="WHITE-CLIFFS-NORTH"),
         },
         global_objects=["GLOBAL-WATER", "RIVER"])

    room("WHITE-CLIFFS-NORTH", "White Cliffs Beach",
         ldesc="You are on a narrow strip of beach which runs along the base of the\nWhite Cliffs. There is a narrow path heading south along the Cliffs\nand a tight passage leading west into the cliffs themselves.",
         flags=[RLANDBIT, SACREDBIT],
         exits={
             "south": Exit(destination="WHITE-CLIFFS-SOUTH",
                           condition=_cond("DEFLATE"),
                           fail_message="The path is too narrow."),
             "west": Exit(destination="DAMP-CAVE",
                          condition=_cond("DEFLATE"),
                          fail_message="The path is too narrow."),
         },
         action_name="WHITE-CLIFFS-FUNCTION",
         global_objects=["GLOBAL-WATER", "WHITE-CLIFF", "RIVER"])

    room("WHITE-CLIFFS-SOUTH", "White Cliffs Beach",
         ldesc="You are on a rocky, narrow strip of beach beside the Cliffs. A\nnarrow path leads north along the shore.",
         flags=[RLANDBIT, SACREDBIT],
         exits={
             "north": Exit(destination="WHITE-CLIFFS-NORTH",
                           condition=_cond("DEFLATE"),
                           fail_message="The path is too narrow."),
         },
         action_name="WHITE-CLIFFS-FUNCTION",
         global_objects=["GLOBAL-WATER", "WHITE-CLIFF", "RIVER"])

    room("RIVER-4", "Frigid River",
         ldesc="The river is running faster here and the sound ahead appears to be\nthat of rushing water. On the east shore is a sandy beach. A small\narea of beach can also be seen below the cliffs on the west shore.",
         flags=[NONLANDBIT, SACREDBIT],
         exits={
             "up": Exit(message="You cannot go upstream due to strong currents."),
             "down": Exit(destination="RIVER-5"),
             "land": Exit(message="You can land either to the east or the west."),
             "west": Exit(destination="WHITE-CLIFFS-SOUTH"),
             "east": Exit(destination="SANDY-BEACH"),
         },
         action_name="RIVR4-ROOM",
         global_objects=["GLOBAL-WATER", "RIVER"])

    room("RIVER-5", "Frigid River",
         ldesc="The sound of rushing water is nearly unbearable here. On the east\nshore is a large landing area.",
         flags=[NONLANDBIT, SACREDBIT, ONBIT],
         exits={
             "up": Exit(message="You cannot go upstream due to strong currents."),
             "east": Exit(destination="SHORE"),
             "land": Exit(destination="SHORE"),
         },
         global_objects=["GLOBAL-WATER", "RIVER"])

    room("SHORE", "Shore",
         ldesc="You are on the east shore of the river. The water here seems somewhat\ntreacherous. A path travels from north to south here, the south end\nquickly turning around a sharp corner.",
         flags=[RLANDBIT, SACREDBIT, ONBIT],
         exits={
             "north": Exit(destination="SANDY-BEACH"),
             "south": Exit(destination="ARAGAIN-FALLS"),
         },
         global_objects=["GLOBAL-WATER", "RIVER"])

    room("SANDY-BEACH", "Sandy Beach",
         ldesc="You are on a large sandy beach on the east shore of the river, which is\nflowing quickly by. A path runs beside the river to the south here, and\na passage is partially buried in sand to the northeast.",
         flags=[RLANDBIT, SACREDBIT],
         exits={
             "northeast": Exit(destination="SANDY-CAVE"),
             "south": Exit(destination="SHORE"),
         },
         global_objects=["GLOBAL-WATER", "RIVER"])

    room("SANDY-CAVE", "Sandy Cave",
         ldesc="This is a sand-filled cave whose exit is to the southwest.",
         flags=[RLANDBIT],
         exits={
             "southwest": Exit(destination="SANDY-BEACH"),
         })

    room("ARAGAIN-FALLS", "Aragain Falls",
         flags=[RLANDBIT, SACREDBIT, ONBIT],
         exits={
             "west": Exit(destination="ON-RAINBOW",
                          condition=_cond("RAINBOW-FLAG")),
             "down": Exit(message="It's a long way..."),
             "north": Exit(destination="SHORE"),
             "up": Exit(destination="ON-RAINBOW",
                        condition=_cond("RAINBOW-FLAG")),
         },
         action_name="FALLS-ROOM",
         global_objects=["GLOBAL-WATER", "RIVER", "RAINBOW"])

    room("ON-RAINBOW", "On the Rainbow",
         ldesc="You are on top of a rainbow (I bet you never thought you would walk\non a rainbow), with a magnificent view of the Falls. The rainbow\ntravels east-west here.",
         flags=[RLANDBIT, ONBIT, SACREDBIT],
         exits={
             "west": Exit(destination="END-OF-RAINBOW"),
             "east": Exit(destination="ARAGAIN-FALLS"),
         },
         global_objects=["RAINBOW"])

    room("END-OF-RAINBOW", "End of Rainbow",
         ldesc="You are on a small, rocky beach on the continuation of the Frigid\nRiver past the Falls. The beach is narrow due to the presence of the\nWhite Cliffs. The river canyon opens here and sunlight shines in\nfrom above. A rainbow crosses over the falls to the east and a narrow\npath continues to the southwest.",
         flags=[RLANDBIT, ONBIT],
         exits={
             "up": Exit(destination="ON-RAINBOW", condition=_cond("RAINBOW-FLAG")),
             "northeast": Exit(destination="ON-RAINBOW", condition=_cond("RAINBOW-FLAG")),
             "east": Exit(destination="ON-RAINBOW", condition=_cond("RAINBOW-FLAG")),
             "southwest": Exit(destination="CANYON-BOTTOM"),
         },
         global_objects=["GLOBAL-WATER", "RAINBOW", "RIVER"])

    room("CANYON-BOTTOM", "Canyon Bottom",
         ldesc="You are beneath the walls of the river canyon which may be climbable\nhere. The lesser part of the runoff of Aragain Falls flows by below.\nTo the north is a narrow path.",
         flags=[RLANDBIT, ONBIT, SACREDBIT],
         exits={
             "up": Exit(destination="CLIFF-MIDDLE"),
             "north": Exit(destination="END-OF-RAINBOW"),
         },
         global_objects=["GLOBAL-WATER", "CLIMBABLE-CLIFF", "RIVER"])

    room("CLIFF-MIDDLE", "Rocky Ledge",
         ldesc="You are on a ledge about halfway up the wall of the river canyon.\nYou can see from here that the main flow from Aragain Falls twists\nalong a passage which it is impossible for you to enter. Below you is the\ncanyon bottom. Above you is more cliff, which appears\nclimbable.",
         flags=[RLANDBIT, ONBIT, SACREDBIT],
         exits={
             "up": Exit(destination="CANYON-VIEW"),
             "down": Exit(destination="CANYON-BOTTOM"),
         },
         global_objects=["CLIMBABLE-CLIFF", "RIVER"])

    room("CANYON-VIEW", "Canyon View",
         ldesc="You are at the top of the Great Canyon on its west wall. From here\nthere is a marvelous view of the canyon and parts of the Frigid River\nupstream.",
         flags=[RLANDBIT, ONBIT, SACREDBIT],
         exits={
             "east": Exit(destination="CLIFF-MIDDLE"),
             "down": Exit(destination="CLIFF-MIDDLE"),
             "northwest": Exit(destination="CLEARING"),
             "west": Exit(destination="FOREST-3"),
             "south": Exit(message="Storm-tossed trees block your way."),
         },
         action_name="CANYON-VIEW-F",
         global_objects=["CLIMBABLE-CLIFF", "RIVER", "RAINBOW"])

    # ---- Coal mine area ----

    room("MINE-ENTRANCE", "Mine Entrance",
         ldesc="You are standing at the entrance of what might have been a coal mine.\nThe shaft enters the west wall, and there is another exit on the south\nend of the room.",
         flags=[RLANDBIT],
         exits={
             "south": Exit(destination="SLIDE-ROOM"),
             "in": Exit(destination="SQUEEKY-ROOM"),
             "west": Exit(destination="SQUEEKY-ROOM"),
         })

    room("SQUEEKY-ROOM", "Squeaky Room",
         ldesc="You are in a small room. Strange squeaky sounds may be heard coming\nfrom the passage at the north end. You may also escape to the east.",
         flags=[RLANDBIT],
         exits={
             "north": Exit(destination="BAT-ROOM"),
             "east": Exit(destination="MINE-ENTRANCE"),
         })

    room("BAT-ROOM", "Bat Room",
         flags=[RLANDBIT, SACREDBIT],
         exits={
             "south": Exit(destination="SQUEEKY-ROOM"),
             "east": Exit(destination="SHAFT-ROOM"),
         },
         action_name="BATS-ROOM")

    room("SHAFT-ROOM", "Shaft Room",
         ldesc="This is a large room, in the middle of which is a small shaft\ndescending through the floor into darkness below. To the west and\nthe north are exits from this room. Constructed over the top of the\nshaft is a metal framework to which a heavy iron chain is attached.",
         flags=[RLANDBIT],
         exits={
             "down": Exit(message="You wouldn't fit and would die if you could."),
             "west": Exit(destination="BAT-ROOM"),
             "north": Exit(destination="SMELLY-ROOM"),
         })

    room("SMELLY-ROOM", "Smelly Room",
         ldesc="This is a small nondescript room. However, from the direction\nof a small descending staircase a foul odor can be detected. To the\nsouth is a narrow tunnel.",
         flags=[RLANDBIT],
         exits={
             "down": Exit(destination="GAS-ROOM"),
             "south": Exit(destination="SHAFT-ROOM"),
         },
         global_objects=["STAIRS"])

    room("GAS-ROOM", "Gas Room",
         ldesc="This is a small room which smells strongly of coal gas. There is a\nshort climb up some stairs and a narrow tunnel leading east.",
         flags=[RLANDBIT, SACREDBIT],
         exits={
             "up": Exit(destination="SMELLY-ROOM"),
             "east": Exit(destination="MINE-1"),
         },
         action_name="BOOM-ROOM",
         global_objects=["STAIRS"])

    room("LADDER-TOP", "Ladder Top",
         ldesc="This is a very small room. In the corner is a rickety wooden\nladder, leading downward. It might be safe to descend. There is\nalso a staircase leading upward.",
         flags=[RLANDBIT],
         exits={
             "down": Exit(destination="LADDER-BOTTOM"),
             "up": Exit(destination="MINE-4"),
         },
         global_objects=["LADDER", "STAIRS"])

    room("LADDER-BOTTOM", "Ladder Bottom",
         ldesc="This is a rather wide room. On one side is the bottom of a\nnarrow wooden ladder. To the west and the south are passages\nleaving the room.",
         flags=[RLANDBIT],
         exits={
             "south": Exit(destination="DEAD-END-5"),
             "west": Exit(destination="TIMBER-ROOM"),
             "up": Exit(destination="LADDER-TOP"),
         },
         global_objects=["LADDER"])

    room("DEAD-END-5", "Dead End",
         ldesc="You have come to a dead end in the mine.",
         flags=[RLANDBIT],
         exits={
             "north": Exit(destination="LADDER-BOTTOM"),
         })

    room("TIMBER-ROOM", "Timber Room",
         ldesc="This is a long and narrow passage, which is cluttered with broken\ntimbers. A wide passage comes from the east and turns at the\nwest end of the room into a very narrow passageway. From the west\ncomes a strong draft.",
         flags=[RLANDBIT, SACREDBIT],
         exits={
             "east": Exit(destination="LADDER-BOTTOM"),
             "west": Exit(destination="LOWER-SHAFT",
                          condition=_cond("EMPTY-HANDED"),
                          fail_message="You cannot fit through this passage with that load."),
         },
         action_name="NO-OBJS")

    room("LOWER-SHAFT", "Drafty Room",
         ldesc="This is a small drafty room in which is the bottom of a long\nshaft. To the south is a passageway and to the east a very narrow\npassage. In the shaft can be seen a heavy iron chain.",
         flags=[RLANDBIT, SACREDBIT],
         exits={
             "south": Exit(destination="MACHINE-ROOM"),
             "out": Exit(destination="TIMBER-ROOM",
                         condition=_cond("EMPTY-HANDED"),
                         fail_message="You cannot fit through this passage with that load."),
             "east": Exit(destination="TIMBER-ROOM",
                          condition=_cond("EMPTY-HANDED"),
                          fail_message="You cannot fit through this passage with that load."),
         },
         action_name="NO-OBJS")

    room("MACHINE-ROOM", "Machine Room",
         flags=[RLANDBIT],
         exits={
             "north": Exit(destination="LOWER-SHAFT"),
         },
         action_name="MACHINE-ROOM-FCN")

    # ---- Coal mine ----

    room("MINE-1", "Coal Mine",
         ldesc="This is a nondescript part of a coal mine.",
         flags=[RLANDBIT],
         exits={
             "north": Exit(destination="GAS-ROOM"),
             "east": Exit(destination="MINE-1"),
             "northeast": Exit(destination="MINE-2"),
         })

    room("MINE-2", "Coal Mine",
         ldesc="This is a nondescript part of a coal mine.",
         flags=[RLANDBIT],
         exits={
             "north": Exit(destination="MINE-2"),
             "south": Exit(destination="MINE-1"),
             "southeast": Exit(destination="MINE-3"),
         })

    room("MINE-3", "Coal Mine",
         ldesc="This is a nondescript part of a coal mine.",
         flags=[RLANDBIT],
         exits={
             "south": Exit(destination="MINE-3"),
             "southwest": Exit(destination="MINE-4"),
             "east": Exit(destination="MINE-2"),
         })

    room("MINE-4", "Coal Mine",
         ldesc="This is a nondescript part of a coal mine.",
         flags=[RLANDBIT],
         exits={
             "north": Exit(destination="MINE-3"),
             "west": Exit(destination="MINE-4"),
             "down": Exit(destination="LADDER-TOP"),
         })

    room("SLIDE-ROOM", "Slide Room",
         ldesc="This is a small chamber, which appears to have been part of a\ncoal mine. On the south wall of the chamber the letters \"Granite\nWall\" are etched in the rock. To the east is a long passage, and\nthere is a steep metal slide twisting downward. To the north is\na small opening.",
         flags=[RLANDBIT],
         exits={
             "east": Exit(destination="COLD-PASSAGE"),
             "north": Exit(destination="MINE-ENTRANCE"),
             "down": Exit(destination="CELLAR"),
         },
         global_objects=["SLIDE"])


# ---------------------------------------------------------------------------
# Helper exit condition functions
# ---------------------------------------------------------------------------

def _grating_cond(world) -> bool:
    """Condition for going down from GRATING-CLEARING into GRATING-ROOM."""
    if not world.get_global("GRATE-REVEALED"):
        print("You can't go that way.")
        return False
    if world.flag_set("GRATE", OPENBIT):
        return True
    print("The grating is closed!")
    grate = world.objects.get("GRATE")
    if grate:
        world.it_object = grate
    return False


def _trap_door_cond(world) -> bool:
    """Condition for going down from LIVING-ROOM through trap door to CELLAR."""
    if not world.get_global("RUG-MOVED"):
        print("You can't go that way.")
        return False
    if world.flag_set("TRAP-DOOR", OPENBIT):
        return True
    print("The trap door is closed.")
    trap = world.objects.get("TRAP-DOOR")
    if trap:
        world.it_object = trap
    return False


def _up_chimney(world) -> bool:
    """Condition for going up from STUDIO through chimney to KITCHEN.

    ZIL UP-CHIMNEY-FUNCTION rules (from 1actions.zil):
      - 0 items carried → fail ("Going up empty-handed is a bad idea.")
      - 1-2 items carried AND lamp is one of them → succeed
      - 3+ items OR lamp not carried → fail
    Side-effect: if the trap door is closed, clear its TOUCHBIT so it
    redescribes on the next visit.
    """
    player = world.winner
    if player is None:
        return False
    items = list(player.contents)
    lamp = world.objects.get("LAMP")
    if not items:
        print("Going up empty-handed is a bad idea.")
        return False
    if len(items) <= 2 and lamp and lamp in items:
        trap_door = world.objects.get("TRAP-DOOR")
        if trap_door and not trap_door.has_flag(OPENBIT):
            trap_door.clear_flag(TOUCHBIT)
        return True
    print("You can't get up there with what you're carrying.")
    return False


def _maze_diode_warn(world) -> bool:
    """Condition for maze diode exits: always succeeds but prints a warning."""
    print("You won't be able to get back up to the tunnel you are going through\nwhen it gets to the next room.\n")
    return True
