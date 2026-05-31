"""
Action handlers for Zork I.

Provides ACTION_HANDLERS (object actions) and ROOM_ACTION_HANDLERS (room
actions) dicts, keyed by the ZIL routine name used in objects.py and rooms.py.

Each handler signature:
    object action:  handler(world: World) -> int
    room action:    handler(world: World, msg: int = 0) -> int

Return M_HANDLED (1) to consume the action, M_NOT_HANDLED (0) to pass on,
M_FATAL (2) for game-ending events.
"""

from __future__ import annotations

import random
from typing import TYPE_CHECKING

from engine.game import M_FATAL, M_HANDLED, M_NOT_HANDLED, M_BEG, M_ENTER, M_LOOK, M_END
from engine.world import OPENBIT, ONBIT, INVISIBLE, TOUCHBIT, NDESCBIT, FIGHTBIT, STAGGERED, WEAPONBIT, ACTORBIT, SACREDBIT, TAKEBIT, RLANDBIT

if TYPE_CHECKING:
    from engine.world import World

NONLANDBIT = "NONLANDBIT"

# ---------------------------------------------------------------------------
# River system tables (mirrors ZIL globals in 1actions.zil)
# ---------------------------------------------------------------------------

_RIVER_ROOMS  = {"RIVER-1", "RIVER-2", "RIVER-3", "RIVER-4", "RIVER-5"}
_ON_RIVER     = _RIVER_ROOMS | {"RESERVOIR", "IN-STREAM"}
_RIVER_NEXT   = {"RIVER-1": "RIVER-2", "RIVER-2": "RIVER-3",
                 "RIVER-3": "RIVER-4", "RIVER-4": "RIVER-5"}
