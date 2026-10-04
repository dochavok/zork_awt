"""
Syntax rules for Roundabout: The God-Forsaken Ring.

Covers the complete Zork I base plus Roundabout-specific additions from
mechanics.md §"Verb Canonical Map":
  New canonicals: sail, dock, buy, tip, fish, drive, swap, clear, load, pry, use, cast, rest
  Particle additions: turn left/right (dial), look up, climb aboard
"""

from __future__ import annotations

from engine.parser import (
    SyntaxRule, ObjectSpec,
    LOC_HELD, LOC_CARRIED, LOC_ON_GROUND, LOC_IN_ROOM,
    LOC_HAVE, LOC_MANY, LOC_TAKE,
)
from engine.world import (
    TAKEBIT, CONTBIT, OPENBIT, TRYTAKEBIT, NDESCBIT, BURNBIT, READBIT,
    TURNBIT, ACTORBIT, WEAPONBIT, CLIMBBIT, DRINKBIT, DOORBIT, TOOLBIT,
    INVISIBLE, SACREDBIT, SURFACEBIT, TOUCHBIT, RMUNGBIT, TRANSBIT,
    WEARBIT, VEHBIT, SEARCHBIT, FIGHTBIT, STAGGERED, ONBIT,
)

# Flags not in engine/world.py
LIGHTBIT   = "LIGHTBIT"
FLAMEBIT   = "FLAMEBIT"
FOODBIT    = "FOODBIT"
MAZEBIT    = "MAZEBIT"
NONLANDBIT = "NONLANDBIT"
WEARABLE   = "WEARABLE"     # items the player can put on (armor, ring, glasses)

# ---------------------------------------------------------------------------
# Common location frozensets
# ---------------------------------------------------------------------------
_held_car_og_ir          = frozenset({LOC_HELD, LOC_CARRIED, LOC_ON_GROUND, LOC_IN_ROOM})
_og_ir                   = frozenset({LOC_ON_GROUND, LOC_IN_ROOM})
_og_ir_many              = frozenset({LOC_ON_GROUND, LOC_IN_ROOM, LOC_MANY})
_held_many_have          = frozenset({LOC_HELD, LOC_MANY, LOC_HAVE})
_held_car                = frozenset({LOC_HELD, LOC_CARRIED})
_held_car_have           = frozenset({LOC_HELD, LOC_CARRIED, LOC_HAVE})
_og_ir_held_car          = frozenset({LOC_ON_GROUND, LOC_IN_ROOM, LOC_HELD, LOC_CARRIED})
_og_ir_held_car_have     = frozenset({LOC_ON_GROUND, LOC_IN_ROOM, LOC_HELD, LOC_CARRIED, LOC_HAVE})
_held_car_og_ir_take_have = frozenset({LOC_HELD, LOC_CARRIED, LOC_ON_GROUND, LOC_IN_ROOM, LOC_TAKE, LOC_HAVE})
_many                    = frozenset({LOC_MANY})
_have                    = frozenset({LOC_HAVE})
_take                    = frozenset({LOC_TAKE})
_in_room                 = frozenset({LOC_IN_ROOM})
_held_car_og_ir_take     = frozenset({LOC_HELD, LOC_CARRIED, LOC_ON_GROUND, LOC_IN_ROOM, LOC_TAKE})
_car_ir_many             = frozenset({LOC_CARRIED, LOC_IN_ROOM, LOC_MANY})
_held_car_take_have      = frozenset({LOC_HELD, LOC_CARRIED, LOC_TAKE, LOC_HAVE})
_held_have               = frozenset({LOC_HELD, LOC_HAVE})
_held_car_og_ir_many     = frozenset({LOC_HELD, LOC_CARRIED, LOC_ON_GROUND, LOC_IN_ROOM, LOC_MANY})
_held_car_og_ir_have     = frozenset({LOC_HELD, LOC_CARRIED, LOC_ON_GROUND, LOC_IN_ROOM, LOC_HAVE})
_held_car_og_ir_have_many = frozenset({LOC_HELD, LOC_CARRIED, LOC_ON_GROUND, LOC_IN_ROOM, LOC_HAVE, LOC_MANY})
_held_car_og_ir_take_have_many = frozenset({LOC_HELD, LOC_CARRIED, LOC_ON_GROUND, LOC_IN_ROOM, LOC_TAKE, LOC_HAVE, LOC_MANY})
_held_car_many               = frozenset({LOC_HELD, LOC_CARRIED, LOC_MANY})


