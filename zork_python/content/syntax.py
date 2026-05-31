"""
Syntax rules for Zork I.

Translates all SYNTAX declarations from gsyntax.zil into SyntaxRule objects
that the parser uses to match player input to verb actions.
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

# Extra flag names referenced in SYNTAX that are not in engine/world.py
LIGHTBIT   = "LIGHTBIT"
FLAMEBIT   = "FLAMEBIT"
FOODBIT    = "FOODBIT"
MAZEBIT    = "MAZEBIT"
NONLANDBIT = "NONLANDBIT"

# ---------------------------------------------------------------------------
# Commonly reused location frozensets
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


def make_syntax_rules() -> list[SyntaxRule]:
    """Return the complete list of SyntaxRules for Zork I."""

    rules = [
        # Game commands
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

        # ACTIVATE
        SyntaxRule(verb="activate", action="V-LAMP-ON",
                   obj1=ObjectSpec(find_flag=LIGHTBIT, locations=_held_car_og_ir)),

        # ANSWER
        SyntaxRule(verb="answer", action="V-ANSWER"),
        SyntaxRule(verb="answer", action="V-REPLY",
                   obj1=ObjectSpec()),

        # APPLY
        SyntaxRule(verb="apply", action="V-PUT", preaction="PRE-PUT",
                   obj1=ObjectSpec(), prep="to", obj2=ObjectSpec()),

        # ATTACK
        SyntaxRule(verb="attack", action="V-ATTACK",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir),
                   prep="with",
                   obj2=ObjectSpec(find_flag=WEAPONBIT, locations=_held_car_have)),

        # BACK
        SyntaxRule(verb="back", action="V-BACK"),

        # BLAST
        SyntaxRule(verb="blast", action="V-BLAST"),

        # BLOW
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

        # BOARD
        SyntaxRule(verb="board", action="V-BOARD", preaction="PRE-BOARD",
                   obj1=ObjectSpec(find_flag=VEHBIT, locations=_og_ir)),

        # BRUSH
        SyntaxRule(verb="brush", action="V-BRUSH",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="brush", action="V-BRUSH",
                   obj1=ObjectSpec(locations=_held_car_og_ir),
                   prep="with", obj2=ObjectSpec()),

        # BUG
        SyntaxRule(verb="bug", action="V-BUG"),

        # BURN
        SyntaxRule(verb="burn", action="V-BURN", preaction="PRE-BURN",
                   obj1=ObjectSpec(find_flag=BURNBIT, locations=_held_car_og_ir),
                   prep="with",
                   obj2=ObjectSpec(find_flag=FLAMEBIT, locations=_og_ir_held_car_have)),
        SyntaxRule(verb="burn", particle="down", action="V-BURN", preaction="PRE-BURN",
                   obj1=ObjectSpec(find_flag=BURNBIT, locations=_held_car_og_ir),
                   prep="with",
                   obj2=ObjectSpec(find_flag=FLAMEBIT, locations=_og_ir_held_car_have)),

        # CHOMP
        SyntaxRule(verb="chomp", action="V-CHOMP"),

        # CLIMB
        SyntaxRule(verb="climb", particle="up", action="V-CLIMB-UP",
                   obj1=ObjectSpec(find_flag=RMUNGBIT)),
        SyntaxRule(verb="climb", particle="up", action="V-CLIMB-UP",
                   obj1=ObjectSpec(find_flag=CLIMBBIT, locations=_og_ir)),
        SyntaxRule(verb="climb", particle="down", action="V-CLIMB-DOWN",
                   obj1=ObjectSpec(find_flag=RMUNGBIT)),
        SyntaxRule(verb="climb", particle="down", action="V-CLIMB-DOWN",
                   obj1=ObjectSpec(find_flag=CLIMBBIT, locations=_og_ir)),
        SyntaxRule(verb="climb", action="V-CLIMB-FOO",
                   obj1=ObjectSpec(find_flag=CLIMBBIT, locations=_og_ir)),
        SyntaxRule(verb="climb", particle="in", action="V-BOARD", preaction="PRE-BOARD",
                   obj1=ObjectSpec(find_flag=VEHBIT, locations=_og_ir)),
        SyntaxRule(verb="climb", particle="on", action="V-CLIMB-ON",
                   obj1=ObjectSpec(find_flag=VEHBIT, locations=_og_ir)),
        SyntaxRule(verb="climb", prep="with", action="V-THROUGH",
                   obj1=ObjectSpec()),

        # CLOSE
        SyntaxRule(verb="close", action="V-CLOSE",
                   obj1=ObjectSpec(find_flag=DOORBIT, locations=_held_car_og_ir)),

        # COMMAND
        SyntaxRule(verb="command", action="V-COMMAND",
                   obj1=ObjectSpec(find_flag=ACTORBIT)),

        # COUNT
        SyntaxRule(verb="count", action="V-COUNT",
                   obj1=ObjectSpec()),

        # CROSS
        SyntaxRule(verb="cross", action="V-CROSS",
                   obj1=ObjectSpec()),

        # CUT
        SyntaxRule(verb="cut", action="V-CUT",
                   obj1=ObjectSpec(),
                   prep="with",
                   obj2=ObjectSpec(find_flag=WEAPONBIT, locations=_held_car)),

        # CURSE
        SyntaxRule(verb="curse", action="V-CURSES"),
        SyntaxRule(verb="curse", action="V-CURSES",
                   obj1=ObjectSpec(find_flag=ACTORBIT)),

        # DEFLATE
        SyntaxRule(verb="deflate", action="V-DEFLATE",
                   obj1=ObjectSpec()),

        # DESTROY
        SyntaxRule(verb="destroy", action="V-MUNG", preaction="PRE-MUNG",
                   obj1=ObjectSpec(locations=_og_ir_held_car),
                   prep="with",
                   obj2=ObjectSpec(locations=frozenset({LOC_HELD, LOC_CARRIED, LOC_TAKE}))),
        SyntaxRule(verb="destroy", particle="down", action="V-MUNG", preaction="PRE-MUNG",
                   obj1=ObjectSpec(locations=_og_ir_held_car),
                   prep="with",
                   obj2=ObjectSpec(locations=frozenset({LOC_HELD, LOC_CARRIED, LOC_TAKE}))),
        SyntaxRule(verb="destroy", particle="in", action="V-OPEN",
                   obj1=ObjectSpec(locations=_og_ir_held_car)),

        # DIG
        SyntaxRule(verb="dig", prep="in", action="V-DIG",
                   obj1=ObjectSpec(locations=_og_ir)),
        SyntaxRule(verb="dig", prep="in", action="V-DIG",
                   obj1=ObjectSpec(locations=_og_ir),
                   obj2=ObjectSpec(find_flag=TOOLBIT, locations=_held_car_have)),
        SyntaxRule(verb="dig", action="V-DIG",
                   obj1=ObjectSpec(locations=_og_ir),
                   prep="with",
                   obj2=ObjectSpec(find_flag=TOOLBIT, locations=_held_car_have)),

        # DISEMBARK
        SyntaxRule(verb="disembark", action="V-DISEMBARK",
                   obj1=ObjectSpec(find_flag=VEHBIT, locations=_og_ir)),

        # DISENCHANT
        SyntaxRule(verb="disenchant", action="V-DISENCHANT",
                   obj1=ObjectSpec()),

        # DRINK
        SyntaxRule(verb="drink", action="V-DRINK",
                   obj1=ObjectSpec(find_flag=DRINKBIT, locations=_held_car_og_ir)),
        SyntaxRule(verb="drink", prep="from", action="V-DRINK-FROM",
                   obj1=ObjectSpec(locations=_held_car)),

        # DROP
        SyntaxRule(verb="drop", action="V-DROP", preaction="PRE-DROP",
                   obj1=ObjectSpec(locations=_held_many_have)),
        SyntaxRule(verb="drop", particle="down", action="V-PUT", preaction="PRE-PUT",
                   obj1=ObjectSpec(locations=_held_many_have),
                   obj2=ObjectSpec()),
        SyntaxRule(verb="drop", prep="in", action="V-PUT", preaction="PRE-PUT",
                   obj1=ObjectSpec(locations=_held_many_have),
                   obj2=ObjectSpec()),
        SyntaxRule(verb="drop", prep="on", action="V-PUT-ON", preaction="PRE-PUT",
                   obj1=ObjectSpec(locations=_held_many_have),
                   obj2=ObjectSpec()),

        # EAT
        SyntaxRule(verb="eat", action="V-EAT",
                   obj1=ObjectSpec(find_flag=FOODBIT, locations=_held_car_og_ir_take)),

        # ECHO
        SyntaxRule(verb="echo", action="V-ECHO"),

        # ENCHANT
        SyntaxRule(verb="enchant", action="V-ENCHANT",
                   obj1=ObjectSpec(locations=_og_ir)),

        # ENTER / EXIT
        SyntaxRule(verb="enter", action="V-ENTER"),
        SyntaxRule(verb="enter", action="V-THROUGH",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="exit", action="V-EXIT"),
        SyntaxRule(verb="exit", action="V-EXIT",
                   obj1=ObjectSpec()),

        # EXAMINE
        SyntaxRule(verb="examine", action="V-EXAMINE",
                   obj1=ObjectSpec(locations=_many)),
        SyntaxRule(verb="examine", prep="in", action="V-LOOK-INSIDE",
                   obj1=ObjectSpec(locations=frozenset({LOC_HELD, LOC_CARRIED, LOC_IN_ROOM, LOC_ON_GROUND, LOC_MANY}))),
        SyntaxRule(verb="examine", prep="on", action="V-LOOK-INSIDE",
                   obj1=ObjectSpec(locations=frozenset({LOC_HELD, LOC_CARRIED, LOC_IN_ROOM, LOC_ON_GROUND, LOC_MANY}))),

        # EXORCISE
        SyntaxRule(verb="exorcise", action="V-EXORCISE"),
        SyntaxRule(verb="exorcise", particle="out", action="V-EXORCISE",
                   obj1=ObjectSpec(find_flag=ACTORBIT)),
        SyntaxRule(verb="exorcise", particle="away", action="V-EXORCISE",
                   obj1=ObjectSpec(find_flag=ACTORBIT)),

        # EXTINGUISH
        SyntaxRule(verb="extinguish", action="V-LAMP-OFF",
                   obj1=ObjectSpec(find_flag=ONBIT, locations=_held_car_og_ir_take_have)),

        # FILL
        SyntaxRule(verb="fill", action="V-FILL", preaction="PRE-FILL",
                   obj1=ObjectSpec(find_flag=CONTBIT, locations=_held_car_og_ir),
                   prep="with", obj2=ObjectSpec()),
        SyntaxRule(verb="fill", action="V-FILL", preaction="PRE-FILL",
                   obj1=ObjectSpec(find_flag=CONTBIT, locations=_held_car_og_ir)),

        # FIND
        SyntaxRule(verb="find", action="V-FIND",
                   obj1=ObjectSpec()),

        # FOLLOW
        SyntaxRule(verb="follow", action="V-FOLLOW"),
        SyntaxRule(verb="follow", action="V-FOLLOW",
                   obj1=ObjectSpec()),

        # FROBOZZ
        SyntaxRule(verb="frobozz", action="V-FROBOZZ"),

        # GIVE
        SyntaxRule(verb="give", action="V-GIVE", preaction="PRE-GIVE",
                   obj1=ObjectSpec(locations=frozenset({LOC_MANY, LOC_HELD, LOC_HAVE})),
                   prep="to",
                   obj2=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir)),
        SyntaxRule(verb="give", action="V-SGIVE", preaction="PRE-SGIVE",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir),
                   obj2=ObjectSpec(locations=frozenset({LOC_MANY, LOC_HELD, LOC_HAVE}))),

        # HATCH
        SyntaxRule(verb="hatch", action="V-HATCH",
                   obj1=ObjectSpec()),

        # HELLO
        SyntaxRule(verb="hello", action="V-HELLO"),
        SyntaxRule(verb="hello", action="V-HELLO",
                   obj1=ObjectSpec()),

        # INCANT
        SyntaxRule(verb="incant", action="V-INCANT"),

        # INFLAT / INFLATE
        SyntaxRule(verb="inflat", action="V-INFLATE",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="inflat", action="V-INFLATE",
                   obj1=ObjectSpec(),
                   prep="with",
                   obj2=ObjectSpec(find_flag=TOOLBIT, locations=_og_ir_held_car)),

        # JUMP
        SyntaxRule(verb="jump", action="V-LEAP"),
        SyntaxRule(verb="jump", particle="over", action="V-LEAP",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="jump", particle="across", action="V-LEAP",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="jump", particle="in", action="V-LEAP",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="jump", particle="from", action="V-LEAP",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="jump", particle="off", action="V-LEAP",
                   obj1=ObjectSpec()),

        # KICK
        SyntaxRule(verb="kick", action="V-KICK",
                   obj1=ObjectSpec()),

        # KILL
        SyntaxRule(verb="kill", action="V-ATTACK",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir),
                   prep="with",
                   obj2=ObjectSpec(find_flag=WEAPONBIT, locations=_held_car_have)),

        # STAB
        SyntaxRule(verb="stab", action="V-STAB",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir)),
        SyntaxRule(verb="stab", action="V-ATTACK",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir),
                   prep="with",
                   obj2=ObjectSpec(find_flag=WEAPONBIT, locations=_held_car_have)),

        # KISS
        SyntaxRule(verb="kiss", action="V-KISS",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir)),

        # KNOCK
        SyntaxRule(verb="knock", prep="at", action="V-KNOCK",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="knock", prep="on", action="V-KNOCK",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="knock", particle="down", action="V-ATTACK",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir)),

        # LAUNCH
        SyntaxRule(verb="launch", action="V-LAUNCH"),
        SyntaxRule(verb="launch", action="V-LAUNCH",
                   obj1=ObjectSpec(find_flag=VEHBIT)),

        # LEAN
        SyntaxRule(verb="lean", prep="on", action="V-LEAN-ON",
                   obj1=ObjectSpec(locations=_held_have)),

        # LEAVE
        SyntaxRule(verb="leave", action="V-LEAVE"),
        SyntaxRule(verb="leave", action="V-DROP", preaction="PRE-DROP",
                   obj1=ObjectSpec()),

        # LIGHT
        SyntaxRule(verb="light", action="V-LAMP-ON",
                   obj1=ObjectSpec(find_flag=LIGHTBIT, locations=_held_car_og_ir_take_have)),
        SyntaxRule(verb="light", action="V-BURN", preaction="PRE-BURN",
                   obj1=ObjectSpec(find_flag=LIGHTBIT, locations=_held_car_og_ir),
                   prep="with",
                   obj2=ObjectSpec(find_flag=FLAMEBIT, locations=_held_car_take_have)),

        # LISTEN
        SyntaxRule(verb="listen", prep="to", action="V-LISTEN",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="listen", prep="for", action="V-LISTEN",
                   obj1=ObjectSpec()),

        # LOCK
        SyntaxRule(verb="lock", action="V-LOCK",
                   obj1=ObjectSpec(locations=_og_ir),
                   prep="with",
                   obj2=ObjectSpec(find_flag=TOOLBIT, locations=_held_car_og_ir_take)),

        # LOOK
        SyntaxRule(verb="look", action="V-LOOK"),
        SyntaxRule(verb="look", particle="around", action="V-LOOK",
                   obj1=ObjectSpec(find_flag=RMUNGBIT)),
        SyntaxRule(verb="look", particle="up", action="V-LOOK",
                   obj1=ObjectSpec(find_flag=RMUNGBIT)),
        SyntaxRule(verb="look", particle="down", action="V-LOOK",
                   obj1=ObjectSpec(find_flag=RMUNGBIT)),
        SyntaxRule(verb="look", prep="at", action="V-EXAMINE",
                   obj1=ObjectSpec(locations=_held_car_og_ir)),
        SyntaxRule(verb="look", prep="on", action="V-LOOK-ON",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="look", prep="with", action="V-LOOK-INSIDE",
                   obj1=ObjectSpec(locations=_held_car_og_ir_many)),
        SyntaxRule(verb="look", prep="under", action="V-LOOK-UNDER",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="look", prep="behind", action="V-LOOK-BEHIND",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="look", prep="in", action="V-LOOK-INSIDE",
                   obj1=ObjectSpec(locations=_held_car_og_ir_many)),
        SyntaxRule(verb="look", prep="at", action="V-READ", preaction="PRE-READ",
                   obj1=ObjectSpec(locations=_held_car_og_ir),
                   obj2=ObjectSpec()),
        SyntaxRule(verb="look", prep="for", action="V-FIND",
                   obj1=ObjectSpec()),

        # LOWER
        SyntaxRule(verb="lower", action="V-LOWER",
                   obj1=ObjectSpec()),

        # LUBRICATE
        SyntaxRule(verb="lubricate", action="V-OIL",
                   obj1=ObjectSpec(),
                   prep="with", obj2=ObjectSpec(locations=_held_car)),

        # MAKE
        SyntaxRule(verb="make", action="V-MAKE",
                   obj1=ObjectSpec()),

        # MELT
        SyntaxRule(verb="melt", action="V-MELT",
                   obj1=ObjectSpec(),
                   prep="with",
                   obj2=ObjectSpec(find_flag=FLAMEBIT, locations=_held_car_og_ir)),

        # MOVE
        SyntaxRule(verb="move", action="V-MOVE", preaction="PRE-MOVE",
                   obj1=ObjectSpec(locations=_og_ir)),
        SyntaxRule(verb="move", action="V-PUSH-TO",
                   obj1=ObjectSpec(locations=_og_ir),
                   obj2=ObjectSpec()),
        SyntaxRule(verb="move", prep="to", action="V-PUSH-TO",
                   obj1=ObjectSpec(locations=_og_ir),
                   obj2=ObjectSpec()),
        SyntaxRule(verb="move", prep="in", action="V-PUT", preaction="PRE-PUT",
                   obj1=ObjectSpec(locations=_held_many_have),
                   obj2=ObjectSpec()),
        SyntaxRule(verb="move", prep="with", action="V-TURN", preaction="PRE-TURN",
                   obj1=ObjectSpec(),
                   obj2=ObjectSpec(find_flag=TOOLBIT)),
        SyntaxRule(verb="roll", particle="up", action="V-MOVE", preaction="PRE-MOVE",
                   obj1=ObjectSpec(locations=_og_ir)),
        SyntaxRule(verb="roll", action="V-MOVE", preaction="PRE-MOVE",
                   obj1=ObjectSpec(locations=_og_ir)),

        # MUMBLE
        SyntaxRule(verb="mumble", action="V-MUMBLE"),

        # ODYSSEUS
        SyntaxRule(verb="odysseus", action="V-ODYSSEUS"),

        # OPEN
        SyntaxRule(verb="open", action="V-OPEN",
                   obj1=ObjectSpec(find_flag=DOORBIT, locations=_held_car_og_ir)),
        SyntaxRule(verb="open", particle="up", action="V-OPEN",
                   obj1=ObjectSpec(find_flag=DOORBIT, locations=_held_car_og_ir)),
        SyntaxRule(verb="open", action="V-OPEN",
                   obj1=ObjectSpec(find_flag=DOORBIT, locations=_held_car_og_ir),
                   prep="with",
                   obj2=ObjectSpec(find_flag=TOOLBIT, locations=_og_ir_held_car_have)),

        # PICK
        SyntaxRule(verb="pick", action="V-PICK",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="pick", action="V-PICK",
                   obj1=ObjectSpec(),
                   prep="with", obj2=ObjectSpec()),
        SyntaxRule(verb="pick", particle="up", action="V-TAKE", preaction="PRE-TAKE",
                   obj1=ObjectSpec(find_flag=TAKEBIT, locations=_og_ir_many)),

        # PLAY
        SyntaxRule(verb="play", action="V-PLAY",
                   obj1=ObjectSpec()),

        # PLUG
        SyntaxRule(verb="plug", action="V-PLUG",
                   obj1=ObjectSpec(),
                   prep="with", obj2=ObjectSpec()),

        # PLUGH
        SyntaxRule(verb="plugh", action="V-ADVENT"),

        # POKE
        SyntaxRule(verb="poke", action="V-MUNG", preaction="PRE-MUNG",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir),
                   prep="with",
                   obj2=ObjectSpec(find_flag=WEAPONBIT, locations=_held_car_have)),

        # PUNCTURE
        SyntaxRule(verb="puncture", action="V-MUNG", preaction="PRE-MUNG",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir),
                   prep="with",
                   obj2=ObjectSpec(find_flag=WEAPONBIT, locations=_held_car_have)),

        # POUR
        SyntaxRule(verb="pour", action="V-DROP", preaction="PRE-DROP",
                   obj1=ObjectSpec(locations=_held_car)),
        SyntaxRule(verb="pour", prep="in", action="V-DROP", preaction="PRE-DROP",
                   obj1=ObjectSpec(locations=_held_car),
                   obj2=ObjectSpec()),
        SyntaxRule(verb="pour", prep="on", action="V-POUR-ON",
                   obj1=ObjectSpec(locations=_held_car),
                   obj2=ObjectSpec()),
        SyntaxRule(verb="pour", prep="from", action="V-DROP", preaction="PRE-DROP",
                   obj1=ObjectSpec(locations=_held_car),
                   obj2=ObjectSpec()),

        # PRAY
        SyntaxRule(verb="pray", action="V-PRAY"),

        # PULL
        SyntaxRule(verb="pull", action="V-MOVE", preaction="PRE-MOVE",
                   obj1=ObjectSpec(locations=_og_ir)),
        SyntaxRule(verb="pull", prep="on", action="V-MOVE", preaction="PRE-MOVE",
                   obj1=ObjectSpec(locations=_og_ir)),
        SyntaxRule(verb="pull", particle="up", action="V-MOVE", preaction="PRE-MOVE",
                   obj1=ObjectSpec(locations=_og_ir)),

        # PUMP
        SyntaxRule(verb="pump", particle="up", action="V-PUMP",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="pump", particle="up", action="V-PUMP",
                   obj1=ObjectSpec(),
                   prep="with", obj2=ObjectSpec()),

        # PUSH
        SyntaxRule(verb="push", action="V-PUSH-TO",
                   obj1=ObjectSpec(locations=_og_ir),
                   obj2=ObjectSpec()),
        SyntaxRule(verb="push", prep="to", action="V-PUSH-TO",
                   obj1=ObjectSpec(locations=_og_ir),
                   obj2=ObjectSpec()),
        SyntaxRule(verb="push", action="V-PUSH",
                   obj1=ObjectSpec(locations=_og_ir_many)),
        SyntaxRule(verb="push", prep="on", action="V-PUSH",
                   obj1=ObjectSpec(locations=_og_ir_many)),
        SyntaxRule(verb="push", prep="with", action="V-TURN", preaction="PRE-TURN",
                   obj1=ObjectSpec(),
                   obj2=ObjectSpec(find_flag=TOOLBIT)),
        SyntaxRule(verb="push", prep="under", action="V-PUT-UNDER",
                   obj1=ObjectSpec(),
                   obj2=ObjectSpec()),

        # PUT
        SyntaxRule(verb="put", prep="in", action="V-PUT", preaction="PRE-PUT",
                   obj1=ObjectSpec(locations=_held_many_have),
                   obj2=ObjectSpec()),
        SyntaxRule(verb="put", prep="on", action="V-PUT-ON", preaction="PRE-PUT",
                   obj1=ObjectSpec(locations=_held_many_have),
                   obj2=ObjectSpec()),
        SyntaxRule(verb="put", particle="down", action="V-DROP", preaction="PRE-DROP",
                   obj1=ObjectSpec(locations=frozenset({LOC_HELD, LOC_MANY}))),
        SyntaxRule(verb="put", prep="under", action="V-PUT-UNDER",
                   obj1=ObjectSpec(locations=_held_have),
                   obj2=ObjectSpec()),
        SyntaxRule(verb="put", particle="out", action="V-LAMP-OFF",
                   obj1=ObjectSpec(find_flag=ONBIT, locations=_held_car_og_ir_take_have)),
        SyntaxRule(verb="put", particle="on", action="V-WEAR",
                   obj1=ObjectSpec(locations=frozenset({LOC_IN_ROOM, LOC_ON_GROUND, LOC_CARRIED, LOC_MANY}))),
        SyntaxRule(verb="put", prep="behind", action="V-PUT-BEHIND",
                   obj1=ObjectSpec(locations=_held_many_have),
                   obj2=ObjectSpec()),

        # RAISE
        SyntaxRule(verb="raise", action="V-RAISE",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="raise", particle="up", action="V-RAISE",
                   obj1=ObjectSpec()),

        # RAPE
        SyntaxRule(verb="rape", action="V-RAPE",
                   obj1=ObjectSpec(find_flag=ACTORBIT)),

        # READ
        SyntaxRule(verb="read", action="V-READ", preaction="PRE-READ",
                   obj1=ObjectSpec(find_flag=READBIT, locations=_held_car_og_ir_take)),
        SyntaxRule(verb="read", prep="from", action="V-READ", preaction="PRE-READ",
                   obj1=ObjectSpec(find_flag=READBIT, locations=_held_car_og_ir_take)),
        SyntaxRule(verb="read", action="V-READ", preaction="PRE-READ",
                   obj1=ObjectSpec(find_flag=READBIT, locations=_held_car_og_ir_take),
                   prep="with", obj2=ObjectSpec()),
        SyntaxRule(verb="read", action="V-READ-PAGE",
                   obj1=ObjectSpec(find_flag=READBIT, locations=_held_car_og_ir_take),
                   obj2=ObjectSpec()),

        # REPENT
        SyntaxRule(verb="repent", action="V-REPENT"),

        # RING
        SyntaxRule(verb="ring", action="V-RING",
                   obj1=ObjectSpec(locations=_take)),
        SyntaxRule(verb="ring", action="V-RING",
                   obj1=ObjectSpec(locations=_take),
                   prep="with", obj2=ObjectSpec()),

        # RUB
        SyntaxRule(verb="rub", action="V-RUB",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="rub", action="V-RUB",
                   obj1=ObjectSpec(),
                   prep="with", obj2=ObjectSpec()),

        # TALK / SAY
        SyntaxRule(verb="talk", prep="to", action="V-TELL",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_in_room)),
        SyntaxRule(verb="say", action="V-SAY"),

        # SEARCH
        SyntaxRule(verb="search", action="V-SEARCH",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="search", prep="in", action="V-SEARCH",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="search", prep="for", action="V-FIND",
                   obj1=ObjectSpec()),

        # SEND
        SyntaxRule(verb="send", prep="for", action="V-SEND",
                   obj1=ObjectSpec()),

        # SHAKE
        SyntaxRule(verb="shake", action="V-SHAKE",
                   obj1=ObjectSpec(locations=_have)),

        # SKIP
        SyntaxRule(verb="skip", action="V-SKIP"),

        # SLIDE
        SyntaxRule(verb="slide", prep="under", action="V-PUT-UNDER",
                   obj1=ObjectSpec(),
                   obj2=ObjectSpec()),
        SyntaxRule(verb="slide", action="V-PUSH-TO",
                   obj1=ObjectSpec(locations=_og_ir),
                   obj2=ObjectSpec()),
        SyntaxRule(verb="slide", prep="to", action="V-PUSH-TO",
                   obj1=ObjectSpec(locations=_og_ir),
                   obj2=ObjectSpec()),

        # SMELL
        SyntaxRule(verb="smell", action="V-SMELL",
                   obj1=ObjectSpec()),

        # SPIN
        SyntaxRule(verb="spin", action="V-SPIN",
                   obj1=ObjectSpec()),

        # SPRAY
        SyntaxRule(verb="spray", prep="on", action="V-SPRAY",
                   obj1=ObjectSpec(),
                   obj2=ObjectSpec()),
        SyntaxRule(verb="spray", prep="with", action="V-SSPRAY",
                   obj1=ObjectSpec(),
                   obj2=ObjectSpec()),

        # SQUEEZE
        SyntaxRule(verb="squeeze", action="V-SQUEEZE",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="squeeze", prep="on", action="V-PUT", preaction="PRE-PUT",
                   obj1=ObjectSpec(),
                   obj2=ObjectSpec()),

        # STAND
        SyntaxRule(verb="stand", action="V-STAND"),
        SyntaxRule(verb="stand", particle="up", action="V-STAND",
                   obj1=ObjectSpec(find_flag=RMUNGBIT)),

        # STAY
        SyntaxRule(verb="stay", action="V-STAY"),

        # STRIKE
        SyntaxRule(verb="strike", action="V-ATTACK",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir),
                   prep="with",
                   obj2=ObjectSpec(find_flag=WEAPONBIT, locations=_og_ir_held_car_have)),
        SyntaxRule(verb="strike", action="V-STRIKE",
                   obj1=ObjectSpec(locations=_og_ir_held_car)),

        # SWIM
        SyntaxRule(verb="swim", action="V-SWIM"),
        SyntaxRule(verb="swim", prep="in", action="V-SWIM",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="swim", particle="across", action="V-SWIM",
                   obj1=ObjectSpec()),

        # SWING
        SyntaxRule(verb="swing", action="V-SWING",
                   obj1=ObjectSpec(find_flag=WEAPONBIT, locations=_held_car_have)),
        SyntaxRule(verb="swing", action="V-SWING",
                   obj1=ObjectSpec(find_flag=WEAPONBIT, locations=_held_car_have),
                   prep="at",
                   obj2=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir)),

        # TAKE
        SyntaxRule(verb="take", action="V-TAKE", preaction="PRE-TAKE",
                   obj1=ObjectSpec(find_flag=TAKEBIT, locations=_og_ir_many)),
        SyntaxRule(verb="take", particle="in", action="V-BOARD", preaction="PRE-BOARD",
                   obj1=ObjectSpec(find_flag=VEHBIT, locations=_og_ir)),
        SyntaxRule(verb="take", particle="out", action="V-DISEMBARK",
                   obj1=ObjectSpec(find_flag=RMUNGBIT, locations=_og_ir)),
        SyntaxRule(verb="take", prep="on", action="V-CLIMB-ON",
                   obj1=ObjectSpec(find_flag=VEHBIT, locations=_og_ir)),
        SyntaxRule(verb="take", particle="up", action="V-STAND",
                   obj1=ObjectSpec(find_flag=RMUNGBIT)),
        SyntaxRule(verb="take", particle="out", action="V-TAKE", preaction="PRE-TAKE",
                   obj1=ObjectSpec(find_flag=TAKEBIT, locations=_car_ir_many),
                   obj2=ObjectSpec()),
        SyntaxRule(verb="take", particle="off", action="V-TAKE", preaction="PRE-TAKE",
                   obj1=ObjectSpec(find_flag=TAKEBIT, locations=_car_ir_many),
                   obj2=ObjectSpec()),
        SyntaxRule(verb="take", prep="from", action="V-TAKE", preaction="PRE-TAKE",
                   obj1=ObjectSpec(find_flag=TAKEBIT, locations=frozenset({LOC_IN_ROOM, LOC_CARRIED, LOC_MANY})),
                   obj2=ObjectSpec()),

        # TELL
        SyntaxRule(verb="tell", action="V-TELL",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_in_room)),
        SyntaxRule(verb="tell", action="V-TELL",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_in_room),
                   prep="about", obj2=ObjectSpec()),

        # THROW
        SyntaxRule(verb="throw", action="V-THROW",
                   obj1=ObjectSpec(locations=_held_car_have),
                   prep="at",
                   obj2=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir)),
        SyntaxRule(verb="throw", action="V-THROW",
                   obj1=ObjectSpec(locations=_held_car_have),
                   prep="with",
                   obj2=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir)),
        SyntaxRule(verb="throw", action="V-OVERBOARD",
                   obj1=ObjectSpec(),
                   obj2=ObjectSpec()),
        SyntaxRule(verb="throw", prep="in", action="V-PUT", preaction="PRE-PUT",
                   obj1=ObjectSpec(locations=_held_car_have),
                   obj2=ObjectSpec()),
        SyntaxRule(verb="throw", prep="on", action="V-PUT-ON", preaction="PRE-PUT",
                   obj1=ObjectSpec(locations=_held_car_have),
                   obj2=ObjectSpec()),
        SyntaxRule(verb="throw", particle="off", action="V-THROW-OFF",
                   obj1=ObjectSpec(locations=_held_car_have),
                   obj2=ObjectSpec()),
        SyntaxRule(verb="throw", particle="over", action="V-THROW-OFF",
                   obj1=ObjectSpec(locations=_held_car_have),
                   obj2=ObjectSpec()),

        # TIE
        SyntaxRule(verb="tie", prep="to", action="V-TIE",
                   obj1=ObjectSpec(),
                   obj2=ObjectSpec()),
        SyntaxRule(verb="tie", particle="up", action="V-TIE-UP",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir),
                   prep="with",
                   obj2=ObjectSpec(find_flag=TOOLBIT, locations=_og_ir_held_car_have)),

        # TREASURE
        SyntaxRule(verb="treasure", action="V-TREASURE"),

        # TURN
        SyntaxRule(verb="turn", action="V-TURN", preaction="PRE-TURN",
                   obj1=ObjectSpec(find_flag=TURNBIT, locations=_held_car_og_ir),
                   prep="with",
                   obj2=ObjectSpec(find_flag=RMUNGBIT)),
        SyntaxRule(verb="turn", particle="on", action="V-LAMP-ON",
                   obj1=ObjectSpec(find_flag=LIGHTBIT, locations=_held_car_og_ir)),
        SyntaxRule(verb="turn", particle="on", action="V-LAMP-ON",
                   obj1=ObjectSpec(),
                   prep="with",
                   obj2=ObjectSpec(locations=_have)),
        SyntaxRule(verb="turn", particle="off", action="V-LAMP-OFF",
                   obj1=ObjectSpec(find_flag=ONBIT, locations=_held_car_og_ir_take_have)),
        SyntaxRule(verb="turn", prep="to", action="V-TURN", preaction="PRE-TURN",
                   obj1=ObjectSpec(find_flag=TURNBIT),
                   obj2=ObjectSpec()),
        SyntaxRule(verb="turn", prep="for", action="V-TURN", preaction="PRE-TURN",
                   obj1=ObjectSpec(find_flag=TURNBIT),
                   obj2=ObjectSpec()),

        # UNLOCK
        SyntaxRule(verb="unlock", action="V-UNLOCK",
                   obj1=ObjectSpec(locations=_og_ir),
                   prep="with",
                   obj2=ObjectSpec(find_flag=TOOLBIT, locations=_held_car_og_ir_take)),
        SyntaxRule(verb="unlock", action="V-UNLOCK",
                   obj1=ObjectSpec(locations=_og_ir)),

        # UNTIE
        SyntaxRule(verb="untie", action="V-UNTIE",
                   obj1=ObjectSpec(locations=_og_ir_held_car)),
        SyntaxRule(verb="untie", action="V-UNTIE",
                   obj1=ObjectSpec(locations=_og_ir_held_car),
                   prep="from", obj2=ObjectSpec()),

        # WAIT
        SyntaxRule(verb="wait", action="V-WAIT"),

        # WAKE
        SyntaxRule(verb="wake", action="V-ALARM",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir)),
        SyntaxRule(verb="wake", particle="up", action="V-ALARM",
                   obj1=ObjectSpec(find_flag=ACTORBIT, locations=_og_ir)),

        # WALK
        SyntaxRule(verb="walk", action="V-WALK-AROUND"),
        SyntaxRule(verb="walk", action="V-WALK",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="walk", particle="away", action="V-WALK",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="walk", particle="in", action="V-THROUGH",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="walk", prep="with", action="V-THROUGH",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="walk", prep="on", action="V-THROUGH",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="walk", particle="over", action="V-LEAP",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="walk", prep="to", action="V-WALK-TO",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="walk", particle="around", action="V-WALK-AROUND",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="walk", particle="up", action="V-CLIMB-UP",
                   obj1=ObjectSpec(find_flag=CLIMBBIT, locations=_og_ir)),
        SyntaxRule(verb="walk", particle="down", action="V-CLIMB-DOWN",
                   obj1=ObjectSpec(find_flag=CLIMBBIT, locations=_og_ir)),

        # WAVE
        SyntaxRule(verb="wave", action="V-WAVE",
                   obj1=ObjectSpec(locations=_held_car_take_have)),
        SyntaxRule(verb="wave", action="V-WAVE",
                   obj1=ObjectSpec(locations=_held_car_take_have),
                   prep="at", obj2=ObjectSpec()),
        SyntaxRule(verb="wave", prep="at", action="V-WAVE",
                   obj1=ObjectSpec()),

        # WEAR
        SyntaxRule(verb="wear", action="V-WEAR",
                   obj1=ObjectSpec()),

        # WIN
        SyntaxRule(verb="win", action="V-WIN"),

        # WIND
        SyntaxRule(verb="wind", action="V-WIND",
                   obj1=ObjectSpec()),
        SyntaxRule(verb="wind", particle="up", action="V-WIND",
                   obj1=ObjectSpec()),

        # WISH
        SyntaxRule(verb="wish", action="V-WISH"),

        # YELL
        SyntaxRule(verb="yell", action="V-YELL"),

        # ZORK
        SyntaxRule(verb="zork", action="V-ZORK"),
    ]

    return rules