_RIVER_SPEEDS = {"RIVER-1": 4, "RIVER-2": 4, "RIVER-3": 3, "RIVER-4": 2, "RIVER-5": 1}
_RIVER_LAUNCH = {
    "DAM-BASE":          "RIVER-1",
    "WHITE-CLIFFS-NORTH": "RIVER-3",
    "WHITE-CLIFFS-SOUTH": "RIVER-4",
    "SHORE":             "RIVER-5",
    "SANDY-BEACH":       "RIVER-4",
    "RESERVOIR-SOUTH":   "RESERVOIR",
    "RESERVOIR-NORTH":   "RESERVOIR",
    "STREAM-VIEW":       "IN-STREAM",
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _verb(world: "World", *verbs: str) -> bool:
    """Return True if world.prsa matches any of the given action names."""
    return world.prsa in verbs


def _in_room(world: "World", room_name: str) -> bool:
    return world.here is not None and world.here.name == room_name


def _flag(world: "World", name: str) -> bool:
    return bool(world.get_global(name))


def _set_flag(world: "World", name: str, value) -> None:
    world.set_global(name, value)


def _obj(world: "World", name: str):
    return world.objects.get(name)


def _flag_set(world: "World", obj_name: str, flag: str) -> bool:
    return world.flag_set(obj_name, flag)


# ---------------------------------------------------------------------------
# Lamp / clock constants
# ---------------------------------------------------------------------------

# (countdown_ticks, warning_message) — last entry has ticks=0 (burn-out)
_LAMP_STAGES = [
    (100, "The lamp appears a bit dimmer."),
    (70,  "The lamp is definitely dimmer now."),
    (15,  "The lamp is nearly out."),
    (0,   None),
]


def i_lantern(world: "World") -> bool:
    """Clock interrupt: advance the lamp battery countdown."""
    lamp = world.objects.get("LAMP")
    if lamp is None:
        return False

    stage = int(world.get_global("LAMP-STAGE") or 0)
    if stage >= len(_LAMP_STAGES):
        return False

    ticks, message = _LAMP_STAGES[stage]

    accessible = (lamp.location is world.here or lamp.location is world.winner)

    if ticks == 0:
        lamp.clear_flag(ONBIT)
        lamp.set_flag("RMUNGBIT")
        if accessible:
            print("Your brass lantern has run out of power.")
        world.game.clock.disable("I-LANTERN")
    else:
        if accessible and message:
            print(message)
        next_stage = stage + 1
        world.set_global("LAMP-STAGE", next_stage)
        next_ticks = _LAMP_STAGES[next_stage][0] if next_stage < len(_LAMP_STAGES) else 1
        world.game.clock.queue("I-LANTERN", i_lantern, max(next_ticks, 1))

    return accessible


def i_xb(world: "World") -> bool:
    """Clock interrupt: ceremony timeout — wraiths recover if candles weren't lit in time."""
    if not world.get_global("XC"):
        if world.here and world.here.name == "ENTRANCE-TO-HADES":
            print("The tension of this ceremony is broken, and the wraiths, amused but\n"
                  "shaken at your clumsy attempt, resume their hideous jeering.")
    world.set_global("XB", False)
    return False


def i_xc(world: "World") -> bool:
    """Clock interrupt: book-reading window expired — full ceremony reset."""
    world.set_global("XC", False)
    i_xb(world)
    return False


def i_xbh(world: "World") -> bool:
    """Clock interrupt (or immediate call): hot bell cools, regular bell returns."""
    hot_bell = world.objects.get("HOT-BELL")
    bell = world.objects.get("BELL")
    entrance = world.rooms.get("ENTRANCE-TO-HADES")
    if hot_bell:
        world.move_object(hot_bell, None)
    if bell and entrance:
        world.move_object(bell, entrance)
    if world.here is entrance:
        print("The bell appears to have cooled down.")
    return False


def i_maint_room(world: "World") -> bool:
    """Clock demon: advance maintenance room water flood after blue button is pushed."""
    water_level = world.get_global("WATER-LEVEL") or 0
    if water_level == 0 or water_level >= 15:
        return False

    water_level += 1
    world.set_global("WATER-LEVEL", water_level)

    maint_room = world.rooms.get("MAINTENANCE-ROOM")
    in_room = world.here is maint_room

    if water_level >= 14:
        wrench = world.objects.get("WRENCH")
        screwdriver = world.objects.get("SCREWDRIVER")
        if wrench and wrench.location is maint_room:
            world.move_object(wrench, None)
        if screwdriver and screwdriver.location is maint_room:
            world.move_object(screwdriver, None)
        if in_room:
            print("The water level is now at the ceiling. You are unable to breathe and drown.")
        world.set_global("WATER-LEVEL", 15)
        return in_room

    world.game.clock.queue("I-MAINT-ROOM", i_maint_room, 1)
    if in_room:
        _water_msgs = {
            1:  "Water is beginning to rise in the room.",
            7:  "The water is rising around your feet.",
            10: "The water is now up to your waist.",
            13: "The water level is nearly at the ceiling.",
        }
        msg = _water_msgs.get(water_level, "")
        if msg:
            print(msg)
            return True
    return False


# ---------------------------------------------------------------------------
# Object action handlers
# ---------------------------------------------------------------------------

def _board_f(world: "World") -> int:
    if _verb(world, "V-TAKE", "V-EXAMINE"):
        print("The boards are securely fastened.")
        return M_HANDLED
    return M_NOT_HANDLED


def _teeth_f(world: "World") -> int:
    prso = world.prso
    prsi = world.prsi
    if _verb(world, "V-BRUSH") and prso and prso.name == "TEETH":
        putty = _obj(world, "PUTTY")
        if putty and prsi and prsi.name == "PUTTY" and putty.location is world.winner:
            world.game.jigs_up(
                "Well, you seem to have been brushing your teeth with some sort of\n"
                "glue. As a result, your mouth gets glued together (with your nose)\n"
                "and you die of respiratory failure."
            )
            return M_FATAL
        if not prsi:
            print(
                "Dental hygiene is highly recommended, but I'm not sure what you want\n"
                "to brush them with."
            )
            return M_HANDLED
        print(f"A nice idea, but with a {prsi.desc}?")
        return M_HANDLED
    return M_NOT_HANDLED


def _granite_wall_f(world: "World") -> int:
    here = world.here
    if here is None:
        return M_NOT_HANDLED
    if here.name == "NORTH-TEMPLE":
        if _verb(world, "V-FIND"):
            print("The west wall is solid granite here.")
            return M_HANDLED
        if _verb(world, "V-TAKE", "V-RAISE", "V-LOWER"):
            print("It's solid granite.")
            return M_HANDLED
    elif here.name == "TREASURE-ROOM":
        if _verb(world, "V-FIND"):
            print("The east wall is solid granite here.")
            return M_HANDLED
        if _verb(world, "V-TAKE", "V-RAISE", "V-LOWER"):
            print("It's solid granite.")
            return M_HANDLED
    elif here.name == "SLIDE-ROOM":
        if _verb(world, "V-FIND", "V-READ"):
            print("It only SAYS \"Granite Wall\".")
            return M_HANDLED
        print("The wall isn't granite.")
        return M_HANDLED
    else:
        print("There is no granite wall here.")
        return M_HANDLED
    return M_NOT_HANDLED


def _songbird_f(world: "World") -> int:
    if _verb(world, "V-FIND", "V-TAKE"):
        print("The songbird is not here but is probably nearby.")
        return M_HANDLED
    if _verb(world, "V-LISTEN"):
        print("You can't hear the songbird now.")
        return M_HANDLED
    if _verb(world, "V-FOLLOW"):
        print("It can't be followed.")
        return M_HANDLED
    print("You can't see any songbird here.")
    return M_HANDLED


def _white_house_f(world: "World") -> int:
    here = world.here
    if here is None:
        return M_NOT_HANDLED
    if here.name in ("KITCHEN", "LIVING-ROOM", "ATTIC"):
        if _verb(world, "V-FIND"):
            print("Why not find your brains?")
            return M_HANDLED
        return M_NOT_HANDLED
    if here.name not in ("EAST-OF-HOUSE", "WEST-OF-HOUSE", "NORTH-OF-HOUSE", "SOUTH-OF-HOUSE"):
        if _verb(world, "V-FIND"):
            if here.name == "CLEARING":
                print("It seems to be to the west.")
            else:
                print("It was here just a minute ago....")
            return M_HANDLED
        print("You're not at the house.")
        return M_HANDLED
    if _verb(world, "V-FIND"):
        print("It's right here! Are you blind or something?")
        return M_HANDLED
    if _verb(world, "V-EXAMINE"):
        print(
            "The house is a beautiful colonial house which is painted white.\n"
            "It is clear that the owners must have been extremely wealthy."
        )
        return M_HANDLED
    if _verb(world, "V-BURN"):
        print("You must be joking.")
        return M_HANDLED
    return M_NOT_HANDLED


def _forest_f(world: "World") -> int:
    if _verb(world, "V-FIND"):
        print("You cannot see the forest for the trees.")
        return M_HANDLED
    if _verb(world, "V-LISTEN"):
        print("The pines and the hemlocks seem to be murmuring.")
        return M_HANDLED
    return M_NOT_HANDLED


def _mountain_range_f(world: "World") -> int:
    if _verb(world, "V-CLIMB"):
        print("Don't you believe me? The mountains are impassable!")
        return M_HANDLED
    return M_NOT_HANDLED


def _water_f(world: "World") -> int:
    if _verb(world, "V-DRINK", "V-EAT"):
        print("Thank you very much. I was rather thirsty (from all this talking, probably).")
        return M_HANDLED
    if _verb(world, "V-TAKE"):
        print("The water slips through your fingers.")
        return M_HANDLED
    if _verb(world, "V-DROP"):
        water = _obj(world, "WATER")
        if water:
            world.move_object(water, None)
        print("The water spills to the floor and evaporates immediately.")
        return M_HANDLED
    return M_NOT_HANDLED


def _kitchen_window_f(world: "World") -> int:
    win = _obj(world, "KITCHEN-WINDOW")
    if _verb(world, "V-OPEN"):
        if win and win.has_flag(OPENBIT):
            print("It is already open.")
        else:
            if win:
                win.set_flag(OPENBIT)
            print("With great effort, you open the window far enough to allow entry.")
        return M_HANDLED
    if _verb(world, "V-CLOSE"):
        if win and not win.has_flag(OPENBIT):
            print("It is already closed.")
        else:
            if win:
                win.clear_flag(OPENBIT)
            print("The window closes (more easily than it opened).")
        return M_HANDLED
    return M_NOT_HANDLED


def _ghosts_f(world: "World") -> int:
    if _verb(world, "V-ATTACK"):
        print("How can you attack a spirit with material objects?")
        return M_HANDLED
    print("You seem unable to interact with these spirits.")
    return M_HANDLED


def _basket_f(world: "World") -> int:
    if _verb(world, "V-RAISE"):
        cage_top = world.get_global("CAGE-TOP")
        if cage_top:
            print("You can't do that.")
        else:
            raised = _obj(world, "RAISED-BASKET")
            lowered = _obj(world, "LOWERED-BASKET")
            shaft = world.rooms.get("SHAFT-ROOM")
            lower = world.rooms.get("LOWER-SHAFT")
            if raised and shaft:
                world.move_object(raised, shaft)
            if lowered and lower:
                world.move_object(lowered, lower)
            world.set_global("CAGE-TOP", True)
            print("The basket is raised to the top of the shaft.")
        return M_HANDLED
    if _verb(world, "V-LOWER"):
        cage_top = world.get_global("CAGE-TOP")
        if not cage_top:
            print("You can't do that.")
        else:
            raised = _obj(world, "RAISED-BASKET")
            lowered = _obj(world, "LOWERED-BASKET")
            shaft = world.rooms.get("SHAFT-ROOM")
            lower = world.rooms.get("LOWER-SHAFT")
            if raised and lower:
                world.move_object(raised, lower)
            if lowered and shaft:
                world.move_object(lowered, shaft)
            world.set_global("CAGE-TOP", False)
            print("The basket is lowered to the bottom of the shaft.")
        return M_HANDLED
    if _verb(world, "V-TAKE"):
        print("The cage is securely fastened to the iron chain.")
        return M_HANDLED
    return M_NOT_HANDLED


def _bat_f(world: "World") -> int:
    if _verb(world, "V-TAKE", "V-ATTACK"):
        garlic = _obj(world, "GARLIC")
        if garlic and (garlic.location is world.winner or garlic.location is world.here):
            print("You can't reach him; he's on the ceiling.")
        else:
            import random
            bat_drops = [
                "MINE-1", "MINE-2", "MINE-3", "MINE-4",
                "LADDER-TOP", "LADDER-BOTTOM", "SQUEEKY-ROOM", "MINE-ENTRANCE",
            ]
            print("The bat grabs you by the scruff of your neck and lifts you away....\n")
            dest_name = random.choice(bat_drops)
            dest = world.rooms.get(dest_name)
            if dest:
                world.game.enter_room(dest)
        return M_HANDLED
    return M_NOT_HANDLED


def _bell_f(world: "World") -> int:
    if _verb(world, "V-RING"):
        if _in_room(world, "ENTRANCE-TO-HADES") and not _flag(world, "LLD-FLAG"):
            return M_NOT_HANDLED
        print("Ding, dong.")
        return M_HANDLED
    return M_NOT_HANDLED


def _hot_bell_f(world: "World") -> int:
    if _verb(world, "V-TAKE"):
        print("The bell is very hot and cannot be taken.")
        return M_HANDLED
    if _verb(world, "V-RING"):
        print("The bell is too hot to reach.")
        return M_HANDLED
    if _verb(world, "V-POUR-ON"):
        if world.prso:
            world.move_object(world.prso, None)
        print("The water cools the bell and is evaporated.")
        world.game.clock.queue("I-XBH", i_xbh, 0)
        i_xbh(world)
        return M_HANDLED
    return M_NOT_HANDLED


def _boarded_window_fcn(world: "World") -> int:
    if _verb(world, "V-OPEN"):
        print("The windows are boarded and can't be opened.")
        return M_HANDLED
    return M_NOT_HANDLED


def _crack_fcn(world: "World") -> int:
    if _verb(world, "V-THROUGH"):
        print("You can't fit through the crack.")
        return M_HANDLED
    return M_NOT_HANDLED


def _trophy_case_fcn(world: "World") -> int:
    prso = world.prso
    tc = _obj(world, "TROPHY-CASE")
    if _verb(world, "V-TAKE") and prso and prso is tc:
        print("The trophy case is securely fastened to the wall.")
        return M_HANDLED
    return M_NOT_HANDLED


def _rug_fcn(world: "World") -> int:
    trap = _obj(world, "TRAP-DOOR")
    if _verb(world, "V-RAISE"):
        if _flag(world, "RUG-MOVED"):
            print("The rug is too heavy to lift.")
        else:
            print("The rug is too heavy to lift, but in trying to take it you have\nnoticed an irregularity beneath it.")
        return M_HANDLED
    if _verb(world, "V-MOVE", "V-PUSH"):
        if _flag(world, "RUG-MOVED"):
            print("Having moved the carpet previously, you find it impossible to move\nit again.")
        else:
            print(
                "With a great effort, the rug is moved to one side of the room, revealing\n"
                "the dusty cover of a closed trap door."
            )
            if trap:
                trap.clear_flag(INVISIBLE)
                world.it_object = trap
            world.set_global("RUG-MOVED", True)
        return M_HANDLED
    if _verb(world, "V-TAKE"):
        print("The rug is extremely heavy and cannot be carried.")
        return M_HANDLED
    return M_NOT_HANDLED


def _trap_door_fcn(world: "World") -> int:
    trap = _obj(world, "TRAP-DOOR")
    if _verb(world, "V-RAISE", "V-OPEN"):
        if trap:
            if trap.has_flag(OPENBIT):
                print("It is already open.")
            else:
                trap.set_flag(OPENBIT)
                print("The door reluctantly opens to reveal a rickety staircase descending into darkness.")
        return M_HANDLED
    if _verb(world, "V-CLOSE"):
        if trap:
            if not trap.has_flag(OPENBIT):
                print("It is already closed.")
            else:
                trap.clear_flag(OPENBIT)
                print("The door swings shut and closes.")
        return M_HANDLED
    if _verb(world, "V-EXAMINE"):
        if trap and trap.has_flag(OPENBIT):
            print("You see a rickety staircase descending into darkness.")
        else:
            print("It's closed.")
        return M_HANDLED
    return M_NOT_HANDLED


def _front_door_fcn(world: "World") -> int:
    if _verb(world, "V-OPEN", "V-CLOSE"):
        print("The door is nailed shut.")
        return M_HANDLED
    if _verb(world, "V-READ"):
        print("The engravings translate to \"This space intentionally left blank.\"")
        return M_HANDLED
    return M_NOT_HANDLED


def _axe_f(world: "World") -> int:
    if _flag(world, "TROLL-FLAG"):
        return M_NOT_HANDLED
    troll = _obj(world, "TROLL")
    if _verb(world, "V-TAKE") and troll and troll.location is world.here:
        print("The troll swings it out of your reach.")
        return M_HANDLED
    return M_NOT_HANDLED


def _stiletto_function(world: "World") -> int:
    thief = _obj(world, "THIEF")
    stiletto = _obj(world, "STILETTO")
    if (_verb(world, "V-TAKE") and thief
            and not thief.has_flag(INVISIBLE)
            and thief.location is world.here):
        if stiletto and stiletto.location is thief:
            print("The thief swings it out of your reach.")
        else:
            print("The stiletto seems white-hot. You can't hold on to it.")
        return M_HANDLED
    return M_NOT_HANDLED


def _troll_fcn(world: "World") -> int:
    if _verb(world, "V-TELL"):
        print("The troll isn't much of a conversationalist.")
        return M_HANDLED
    if _verb(world, "V-LISTEN"):
        print("Every so often the troll says something, probably uncomplimentary, in\nhis guttural tongue.")
        return M_HANDLED
    if _verb(world, "V-EXAMINE"):
        troll = _obj(world, "TROLL")
        if troll and troll.ldesc:
            print(troll.ldesc)
        else:
            print("A nasty-looking troll, brandishing a bloody axe, blocks all passages out of the room.")
        return M_HANDLED
    if _verb(world, "V-ATTACK"):
        return _hero_blow(world, "TROLL", "TROLL-FLAG")
    if _verb(world, "V-THROW", "V-GIVE"):
        prso = world.prso
        troll = _obj(world, "TROLL")
        if prso and troll:
            if prso.name in ("AXE", "KNIFE", "SWORD"):
                if world.here:
                    world.move_object(prso, world.here)
                print(
                    "The troll scratches his head in confusion" if world.prsa == "V-GIVE"
                    else "The troll, who is remarkably coordinated, catches the "
                    + (prso.desc if prso else "it")
                )
                if random.randint(1, 5) == 1:
                    print(" and eats it hungrily. Poor troll, he dies from an internal "
                          "hemorrhage\nand his carcass disappears in a sinister black fog.")
                    if world.here:
                        world.move_object(prso, world.here)
                    _kill_villain(world, troll, "TROLL", "TROLL-FLAG")
                else:
                    if world.here:
                        world.move_object(prso, world.here)
                    troll.set_flag(FIGHTBIT)
                    print(" and throws it back. He does not look pleased.")
            else:
                print(f"The troll, not overly proud, graciously accepts the gift and eats it.")
                if world.here:
                    world.move_object(prso, world.here)
        return M_HANDLED
    return M_NOT_HANDLED


def _grate_function(world: "World") -> int:
    grate = _obj(world, "GRATE")
    keys = _obj(world, "KEYS")
    prsi = world.prsi
    here = world.here
    if grate is None:
        return M_NOT_HANDLED
    if _verb(world, "V-UNLOCK"):
        key = prsi if (prsi and prsi.name == "KEYS") else _obj(world, "KEYS")
        if key is None or (world.winner and key.location is not world.winner):
            print("You don't have anything to unlock it with.")
            return M_HANDLED
        if here and here.name == "GRATING-ROOM":
            world.set_global("GRUNLOCK", True)
            print("The grate is unlocked.")
        else:
            print("You can't reach the lock from here.")
        return M_HANDLED
    if _verb(world, "V-LOCK"):
        if here and here.name == "GRATING-ROOM":
            world.set_global("GRUNLOCK", False)
            print("The grate is locked.")
        else:
            print("You can't lock it from this side.")
        return M_HANDLED
    if _verb(world, "V-OPEN"):
        if not world.get_global("GRUNLOCK"):
            print("The grating is locked.")
            return M_HANDLED
        if grate.has_flag(OPENBIT):
            print("It is already open.")
        else:
            grate.set_flag(OPENBIT)
            grating_room = world.rooms.get("GRATING-ROOM")
            if grating_room:
                grating_room.set_flag(ONBIT)
            if here and here.name != "GRATING-CLEARING" and not world.get_global("GRATE-REVEALED"):
                print("A pile of leaves falls onto your head and to the ground.")
                world.set_global("GRATE-REVEALED", True)
                leaves = _obj(world, "LEAVES")
                if leaves and here:
                    world.move_object(leaves, here)
            if here and here.name == "GRATING-CLEARING":
                print("The grating opens.")
            else:
                print("The grating opens to reveal trees above you.")
        return M_HANDLED
    if _verb(world, "V-CLOSE"):
        if not world.get_global("GRUNLOCK"):
            print("The grating is locked.")
            return M_HANDLED
        if not grate.has_flag(OPENBIT):
            print("It is already closed.")
        else:
            grate.clear_flag(OPENBIT)
            grating_room = world.rooms.get("GRATING-ROOM")
            if grating_room:
                grating_room.clear_flag(ONBIT)
            print("The grating is closed.")
        return M_HANDLED
    if _verb(world, "V-PUT"):
        prso = world.prso
        if prso and getattr(prso, "size", 0) > 20:
            print("It won't fit through the grating.")
        elif prso:
            grating_room = world.rooms.get("GRATING-ROOM")
            if grating_room:
                world.move_object(prso, grating_room)
            print(f"The {prso.desc} goes through the grating into the darkness below.")
        return M_HANDLED
    return M_NOT_HANDLED


def _leaf_pile(world: "World") -> int:
    prso = world.prso
    if _verb(world, "V-COUNT"):
        print("There are 69,105 leaves here.")
        return M_HANDLED
    if _verb(world, "V-BURN"):
        grate = _obj(world, "GRATE")
        if grate and not grate.has_flag(INVISIBLE) and not world.get_global("GRATE-REVEALED"):
            world.set_global("GRATE-REVEALED", True)
            if grate:
                grate.clear_flag(INVISIBLE)
        if prso:
            world.move_object(prso)
        print("The leaves burn.")
        return M_HANDLED
    if _verb(world, "V-MOVE", "V-TAKE"):
        if not world.get_global("GRATE-REVEALED"):
            grate = _obj(world, "GRATE")
            if grate:
                grate.clear_flag(INVISIBLE)
                world.it_object = grate
            world.set_global("GRATE-REVEALED", True)
            if _verb(world, "V-MOVE"):
                print("In disturbing the pile of leaves, a grating is revealed.")
                return M_HANDLED
        return M_NOT_HANDLED
    return M_NOT_HANDLED


def _leaves_appear_action(world: "World") -> int:
    return _leaf_pile(world)


def _rusty_knife_fcn(world: "World") -> int:
    if _verb(world, "V-TAKE"):
        sword = _obj(world, "SWORD")
        if sword and sword.location is world.winner:
            print("As you touch the rusty knife, your sword gives a single pulse of blinding\nblue light.")
        return M_NOT_HANDLED
    if _verb(world, "V-ATTACK", "V-SWING"):
        prso = world.prso
        prsi = world.prsi
        rusty = _obj(world, "RUSTY-KNIFE")
        if (prsi and prsi.name == "RUSTY-KNIFE") or (prso and prso.name == "RUSTY-KNIFE" and prsi):
            if rusty:
                world.move_object(rusty)
            world.game.jigs_up(
                "As the knife approaches its victim, your mind is submerged by an\n"
                "overmastering will. Slowly, your hand turns, until the rusty blade\n"
                "is an inch from your neck. The knife seems to sing as it savagely\n"
                "slits your throat."
            )
            return M_FATAL
    return M_NOT_HANDLED


def _knife_f(world: "World") -> int:
    if _verb(world, "V-TAKE"):
        attic_table = _obj(world, "ATTIC-TABLE")
        if attic_table:
            attic_table.clear_flag(NDESCBIT)
    return M_NOT_HANDLED


def _skeleton_fcn(world: "World") -> int:
    if _verb(world, "V-TAKE", "V-RUB", "V-MOVE", "V-PUSH", "V-RAISE", "V-LOWER",
             "V-ATTACK", "V-KICK", "V-KISS"):
        print(
            "A ghost appears in the room and is appalled at your desecration of\n"
            "the remains of a fellow adventurer. He casts a curse on your valuables\n"
            "and banishes them to the Land of the Living Dead. The ghost leaves,\n"
            "muttering obscenities."
        )
        lld = world.rooms.get("LAND-OF-LIVING-DEAD")
        if lld and world.winner:
            for item in list(world.winner.contents):
                world.move_object(item, lld)
        return M_HANDLED
    return M_NOT_HANDLED


def _torch_object(world: "World") -> int:
    if _verb(world, "V-EXAMINE"):
        print("The torch is burning.")
        return M_HANDLED
    if _verb(world, "V-LAMP-OFF"):
        print("You nearly burn your hand trying to extinguish the flame.")
        return M_HANDLED
    return M_NOT_HANDLED


def _mirror_mirror(world: "World") -> int:
    if _verb(world, "V-RUB"):
        mirror1 = world.rooms.get("MIRROR-ROOM-1")
        mirror2 = world.rooms.get("MIRROR-ROOM-2")
        here = world.here
        if here and mirror1 and mirror2:
            other = mirror2 if here is mirror1 else mirror1
            here_items = list(here.contents)
            other_items = list(other.contents)
            for item in here_items:
                if item is not world.winner:
                    world.move_object(item, other)
            for item in other_items:
                world.move_object(item, here)
            world.game.enter_room(other)
            print("There is a rumble from deep within the earth and the room shakes.")
        return M_HANDLED
    if _verb(world, "V-EXAMINE"):
        if world.get_global("MIRROR-MUNG"):
            print("The mirror is broken into many pieces.")
        else:
            print("There is an ugly person staring back at you.")
        return M_HANDLED
    if _verb(world, "V-ATTACK"):
        print("The mirror shatters into a thousand pieces.")
        world.set_global("MIRROR-MUNG", True)
        return M_HANDLED
    return M_NOT_HANDLED


def _bolt_f(world: "World") -> int:
    if _verb(world, "V-TURN"):
        wrench = _obj(world, "WRENCH")
        if world.prsi is wrench:
            if world.get_global("GATE-FLAG"):
                if world.get_global("GATES-OPEN"):
                    world.set_global("GATES-OPEN", False)
                    world.set_global("LOW-TIDE", False)
                    trunk = _obj(world, "TRUNK")
                    if trunk:
                        trunk.set_flag("INVISIBLE")
                    reservoir = world.rooms.get("RESERVOIR")
                    if reservoir:
                        reservoir.set_flag("NONLANDBIT")
                        reservoir.clear_flag("RLANDBIT")
                    print("The sluice gates close and water starts to collect behind the dam.")
                else:
                    world.set_global("GATES-OPEN", True)
                    world.set_global("LOW-TIDE", True)
                    trunk = _obj(world, "TRUNK")
                    if trunk:
                        trunk.clear_flag("INVISIBLE")
                    reservoir = world.rooms.get("RESERVOIR")
                    if reservoir:
                        reservoir.clear_flag("NONLANDBIT")
                        reservoir.set_flag("RLANDBIT")
                    print("The sluice gates open and water pours through the dam.")
            else:
                print("The bolt won't turn with your best effort.")
        else:
            prsi = world.prsi
            desc = prsi.desc if prsi else "that"
            print(f"The bolt won't turn using the {desc}.")
        return M_HANDLED
    return M_NOT_HANDLED


def _button_f(world: "World") -> int:
    if _verb(world, "V-READ"):
        print("They're greek to you.")
        return M_HANDLED
    if _verb(world, "V-PUSH", "V-PRESS"):
        prso = world.prso
        yellow = _obj(world, "YELLOW-BUTTON")
        brown  = _obj(world, "BROWN-BUTTON")
        red    = _obj(world, "RED-BUTTON")
        blue   = _obj(world, "BLUE-BUTTON")
        dam_room   = world.rooms.get("DAM-ROOM")
        maint_room = world.rooms.get("MAINTENANCE-ROOM")
        if prso is yellow:
            if dam_room:
                dam_room.clear_flag("TOUCHBIT")
            world.set_global("GATE-FLAG", True)
            print("Click.")
        elif prso is brown:
            if dam_room:
                dam_room.clear_flag("TOUCHBIT")
            world.set_global("GATE-FLAG", False)
            print("Click.")
        elif prso is red:
            if maint_room:
                if maint_room.has_flag(ONBIT):
                    maint_room.clear_flag(ONBIT)
                    print("The lights within the room shut off.")
                else:
                    maint_room.set_flag(ONBIT)
                    print("The lights within the room come on.")
        elif prso is blue:
            water_level = world.get_global("WATER-LEVEL") or 0
            if water_level == 0:
                leak = _obj(world, "LEAK")
                if leak:
                    leak.clear_flag(INVISIBLE)
                print(
                    "There is a rumbling sound and a stream of water appears to burst\n"
                    "from the east wall of the room (apparently, a leak has occurred in a\n"
                    "pipe)."
                )
                world.set_global("WATER-LEVEL", 1)
                world.game.clock.queue("I-MAINT-ROOM", i_maint_room, 1)
            else:
                print("The blue button appears to be jammed.")
        else:
            print("Click.")
        return M_HANDLED
    return M_NOT_HANDLED


def _bubble_f(world: "World") -> int:
    if _verb(world, "V-PUSH", "V-PRESS"):
        print("Click.")
        return M_HANDLED
    return M_NOT_HANDLED


def _black_book(world: "World") -> int:
    if _verb(world, "V-READ"):
        text = (
            "Commandment #12592\n\n"
            "Oh ye who go about saying unto each:  \"Hello sailor\":\n"
            "Dost thou know the magnitude of thy sin before the gods?\n"
            "Yea, verily, thou shalt be ground between two stones.\n"
            "Shall the angry gods cast thy body into the whirlpool?\n"
            "Surely, thy eye shall be put out with a sharp stick!\n"
            "Even unto the ends of the earth shalt thou wander and\n"
            "Unto the land of the dead shalt thou be sent at last.\n"
            "Surely thou shalt repent of thy cunning."
        )
        print(text)
        return M_HANDLED
    return M_NOT_HANDLED


def _sceptre_function(world: "World") -> int:
    if _verb(world, "V-EXAMINE"):
        print("The sceptre is ornamented with colored enamel, and tapers to a sharp point.")
        return M_HANDLED
    if _verb(world, "V-WAVE", "V-RAISE"):
        here = world.here
        here_name = here.name if here else ""
        if here_name in ("ARAGAIN-FALLS", "END-OF-RAINBOW"):
            if not world.get_global("RAINBOW-FLAG"):
                pot = _obj(world, "POT-OF-GOLD")
                if pot:
                    pot.clear_flag(INVISIBLE)
                print(
                    "Suddenly, the rainbow appears to become solid and, I venture,\n"
                    "walkable (I think the giveaway was the stairs and bannister)."
                )
                if (here_name == "END-OF-RAINBOW" and pot
                        and pot.location is here):
                    print("A shimmering pot of gold appears at the end of the rainbow.")
                world.set_global("RAINBOW-FLAG", True)
            else:
                print("The rainbow seems to have become somewhat run-of-the-mill.")
                world.set_global("RAINBOW-FLAG", False)
        elif here_name == "ON-RAINBOW":
            world.set_global("RAINBOW-FLAG", False)
            world.game.jigs_up(
                "The structural integrity of the rainbow is severely compromised,\n"
                "leaving you hanging in midair, supported only by water vapor. Bye."
            )
        else:
            print("A dazzling display of color briefly emanates from the sceptre.")
        return M_HANDLED
    return M_NOT_HANDLED


def _sandwich_bag_fcn(world: "World") -> int:
    # ZIL SANDWICH-BAG-FCN only handles V-SMELL; V-OPEN falls through to default.
    if _verb(world, "V-SMELL"):
        bag = world.prso
        lunch = _obj(world, "LUNCH")
        if lunch and bag and lunch.location is bag:
            print("It smells of hot peppers.")
            return M_HANDLED
    return M_NOT_HANDLED


def _machine_f(world: "World") -> int:
    machine = _obj(world, "MACHINE")
    if machine is None:
        return M_NOT_HANDLED
    if _verb(world, "V-OPEN"):
        if machine.has_flag(OPENBIT):
            print("It is already open.")
            return M_HANDLED
        machine.set_flag(OPENBIT)
        diamond = _obj(world, "DIAMOND")
        if diamond and diamond.location is machine:
            print("The lid opens, revealing a huge diamond.")
        else:
            print("The lid opens.")
        return M_HANDLED
    if _verb(world, "V-CLOSE"):
        if not machine.has_flag(OPENBIT):
            print("It is already closed.")
        else:
            machine.clear_flag(OPENBIT)
            print("The lid closes.")
        return M_HANDLED
    return M_NOT_HANDLED


def _mswitch_function(world: "World") -> int:
    if _verb(world, "V-TURN"):
        coal = _obj(world, "COAL")
        machine = _obj(world, "MACHINE")
        coal_inside = coal and machine and coal.location is machine
        if coal_inside:
            world.move_object(coal, None)
            diamond = _obj(world, "DIAMOND")
            if diamond is None:
                from engine.world import GameObject
                diamond = GameObject(
                    name="DIAMOND",
                    desc="large diamond",
                    synonyms=["diamond", "treasure"],
                    adjectives=["large", "brilliant"],
                    flags={"TAKEBIT"},
                    value=10,
                    tvalue=10,
                )
                world.register_object(diamond)
            if machine:
                world.move_object(diamond, machine)
            print("The machine comes to life (figuratively) with a dazzling display of colored\nlights and bizarre noises. After a few moments, the excitement abates.")
        else:
            print("The machine grinds noisily for a moment, then stops.")
        return M_HANDLED
    return M_NOT_HANDLED


def _slide_function(world: "World") -> int:
    if _verb(world, "V-CLIMB", "V-EXAMINE"):
        print("The slide is a steep metal chute. Going up would be impossible.")
        return M_HANDLED
    return M_NOT_HANDLED


_ROBBER_C_DESC = (
    "There is a suspicious-looking individual, holding a bag, leaning\n"
    "against one wall. He is armed with a vicious-looking stiletto."
)
_ROBBER_U_DESC = "There is a suspicious-looking individual lying unconscious on the ground."

F_FIRST      = "F-FIRST?"
F_BUSY       = "F-BUSY?"
F_DEAD       = "F-DEAD"
F_UNCONSCIOUS = "F-UNCONSCIOUS"
F_CONSCIOUS  = "F-CONSCIOUS"


def _recover_stiletto(world: "World") -> None:
    thief    = _obj(world, "THIEF")
    stiletto = _obj(world, "STILETTO")
    if (thief and stiletto
            and stiletto.location is not thief
            and stiletto.location is thief.location):
        stiletto.set_flag(NDESCBIT)
        world.move_object(stiletto, thief)


def _rob(world: "World", from_obj, to_obj, prob: int = 0) -> bool:
    robbed = False
    for item in list(from_obj.contents):
        if (not item.has_flag(INVISIBLE)
                and not item.has_flag(SACREDBIT)
                and getattr(item, "tvalue", 0) > 0
                and (prob == 0 or random.randint(1, 100) <= prob)):
            world.move_object(item, to_obj)
            item.set_flag(TOUCHBIT)
            if to_obj.name == "THIEF":
                item.set_flag(INVISIBLE)
            robbed = True
    return robbed


def _steal_junk(world: "World", rm) -> bool:
    thief    = _obj(world, "THIEF")
    stiletto = _obj(world, "STILETTO")
    if not thief:
        return False
    for item in list(rm.contents):
        if (getattr(item, "tvalue", 0) == 0
                and item.has_flag(TAKEBIT)
                and not item.has_flag(SACREDBIT)
                and not item.has_flag(INVISIBLE)
                and (item is stiletto or random.randint(1, 100) <= 10)):
            world.move_object(item, thief)
            item.set_flag(TOUCHBIT)
            item.set_flag(INVISIBLE)
            if item.name == "ROPE":
                world.set_global("DOME-FLAG", False)
            if rm is world.here:
                print(f"You suddenly notice that the {item.desc} vanished.")
                return True
    return False


def _drop_junk(world: "World", rm) -> None:
    thief    = _obj(world, "THIEF")
    stiletto = _obj(world, "STILETTO")
    if not thief:
        return
    dropped = False
    for item in list(thief.contents):
        if item is stiletto or item.name == "LARGE-BAG":
            continue
        if getattr(item, "tvalue", 0) == 0 and random.randint(1, 100) <= 30:
            item.clear_flag(INVISIBLE)
            world.move_object(item, rm)
            if not dropped and rm is world.here:
                print("The robber, rummaging through his bag, dropped a few items he found valueless.")
                dropped = True


def _deposit_booty(world: "World", rm) -> bool:
    thief    = _obj(world, "THIEF")
    stiletto = _obj(world, "STILETTO")
    if not thief:
        return False
    deposited = False
    for item in list(thief.contents):
        if item is stiletto or item.name == "LARGE-BAG":
            continue
        if getattr(item, "tvalue", 0) > 0:
            world.move_object(item, rm)
            if item.name == "EGG":
                world.set_global("EGG-SOLVE", True)
                item.set_flag(OPENBIT)
            deposited = True
    return deposited


def _hack_treasures(world: "World") -> None:
    treasure_room = world.rooms.get("TREASURE-ROOM")
    if treasure_room:
        for item in list(treasure_room.contents):
            item.clear_flag(INVISIBLE)


def _rob_maze(world: "World", rm) -> bool:
    thief = _obj(world, "THIEF")
    if not thief:
        return False
    for item in list(rm.contents):
        if item.has_flag(TAKEBIT) and not item.has_flag(INVISIBLE) and random.randint(1, 100) <= 40:
            print(f'You hear, off in the distance, someone saying "My, I wonder what\n'
                  f'this fine {item.desc} is doing here."')
            if random.randint(1, 100) <= 70:
                world.move_object(item, thief)
                item.set_flag(TOUCHBIT)
                item.set_flag(INVISIBLE)
            return True
    return False


def _thief_vs_adventurer(world: "World", here_flag: bool) -> bool:
    thief    = _obj(world, "THIEF")
    stiletto = _obj(world, "STILETTO")
    if thief is None:
        return False

    thief_here = bool(world.get_global("THIEF-HERE"))

    if not thief_here:
        if not here_flag and random.randint(1, 100) <= 30:
            if stiletto and stiletto.location is thief:
                thief.clear_flag(INVISIBLE)
                print(
                    "Someone carrying a large bag is casually leaning against one of the\n"
                    "walls here. He does not speak, but it is clear from his aspect that\n"
                    "the bag will be taken only over his dead body."
                )
                world.set_global("THIEF-HERE", True)
                return True
        if (here_flag and thief.has_flag(FIGHTBIT)
                and getattr(thief, "strength", 1) <= 0):
            print(
                "Your opponent, determining discretion to be the better part of\n"
                "valor, decides to terminate this little contretemps. With a rueful\n"
                "nod of his head, he steps backward into the gloom and disappears."
            )
            thief.set_flag(INVISIBLE)
            thief.clear_flag(FIGHTBIT)
            _recover_stiletto(world)
            return True
        if here_flag and thief.has_flag(FIGHTBIT) and random.randint(1, 100) <= 90:
            return False
        if here_flag and random.randint(1, 100) <= 30:
            print("The holder of the large bag just left, looking disgusted.\nFortunately, he took nothing.")
            thief.set_flag(INVISIBLE)
            _recover_stiletto(world)
            return True
        if random.randint(1, 100) > 30:
            return False
        robbed_from = None
        if _rob(world, world.here, thief, 100):
            robbed_from = "room"
        elif _rob(world, world.winner, thief):
            robbed_from = "player"
        world.set_global("THIEF-HERE", True)
        if robbed_from and not here_flag:
            loc_str = "the room" if robbed_from == "room" else "your possession"
            print(
                f'A seedy-looking individual with a large bag just wandered through\n'
                f'the room. On the way through, he quietly abstracted some valuables from\n'
                f'{loc_str}, mumbling something about\n"Doing unto others before..."'
            )
        elif here_flag:
            _recover_stiletto(world)
            if robbed_from:
                victim = "robbed you blind first." if robbed_from == "player" else "appropriated the valuables in the room."
                print(f"The thief just left, still carrying his large bag. You may\n"
                      f"not have noticed that he {victim}")
            else:
                print("The thief, finding nothing of value, left disgusted.")
            thief.set_flag(INVISIBLE)
            return True
        elif not robbed_from:
            print('A "lean and hungry" gentleman just wandered through, carrying a\n'
                  "large bag. Finding nothing of value, he left disgruntled.")
            return True
        return True
    else:
        if here_flag and random.randint(1, 100) <= 30:
            robbed_from = None
            if _rob(world, world.here, thief, 100):
                robbed_from = "room"
            elif _rob(world, world.winner, thief):
                robbed_from = "player"
            if robbed_from:
                victim = "robbed you blind first." if robbed_from == "player" else "appropriated the valuables in the room."
                print(f"The thief just left, still carrying his large bag. You may\n"
                      f"not have noticed that he {victim}")
            else:
                print("The thief, finding nothing of value, left disgusted.")
            thief.set_flag(INVISIBLE)
            world.set_global("THIEF-HERE", False)
            _recover_stiletto(world)
    return False


def i_thief(world: "World") -> bool:
    """Thief demon — runs every turn via clock."""
    thief = _obj(world, "THIEF")
    if thief is None:
        world.game.clock.queue("I-THIEF", i_thief, 1, is_demon=True)
        return False

    treasure_room = world.rooms.get("TREASURE-ROOM")
    here_flag = not thief.has_flag(INVISIBLE)
    rm = thief.location
    output = False

    if rm is treasure_room and rm is not world.here:
        if here_flag:
            _hack_treasures(world)
            here_flag = False
        _deposit_booty(world, treasure_room)
    elif rm is world.here and world.is_lit():
        troll = _obj(world, "TROLL")
        troll_here = troll and troll.location is world.here and not troll.has_flag(INVISIBLE)
        if not troll_here:
            if _thief_vs_adventurer(world, here_flag):
                output = True
            if thief.has_flag(INVISIBLE):
                here_flag = False
    else:
        if rm is not None and not thief.has_flag(INVISIBLE):
            thief.set_flag(INVISIBLE)
            here_flag = False
        if rm is not None and rm.has_flag(TOUCHBIT):
            _rob(world, rm, thief, 75)
            if rm.has_flag("MAZEBIT") and world.here and world.here.has_flag("MAZEBIT"):
                _rob_maze(world, rm)
            else:
                _steal_junk(world, rm)

    if not here_flag:
        _recover_stiletto(world)
        rooms = list(world.rooms.values())
        start_idx = rooms.index(rm) if rm in rooms else 0
        for i in range(1, len(rooms) + 1):
            next_rm = rooms[(start_idx + i) % len(rooms)]
            if not next_rm.has_flag(SACREDBIT) and next_rm.has_flag(RLANDBIT):
                world.move_object(thief, next_rm)
                thief.clear_flag(FIGHTBIT)
                thief.set_flag(INVISIBLE)
                world.set_global("THIEF-HERE", False)
                break

    if rm is not None and rm is not treasure_room:
        _drop_junk(world, rm)

    world.game.clock.queue("I-THIEF", i_thief, 1, is_demon=True)
    return output


def _robber_function(world: "World", mode=None) -> int:
    thief = _obj(world, "THIEF")
    stiletto = _obj(world, "STILETTO")

    if mode is None:
        if _verb(world, "V-TELL"):
            print("The thief is a strong, silent type.")
            return M_HANDLED
        if _verb(world, "V-HELLO"):
            if thief and thief.ldesc == _ROBBER_U_DESC:
                print("The thief, being temporarily incapacitated, is unable to acknowledge\n"
                      "your greeting with his usual graciousness.")
            return M_HANDLED
        if _verb(world, "V-THROW") and world.prso and world.prso.name == "KNIFE":
            if stiletto and thief and not thief.has_flag(FIGHTBIT):
                world.move_object(world.prso, world.here)
                if random.randint(1, 100) <= 10:
                    print("You evidently frightened the robber, though you didn't hit him. He flees")
                    large_bag = _obj(world, "LARGE-BAG")
                    had_stiletto = stiletto and stiletto.location is thief
                    if thief.contents:
                        for item in list(thief.contents):
                            if item is not large_bag and item is not stiletto:
                                world.move_object(item, world.here)
                        print(", but the contents of his bag fall on the floor.")
                    else:
                        print(".")
                    if large_bag:
                        world.move_object(large_bag, thief)
                    if had_stiletto and stiletto:
                        world.move_object(stiletto, thief)
                    thief.set_flag(INVISIBLE)
                else:
                    print("You missed. The thief makes no attempt to take the knife, though it\n"
                          "would be a fine addition to the collection in his bag. He does seem\n"
                          "angered by your attempt.")
                    thief.set_flag(FIGHTBIT)
                return M_HANDLED
        if (_verb(world, "V-THROW", "V-GIVE")
                and world.prso and world.prso is not thief
                and world.prsi is thief):
            if thief and getattr(thief, "strength", 1) < 0:
                thief.strength = -thief.strength
                world.game.clock.enable("I-THIEF")
                _recover_stiletto(world)
                if thief.ldesc:
                    thief.ldesc = _ROBBER_C_DESC
                print("Your proposed victim suddenly recovers consciousness.")
            world.move_object(world.prso, thief)
            if getattr(world.prso, "tvalue", 0) > 0:
                world.set_global("THIEF-ENGROSSED", True)
                print(f"The thief is taken aback by your unexpected generosity, but accepts\n"
                      f"the {world.prso.desc} and stops to admire its beauty.")
            else:
                print(f"The thief places the {world.prso.desc} in his bag and thanks\nyou politely.")
            return M_HANDLED
        if _verb(world, "V-TAKE"):
            print("Once you got him, what would you do with him?")
            return M_HANDLED
        if _verb(world, "V-EXAMINE", "V-LOOK-INSIDE"):
            print("The thief is a slippery character with beady eyes that flit back\n"
                  "and forth. He carries, along with an unmistakable arrogance, a large bag\n"
                  "over his shoulder and a vicious stiletto, whose blade is aimed\n"
                  "menacingly in your direction. I'd watch out if I were you.")
            return M_HANDLED
        if _verb(world, "V-LISTEN"):
            print("The thief says nothing, as you have not been formally introduced.")
            return M_HANDLED
        return M_NOT_HANDLED

    if mode == F_BUSY:
        if stiletto and thief and stiletto.location is thief.location and stiletto.location is not thief:
            world.move_object(stiletto, thief)
            stiletto.set_flag(NDESCBIT)
            if thief.location is world.here:
                print("The robber, somewhat surprised at this turn of events, nimbly\nretrieves his stiletto.")
            return M_HANDLED
        return M_NOT_HANDLED

    if mode == F_DEAD:
        if stiletto and thief:
            stiletto.clear_flag(NDESCBIT)
            world.move_object(stiletto, world.here)
        if thief:
            thief.set_flag(INVISIBLE)
            _deposit_booty(world, world.here)
            treasure_room = world.rooms.get("TREASURE-ROOM")
            if treasure_room and thief.location is treasure_room:
                for item in list(treasure_room.contents):
                    if item.name not in ("CHALICE", "THIEF", "ADVENTURER"):
                        item.clear_flag(INVISIBLE)
                        print(f"  A {item.desc}")
        world.game.clock.disable("I-THIEF")
        return M_HANDLED

    if mode == F_FIRST:
        if (world.get_global("THIEF-HERE")
                and thief and not thief.has_flag(INVISIBLE)
                and random.randint(1, 100) <= 20):
            thief.set_flag(FIGHTBIT)
            return M_HANDLED
        return M_NOT_HANDLED

    if mode == F_UNCONSCIOUS:
        world.game.clock.disable("I-THIEF")
        if thief:
            thief.clear_flag(FIGHTBIT)
        if stiletto and thief:
            stiletto.clear_flag(NDESCBIT)
            world.move_object(stiletto, world.here)
        if thief:
            thief.ldesc = _ROBBER_U_DESC
        return M_HANDLED

    if mode == F_CONSCIOUS:
        if thief and thief.location is world.here:
            thief.set_flag(FIGHTBIT)
            print("The robber revives, briefly feigning continued unconsciousness, and,\n"
                  "when he sees his moment, scrambles away from you.")
        world.game.clock.enable("I-THIEF")
        if thief:
            thief.ldesc = _ROBBER_C_DESC
        _recover_stiletto(world)
        return M_HANDLED

    return M_NOT_HANDLED


def _large_bag_f(world: "World") -> int:
    if _verb(world, "V-TAKE"):
        print("The bag is held firmly by the thief.")
        return M_HANDLED
    return M_NOT_HANDLED


def _rope_function(world: "World") -> int:
    if _verb(world, "V-TIE"):
        if world.here and world.here.name != "DOME-ROOM":
            world.set_global("DOME-FLAG", False)
            print("You can't tie the rope to that.")
            return M_HANDLED
        prsi = world.prsi
        if prsi and prsi.name == "RAILING":
            if world.get_global("DOME-FLAG"):
                print("The rope is already tied to it.")
            else:
                print("The rope drops over the side and comes within ten feet of the floor.")
                world.set_global("DOME-FLAG", True)
                rope = _obj(world, "ROPE")
                if rope:
                    rope.set_flag(NDESCBIT)
                    if rope.location is not None and not hasattr(rope.location, 'contents'):
                        world.move_object(rope, world.here)
            return M_HANDLED
        print("You can't tie the rope to that.")
        return M_HANDLED
    if _verb(world, "V-UNTIE"):
        if world.get_global("DOME-FLAG"):
            world.set_global("DOME-FLAG", False)
            rope = _obj(world, "ROPE")
            if rope:
                rope.clear_flag(NDESCBIT)
            print("The rope is now untied.")
        else:
            print("It is not tied to anything.")
        return M_HANDLED
    if _verb(world, "V-TAKE"):
        if world.get_global("DOME-FLAG"):
            print("The rope is tied to the railing.")
            return M_HANDLED
    if _verb(world, "V-DROP"):
        if world.here and world.here.name == "DOME-ROOM" and not world.get_global("DOME-FLAG"):
            torch_room = world.rooms.get("TORCH-ROOM")
            rope = _obj(world, "ROPE")
            if rope and torch_room:
                world.move_object(rope, torch_room)
            print("The rope drops gently to the floor below.")
            return M_HANDLED
    return M_NOT_HANDLED


def _sand_function(world: "World") -> int:
    if _verb(world, "V-DIG"):
        scarab = _obj(world, "SCARAB")
        if scarab and scarab.has_flag(INVISIBLE):
            scarab.clear_flag(INVISIBLE)
            print("Your digging reveals a scarab!")
        else:
            print("There's nothing more to find here.")
        return M_HANDLED
    return M_NOT_HANDLED


def _sword_fcn(world: "World") -> int:
    return M_NOT_HANDLED


def _canary_object(world: "World") -> int:
    if _verb(world, "V-WIND"):
        canary = _obj(world, "CANARY")
        if world.prso is canary:
            forest_rooms = {"FOREST-1", "FOREST-2", "FOREST-3", "PATH", "UP-A-TREE"}
            here = world.here
            here_name = here.name if here else ""
            if not world.get_global("SING-SONG") and here_name in forest_rooms:
                print(
                    "The canary chirps, slightly off-key, an aria from a forgotten opera.\n"
                    "From out of the greenery flies a lovely songbird. It perches on a\n"
                    "limb just over your head and opens its beak to sing. As it does so\n"
                    "a beautiful brass bauble drops from its mouth, bounces off the top of\n"
                    "your head, and lands glimmering in the grass. As the canary winds\n"
                    "down, the songbird flies away."
                )
                world.set_global("SING-SONG", True)
                bauble = _obj(world, "BAUBLE")
                if bauble:
                    path_room = world.rooms.get("PATH")
                    target = path_room if (here_name == "UP-A-TREE" and path_room) else here
                    world.move_object(bauble, target)
            else:
                print("The canary chirps blithely, if somewhat tinnily, for a short time.")
        else:
            print("There is an unpleasant grinding noise from inside the canary.")
        return M_HANDLED
    return M_NOT_HANDLED


def _broken_canary_fcn(world: "World") -> int:
    if _verb(world, "V-WIND"):
        print("The broken spring makes a sad twanging noise.")
        return M_HANDLED
    return M_NOT_HANDLED


def _egg_object(world: "World") -> int:
    if _verb(world, "V-OPEN"):
        egg = _obj(world, "EGG")
        if egg and not egg.has_flag("OPENBIT"):
            egg.set_flag("OPENBIT")
            canary = _obj(world, "CANARY")
            if canary:
                world.move_object(canary, world.here or egg)
            print("The jeweled egg opens, revealing a clockwork canary.")
        else:
            print("It is already open.")
        return M_HANDLED
    return M_NOT_HANDLED


def _cretin_fcn(world: "World") -> int:
    print("I beg your pardon?")
    return M_HANDLED


def _not_here_object_f(world: "World") -> int:
    print("I can't see any such thing.")
    return M_HANDLED


def _dumb_container(world: "World") -> int:
    return M_NOT_HANDLED


def _chimney_f(world: "World") -> int:
    if _verb(world, "V-EXAMINE"):
        here = world.here
        if here and here.name == "KITCHEN":
            print("The chimney leads downward, and looks climbable.")
        else:
            print("The chimney leads upward, and looks climbable.")
        return M_HANDLED
    return M_NOT_HANDLED


def _river_pseudo(world: "World") -> int:
    if _verb(world, "V-SWIM", "V-BOARD"):
        print("Swimming isn't usually allowed in the dungeon.")
        return M_HANDLED
    return M_NOT_HANDLED


def _coffin_object(world: "World") -> int:
    if _verb(world, "V-OPEN"):
        coffin = _obj(world, "COFFIN")
        if coffin:
            if coffin.has_flag("OPENBIT"):
                print("It is already open.")
            else:
                coffin.set_flag("OPENBIT")
                print("The lid of the coffin swings open, revealing a sceptre.")
        return M_HANDLED
    return M_NOT_HANDLED


def _bodies_f(world: "World") -> int:
    if _verb(world, "V-EXAMINE"):
        print("The bodies are in various states of decomposition.")
        return M_HANDLED
    return M_NOT_HANDLED


def _rainbow_object(world: "World") -> int:
    if _verb(world, "V-TOUCH", "V-RUB"):
        print("The rainbow shimmers as you touch it.")
        return M_HANDLED
    return M_NOT_HANDLED


def _white_cliff_f(world: "World") -> int:
    if _verb(world, "V-CLIMB"):
        print("The cliffs are too sheer to climb here.")
        return M_HANDLED
    return M_NOT_HANDLED


def _climbable_cliff_f(world: "World") -> int:
    if _verb(world, "V-CLIMB"):
        here = world.here
        if here:
            if here.name == "CANYON-BOTTOM":
                world.game.do_walk("up")
            elif here.name == "CLIFF-MIDDLE":
                world.game.do_walk("up")
        return M_HANDLED
    return M_NOT_HANDLED


def _cyclops_f(world: "World") -> int:
    if _verb(world, "V-EXAMINE"):
        print("The cyclops is gazing at you hungrily.")
        return M_HANDLED
    if _verb(world, "V-ATTACK", "V-KILL"):
        print("You would have to be as strong as a cyclops to attack a cyclops!")
        return M_HANDLED
    return M_NOT_HANDLED


def _barrow_door_fcn(world: "World") -> int:
    if _verb(world, "V-OPEN", "V-CLOSE"):
        print("The door is too heavy.")
        return M_HANDLED
    return M_NOT_HANDLED


def _barrow_fcn(world: "World") -> int:
    return M_NOT_HANDLED


def _map_object(world: "World") -> int:
    if _verb(world, "V-READ"):
        print(
            "The map shows a forest with three clearings. The largest clearing contains\n"
            "a house. Three paths leave the large clearing. One of these paths, leading\n"
            "southwest, is marked \"To Stone Barrow\"."
        )
        return M_HANDLED
    return M_NOT_HANDLED


def _boat_label_f(world: "World") -> int:
    if _verb(world, "V-READ"):
        print(
            "  !!!!FROBOZZ MAGIC BOAT COMPANY!!!!\n\n"
            "Hello, Sailor!\n\n"
            "Instructions for use:\n\n"
            "   To get into a body of water, say \"Launch\".\n"
            "   To get to shore, say \"Land\" or the direction in which you want\n"
            "to maneuver the boat.\n\n"
            "Warranty:\n\n"
            "  This boat is guaranteed against all defects for a period of 76\n"
            "milliseconds from date of purchase or until first used, whichever comes first.\n\n"
            "Warning:\n"
            "   This boat is made of thin plastic.\n"
            "   Good Luck!"
        )
        return M_HANDLED
    return M_NOT_HANDLED


def _iboat_function(world: "World") -> int:
    """IBOAT-FUNCTION: action for INFLATABLE-BOAT (ZIL line 2820)."""
    if _verb(world, "V-INFLATE"):
        here = world.here
        inflatable = _obj(world, "INFLATABLE-BOAT")
        inflated = _obj(world, "INFLATED-BOAT")
        label = _obj(world, "BOAT-LABEL")
        if inflatable is None or inflatable.location is not here:
            print("The boat must be on the ground to be inflated.")
            return M_HANDLED
        pump = _obj(world, "PUMP")
        prsi = world.prsi
        if prsi is pump:
            print("The boat inflates and appears seaworthy.")
            if label and not label.has_flag(TOUCHBIT):
                print("A tan label is lying inside the boat.")
            world.set_global("DEFLATE", False)
            world.move_object(inflatable, None)
            if inflated:
                world.move_object(inflated, here)
                world.it_object = inflated
        else:
            prsi_desc = prsi.desc if prsi else "that"
            print(f"With a {prsi_desc}? Surely you jest!")
        return M_HANDLED
    return M_NOT_HANDLED


def i_river(world: "World") -> bool:
    """I-RIVER clock demon: moves the inflated boat downstream (ZIL line 2708)."""
    here = world.here
    here_name = here.name if here else None

    if here_name not in _RIVER_ROOMS:
        world.game.clock.disable("I-RIVER")
        return False

    next_name = _RIVER_NEXT.get(here_name)
    if next_name is None:
        world.game.jigs_up(
            "Unfortunately, the magic boat doesn't provide protection from\n"
            "the rocks and boulders one meets at the bottom of waterfalls.\n"
            "Including this one."
        )
        return True

    print("The flow of the river carries you downstream.\n")
    next_room = world.rooms.get(next_name)
    if next_room:
        world.game.enter_room(next_room)

    new_speed = _RIVER_SPEEDS.get(next_name, 2)
    world.game.clock.queue("I-RIVER", i_river, new_speed)
    return True


def _rboat_function(world: "World", msg: int = 0) -> int:
    """RBOAT-FUNCTION: action for INFLATED-BOAT (ZIL line 2722).

    Called with msg=M_BEG when player is inside the vehicle (via vehicle
    M-BEG dispatch).  Called with msg=0 as a plain object action.
    """
    if msg == M_BEG:
        here = world.here
        here_name = here.name if here else None

        if _verb(world, "V-WALK"):
            walk_dir = getattr(world, "walk_dir", None)
            # Land/east/west always allowed
            if walk_dir in ("land", "east", "west"):
                return M_NOT_HANDLED
            # north/south allowed on reservoir or in-stream
            if walk_dir in ("north", "south") and here_name in ("RESERVOIR", "IN-STREAM"):
                return M_NOT_HANDLED
            print("Read the label for the boat's instructions.")
            return M_HANDLED

        if _verb(world, "V-LAUNCH"):
            if here_name in _ON_RIVER:
                water = ("reservoir" if here_name == "RESERVOIR"
                         else "stream" if here_name == "IN-STREAM"
                         else "river")
                print(f"You are on the {water}, or have you forgotten?")
                return M_HANDLED
            dest_name = _RIVER_LAUNCH.get(here_name)
            if dest_name is None:
                print("You can't launch it here.")
                return M_HANDLED
            dest_room = world.rooms.get(dest_name)
            if dest_room:
                world.game.enter_room(dest_room)
                speed = _RIVER_SPEEDS.get(dest_name, 4)
                world.game.clock.queue("I-RIVER", i_river, speed)
            return M_HANDLED

        # Weapon puncture while on water (DROP, PUT, or ATTACK with weapon)
        prso = world.prso
        prsi = world.prsi
        weapon_drop = _verb(world, "V-DROP") and prso is not None and prso.has_flag(WEAPONBIT)
        weapon_put = (
            _verb(world, "V-PUT") and prso is not None and prso.has_flag(WEAPONBIT)
            and prsi is _obj(world, "INFLATED-BOAT")
        )
        weapon_attack = (
            _verb(world, "V-ATTACK", "V-MUNG")
            and prsi is not None and prsi.has_flag(WEAPONBIT)
        )
        if weapon_drop or weapon_put or weapon_attack:
            inflated = _obj(world, "INFLATED-BOAT")
            punctured = _obj(world, "PUNCTURED-BOAT")
            winner = world.winner
            if winner:
                world.move_object(winner, here)
            if inflated:
                for item in list(getattr(inflated, "contents", [])):
                    world.move_object(item, here)
                world.move_object(inflated, None)
            if punctured and here:
                world.move_object(punctured, here)
            weapon_obj = (prso if (weapon_drop or weapon_put) else prsi)
            weapon_desc = weapon_obj.desc if weapon_obj else "it"
            print(
                f"It seems that the {weapon_desc} didn't agree with the boat, as evidenced\n"
                "by the loud hissing noise issuing therefrom. With a pathetic sputter, the\n"
                "boat deflates, leaving you without."
            )
            if here and here.has_flag(NONLANDBIT):
                if here_name in ("RESERVOIR", "IN-STREAM"):
                    world.game.jigs_up(
                        "Another pathetic sputter, this time from you, heralds your drowning."
                    )
                else:
                    world.game.jigs_up(
                        "In other words, fighting the fierce currents of the Frigid River. You\n"
                        "manage to hold your own for a bit, but then you are carried over a\n"
                        "waterfall and into some nasty rocks. Ouch!"
                    )
            return M_HANDLED

        return M_NOT_HANDLED

    # Object-action context (msg == 0)

    if _verb(world, "V-BOARD"):
        winner = world.winner
        if winner:
            weapon_names = ["SCEPTRE", "KNIFE", "SWORD", "RUSTY-KNIFE", "AXE", "STILETTO"]
            has_weapon = any(_obj(world, w) in winner.contents for w in weapon_names)
            if has_weapon:
                inflated = _obj(world, "INFLATED-BOAT")
                punctured = _obj(world, "PUNCTURED-BOAT")
                here = world.here
                if inflated:
                    world.move_object(inflated, None)
                if punctured and here:
                    world.move_object(punctured, here)
                    world.it_object = punctured
                print(
                    "Oops! Something sharp seems to have slipped and punctured the boat.\n"
                    "The boat deflates to the sounds of hissing, sputtering, and cursing."
                )
                return M_HANDLED
        return M_NOT_HANDLED

    if _verb(world, "V-INFLATE"):
        print("Inflating it further would probably burst it.")
        return M_HANDLED

    if _verb(world, "V-DEFLATE"):
        winner = world.winner
        inflated = _obj(world, "INFLATED-BOAT")
        here = world.here
        if winner and winner.location is inflated:
            print("You can't deflate the boat while you're in it.")
            return M_HANDLED
        if not inflated or inflated.location is not here:
            print("The boat must be on the ground to be deflated.")
            return M_HANDLED
        print("The boat deflates.")
        world.set_global("DEFLATE", True)
        deflatable = _obj(world, "INFLATABLE-BOAT")
        world.move_object(inflated, None)
        if deflatable and here:
            world.move_object(deflatable, here)
            world.it_object = deflatable
        return M_HANDLED

    if _verb(world, "V-LAUNCH"):
        print("You're not in the boat!")
        return M_HANDLED

    return M_NOT_HANDLED


def _wooden_door_f(world: "World") -> int:
    if _verb(world, "V-OPEN"):
        if not _flag(world, "MAGIC-FLAG"):
            print("The door is nailed shut.")
        else:
            print("The door has a large cyclops-shaped hole in it.")
        return M_HANDLED
    return M_NOT_HANDLED


def _garlic_f(world: "World") -> int:
    if _verb(world, "V-EAT"):
        print("Yuch! How can you eat that?")
        world.move_object(world.prso, None)
        return M_HANDLED
    return M_NOT_HANDLED


# ---------------------------------------------------------------------------
# Room action handlers
# ---------------------------------------------------------------------------

def _west_house(world: "World", msg: int = 0) -> int:
    if msg == M_LOOK:
        won = world.get_global("WON-FLAG")
        extra = " A secret path leads southwest into the forest." if won else ""
        print(
            "You are standing in an open field west of a white house, with a boarded\n"
            f"front door.{extra}"
        )
        return M_HANDLED
    return M_NOT_HANDLED


def _east_house(world: "World", msg: int = 0) -> int:
    if msg == M_LOOK:
        win = _obj(world, "KITCHEN-WINDOW")
        state = "open." if (win and win.has_flag(OPENBIT)) else "slightly ajar."
        print(
            "You are behind the white house. A path leads into the forest\n"
            "to the east. In one corner of the house there is a small window\n"
            f"which is {state}"
        )
        return M_HANDLED
    return M_NOT_HANDLED


def _forest_room(world: "World", msg: int = 0) -> int:
    return M_NOT_HANDLED


def _tree_room(world: "World", msg: int = 0) -> int:
    if msg == M_LOOK:
        print(
            "You are about 10 feet above the ground nestled among some large branches.\n"
            "The nearest branch above you is beyond your reach. Beside you on the branch\n"
            "is a small bird's nest. In the nest is a large egg encrusted with precious\n"
            "jewels, apparently scavenged somewhere by a childless songbird. The egg is\n"
            "covered with fine gold inlay, and is worth a fortune."
        )
        return M_HANDLED
    return M_NOT_HANDLED


def _clearing_fcn(world: "World", msg: int = 0) -> int:
    if msg == M_ENTER:
        grate = _obj(world, "GRATE")
        if grate and not world.get_global("GRATE-REVEALED"):
            grate.set_flag(INVISIBLE)
        return M_NOT_HANDLED
    if msg == M_LOOK:
        grate = _obj(world, "GRATE")
        print("You are in a clearing, with a forest surrounding you on all sides. A\npath leads south.")
        if grate and grate.has_flag(OPENBIT):
            print("\nThere is an open grating, descending into darkness.")
        elif world.get_global("GRATE-REVEALED"):
            print("\nThere is a grating securely fastened into the ground.")
        return M_HANDLED
    return M_NOT_HANDLED


def _kitchen_fcn(world: "World", msg: int = 0) -> int:
    if msg == M_LOOK:
        win = _obj(world, "KITCHEN-WINDOW")
        state = "open." if (win and win.has_flag(OPENBIT)) else "slightly ajar."
        print(
            "You are in the kitchen of the white house. A table seems to\n"
            "have been used recently for the preparation of food. A passage\n"
            "leads to the west and a dark staircase can be seen leading\n"
            f"upward. A dark chimney leads down and to the east is a small\n"
            f"window which is {state}"
        )
        return M_HANDLED
    return M_NOT_HANDLED


def _stone_barrow_fcn(world: "World", msg: int = 0) -> int:
    if msg == M_BEG:
        if _verb(world, "V-ENTER", "V-WALK"):
            print(
                "Inside the Barrow\n"
                "As you enter the barrow, the door closes inexorably behind you. Around\n"
                "you it is dark, but ahead is an enormous cavern, brightly lit. Through\n"
                "its center runs a wide stream. Spanning the stream is a small wooden\n"
                "footbridge, and beyond a path leads into a dark tunnel. Above the\n"
                "bridge, floating in the air, is a large sign. It reads:  All ye who\n"
                "stand before this bridge have completed a great and perilous adventure\n"
                "which has tested your wit and courage. You have mastered\n"
                "the first part of the ZORK trilogy. Those who pass over this bridge must be\n"
                "prepared to undertake an even greater adventure that will severely test your\n"
                "skill and bravery!\n\n"
                "The ZORK trilogy continues with \"ZORK II: The Wizard of Frobozz\" and\n"
                "is completed in \"ZORK III: The Dungeon Master.\""
            )
            world.game.quit()
            return M_FATAL
    return M_NOT_HANDLED


def _living_room_fcn(world: "World", msg: int = 0) -> int:
    if msg == M_LOOK:
        magic = world.get_global("MAGIC-FLAG")
        rug_moved = world.get_global("RUG-MOVED")
        trap = _obj(world, "TRAP-DOOR")
        trap_open = trap and trap.has_flag(OPENBIT)
        west_desc = (
            ". To the\nwest is a cyclops-shaped opening in an old wooden door, above which is\n"
            "some strange gothic lettering, " if magic else
            ", a wooden\ndoor with strange gothic lettering to the west, which appears to be\n"
            "nailed shut, "
        )
        if rug_moved and trap_open:
            rug_desc = "and a rug lying beside an open trap door."
        elif rug_moved:
            rug_desc = "and a closed trap door at your feet."
        elif trap_open:
            rug_desc = "and an open trap door at your feet."
        else:
            rug_desc = "and a large oriental rug in the center of the room."
        print(
            f"You are in the living room. There is a doorway to the east{west_desc}"
            f"a trophy case, {rug_desc}"
        )
        return M_HANDLED
    if msg == M_END:
        # Always recompute score from trophy-case contents each turn in Living Room.
        # (world.prsa is restored by perform() before M_END fires, so we can't
        # gate this on verb name — just recompute unconditionally.)
        _update_trophy_score(world)
    return M_NOT_HANDLED


def _touch_all(obj) -> None:
    obj.set_flag(TOUCHBIT)
    for child in list(obj.contents):
        _touch_all(child)


def _update_trophy_score(world: "World") -> None:
    trophy = world.objects.get("TROPHY-CASE")
    if trophy is None:
        return
    tval = _otval_frob(trophy)
    base = int(world.get_global("BASE-SCORE") or 0)
    world.score = base + tval
    world.set_global("SCORE", world.score)
    if world.score >= 350 and not world.get_global("WON-FLAG"):
        world.set_global("WON-FLAG", True)
        _map = world.objects.get("MAP")
        if _map:
            _map.clear_flag("INVISIBLE")
        print('\nAn almost inaudible voice whispers in your ear, "Look to your treasures'
              '\nfor the final secret."')


def _otval_frob(obj) -> int:
    total = 0
    for item in obj.contents:
        total += item.tvalue
        if item.contents:
            total += _otval_frob(item)
    return total


def _cellar_fcn(world: "World", msg: int = 0) -> int:
    if msg == M_LOOK:
        print(
            "You are in a dark and damp cellar with a narrow passageway leading\n"
            "north, and a crawlway to the south. On the west is the bottom of a\n"
            "steep metal ramp which is unclimbable."
        )
        return M_HANDLED
    if msg == M_ENTER:
        trap = _obj(world, "TRAP-DOOR")
        if trap and trap.has_flag(OPENBIT) and not trap.has_flag(TOUCHBIT):
            trap.clear_flag(OPENBIT)
            trap.set_flag(TOUCHBIT)
            print("The trap door crashes shut, and you hear someone barring it.\n")
        return M_NOT_HANDLED
    return M_NOT_HANDLED


def _troll_room_f(world: "World", msg: int = 0) -> int:
    return M_NOT_HANDLED


def _cyclops_room_fcn(world: "World", msg: int = 0) -> int:
    if msg == M_LOOK:
        cyclops = _obj(world, "CYCLOPS")
        if cyclops and cyclops.location is world.here:
            print(
                "This is a large room, in the middle of which is a cyclops who is\n"
                "staring at you with great interest."
            )
        else:
            print(
                "This is a large room. There is a cyclops-shaped hole in the east wall."
            )
        return M_HANDLED
    return M_NOT_HANDLED


def _maze_11_fcn(world: "World", msg: int = 0) -> int:
    if msg == M_ENTER:
        grate = _obj(world, "GRATE")
        if grate:
            grate.clear_flag(INVISIBLE)
        return M_NOT_HANDLED
    if msg == M_LOOK:
        grate = _obj(world, "GRATE")
        print("You are in a small room near the maze. There are twisty passages\nin the immediate vicinity.")
        if grate and grate.has_flag(OPENBIT):
            print("Above you is an open grating with sunlight pouring in.")
        elif world.get_global("GRUNLOCK"):
            print("Above you is a grating.")
        else:
            print("Above you is a grating locked with a skull-and-crossbones lock.")
        return M_HANDLED
    return M_NOT_HANDLED


def _thief_in_treasure(world: "World") -> None:
    """Hide all TREASURE-ROOM items except CHALICE and THIEF (ZIL THIEF-IN-TREASURE)."""
    here = world.here
    if here is None:
        return
    contents = list(here.contents)
    if len(contents) >= 2:
        print("The thief gestures mysteriously, and the treasures in the room\nsuddenly vanish.")
    for item in contents:
        if item.name not in ("CHALICE", "THIEF"):
            item.set_flag(INVISIBLE)


def _treasure_room_fcn(world: "World", msg: int = 0) -> int:
    if msg == M_ENTER:
        # Only fires while the thief demon is running (ZIL: <1? <GET <INT I-THIEF> ,C-ENABLED?>>)
        thief_event = world.game.clock.get("I-THIEF")
        if not (thief_event and thief_event.enabled):
            return M_NOT_HANDLED
        thief = _obj(world, "THIEF")
        if thief is None:
            return M_NOT_HANDLED
        # Teleport thief to the room if he isn't here already
        if thief.location is not world.here:
            print("You hear a scream of anguish as you violate the robber's hideaway.\n"
                  "Using passages unknown to you, he rushes to its defense.")
            world.move_object(thief, world.here)
        thief.set_flag(FIGHTBIT)
        thief.clear_flag(INVISIBLE)
        world.set_global("THIEF-HERE", True)
        _thief_in_treasure(world)
        return M_HANDLED
    return M_NOT_HANDLED


def _reservoir_south_fcn(world: "World", msg: int = 0) -> int:
    return M_NOT_HANDLED


def _reservoir_fcn(world: "World", msg: int = 0) -> int:
    return M_NOT_HANDLED


def _reservoir_north_fcn(world: "World", msg: int = 0) -> int:
    return M_NOT_HANDLED


def _mirror_room(world: "World", msg: int = 0) -> int:
    if msg == M_LOOK:
        print(
            "You are in a large square room with tall ceilings. On the south wall\n"
            "is an enormous mirror which fills the entire wall. There are exits\n"
            "on the other three sides of the room."
        )
        if world.get_global("MIRROR-MUNG"):
            print("Unfortunately, the mirror has been destroyed by your recklessness.")
        return M_HANDLED
    return M_NOT_HANDLED


def _cave2_room(world: "World", msg: int = 0) -> int:
    return M_NOT_HANDLED


def _lld_room(world: "World", msg: int = 0) -> int:
    if msg == M_LOOK:
        print(
            "You are outside a large gateway, on which is inscribed\n\n"
            "  Abandon every hope\nall ye who enter here!\n\n"
            "The gate is open; through it you can see a desolation, with a pile of\n"
            "mangled bodies in one corner. Thousands of voices, lamenting some\n"
            "hideous fate, can be heard."
        )
        if not world.get_global("LLD-FLAG"):
            print("The way through the gate is barred by evil spirits, who jeer at your\nattempts to pass.")
        return M_HANDLED

    if msg == M_BEG:
        lld_flag = world.get_global("LLD-FLAG")
        xb = world.get_global("XB")
        xc = world.get_global("XC")
        bell = _obj(world, "BELL")
        candles = _obj(world, "CANDLES")
        book = _obj(world, "BOOK")
        player = world.winner

        if _verb(world, "V-RING") and world.prso is bell and not lld_flag:
            world.set_global("XB", True)
            hot_bell = _obj(world, "HOT-BELL")
            if bell and player and bell.location is player:
                world.move_object(bell, None)
            if hot_bell:
                world.move_object(hot_bell, world.here)
            print(
                "The bell suddenly becomes red hot and falls to the ground. The\n"
                "wraiths, as if paralyzed, stop their jeering and slowly turn to face\n"
                "you. On their ashen faces, the expression of a long-forgotten terror\n"
                "takes shape."
            )
            if candles and player and candles.location is player:
                print("In your confusion, the candles drop to the ground (and they are out).")
                world.move_object(candles, world.here)
                candles.clear_flag(ONBIT)
            world.game.clock.queue("I-XB", i_xb, 6)
            world.game.clock.queue("I-XBH", i_xbh, 20)
            return M_HANDLED

        if xc and _verb(world, "V-READ") and world.prso is book and not lld_flag:
            print(
                "Each word of the prayer reverberates through the hall in a deafening\n"
                "confusion. As the last word fades, a voice, loud and commanding,\n"
                "speaks: \"Begone, fiends!\" A heart-stopping scream fills the cavern,\n"
                "and the spirits, sensing a greater power, flee through the walls."
            )
            ghosts = _obj(world, "GHOSTS")
            if ghosts:
                world.move_object(ghosts, None)
            world.set_global("LLD-FLAG", True)
            world.game.clock.disable("I-XC")
            return M_HANDLED

        return M_NOT_HANDLED

    if msg == M_END:
        xb = world.get_global("XB")
        xc = world.get_global("XC")
        candles = _obj(world, "CANDLES")
        player = world.winner
        if (xb and not xc and candles and player
                and candles.location is player
                and candles.has_flag(ONBIT)):
            world.set_global("XC", True)
            world.game.clock.disable("I-XB")
            world.game.clock.queue("I-XC", i_xc, 3)
            print(
                "The flames flicker wildly and appear to dance. The earth beneath\n"
                "your feet trembles, and your legs nearly buckle beneath you.\n"
                "The spirits cower at your unearthly power."
            )
        return M_NOT_HANDLED

    return M_NOT_HANDLED


def _dome_room_fcn(world: "World", msg: int = 0) -> int:
    if msg == M_LOOK:
        print(
            "You are at the top of the Dome Room. From here you can see that the\n"
            "room below is enormous. A passage exits to the west, and a rope\n"
            "hangs from the ceiling above you."
        )
        if world.get_global("DOME-FLAG"):
            print("A rope hangs down from the railing.")
        return M_HANDLED
    return M_NOT_HANDLED


def _torch_room_fcn(world: "World", msg: int = 0) -> int:
    if msg == M_LOOK:
        print(
            "This is a large room with a prominent doorway leading to a dimly lit\n"
            "hallway to the south. On the west and northeast walls, there are\n"
            "glowing white marble pillars."
        )
        return M_HANDLED
    return M_NOT_HANDLED


def _south_temple_fcn(world: "World", msg: int = 0) -> int:
    if msg == M_BEG:
        coffin = _obj(world, "COFFIN")
        player = world.winner
        carrying_coffin = (coffin is not None and player is not None
                           and coffin.location is player)
        world.set_global("COFFIN-CURE", not carrying_coffin)
    return M_NOT_HANDLED


def _dam_room_fcn(world: "World", msg: int = 0) -> int:
    if msg == M_LOOK:
        print(
            "You are standing on the top of Flood Control Dam #3, which was quite\n"
            "a tourist attraction in its day. The river Frigid is flowing by below.\n"
            "There is a small path on the north end of the dam."
        )
        return M_HANDLED
    return M_NOT_HANDLED


def _white_cliffs_function(world: "World", msg: int = 0) -> int:
    return M_NOT_HANDLED


def _falls_room(world: "World", msg: int = 0) -> int:
    if msg == M_LOOK:
        print(
            "You are at the top of the Aragain Falls. The falls themselves are\n"
            "spectacularly beautiful. To the north is a small path."
        )
        if world.get_global("RAINBOW-FLAG"):
            print("Spanning the falls is a brilliant rainbow.")
        return M_HANDLED
    return M_NOT_HANDLED


def _rivr4_room(world: "World", msg: int = 0) -> int:
    return M_NOT_HANDLED


def _canyon_view_f(world: "World", msg: int = 0) -> int:
    return M_NOT_HANDLED


def _deep_canyon_f(world: "World", msg: int = 0) -> int:
    return M_NOT_HANDLED


def _loud_room_fcn(world: "World", msg: int = 0) -> int:
    if msg == M_LOOK:
        quiet = world.get_global("LOUD-FLAG")
        print(
            "This is a large room with a ceiling which cannot be detected from\n"
            "the ground. There is a narrow passage from east to west and a stone\n"
            "stairway leading upward."
        )
        if quiet:
            print("The room is eerie in its quietness.")
        else:
            print(
                "The room is deafeningly loud with an undetermined rushing sound.\n"
                "The sound seems to reverberate from all of the walls, making it\n"
                "difficult even to think."
            )
        return M_HANDLED
    if msg == M_BEG and _verb(world, "V-ECHO"):
        if world.here and world.here.name == "LOUD-ROOM":
            world.set_global("LOUD-FLAG", True)
            bar = _obj(world, "BAR")
            if bar:
                bar.clear_flag("SACREDBIT")
            print("The acoustics of the room change subtly.")
            return M_HANDLED
    return M_NOT_HANDLED


def _no_objs(world: "World", msg: int = 0) -> int:
    if msg == M_BEG:
        if world.winner:
            empty = True
            for item in world.winner.contents:
                if getattr(item, "size", 0) > 4:
                    empty = False
                    break
            world.set_global("EMPTY-HANDED", empty)
        # LIGHT-SHAFT bonus: award once when player is in LOWER-SHAFT and area is lit
        here = world.here
        light_shaft = world.get_global("LIGHT-SHAFT")
        if here and here.name == "LOWER-SHAFT" and light_shaft and world.is_lit():
            from content.verbs import _score_upd
            _score_upd(world, light_shaft)
            world.set_global("LIGHT-SHAFT", 0)
    return M_NOT_HANDLED


def _machine_room_fcn(world: "World", msg: int = 0) -> int:
    if msg == M_LOOK:
        print(
            "This is a small room. On one wall is a machine which appears to have\n"
            "a large slot (about 15 inches square). On the front panel is a switch."
        )
        return M_HANDLED
    return M_NOT_HANDLED


def _bats_room(world: "World", msg: int = 0) -> int:
    if msg == M_ENTER:
        garlic = _obj(world, "GARLIC")
        winner = world.winner
        if not (garlic and winner and garlic.location is winner):
            # No garlic in hand — bat grabs the player
            import random
            bat_drops = [
                "MINE-1", "MINE-2", "MINE-3", "MINE-4",
                "LADDER-TOP", "LADDER-BOTTOM", "SQUEEKY-ROOM", "MINE-ENTRANCE",
            ]
            print("The bat grabs you by the scruff of your neck and lifts you away....\n")
            dest_name = random.choice(bat_drops)
            dest = world.rooms.get(dest_name)
            if dest:
                world.game.enter_room(dest)
            return M_HANDLED
    return M_NOT_HANDLED


def _boom_room(world: "World", msg: int = 0) -> int:
    # ZIL BOOM-ROOM fires on M_END (not M_ENTER).
    # Only open-flame objects (candles, torch, match) trigger it; the electric lamp is safe.
    if msg == M_END:
        winner = world.winner
        if not winner:
            return M_NOT_HANDLED
        candles = _obj(world, "CANDLES")
        torch = _obj(world, "TORCH")
        match = _obj(world, "MATCH")
        def held_and_lit(obj):
            return obj and obj.location is winner and obj.has_flag(ONBIT)
        if held_and_lit(candles) or held_and_lit(torch) or held_and_lit(match):
            being_lit = _verb(world, "V-LAMP-ON", "V-BURN") and (
                world.prso in (candles, torch, match)
            )
            if being_lit:
                world.game.jigs_up(
                    f"How sad for an aspiring adventurer to light a "
                    f"{world.prso.desc if world.prso else 'flame'} in a room which\n"
                    "reeks of gas. Fortunately, there is justice in the world."
                )
            else:
                world.game.jigs_up(
                    "Oh dear. It appears that the smell coming from this room was coal gas.\n"
                    "I would have thought twice about carrying flaming objects in here."
                )
            return M_FATAL
    return M_NOT_HANDLED


def _scoring_fcn(world: "World", msg: int = 0) -> int:
    return M_NOT_HANDLED


def _lantern_fcn(world: "World") -> int:
    """LANTERN object action handler (ZIL LANTERN routine)."""
    lamp = world.objects.get("LAMP")
    if lamp is None:
        return M_NOT_HANDLED

    if _verb(world, "V-THROW"):
        print("The lamp has smashed into the floor, and the light has gone out.")
        world.game.clock.disable("I-LANTERN")
        here = world.here
        if here:
            world.move_object(lamp, here)
        broken = world.objects.get("BROKEN-LAMP")
        if broken and here:
            world.move_object(broken, here)
        return M_HANDLED

    if _verb(world, "V-LAMP-ON"):
        if lamp.has_flag("RMUNGBIT"):
            print("A burned-out lamp won't light.")
            return M_HANDLED
        world.game.clock.enable("I-LANTERN")
        return M_NOT_HANDLED  # let V-LAMP-ON set ONBIT and print message

    if _verb(world, "V-LAMP-OFF"):
        if lamp.has_flag("RMUNGBIT"):
            print("The lamp has already burned out.")
            return M_HANDLED
        world.game.clock.disable("I-LANTERN")
        return M_NOT_HANDLED  # let V-LAMP-OFF clear ONBIT and print message

    if _verb(world, "V-EXAMINE"):
        if lamp.has_flag("RMUNGBIT"):
            print("The lamp has burned out.")
        elif lamp.has_flag(ONBIT):
            print("The lamp is on.")
        else:
            print("The lamp is turned off.")
        return M_HANDLED

    return M_NOT_HANDLED


def _hero_blow(world: "World", villain_name: str, villain_flag: str) -> int:
    """Simplified HERO-BLOW: player attacks a named villain with PRSI weapon."""
    villain = world.objects.get(villain_name)
    weapon = world.prsi
    winner = world.winner

    if villain is None or winner is None:
        return M_NOT_HANDLED

    if winner.has_flag(STAGGERED):
        print("You are still recovering from that last blow, so your attack is ineffective.")
        winner.clear_flag(STAGGERED)
        return M_HANDLED

    villain_strength = villain.strength
    if villain_strength <= 0:
        print(f"The {villain.desc} cannot defend himself: He dies.")
        _kill_villain(world, villain, villain_name, villain_flag)
        return M_HANDLED

    roll = random.randint(1, 10)
    if roll <= 3:
        print(f"You missed the {villain.desc}.")
    elif roll <= 6:
        villain.strength -= 1
        print(f"You hit the {villain.desc}.")
        if villain.strength <= 0:
            print(f"\nAlmost as soon as the {villain.desc} breathes his last breath, a cloud\n"
                  f"of sinister black fog envelops him, and when the fog lifts, the\n"
                  f"carcass has disappeared.")
            _kill_villain(world, villain, villain_name, villain_flag)
    elif roll <= 8:
        villain.strength -= 2
        print(f"You gave the {villain.desc} a serious wound.")
        if villain.strength <= 0:
            print(f"\nAlmost as soon as the {villain.desc} breathes his last breath, a cloud\n"
                  f"of sinister black fog envelops him, and when the fog lifts, the\n"
                  f"carcass has disappeared.")
            _kill_villain(world, villain, villain_name, villain_flag)
    elif roll == 9:
        print(f"The {villain.desc} is knocked out!")
        villain.strength = -1
        _kill_villain(world, villain, villain_name, villain_flag)
    else:
        print(f"A killing blow! The {villain.desc} falls dead.")
        villain.strength = 0
        _kill_villain(world, villain, villain_name, villain_flag)

    # Villain counter-attack (simplified): 30% chance of wounding player
    if villain.location is world.here and villain.strength > 0:
        if random.randint(1, 10) <= 3:
            winner.strength = getattr(winner, "strength", 0) - 1
            print(f"The {villain.desc} swings at you!")
            if winner.strength < -3:
                world.game.jigs_up(f"The {villain.desc} has killed you.")
                return M_FATAL

    return M_HANDLED


def _kill_villain(world: "World", villain, villain_name: str, flag_name: str) -> None:
    villain.clear_flag(FIGHTBIT)
    world.move_object(villain, None)
    world.set_global(flag_name, True)
    # Drop the villain's weapon
    axe = world.objects.get("AXE") if villain_name == "TROLL" else None
    if axe and axe.location is villain:
        from engine.world import NDESCBIT
        axe.clear_flag(NDESCBIT)
        axe.set_flag(WEAPONBIT)
        if world.here:
            world.move_object(axe, world.here)


# ---------------------------------------------------------------------------
# Match and Candles
# ---------------------------------------------------------------------------

_FLAMEBIT = "FLAMEBIT"
_RMUNGBIT = "RMUNGBIT"


def i_match(world: "World") -> bool:
    """Clock interrupt: match burns out after 2 turns."""
    match = _obj(world, "MATCH")
    if match:
        print("The match has gone out.")
        match.clear_flag(ONBIT)
        match.clear_flag(_FLAMEBIT)
    return True


def _match_function(world: "World") -> int:
    match = _obj(world, "MATCH")
    if match is None:
        return M_NOT_HANDLED

    if _verb(world, "V-LAMP-ON", "V-BURN") and world.prso is match:
        count = int(world.get_global("MATCH-COUNT") or 0)
        if count > 0:
            world.set_global("MATCH-COUNT", count - 1)
        new_count = int(world.get_global("MATCH-COUNT") or 0)
        if new_count <= 0:
            print("I'm afraid that you have run out of matches.")
        elif world.here and world.here.name in ("LOWER-SHAFT", "TIMBER-ROOM"):
            print("This room is drafty, and the match goes out instantly.")
        else:
            match.set_flag(_FLAMEBIT)
            match.set_flag(ONBIT)
            world.game.clock.queue("I-MATCH", i_match, 2)
            print("One of the matches starts to burn.")
        return M_HANDLED

    if _verb(world, "V-LAMP-OFF") and match.has_flag(_FLAMEBIT):
        print("The match is out.")
        match.clear_flag(_FLAMEBIT)
        match.clear_flag(ONBIT)
        world.game.clock.queue("I-MATCH", i_match, 0)
        return M_HANDLED

    if _verb(world, "V-COUNT", "V-OPEN"):
        remaining = int(world.get_global("MATCH-COUNT") or 0)
        if remaining <= 0:
            print("You have no matches.")
        else:
            noun = "match" if remaining == 1 else "matches"
            print(f"You have {remaining} {noun}.")
        return M_HANDLED

    if _verb(world, "V-EXAMINE"):
        if match.has_flag(ONBIT):
            print("The match is burning.")
        else:
            print("The matchbook isn't very interesting, except for what's written on it.")
        return M_HANDLED

    return M_NOT_HANDLED


def _candles_fcn(world: "World") -> int:
    candles = _obj(world, "CANDLES")
    if candles is None:
        return M_NOT_HANDLED

    if not candles.has_flag(TOUCHBIT):
        pass  # I-CANDLES timer would be enabled here; simplified for now

    if world.prsi is candles:
        return M_NOT_HANDLED

    if _verb(world, "V-LAMP-ON", "V-BURN"):
        if candles.has_flag(_RMUNGBIT):
            print("Alas, there's not much left of the candles. Certainly not enough to burn.")
            return M_HANDLED

        prsi = world.prsi
        match = _obj(world, "MATCH")
        torch = _obj(world, "TORCH")

        if prsi is None:
            if match and match.has_flag(_FLAMEBIT):
                print("(with the match)")
                return world.game.perform("V-LAMP-ON", candles, match)
            else:
                print("You should say what to light them with.")
                return M_FATAL

        if prsi is match and match.has_flag(ONBIT):
            if candles.has_flag(ONBIT):
                print("The candles are already lit.")
            else:
                candles.set_flag(ONBIT)
                print("The candles are lit.")
            return M_HANDLED

        if prsi is torch:
            if candles.has_flag(ONBIT):
                print("You realize, just in time, that the candles are already lighted.")
            else:
                print("The heat from the torch is so intense that the candles are vaporized.")
                world.move_object(candles, None)
            return M_HANDLED

        print("You have to light them with something that's burning, you know.")
        return M_HANDLED

    if _verb(world, "V-COUNT"):
        print("Let's see, how many objects in a pair? Don't tell me, I'll get it.")
        return M_HANDLED

    if _verb(world, "V-LAMP-OFF"):
        if candles.has_flag(ONBIT):
            candles.clear_flag(ONBIT)
            candles.set_flag(TOUCHBIT)
            print("The flame is extinguished.")
        else:
            print("The candles are not lighted.")
        return M_HANDLED

    if _verb(world, "V-PUT") and world.prsi is not None and world.prsi.has_flag("BURNBIT"):
        print("That wouldn't be smart.")
        return M_HANDLED

    if _verb(world, "V-EXAMINE"):
        state = "burning" if candles.has_flag(ONBIT) else "out"
        print(f"The candles are {state}.")
        return M_HANDLED

    return M_NOT_HANDLED


# ---------------------------------------------------------------------------
# Handler registries
# ---------------------------------------------------------------------------

ACTION_HANDLERS: dict = {
    "BOARD-F":            _board_f,
    "TEETH-F":            _teeth_f,
    "GRANITE-WALL-F":     _granite_wall_f,
    "SONGBIRD-F":         _songbird_f,
    "WHITE-HOUSE-F":      _white_house_f,
    "FOREST-F":           _forest_f,
    "MOUNTAIN-RANGE-F":   _mountain_range_f,
    "WATER-F":            _water_f,
    "KITCHEN-WINDOW-F":   _kitchen_window_f,
    "GHOSTS-F":           _ghosts_f,
    "BASKET-F":           _basket_f,
    "BAT-F":              _bat_f,
    "BELL-F":             _bell_f,
    "HOT-BELL-F":         _hot_bell_f,
    "BOARDED-WINDOW-FCN": _boarded_window_fcn,
    "CRACK-FCN":          _crack_fcn,
    "TROPHY-CASE-FCN":    _trophy_case_fcn,
    "RUG-FCN":            _rug_fcn,
    "TRAP-DOOR-FCN":      _trap_door_fcn,
    "FRONT-DOOR-FCN":     _front_door_fcn,
    "AXE-F":              _axe_f,
    "STILETTO-FUNCTION":  _stiletto_function,
    "TROLL-FCN":          _troll_fcn,
    "GRATE-FUNCTION":     _grate_function,
    "LEAF-PILE":          _leaf_pile,
    "LEAVES-APPEAR":      _leaves_appear_action,
    "RUSTY-KNIFE-FCN":    _rusty_knife_fcn,
    "KNIFE-F":            _knife_f,
    "SKELETON":           _skeleton_fcn,
    "TORCH-OBJECT":       _torch_object,
    "MIRROR-MIRROR":      _mirror_mirror,
    "BUTTON-F":           _button_f,
    "BOLT-F":             _bolt_f,
    "BUBBLE-F":           _bubble_f,
    "BLACK-BOOK":         _black_book,
    "SCEPTRE-FUNCTION":   _sceptre_function,
    "SANDWICH-BAG-FCN":   _sandwich_bag_fcn,
    "MACHINE-F":          _machine_f,
    "MSWITCH-FUNCTION":   _mswitch_function,
    "SLIDE-FUNCTION":     _slide_function,
    "ROBBER-FUNCTION":    _robber_function,
    "LARGE-BAG-F":        _large_bag_f,
    "ROPE-FUNCTION":      _rope_function,
    "SAND-FUNCTION":      _sand_function,
    "SWORD-FCN":          _sword_fcn,
    "CANARY-OBJECT":      _canary_object,
    "BROKEN-CANARY-FCN":  _broken_canary_fcn,
    "EGG-OBJECT":         _egg_object,
    "CRETIN-FCN":         _cretin_fcn,
    "NOT-HERE-OBJECT-F":  _not_here_object_f,
    "DUMB-CONTAINER":     _dumb_container,
    "CHIMNEY-F":          _chimney_f,
    "RIVER-PSEUDO":       _river_pseudo,
    "COFFIN-OBJECT":      _coffin_object,
    "BODIES-F":           _bodies_f,
    "RAINBOW-OBJECT":     _rainbow_object,
    "WHITE-CLIFF-F":      _white_cliff_f,
    "CLIMBABLE-CLIFF-F":  _climbable_cliff_f,
    "CYCLOPS-F":          _cyclops_f,
    "BARROW-DOOR-FCN":    _barrow_door_fcn,
    "BARROW-FCN":         _barrow_fcn,
    "MAP-OBJECT":         _map_object,
    "BOAT-LABEL-F":       _boat_label_f,
    "IBOAT-FUNCTION":     _iboat_function,
    "RBOAT-FUNCTION":     _rboat_function,
    "WOODEN-DOOR-F":      _wooden_door_f,
    "GARLIC-F":           _garlic_f,
    "LANTERN":            _lantern_fcn,
    "MATCH-FUNCTION":     _match_function,
    "CANDLES-FCN":        _candles_fcn,
}

ROOM_ACTION_HANDLERS: dict = {
    "WEST-HOUSE":          _west_house,
    "EAST-HOUSE":          _east_house,
    "FOREST-ROOM":         _forest_room,
    "TREE-ROOM":           _tree_room,
    "CLEARING-FCN":        _clearing_fcn,
    "KITCHEN-FCN":         _kitchen_fcn,
    "STONE-BARROW-FCN":    _stone_barrow_fcn,
    "LIVING-ROOM-FCN":     _living_room_fcn,
    "CELLAR-FCN":          _cellar_fcn,
    "TROLL-ROOM-F":        _troll_room_f,
    "CYCLOPS-ROOM-FCN":    _cyclops_room_fcn,
    "MAZE-11-FCN":         _maze_11_fcn,
    "TREASURE-ROOM-FCN":   _treasure_room_fcn,
    "RESERVOIR-SOUTH-FCN": _reservoir_south_fcn,
    "RESERVOIR-FCN":       _reservoir_fcn,
    "RESERVOIR-NORTH-FCN": _reservoir_north_fcn,
    "MIRROR-ROOM":         _mirror_room,
    "CAVE2-ROOM":          _cave2_room,
    "LLD-ROOM":            _lld_room,
    "DOME-ROOM-FCN":       _dome_room_fcn,
    "TORCH-ROOM-FCN":      _torch_room_fcn,
    "SOUTH-TEMPLE-FCN":    _south_temple_fcn,
    "DAM-ROOM-FCN":        _dam_room_fcn,
    "WHITE-CLIFFS-FUNCTION": _white_cliffs_function,
    "FALLS-ROOM":          _falls_room,
    "RIVR4-ROOM":          _rivr4_room,
    "CANYON-VIEW-F":       _canyon_view_f,
    "DEEP-CANYON-F":       _deep_canyon_f,
    "LOUD-ROOM-FCN":       _loud_room_fcn,
    "NO-OBJS":             _no_objs,
    "MACHINE-ROOM-FCN":    _machine_room_fcn,
    "BATS-ROOM":           _bats_room,
    "BOOM-ROOM":           _boom_room,
}