def make_syntax_rules() -> list[SyntaxRule]:
    """Return the complete SyntaxRule list for Roundabout."""

    rules = [
        # ------------------------------------------------------------------ #
        # Game / meta commands                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="verbose",   action="V-VERBOSE"),
        SyntaxRule(verb="brief",     action="V-BRIEF"),
        SyntaxRule(verb="super",     action="V-SUPER-BRIEF"),
        SyntaxRule(verb="diagnose",  action="V-DIAGNOSE"),
        SyntaxRule(verb="inventory", action="V-INVENTORY"),
        SyntaxRule(verb="quit",      action="V-QUIT"),
        SyntaxRule(verb="restart",   action="V-RESTART"),
        SyntaxRule(verb="restore",   action="V-RESTORE"),
        SyntaxRule(verb="save",      action="V-SAVE"),
        SyntaxRule(verb="score",     action="V-SCORE"),
        SyntaxRule(verb="script",    action="V-SCRIPT"),
        SyntaxRule(verb="unscript",  action="V-UNSCRIPT"),
        SyntaxRule(verb="version",   action="V-VERSION"),

        # ------------------------------------------------------------------ #
        # ACTIVATE — altar elements, lamp-like objects                        #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="activate", action="V-LAMP-ON",
                   obj1=ObjectSpec(find_flag=LIGHTBIT, locations=_held_car_og_ir)),
        SyntaxRule(verb="activate", action="V-ACTIVATE",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # ANSWER                                                              #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="answer", action="V-ANSWER"),
        SyntaxRule(verb="answer", action="V-REPLY",
                   obj1=ObjectSpec()),

        # ------------------------------------------------------------------ #
        # APPLY                                                               #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="apply", action="V-PUT", preaction="PRE-PUT",
                   obj1=ObjectSpec(), prep="to", obj2=ObjectSpec()),

        # ------------------------------------------------------------------ #
        # ATTACK / KILL / STAB — combat                                       #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="attack", action="V-MELEE",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir),
                   prep="with",
                   obj2=ObjectSpec(find_flag=WEAPONBIT, locations=_held_car_have)),
        SyntaxRule(verb="attack", action="V-MELEE",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir)),
        SyntaxRule(verb="kill", action="V-MELEE",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir),
                   prep="with",
                   obj2=ObjectSpec(find_flag=WEAPONBIT, locations=_held_car_have)),
        SyntaxRule(verb="kill", action="V-MELEE",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir)),
        SyntaxRule(verb="stab", action="V-MELEE",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir),
                   prep="with",
                   obj2=ObjectSpec(find_flag=WEAPONBIT, locations=_held_car_have)),
        SyntaxRule(verb="stab", action="V-MELEE",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir)),

        # SHOOT — bow attack
        SyntaxRule(verb="attack", particle="shoot",
                   action="V-SHOOT",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir),
                   prep="with",
                   obj2=ObjectSpec(locations=_held_car_have)),
        SyntaxRule(verb="attack", particle="shoot",
                   action="V-SHOOT",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir)),

        # ------------------------------------------------------------------ #
        # BACK                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="back", action="V-BACK"),

        # ------------------------------------------------------------------ #
        # BLAST                                                               #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="blast", action="V-BLAST"),

        # ------------------------------------------------------------------ #
        # BLOW                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="blow", particle="out", action="V-LAMP-OFF",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="blow", particle="up", action="V-INFLATE",
                   obj1=ObjectSpec(),
                   prep="with",
                   obj2=ObjectSpec(find_flag=TOOLBIT, locations=_og_ir_held_car)),
        SyntaxRule(verb="blow", particle="up", action="V-BLAST",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="blow", particle="in", action="V-BREATHE",
                   obj1=ObjectSpec()),

        # ------------------------------------------------------------------ #
        # BOARD — vehicle + "aboard" synonym + CLIMB ABOARD particle         #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="board", action="V-BOARD", preaction="PRE-BOARD",
                   obj1=ObjectSpec(find_flag=VEHBIT, locations=_og_ir)),
        SyntaxRule(verb="board", particle="ship", action="V-BOARD-SHIP"),
        SyntaxRule(verb="board", action="V-BOARD-SHIP"),  # no obj: board the ship
        SyntaxRule(verb="climb", particle="aboard", action="V-BOARD-SHIP"),
        SyntaxRule(verb="enter", particle="ship", action="V-BOARD-SHIP"),

        # ------------------------------------------------------------------ #
        # BRUSH                                                               #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="brush", action="V-BRUSH",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="brush", action="V-BRUSH",
                   obj1=ObjectSpec(locations=_held_car_og_ir),
                   prep="with", obj2=ObjectSpec()),

        # ------------------------------------------------------------------ #
        # BURN                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="burn", action="V-BURN",
                   obj1=ObjectSpec(find_flag=BURNBIT, locations=_held_car_og_ir),
                   prep="with",
                   obj2=ObjectSpec(find_flag=FLAMEBIT, locations=_held_car_og_ir)),
        SyntaxRule(verb="burn", action="V-BURN",
                   obj1=ObjectSpec(find_flag=BURNBIT, locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # BUY — new canonical: BUY DRINK / ORDER FOOD / RENT ROOM           #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="buy", action="V-BUY",
                   obj1=ObjectSpec(locations=_og_ir_held_car_have)),
        SyntaxRule(verb="buy", action="V-BUY"),

        # ------------------------------------------------------------------ #
        # CAST — new canonical: CAST LIGHT / CAST FIREBALL etc.             #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="cast", action="V-CAST",
                   obj1=ObjectSpec(locations=_have)),
        SyntaxRule(verb="cast", action="V-CAST"),
        SyntaxRule(verb="cast", action="V-CAST",
                   obj1=ObjectSpec(locations=_have),
                   prep="at",
                   obj2=ObjectSpec(locations=_og_ir)),

        # ------------------------------------------------------------------ #
        # CLEAR — CLEAR BONES / CLEAR DRAIN                                 #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="clear", action="V-CLEAR",
                   obj1=ObjectSpec(locations=_og_ir_held_car_have)),
        SyntaxRule(verb="clear", action="V-CLEAR"),

        # ------------------------------------------------------------------ #
        # CLIMB                                                               #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="climb", action="V-CLIMB",
                   obj1=ObjectSpec(find_flag=CLIMBBIT, locations=_held_car_og_ir)),
        SyntaxRule(verb="climb", particle="down", action="V-CLIMB-DOWN",
                   obj1=ObjectSpec(locations=_og_ir_held_car_have)),
        SyntaxRule(verb="climb", particle="down", action="V-CLIMB-DOWN"),
        SyntaxRule(verb="climb", particle="up", action="V-CLIMB-UP",
                   obj1=ObjectSpec(locations=_og_ir_held_car_have)),
        SyntaxRule(verb="climb", particle="up", action="V-CLIMB-UP"),
        SyntaxRule(verb="climb", particle="tree", action="V-CLIMB-TREE"),

        # ------------------------------------------------------------------ #
        # CLOSE                                                               #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="close", action="V-CLOSE",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # COUNT                                                               #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="count", action="V-COUNT",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # CROSS                                                               #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="cross", action="V-CROSS",
                   obj1=ObjectSpec(locations=_og_ir)),

        # ------------------------------------------------------------------ #
        # CURSE                                                               #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="curse", action="V-CURSE",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="curse", action="V-CURSE"),

        # ------------------------------------------------------------------ #
        # CUT                                                                 #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="cut", action="V-CUT",
                   obj1=ObjectSpec(locations=_held_car_og_ir),
                   prep="with",
                   obj2=ObjectSpec(find_flag=WEAPONBIT, locations=_held_car_have)),
        SyntaxRule(verb="cut", action="V-CUT",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # DESTROY                                                             #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="destroy", action="V-DESTROY",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # DIG                                                                 #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="dig", action="V-DIG",
                   prep="with",
                   obj1=ObjectSpec(locations=_held_car_have)),
        SyntaxRule(verb="dig", action="V-DIG", prep="in",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="dig", action="V-DIG",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="dig", action="V-DIG"),

        # ------------------------------------------------------------------ #
        # DISEMBARK                                                           #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="disembark", action="V-DISEMBARK"),

        # ------------------------------------------------------------------ #
        # DOCK — return ship to harbor                                        #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="dock", action="V-DOCK"),

        # ------------------------------------------------------------------ #
        # DRINK                                                               #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="drink", action="V-DRINK",
                   obj1=ObjectSpec(find_flag=DRINKBIT, locations=_held_car_og_ir_take)),
        SyntaxRule(verb="drink", action="V-DRINK"),

        # ------------------------------------------------------------------ #
        # DRIVE — DRIVE STAKE INTO WEREWOLF                                  #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="drive", action="V-DRIVE-STAKE",
                   obj1=ObjectSpec(locations=_held_car_have),
                   prep="in",          # "into" is a synonym of "in"
                   obj2=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir)),
        SyntaxRule(verb="drive", action="V-DRIVE-STAKE",
                   obj1=ObjectSpec(locations=_held_car_have)),

        # ------------------------------------------------------------------ #
        # DROP                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="drop", action="V-DROP", preaction="PRE-DROP",
                   obj1=ObjectSpec(locations=_held_car_many)),
        SyntaxRule(verb="drop", action="V-PUT-IN", preaction="PRE-PUT",
                   obj1=ObjectSpec(locations=_held_car_many),
                   prep="in",
                   obj2=ObjectSpec(find_flag=CONTBIT, locations=_held_car_og_ir)),
        SyntaxRule(verb="drop", action="V-PUT-ON",
                   obj1=ObjectSpec(locations=_held_car_many),
                   prep="on",
                   obj2=ObjectSpec(find_flag=SURFACEBIT, locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # EAT                                                                 #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="eat", action="V-EAT",
                   obj1=ObjectSpec(find_flag=FOODBIT, locations=_held_car_og_ir_take)),
        SyntaxRule(verb="eat", action="V-EAT",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # ENCHANT / DISENCHANT                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="enchant", action="V-ENCHANT",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="disenchant", action="V-ENCHANT",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # ENTER / EXIT                                                        #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="enter", action="V-ENTER",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="enter", action="V-ENTER"),
        SyntaxRule(verb="exit",  action="V-EXIT",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="exit",  action="V-EXIT"),

        # ------------------------------------------------------------------ #
        # EXAMINE                                                             #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="examine", action="V-EXAMINE",
                   obj1=ObjectSpec(locations=_held_car_og_ir_have)),

        # ------------------------------------------------------------------ #
        # EXORCISE                                                            #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="exorcise", action="V-EXORCISE",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir)),
        SyntaxRule(verb="exorcise", action="V-EXORCISE"),

        # ------------------------------------------------------------------ #
        # EXTINGUISH                                                          #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="extinguish", action="V-LAMP-OFF",
                   obj1=ObjectSpec(find_flag=LIGHTBIT, locations=_held_car_og_ir)),
        SyntaxRule(verb="extinguish", action="V-LAMP-OFF",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # FILL                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="fill", action="V-FILL",
                   obj1=ObjectSpec(find_flag=CONTBIT, locations=_held_car_og_ir)),
        SyntaxRule(verb="fill", action="V-FILL",
                   obj1=ObjectSpec(find_flag=CONTBIT, locations=_held_car_og_ir),
                   prep="with",
                   obj2=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # FIND                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="find", action="V-FIND",
                   obj1=ObjectSpec(locations=_held_car_og_ir_have)),
        SyntaxRule(verb="find", action="V-FIND"),

        # ------------------------------------------------------------------ #
        # FISH — new canonical: FISH at Roundabout Pond                      #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="fish", action="V-FISH",
                   prep="with",
                   obj1=ObjectSpec(locations=_held_car_have)),
        SyntaxRule(verb="fish", action="V-FISH"),

        # ------------------------------------------------------------------ #
        # FOLLOW                                                              #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="follow", action="V-FOLLOW",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir_held_car_have)),

        # ------------------------------------------------------------------ #
        # GIVE                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="give", action="V-GIVE",
                   obj1=ObjectSpec(locations=_held_car_og_ir_take),
                   prep="to",
                   obj2=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir)),
        SyntaxRule(verb="give", action="V-GIVE",
                   obj1=ObjectSpec(locations=_held_car_og_ir_take)),

        # ------------------------------------------------------------------ #
        # HELLO                                                               #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="hello", action="V-HELLO"),

        # ------------------------------------------------------------------ #
        # INFLATE                                                             #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="inflate", action="V-INFLATE",
                   obj1=ObjectSpec(),
                   prep="with",
                   obj2=ObjectSpec(find_flag=TOOLBIT, locations=_og_ir_held_car)),
        SyntaxRule(verb="inflate", action="V-INFLATE",
                   obj1=ObjectSpec()),

        # ------------------------------------------------------------------ #
        # JUMP                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="jump", action="V-JUMP",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="jump", action="V-JUMP"),
        SyntaxRule(verb="jump", particle="on", action="V-JUMP-ON",
                   obj1=ObjectSpec(locations=_og_ir)),

        # ------------------------------------------------------------------ #
        # KICK                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="kick", action="V-KICK",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # KISS                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="kiss", action="V-KISS",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="kiss", action="V-KISS"),

        # ------------------------------------------------------------------ #
        # KNOCK                                                               #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="knock", action="V-KNOCK",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # LEAN                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="lean", action="V-LEAN",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # LEAVE                                                               #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="leave", action="V-LEAVE",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="leave", action="V-LEAVE"),

        # ------------------------------------------------------------------ #
        # LIGHT                                                               #
        # ------------------------------------------------------------------ #
        # BURNBIT rule first — catches gunpowder/fuses before the LAMP-ON rule
        SyntaxRule(verb="light", action="V-LIGHT",
                   obj1=ObjectSpec(find_flag=BURNBIT, locations=_held_car_og_ir)),
        SyntaxRule(verb="light", action="V-LAMP-ON",
                   obj1=ObjectSpec(find_flag=LIGHTBIT, locations=_held_car_og_ir)),
        SyntaxRule(verb="light", action="V-LIGHT",
                   obj1=ObjectSpec(locations=_held_car_og_ir),
                   prep="with",
                   obj2=ObjectSpec(find_flag=FLAMEBIT, locations=_held_car_og_ir)),
        SyntaxRule(verb="light", action="V-LIGHT",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # LISTEN                                                              #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="listen", action="V-LISTEN"),
        SyntaxRule(verb="listen", action="V-LISTEN",
                   prep="to", obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # LOAD — LOAD STONE ONTO CART                                        #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="load", action="V-LOAD",
                   obj1=ObjectSpec(locations=_held_car_og_ir),
                   prep="on",
                   obj2=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="load", action="V-LOAD",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # LOCK                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="lock", action="V-LOCK",
                   obj1=ObjectSpec(locations=_held_car_og_ir),
                   prep="with",
                   obj2=ObjectSpec(locations=_held_car_have)),
        SyntaxRule(verb="lock", action="V-LOCK",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # LOOK                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="look", action="V-LOOK"),
        SyntaxRule(verb="look", particle="up", action="V-LOOK-UP"),
        SyntaxRule(verb="look", particle="around", action="V-LOOK"),
        SyntaxRule(verb="look", prep="at",
                   action="V-EXAMINE",
                   obj1=ObjectSpec(locations=_held_car_og_ir_have)),
        SyntaxRule(verb="look", prep="in",
                   action="V-LOOK-INSIDE",
                   obj1=ObjectSpec(find_flag=CONTBIT, locations=_held_car_og_ir_have)),
        SyntaxRule(verb="look", prep="under",
                   action="V-LOOK-UNDER",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="look", particle="at", prep="ceiling",
                   action="V-LOOK-UP"),

        # ------------------------------------------------------------------ #
        # LOWER                                                               #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="lower", action="V-LOWER",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # LUBRICATE                                                           #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="lubricate", action="V-LUBRICATE",
                   obj1=ObjectSpec(locations=_held_car_og_ir),
                   prep="with",
                   obj2=ObjectSpec(locations=_held_car_have)),
        SyntaxRule(verb="lubricate", action="V-LUBRICATE",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # MAKE                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="make", action="V-MAKE",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # MELT                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="melt", action="V-MELT",
                   obj1=ObjectSpec(locations=_held_car_og_ir),
                   prep="with",
                   obj2=ObjectSpec(locations=_held_car_have)),
        SyntaxRule(verb="melt", action="V-MELT",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),
        # HOLD TORCH NEAR ICE ("hold" is a TAKE word) — Quest 34
        SyntaxRule(verb="take", action="V-HOLD-NEAR",
                   obj1=ObjectSpec(locations=_held_car_have),
                   prep="near", obj2=ObjectSpec(locations=_og_ir)),

        # ------------------------------------------------------------------ #
        # MOVE                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="move", action="V-MOVE",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # OPEN                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="open", action="V-OPEN",
                   obj1=ObjectSpec(locations=_held_car_og_ir),
                   prep="with",
                   obj2=ObjectSpec(locations=_held_car_have)),
        SyntaxRule(verb="open", action="V-OPEN",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # PICK                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="pick", particle="up", action="V-TAKE",
                   obj1=ObjectSpec(find_flag=TAKEBIT, locations=_held_car_og_ir_take)),
        SyntaxRule(verb="pick", action="V-PICK",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # PLAY                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="play", action="V-PLAY",
                   obj1=ObjectSpec(locations=_held_car_og_ir_have)),
        SyntaxRule(verb="play", action="V-PLAY"),

        # ------------------------------------------------------------------ #
        # PLUG                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="plug", action="V-PLUG",
                   obj1=ObjectSpec(locations=_held_car_og_ir),
                   prep="with",
                   obj2=ObjectSpec(locations=_held_car_have)),
        SyntaxRule(verb="plug", action="V-PLUG",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # POUR                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="pour", action="V-POUR",
                   obj1=ObjectSpec(locations=_held_car_have),
                   prep="on",
                   obj2=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="pour", action="V-POUR",
                   obj1=ObjectSpec(locations=_held_car_have),
                   prep="in",
                   obj2=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="pour", action="V-POUR",
                   obj1=ObjectSpec(locations=_held_car_have)),

        # ------------------------------------------------------------------ #
        # PRAY                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="pray", action="V-PRAY",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="pray", action="V-PRAY"),

        # ------------------------------------------------------------------ #
        # PRY — PRY DOOR (crowbar + strength check)                          #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="pry", action="V-PRY",
                   obj1=ObjectSpec(locations=_held_car_og_ir),
                   prep="with",
                   obj2=ObjectSpec(locations=_held_car_have)),
        SyntaxRule(verb="pry", action="V-PRY",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # PULL                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="pull", particle="free", action="V-STRUGGLE"),
        SyntaxRule(verb="pull", action="V-PULL",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="struggle", action="V-STRUGGLE"),

        # ------------------------------------------------------------------ #
        # PUMP                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="pump", action="V-PUMP",
                   obj1=ObjectSpec(locations=_held_car_og_ir),
                   prep="with",
                   obj2=ObjectSpec(find_flag=TOOLBIT, locations=_held_car_have)),
        SyntaxRule(verb="pump", action="V-PUMP",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # PUSH                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="push", action="V-PUSH",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),
        # PRESS SEAL ON / INTO JAR — Quest 4
        SyntaxRule(verb="push", action="V-PUSH",
                   obj1=ObjectSpec(locations=_held_car_og_ir),
                   prep="on", obj2=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="push", action="V-PUSH",
                   obj1=ObjectSpec(locations=_held_car_og_ir),
                   prep="into", obj2=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # DUST / SPRINKLE (Quest 4 — the Whispering Jar)                      #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="dust", action="V-DUST"),
        SyntaxRule(verb="dust", action="V-DUST",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="sprinkle", action="V-PUT-ON",
                   obj1=ObjectSpec(locations=_held_car_og_ir_take_have),
                   prep="on", obj2=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # PUT                                                                 #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="put", action="V-PUT-IN", preaction="PRE-PUT",
                   obj1=ObjectSpec(locations=_held_car_og_ir_take_have),
                   prep="in",
                   obj2=ObjectSpec(find_flag=CONTBIT, locations=_held_car_og_ir)),
        SyntaxRule(verb="put", action="V-PUT-ON",
                   obj1=ObjectSpec(locations=_held_car_og_ir_take_have),
                   prep="on",
                   obj2=ObjectSpec(find_flag=SURFACEBIT, locations=_held_car_og_ir)),
        SyntaxRule(verb="put", action="V-DROP", preaction="PRE-DROP",
                   obj1=ObjectSpec(locations=_held_car_many)),
        # PLACE BLOCKS (Quest 22): "place" is a "put" synonym; things on the
        # floor fall through to here when the drop rule can't find them held
        SyntaxRule(verb="put", action="V-PLACE",
                   obj1=ObjectSpec(locations=_og_ir)),

        # ------------------------------------------------------------------ #
        # RAISE                                                               #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="raise", action="V-RAISE",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # READ                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="read", action="V-READ",
                   obj1=ObjectSpec(find_flag=READBIT, locations=_held_car_og_ir)),
        SyntaxRule(verb="read", action="V-READ",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # REST — Level 6+ spell; no object needed                            #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="rest", action="V-REST"),

        # ------------------------------------------------------------------ #
        # RING                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="ring", action="V-RING",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # ROLL                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="roll", action="V-ROLL",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # RUB                                                                 #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="rub", action="V-RUB",
                   obj1=ObjectSpec(locations=_held_car_og_ir),
                   prep="on",
                   obj2=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="rub", action="V-RUB",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # SAIL — new canonical                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="sail", action="V-SAIL"),
        SyntaxRule(verb="sail", particle="north", action="V-SAIL-NORTH"),
        SyntaxRule(verb="sail", particle="south", action="V-SAIL-SOUTH"),
        SyntaxRule(verb="sail", particle="east",  action="V-SAIL-EAST"),
        SyntaxRule(verb="sail", particle="west",  action="V-SAIL-WEST"),

        # ------------------------------------------------------------------ #
        # SAY                                                                 #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="say", action="V-SAY",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="say", action="V-SAY"),

        # ------------------------------------------------------------------ #
        # SEARCH                                                              #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="search", action="V-SEARCH",
                   obj1=ObjectSpec(locations=_held_car_og_ir_have)),
        SyntaxRule(verb="search", action="V-SEARCH"),

        # ------------------------------------------------------------------ #
        # SHAKE                                                               #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="shake", action="V-SHAKE",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # SMELL                                                               #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="smell", action="V-SMELL",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="smell", action="V-SMELL"),

        # ------------------------------------------------------------------ #
        # SPIN                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="spin", action="V-SPIN",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # SQUEEZE                                                             #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="squeeze", action="V-SQUEEZE",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # STAND                                                               #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="stand", action="V-STAND"),

        # ------------------------------------------------------------------ #
        # SWAP — SWAP IDOL WITH SALT                                         #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="swap", action="V-SWAP",
                   obj1=ObjectSpec(locations=_held_car_have),
                   prep="with",
                   obj2=ObjectSpec(locations=_held_car_og_ir_have)),
        SyntaxRule(verb="swap", action="V-SWAP",
                   obj1=ObjectSpec(locations=_held_car_og_ir_have)),

        # PROP PASSAGE WITH BEAM (Quest 38)
        SyntaxRule(verb="prop", action="V-PROP",
                   obj1=ObjectSpec(locations=_held_car_og_ir),
                   prep="with",
                   obj2=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="prop", action="V-PROP",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # SWIM                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="swim", action="V-SWIM"),

        # ------------------------------------------------------------------ #
        # SWING                                                               #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="swing", action="V-SWING",
                   obj1=ObjectSpec(locations=_held_car_og_ir),
                   prep="at",
                   obj2=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir)),
        SyntaxRule(verb="swing", action="V-SWING",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # TAKE                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="take", action="V-TAKE", preaction="PRE-TAKE",
                   obj1=ObjectSpec(find_flag=TAKEBIT, locations=_held_car_og_ir_take_have_many)),
        SyntaxRule(verb="take", action="V-TAKE-FROM",
                   obj1=ObjectSpec(find_flag=TAKEBIT, locations=_held_car_og_ir_take_have_many),
                   prep="from",
                   obj2=ObjectSpec(find_flag=CONTBIT, locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # REMOVE — take off a worn item; REMOVE X FROM Y is a take           #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="remove", action="V-PRY",
                   obj1=ObjectSpec(locations=_held_car_og_ir),
                   prep="with",
                   obj2=ObjectSpec(locations=_held_car_have)),
        SyntaxRule(verb="remove", action="V-REMOVE",
                   obj1=ObjectSpec(locations=_held_car_og_ir_take)),
        SyntaxRule(verb="remove", action="V-TAKE-FROM",
                   obj1=ObjectSpec(find_flag=TAKEBIT, locations=_held_car_og_ir_take_have_many),
                   prep="from",
                   obj2=ObjectSpec(find_flag=CONTBIT, locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # TALK / TELL / ASK                                                  #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="disarm", action="V-DISARM",
                   obj1=ObjectSpec(locations=_og_ir)),
        SyntaxRule(verb="pay", action="V-PAY",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir)),
        SyntaxRule(verb="pay", action="V-PAY"),
        SyntaxRule(verb="challenge", action="V-CHALLENGE",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir)),
        SyntaxRule(verb="talk", particle="to",
                   action="V-TALK",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir)),
        SyntaxRule(verb="talk", action="V-TALK",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir)),
        SyntaxRule(verb="tell", action="V-TALK",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir),
                   prep="about",
                   obj2=ObjectSpec(locations=_held_car_og_ir_have)),
        SyntaxRule(verb="tell", action="V-TALK",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir)),

        # ------------------------------------------------------------------ #
        # THROW                                                               #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="throw", action="V-THROW",
                   obj1=ObjectSpec(locations=_held_car_have),
                   prep="at",
                   obj2=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir)),
        SyntaxRule(verb="throw", action="V-THROW",
                   obj1=ObjectSpec(locations=_held_car_have)),

        # ------------------------------------------------------------------ #
        # TIE                                                                 #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="tie", action="V-TIE",
                   obj1=ObjectSpec(locations=_held_car_have),
                   prep="to",
                   obj2=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="tie", action="V-TIE",
                   obj1=ObjectSpec(locations=_held_car_have)),

        # ------------------------------------------------------------------ #
        # TIP — TIP MAY [#] / TIP MAY [#] ZENNI                             #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="tip", action="V-TIP",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir)),
        SyntaxRule(verb="tip", action="V-TIP"),

        # ------------------------------------------------------------------ #
        # TURN                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="turn", particle="on", action="V-LAMP-ON",
                   obj1=ObjectSpec(find_flag=LIGHTBIT, locations=_held_car_og_ir)),
        SyntaxRule(verb="turn", particle="on", action="V-TURN-ON",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="turn", particle="off", action="V-LAMP-OFF",
                   obj1=ObjectSpec(find_flag=LIGHTBIT, locations=_held_car_og_ir)),
        SyntaxRule(verb="turn", particle="off", action="V-TURN-OFF",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="turn", particle="left", action="V-TURN-DIAL-LEFT",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="turn", particle="left", action="V-TURN-DIAL-LEFT"),
        SyntaxRule(verb="turn", particle="right", action="V-TURN-DIAL-RIGHT",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="turn", particle="right", action="V-TURN-DIAL-RIGHT"),
        SyntaxRule(verb="turn", action="V-TURN",
                   obj1=ObjectSpec(find_flag=TURNBIT, locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # UNLOCK                                                              #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="unlock", action="V-UNLOCK",
                   obj1=ObjectSpec(locations=_held_car_og_ir),
                   prep="with",
                   obj2=ObjectSpec(locations=_held_car_have)),
        SyntaxRule(verb="unlock", action="V-UNLOCK",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # UNLOAD — UNLOAD STONE / UNLOAD STONE FROM CART / RETURN STONE      #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="unload", action="V-UNLOAD",
                   obj1=ObjectSpec(locations=_held_car_og_ir),
                   prep="from",
                   obj2=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="unload", action="V-UNLOAD",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="unload", action="V-UNLOAD"),

        # ------------------------------------------------------------------ #
        # UNTIE                                                               #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="untie", action="V-UNTIE",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # MIX — MIX CLAY WITH WATER (Quest 49)                               #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="mix", action="V-MIX",
                   obj1=ObjectSpec(locations=_held_car_have),
                   prep="with",
                   obj2=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="mix", action="V-MIX",
                   obj1=ObjectSpec(locations=_held_car_have)),

        # ------------------------------------------------------------------ #
        # SEAL — SEAL JOINTS WITH MORTAR (Quest 22)                          #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="seal", action="V-SEAL",
                   obj1=ObjectSpec(locations=_og_ir),
                   prep="with",
                   obj2=ObjectSpec(locations=_held_car_have)),
        SyntaxRule(verb="seal", action="V-SEAL",
                   obj1=ObjectSpec(locations=_og_ir)),

        # ------------------------------------------------------------------ #
        # USE — USE PORTCULLIS BAR                                           #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="use", action="V-USE",
                   obj1=ObjectSpec(locations=_held_car_og_ir_have),
                   prep="on",
                   obj2=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="use", action="V-USE",
                   obj1=ObjectSpec(locations=_held_car_og_ir_have)),
        SyntaxRule(verb="use", action="V-USE"),

        # ------------------------------------------------------------------ #
        # WAIT                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="wait", action="V-WAIT"),

        # ------------------------------------------------------------------ #
        # WAKE                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="wake", action="V-WAKE",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir)),
        SyntaxRule(verb="wake", action="V-WAKE"),

        # ------------------------------------------------------------------ #
        # WALK / GO                                                           #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="walk", action="V-WALK",
                   obj1=ObjectSpec(locations=_og_ir)),
        SyntaxRule(verb="walk", action="V-WALK"),

        # ------------------------------------------------------------------ #
        # WAVE                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="wave", action="V-WAVE",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="wave", action="V-WAVE"),

        # ------------------------------------------------------------------ #
        # WEAR                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="wear", action="V-WEAR",
                   obj1=ObjectSpec(find_flag=WEARABLE, locations=_held_car_og_ir_take)),
        SyntaxRule(verb="wear", action="V-WEAR",
                   obj1=ObjectSpec(locations=_held_car_og_ir_take)),

        # ------------------------------------------------------------------ #
        # WIND                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="wind", action="V-WIND",
                   obj1=ObjectSpec(find_flag=TURNBIT, locations=_held_car_og_ir)),

        # ------------------------------------------------------------------ #
        # WISH                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="wish", action="V-WISH"),

        # ------------------------------------------------------------------ #
        # YELL                                                                #
        # ------------------------------------------------------------------ #
        SyntaxRule(verb="yell", action="V-YELL",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="yell", action="V-YELL"),
    ]

    return rules
