"""
Game objects for Zork I.

Translates all <OBJECT> declarations from 1dungeon.zil and gglobals.zil
into GameObject instances registered with the World.
"""

from __future__ import annotations

from engine.world import (
    World, GameObject,
    TAKEBIT, CONTBIT, OPENBIT, TRYTAKEBIT, NDESCBIT, BURNBIT, READBIT,
    TURNBIT, ACTORBIT, WEAPONBIT, CLIMBBIT, DRINKBIT, DOORBIT, TOOLBIT,
    INVISIBLE, SACREDBIT, SURFACEBIT, TOUCHBIT, RMUNGBIT, TRANSBIT,
    WEARBIT, VEHBIT, SEARCHBIT, FIGHTBIT, STAGGERED, ONBIT, RLANDBIT,
)

# Additional flags not in engine/world.py
LIGHTBIT   = "LIGHTBIT"
FLAMEBIT   = "FLAMEBIT"
FOODBIT    = "FOODBIT"
MAZEBIT    = "MAZEBIT"
NONLANDBIT = "NONLANDBIT"


def make_objects(world: World) -> None:
    """Create all GameObjects and register them with the world."""
    from content.actions import ACTION_HANDLERS

    def obj(name, **kwargs):
        action_name = kwargs.pop("action_name", None)
        if action_name:
            kwargs["action"] = ACTION_HANDLERS.get(action_name)
        o = GameObject(name=name, **kwargs)
        world.register_object(o)
        return o

    # ---- Global scenery objects (from gglobals.zil) ----

    obj("GLOBAL-OBJECTS",
        synonyms=[],
        flags={RMUNGBIT, INVISIBLE, TOUCHBIT, SURFACEBIT, TRYTAKEBIT,
               OPENBIT, SEARCHBIT, TRANSBIT, ONBIT, RLANDBIT, FIGHTBIT,
               STAGGERED, WEARBIT},
        capacity=10000)

    obj("LOCAL-GLOBALS",
        synonyms=["zzmgck"],
        size=0, capacity=0)

    obj("ROOMS",
        synonyms=[])

    obj("INTNUM",
        synonyms=["intnum"],
        desc="number",
        flags={TOOLBIT})

    obj("PSEUDO-OBJECT",
        synonyms=[],
        desc="pseudo",
        action_name="CRETIN-FCN")

    obj("IT",
        synonyms=["it", "them", "her", "him"],
        desc="random object",
        flags={NDESCBIT, TOUCHBIT})

    obj("NOT-HERE-OBJECT",
        synonyms=[],
        desc="such thing",
        action_name="NOT-HERE-OBJECT-F")

    obj("BLESSINGS",
        synonyms=["blessings", "graces"],
        desc="blessings",
        flags={NDESCBIT})

    obj("STAIRS",
        synonyms=["stairs", "steps", "staircase", "stairway"],
        adjectives=["stone", "dark", "marble", "forbidding", "steep"],
        desc="stairs",
        flags={NDESCBIT, CLIMBBIT},
        action_name="STAIRS-F")

    obj("SAILOR",
        synonyms=["sailor", "footpad", "aviator"],
        desc="sailor",
        flags={NDESCBIT},
        action_name="SAILOR-FCN")

    obj("GROUND",
        synonyms=["ground", "sand", "dirt", "floor"],
        desc="ground",
        action_name="GROUND-FUNCTION")

    obj("GRUE",
        synonyms=["grue"],
        adjectives=["lurking", "sinister", "hungry", "silent"],
        desc="lurking grue",
        action_name="GRUE-FUNCTION")

    obj("LUNGS",
        synonyms=["lungs", "air", "mouth", "breath"],
        desc="blast of air",
        flags={NDESCBIT})

    obj("ME",
        synonyms=["me", "myself", "self", "cretin"],
        desc="you",
        flags={ACTORBIT},
        action_name="CRETIN-FCN")

    obj("ADVENTURER",
        synonyms=["adventurer"],
        desc="cretin",
        flags={NDESCBIT, INVISIBLE, SACREDBIT, ACTORBIT},
        strength=0)

    obj("PATHOBJ",
        synonyms=["trail", "path"],
        adjectives=["forest", "narrow", "long", "winding"],
        desc="passage",
        flags={NDESCBIT},
        action_name="PATH-OBJECT")

    obj("ZORKMID",
        synonyms=["zorkmid"],
        desc="zorkmid",
        action_name="ZORKMID-FUNCTION")

    obj("HANDS",
        synonyms=["pair", "hands", "hand"],
        adjectives=["bare"],
        desc="pair of hands",
        flags={NDESCBIT, TOOLBIT})

    # ---- Objects from 1dungeon.zil ----

    obj("BOARD",
        synonyms=["boards", "board"],
        desc="board",
        flags={NDESCBIT},
        action_name="BOARD-F")

    obj("TEETH",
        synonyms=["overboard", "teeth"],
        desc="set of teeth",
        flags={NDESCBIT},
        action_name="TEETH-F")

    obj("WALL",
        synonyms=["wall", "walls"],
        adjectives=["surrounding"],
        desc="surrounding wall")

    obj("GRANITE-WALL",
        synonyms=["wall"],
        adjectives=["granite"],
        desc="granite wall",
        action_name="GRANITE-WALL-F")

    obj("SONGBIRD",
        synonyms=["bird", "songbird"],
        adjectives=["song"],
        desc="songbird",
        flags={NDESCBIT},
        action_name="SONGBIRD-F")

    obj("WHITE-HOUSE",
        synonyms=["house"],
        adjectives=["white", "beauti", "coloni"],
        desc="white house",
        flags={NDESCBIT},
        action_name="WHITE-HOUSE-F")

    obj("FOREST",
        synonyms=["forest", "trees", "pines", "hemlocks"],
        desc="forest",
        flags={NDESCBIT},
        action_name="FOREST-F")

    obj("TREE",
        synonyms=["tree", "branch"],
        adjectives=["large", "storm"],
        desc="tree",
        flags={NDESCBIT, CLIMBBIT})

    obj("MOUNTAIN-RANGE",
        synonyms=["mountain", "range"],
        adjectives=["impassable", "flathead"],
        desc="mountain range",
        flags={NDESCBIT, CLIMBBIT},
        action_name="MOUNTAIN-RANGE-F")

    obj("GLOBAL-WATER",
        synonyms=["water", "quantity"],
        desc="water",
        flags={DRINKBIT},
        action_name="WATER-F")

    obj("WATER",
        synonyms=["water", "quantity", "liquid", "h2o"],
        desc="quantity of water",
        flags={TRYTAKEBIT, TAKEBIT, DRINKBIT},
        action_name="WATER-F",
        size=4)

    obj("KITCHEN-WINDOW",
        synonyms=["window"],
        adjectives=["kitchen", "small"],
        desc="kitchen window",
        flags={DOORBIT, NDESCBIT},
        action_name="KITCHEN-WINDOW-F")

    obj("CHIMNEY",
        synonyms=["chimney"],
        adjectives=["dark", "narrow"],
        desc="chimney",
        action_name="CHIMNEY-F",
        flags={CLIMBBIT, NDESCBIT})

    obj("GHOSTS",
        synonyms=["ghosts", "spirits", "fiends", "force"],
        adjectives=["invisible", "evil"],
        desc="number of ghosts",
        flags={ACTORBIT, NDESCBIT},
        action_name="GHOSTS-F")

    obj("SKULL",
        synonyms=["skull", "head", "treasure"],
        adjectives=["crystal"],
        desc="crystal skull",
        fdesc="Lying in one corner of the room is a beautifully carved crystal skull.\nIt appears to be grinning at you rather nastily.",
        flags={TAKEBIT},
        value=10, tvalue=10)

    obj("LOWERED-BASKET",
        synonyms=["cage", "dumbwaiter", "basket"],
        adjectives=["lowered"],
        ldesc="From the chain is suspended a basket.",
        desc="basket",
        flags={TRYTAKEBIT},
        action_name="BASKET-F")

    obj("RAISED-BASKET",
        synonyms=["cage", "dumbwaiter", "basket"],
        desc="basket",
        flags={TRANSBIT, TRYTAKEBIT, CONTBIT, OPENBIT},
        action_name="BASKET-F",
        ldesc="At the end of the chain is a basket.",
        capacity=50)

    obj("LUNCH",
        synonyms=["food", "sandwich", "lunch", "dinner"],
        adjectives=["hot", "pepper"],
        desc="lunch",
        flags={TAKEBIT, FOODBIT},
        ldesc="A hot pepper sandwich is here.")

    obj("BAT",
        synonyms=["bat", "vampire"],
        adjectives=["vampire", "deranged"],
        desc="bat",
        flags={ACTORBIT, TRYTAKEBIT},
        action_name="BAT-F")

    obj("BELL",
        synonyms=["bell"],
        adjectives=["small", "brass"],
        desc="brass bell",
        flags={TAKEBIT},
        action_name="BELL-F")

    obj("HOT-BELL",
        synonyms=["bell"],
        adjectives=["brass", "hot", "red", "small"],
        desc="red hot brass bell",
        flags={TRYTAKEBIT},
        action_name="HOT-BELL-F",
        ldesc="On the ground is a red hot bell.")

    obj("AXE",
        synonyms=["axe", "ax"],
        adjectives=["bloody"],
        desc="bloody axe",
        flags={WEAPONBIT, TRYTAKEBIT, TAKEBIT, NDESCBIT},
        action_name="AXE-F",
        size=25)

    obj("BOLT",
        synonyms=["bolt", "nut"],
        adjectives=["metal", "large"],
        desc="bolt",
        flags={NDESCBIT, TURNBIT, TRYTAKEBIT},
        action_name="BOLT-F")

    obj("BUBBLE",
        synonyms=["bubble"],
        adjectives=["small", "green", "plastic"],
        desc="green bubble",
        flags={NDESCBIT, TRYTAKEBIT},
        action_name="BUBBLE-F")

    obj("ALTAR",
        synonyms=["altar"],
        desc="altar",
        flags={NDESCBIT, SURFACEBIT, CONTBIT, OPENBIT},
        capacity=50)

    obj("BOOK",
        synonyms=["book", "prayer", "page", "books"],
        adjectives=["large", "black"],
        desc="black book",
        flags={READBIT, TAKEBIT, CONTBIT, BURNBIT, TURNBIT},
        action_name="BLACK-BOOK",
        fdesc="On the altar is a large black book, open to page 569.",
        size=10,
        text='Commandment #12592\n\nOh ye who go about saying unto each:  "Hello sailor":\nDost thou know the magnitude of thy sin before the gods?\nYea, verily, thou shalt be ground between two stones.\nShall the angry gods cast thy body into the whirlpool?\nSurely, thy eye shall be put out with a sharp stick!\nEven unto the ends of the earth shalt thou wander and\nUnto the land of the dead shalt thou be sent at last.\nSurely thou shalt repent of thy cunning.')

    obj("BROKEN-LAMP",
        synonyms=["lamp", "lantern"],
        adjectives=["broken"],
        desc="broken lantern",
        flags={TAKEBIT})

    obj("SCEPTRE",
        synonyms=["sceptre", "scepter", "treasure"],
        adjectives=["sharp", "egyptian", "ancient", "enameled"],
        desc="sceptre",
        flags={TAKEBIT, WEAPONBIT},
        action_name="SCEPTRE-FUNCTION",
        ldesc="An ornamented sceptre, tapering to a sharp point, is here.",
        fdesc="A sceptre, possibly that of ancient Egypt itself, is in the coffin. The\nsceptre is ornamented with colored enamel, and tapers to a sharp point.",
        size=3, value=4, tvalue=6)

    obj("TIMBERS",
        synonyms=["timbers", "pile"],
        adjectives=["wooden", "broken"],
        desc="broken timber",
        flags={TAKEBIT},
        size=50)

    obj("SLIDE",
        synonyms=["chute", "ramp", "slide"],
        adjectives=["steep", "metal", "twisting"],
        desc="chute",
        flags={CLIMBBIT},
        action_name="SLIDE-FUNCTION")

    obj("KITCHEN-TABLE",
        synonyms=["table"],
        adjectives=["kitchen"],
        desc="kitchen table",
        flags={NDESCBIT, CONTBIT, OPENBIT, SURFACEBIT},
        capacity=50)

    obj("ATTIC-TABLE",
        synonyms=["table"],
        desc="table",
        flags={NDESCBIT, CONTBIT, OPENBIT, SURFACEBIT},
        capacity=40)

    obj("SANDWICH-BAG",
        synonyms=["bag", "sack"],
        adjectives=["brown", "elongated", "smelly"],
        desc="brown sack",
        flags={TAKEBIT, CONTBIT, DOORBIT, BURNBIT},
        fdesc="On the table is an elongated brown sack, smelling of hot peppers.",
        capacity=9, size=9,
        action_name="SANDWICH-BAG-FCN")

    obj("TOOL-CHEST",
        synonyms=["chest", "chests", "group", "toolchests"],
        adjectives=["tool"],
        desc="group of tool chests",
        flags={CONTBIT, OPENBIT, TRYTAKEBIT, SACREDBIT},
        action_name="TOOL-CHEST-FCN")

    obj("YELLOW-BUTTON",
        synonyms=["button", "switch"],
        adjectives=["yellow"],
        desc="yellow button",
        flags={NDESCBIT},
        action_name="BUTTON-F")

    obj("BROWN-BUTTON",
        synonyms=["button", "switch"],
        adjectives=["brown"],
        desc="brown button",
        flags={NDESCBIT},
        action_name="BUTTON-F")

    obj("RED-BUTTON",
        synonyms=["button", "switch"],
        adjectives=["red"],
        desc="red button",
        flags={NDESCBIT},
        action_name="BUTTON-F")

    obj("BLUE-BUTTON",
        synonyms=["button", "switch"],
        adjectives=["blue"],
        desc="blue button",
        flags={NDESCBIT},
        action_name="BUTTON-F")

    obj("TROPHY-CASE",
        synonyms=["case"],
        adjectives=["trophy"],
        desc="trophy case",
        flags={TRANSBIT, CONTBIT, DOORBIT, NDESCBIT, TRYTAKEBIT, SEARCHBIT},
        action_name="TROPHY-CASE-FCN",
        capacity=10000)

    obj("RUG",
        synonyms=["rug", "carpet"],
        adjectives=["large", "oriental"],
        desc="carpet",
        flags={NDESCBIT, TRYTAKEBIT},
        action_name="RUG-FCN")

    obj("CHALICE",
        synonyms=["chalice", "cup", "silver", "treasure"],
        adjectives=["silver", "engravings"],
        desc="chalice",
        flags={TAKEBIT, TRYTAKEBIT, CONTBIT},
        action_name="CHALICE-FCN",
        ldesc="There is a silver chalice, intricately engraved, here.",
        capacity=5, size=10, value=10, tvalue=5)

    obj("GARLIC",
        synonyms=["garlic", "clove"],
        desc="clove of garlic",
        flags={TAKEBIT, FOODBIT},
        action_name="GARLIC-F",
        size=4)

    obj("TRIDENT",
        synonyms=["trident", "fork", "treasure"],
        adjectives=["poseidon", "own", "crystal"],
        desc="crystal trident",
        flags={TAKEBIT},
        fdesc="On the shore lies Poseidon's own crystal trident.",
        size=20, value=4, tvalue=11)

    obj("CYCLOPS",
        synonyms=["cyclops", "monster", "eye"],
        adjectives=["hungry", "giant"],
        desc="cyclops",
        flags={ACTORBIT, NDESCBIT, TRYTAKEBIT},
        action_name="CYCLOPS-FCN",
        strength=10000)

    obj("DAM",
        synonyms=["dam", "gate", "gates", "fcd#3"],
        desc="dam",
        flags={NDESCBIT, TRYTAKEBIT},
        action_name="DAM-FUNCTION")

    obj("TRAP-DOOR",
        synonyms=["door", "trapdoor", "trap-door", "cover"],
        adjectives=["trap", "dusty"],
        desc="trap door",
        flags={DOORBIT, NDESCBIT, INVISIBLE},
        action_name="TRAP-DOOR-FCN")

    obj("BOARDED-WINDOW",
        synonyms=["window"],
        adjectives=["boarded"],
        desc="boarded window",
        flags={NDESCBIT},
        action_name="BOARDED-WINDOW-FCN")

    obj("FRONT-DOOR",
        synonyms=["door"],
        adjectives=["front", "boarded"],
        desc="door",
        flags={DOORBIT, NDESCBIT},
        action_name="FRONT-DOOR-FCN")

    obj("BARROW-DOOR",
        synonyms=["door"],
        adjectives=["huge", "stone"],
        desc="stone door",
        flags={DOORBIT, NDESCBIT, OPENBIT},
        action_name="BARROW-DOOR-FCN")

    obj("BARROW",
        synonyms=["barrow", "tomb"],
        adjectives=["massive", "stone"],
        desc="stone barrow",
        flags={NDESCBIT},
        action_name="BARROW-FCN")

    obj("BOTTLE",
        synonyms=["bottle", "container"],
        adjectives=["clear", "glass"],
        desc="glass bottle",
        flags={TAKEBIT, TRANSBIT, CONTBIT},
        action_name="BOTTLE-FUNCTION",
        fdesc="A bottle is sitting on the table.",
        capacity=4)

    obj("CRACK",
        synonyms=["crack"],
        adjectives=["narrow"],
        desc="crack",
        flags={NDESCBIT},
        action_name="CRACK-FCN")

    obj("COFFIN",
        synonyms=["coffin", "casket", "treasure"],
        adjectives=["solid", "gold"],
        desc="gold coffin",
        flags={TAKEBIT, CONTBIT, DOORBIT, SACREDBIT, SEARCHBIT},
        ldesc="The solid-gold coffin used for the burial of Ramses II is here.",
        capacity=35, size=55, value=10, tvalue=15)

    obj("GRATE",
        synonyms=["grate", "grating"],
        desc="grating",
        flags={DOORBIT, NDESCBIT, INVISIBLE},
        action_name="GRATE-FUNCTION")

    obj("PUMP",
        synonyms=["pump", "air-pump", "tool", "tools"],
        adjectives=["small", "hand-held"],
        desc="hand-held air pump",
        flags={TAKEBIT, TOOLBIT})

    obj("DIAMOND",
        synonyms=["diamond", "treasure"],
        adjectives=["huge", "enormous"],
        desc="huge diamond",
        flags={TAKEBIT},
        ldesc="There is an enormous diamond (perfectly cut) here.",
        value=10, tvalue=10)

    obj("JADE",
        synonyms=["figurine", "treasure"],
        adjectives=["exquisite", "jade"],
        desc="jade figurine",
        flags={TAKEBIT},
        ldesc="There is an exquisite jade figurine here.",
        size=10, value=5, tvalue=5)

    obj("KNIFE",
        synonyms=["knives", "knife", "blade"],
        adjectives=["nasty", "unrusty"],
        desc="nasty knife",
        flags={TAKEBIT, WEAPONBIT, TRYTAKEBIT},
        fdesc="On a table is a nasty-looking knife.",
        action_name="KNIFE-F")

    obj("BONES",
        synonyms=["bones", "skeleton", "body"],
        desc="skeleton",
        flags={TRYTAKEBIT, NDESCBIT},
        action_name="SKELETON")

    obj("BURNED-OUT-LANTERN",
        synonyms=["lantern", "lamp"],
        adjectives=["rusty", "burned", "dead", "useless"],
        desc="burned-out lantern",
        flags={TAKEBIT},
        fdesc="The deceased adventurer's useless lantern is here.",
        size=20)

    obj("BAG-OF-COINS",
        synonyms=["bag", "coins", "treasure"],
        adjectives=["old", "leather"],
        desc="leather bag of coins",
        flags={TAKEBIT},
        ldesc="An old leather bag, bulging with coins, is here.",
        action_name="BAG-OF-COINS-F",
        size=15, value=10, tvalue=5)

    obj("LAMP",
        synonyms=["lamp", "lantern", "light"],
        adjectives=["brass"],
        desc="brass lantern",
        flags={TAKEBIT, LIGHTBIT},
        action_name="LANTERN",
        fdesc="A battery-powered brass lantern is on the trophy case.",
        ldesc="There is a brass lantern (battery-powered) here.",
        size=15)

    obj("EMERALD",
        synonyms=["emerald", "treasure"],
        adjectives=["large"],
        desc="large emerald",
        flags={TAKEBIT},
        value=5, tvalue=10)

    obj("ADVERTISEMENT",
        synonyms=["advertisement", "leaflet", "booklet", "mail"],
        adjectives=["small"],
        desc="leaflet",
        flags={READBIT, TAKEBIT, BURNBIT},
        ldesc="A small leaflet is on the ground.",
        text='"WELCOME TO ZORK!\n\nZORK is a game of adventure, danger, and low cunning. In it you\nwill explore some of the most amazing territory ever seen by mortals.\nNo computer should be without one!"',
        size=2)

    obj("LEAK",
        synonyms=["leak", "drip", "pipe"],
        desc="leak",
        flags={NDESCBIT, INVISIBLE},
        action_name="LEAK-FUNCTION")

    obj("MACHINE",
        synonyms=["machine", "pdp10", "dryer", "lid"],
        desc="machine",
        flags={CONTBIT, DOORBIT, NDESCBIT, TRYTAKEBIT},
        action_name="MACHINE-F",
        capacity=50)

    obj("INFLATED-BOAT",
        synonyms=["boat", "raft"],
        adjectives=["inflat", "magic", "plastic", "seaworthy"],
        desc="magic boat",
        flags={TAKEBIT, BURNBIT, VEHBIT, OPENBIT, SEARCHBIT},
        action_name="RBOAT-FUNCTION",
        capacity=100, size=20)

    obj("MAILBOX",
        synonyms=["mailbox", "box"],
        adjectives=["small"],
        desc="small mailbox",
        flags={CONTBIT, DOORBIT, TRYTAKEBIT},
        capacity=10,
        action_name="MAILBOX-F")

    obj("MATCH",
        synonyms=["match", "matches", "matchbook"],
        adjectives=["match"],
        desc="matchbook",
        flags={READBIT, TAKEBIT, LIGHTBIT},
        action_name="MATCH-FUNCTION",
        ldesc='There is a matchbook whose cover says "Visit Beautiful FCD#3" here.',
        size=2,
        text="\n(Close cover before striking)\n\nYOU too can make BIG MONEY in the exciting field of PAPER SHUFFLING!")

    obj("MIRROR-2",
        synonyms=["reflection", "mirror", "enormous"],
        desc="mirror",
        flags={TRYTAKEBIT, NDESCBIT},
        action_name="MIRROR-MIRROR")

    obj("MIRROR-1",
        synonyms=["reflection", "mirror", "enormous"],
        desc="mirror",
        flags={TRYTAKEBIT, NDESCBIT},
        action_name="MIRROR-MIRROR")

    obj("PAINTING",
        synonyms=["painting", "art", "canvas", "treasure"],
        adjectives=["beauti"],
        desc="painting",
        flags={TAKEBIT, BURNBIT},
        action_name="PAINTING-FCN",
        fdesc="Fortunately, there is still one chance for you to be a vandal, for on\nthe far wall is a painting of unparalleled beauty.",
        ldesc="A painting by a neglected genius is here.",
        size=15, value=4, tvalue=6)

    obj("CANDLES",
        synonyms=["candles", "pair"],
        adjectives=["burning"],
        desc="pair of candles",
        flags={TAKEBIT, FLAMEBIT, ONBIT, LIGHTBIT},
        action_name="CANDLES-FCN",
        fdesc="On the two ends of the altar are burning candles.",
        size=10)

    obj("GUNK",
        synonyms=["gunk", "piece", "slag"],
        adjectives=["small", "vitreous"],
        desc="small piece of vitreous slag",
        flags={TAKEBIT, TRYTAKEBIT},
        action_name="GUNK-FUNCTION",
        size=10)

    obj("BODIES",
        synonyms=["bodies", "body", "remains", "pile"],
        adjectives=["mangled"],
        desc="pile of bodies",
        flags={NDESCBIT, TRYTAKEBIT},
        action_name="BODY-FUNCTION")

    obj("LEAVES",
        synonyms=["leaves", "leaf", "pile"],
        desc="pile of leaves",
        flags={TAKEBIT, BURNBIT, TRYTAKEBIT},
        action_name="LEAF-PILE",
        ldesc="On the ground is a pile of leaves.",
        size=25)

    obj("PUNCTURED-BOAT",
        synonyms=["boat", "pile", "plastic"],
        adjectives=["plastic", "puncture", "large"],
        desc="punctured boat",
        flags={TAKEBIT, BURNBIT},
        action_name="DBOAT-FUNCTION",
        size=20)

    obj("INFLATABLE-BOAT",
        synonyms=["boat", "pile", "plastic", "valve"],
        adjectives=["plastic", "inflat"],
        desc="pile of plastic",
        flags={TAKEBIT, BURNBIT},
        action_name="IBOAT-FUNCTION",
        ldesc="There is a folded pile of plastic here which has a small valve\nattached.",
        size=20)

    obj("BAR",
        synonyms=["bar", "platinum", "treasure"],
        adjectives=["platinum", "large"],
        desc="platinum bar",
        flags={TAKEBIT, SACREDBIT},
        ldesc="On the ground is a large platinum bar.",
        size=20, value=10, tvalue=5)

    obj("POT-OF-GOLD",
        synonyms=["pot", "gold", "treasure"],
        adjectives=["gold"],
        desc="pot of gold",
        flags={TAKEBIT, INVISIBLE},
        fdesc="At the end of the rainbow is a pot of gold.",
        size=15, value=10, tvalue=10)

    obj("PRAYER",
        synonyms=["prayer", "inscription"],
        adjectives=["ancient", "old"],
        desc="prayer",
        flags={READBIT, SACREDBIT, NDESCBIT},
        text="The prayer is inscribed in an ancient script, rarely used today. It seems\nto be a philippic against small insects, absent-mindedness, and the picking\nup and dropping of small objects. The final verse consigns trespassers to\nthe land of the dead. All evidence indicates that the beliefs of the ancient\nZorkers were obscure.")

    obj("RAILING",
        synonyms=["railing", "rail"],
        adjectives=["wooden"],
        desc="wooden railing",
        flags={NDESCBIT})

    obj("RAINBOW",
        synonyms=["rainbow"],
        desc="rainbow",
        flags={NDESCBIT, CLIMBBIT},
        action_name="RAINBOW-FCN")

    obj("RIVER",
        synonyms=["river"],
        adjectives=["frigid"],
        desc="river",
        action_name="RIVER-FUNCTION",
        flags={NDESCBIT})

    obj("BUOY",
        synonyms=["buoy"],
        adjectives=["red"],
        desc="red buoy",
        flags={TAKEBIT, CONTBIT, DOORBIT},
        fdesc="There is a red buoy here (probably a warning).",
        capacity=20, size=10,
        action_name="TREASURE-INSIDE")

    obj("ROPE",
        synonyms=["rope", "hemp", "coil"],
        adjectives=["large"],
        desc="rope",
        flags={TAKEBIT, SACREDBIT, TRYTAKEBIT},
        action_name="ROPE-FUNCTION",
        fdesc="A large coil of rope is lying in the corner.",
        size=10)

    obj("RUSTY-KNIFE",
        synonyms=["knives", "knife"],
        adjectives=["rusty"],
        desc="rusty knife",
        flags={TAKEBIT, TRYTAKEBIT, WEAPONBIT, TOOLBIT},
        action_name="RUSTY-KNIFE-FCN",
        fdesc="Beside the skeleton is a rusty knife.",
        size=20)

    obj("SAND",
        synonyms=["sand"],
        desc="sand",
        flags={NDESCBIT},
        action_name="SAND-FUNCTION")

    obj("BRACELET",
        synonyms=["bracelet", "jewel", "sapphire", "treasure"],
        adjectives=["sapphire"],
        desc="sapphire-encrusted bracelet",
        flags={TAKEBIT},
        size=10, value=5, tvalue=5)

    obj("SCREWDRIVER",
        synonyms=["screwdriver", "tool", "tools", "driver"],
        adjectives=["screw"],
        desc="screwdriver",
        flags={TAKEBIT, TOOLBIT})

    obj("KEYS",
        synonyms=["key"],
        adjectives=["skeleton"],
        desc="skeleton key",
        flags={TAKEBIT, TOOLBIT},
        size=10)

    obj("SHOVEL",
        synonyms=["shovel", "tool", "tools"],
        desc="shovel",
        flags={TAKEBIT, TOOLBIT},
        size=15)

    obj("COAL",
        synonyms=["coal", "pile", "heap"],
        adjectives=["small"],
        desc="small pile of coal",
        flags={TAKEBIT, BURNBIT},
        size=20)

    obj("LADDER",
        synonyms=["ladder"],
        adjectives=["wooden", "rickety", "narrow"],
        desc="wooden ladder",
        flags={NDESCBIT, CLIMBBIT})

    obj("SCARAB",
        synonyms=["scarab", "bug", "beetle", "treasure"],
        adjectives=["beauti", "carved", "jeweled"],
        desc="beautiful jeweled scarab",
        flags={TAKEBIT, INVISIBLE},
        size=8, value=5, tvalue=5)

    obj("LARGE-BAG",
        synonyms=["bag"],
        adjectives=["large", "thiefs"],
        desc="large bag",
        action_name="LARGE-BAG-F",
        flags={TRYTAKEBIT, NDESCBIT})

    obj("STILETTO",
        synonyms=["stiletto"],
        adjectives=["vicious"],
        desc="stiletto",
        action_name="STILETTO-FUNCTION",
        flags={WEAPONBIT, TRYTAKEBIT, TAKEBIT, NDESCBIT},
        size=10)

    obj("MACHINE-SWITCH",
        synonyms=["switch"],
        desc="switch",
        flags={NDESCBIT, TURNBIT},
        action_name="MSWITCH-FUNCTION")

    obj("WOODEN-DOOR",
        synonyms=["door", "lettering", "writing"],
        adjectives=["wooden", "gothic", "strange", "west"],
        desc="wooden door",
        flags={READBIT, DOORBIT, NDESCBIT, TRANSBIT},
        action_name="FRONT-DOOR-FCN",
        text='The engravings translate to "This space intentionally left blank."')

    obj("SWORD",
        synonyms=["sword", "orcrist", "glamdring", "blade"],
        adjectives=["elvish", "old", "antique"],
        desc="sword",
        flags={TAKEBIT, WEAPONBIT, TRYTAKEBIT},
        action_name="SWORD-FCN",
        fdesc="Above the trophy case hangs an elvish sword of great antiquity.",
        size=30, tvalue=0)

    obj("MAP",
        synonyms=["parchment", "map"],
        adjectives=["antique", "old", "ancient"],
        desc="ancient map",
        flags={INVISIBLE, READBIT, TAKEBIT},
        fdesc="In the trophy case is an ancient parchment which appears to be a map.",
        size=2,
        text="The map shows a forest with three clearings. The largest clearing contains\na house. Three paths leave the large clearing. One of these paths, leading\nsouthwest, is marked \"To Stone Barrow\".")

    obj("BOAT-LABEL",
        synonyms=["label", "fineprint", "print"],
        adjectives=["tan", "fine"],
        desc="tan label",
        flags={READBIT, TAKEBIT, BURNBIT},
        size=2,
        text="  !!!!FROBOZZ MAGIC BOAT COMPANY!!!!\n\nHello, Sailor!\n\nInstructions for use:\n\n   To get into a body of water, say \"Launch\".\n   To get to shore, say \"Land\" or the direction in which you want\nto maneuver the boat.")

    obj("THIEF",
        synonyms=["thief", "robber", "man", "person"],
        adjectives=["shady", "suspicious", "seedy"],
        desc="thief",
        flags={ACTORBIT, INVISIBLE, CONTBIT, OPENBIT, TRYTAKEBIT},
        action_name="ROBBER-FUNCTION",
        ldesc="There is a suspicious-looking individual, holding a large bag, leaning\nagainst one wall. He is armed with a deadly stiletto.",
        strength=5)

    obj("PEDESTAL",
        synonyms=["pedestal"],
        adjectives=["white", "marble"],
        desc="pedestal",
        flags={NDESCBIT, CONTBIT, OPENBIT, SURFACEBIT},
        action_name="DUMB-CONTAINER",
        capacity=30)

    obj("TORCH",
        synonyms=["torch", "ivory", "treasure"],
        adjectives=["flaming", "ivory"],
        desc="torch",
        flags={TAKEBIT, FLAMEBIT, ONBIT, LIGHTBIT},
        action_name="TORCH-OBJECT",
        fdesc="Sitting on the pedestal is a flaming torch, made of ivory.",
        size=20, value=14, tvalue=6)

    obj("GUIDE",
        synonyms=["guide", "book", "books", "guidebooks"],
        adjectives=["tour", "guide"],
        desc="tour guidebook",
        flags={READBIT, TAKEBIT, BURNBIT},
        fdesc='Some guidebooks entitled "Flood Control Dam #3" are on the reception\ndesk.',
        text='"    Flood Control Dam #3\n\nFCD#3 was constructed in year 783 of the Great Underground Empire to\nharness the mighty Frigid River."')

    obj("TROLL",
        synonyms=["troll"],
        adjectives=["nasty"],
        desc="troll",
        flags={ACTORBIT, OPENBIT, TRYTAKEBIT},
        action_name="TROLL-FCN",
        ldesc="A nasty-looking troll, brandishing a bloody axe, blocks all passages\nout of the room.",
        strength=2)

    obj("TRUNK",
        synonyms=["trunk", "chest", "jewels", "treasure"],
        adjectives=["old"],
        desc="trunk of jewels",
        flags={TAKEBIT, INVISIBLE},
        fdesc="Lying half buried in the mud is an old trunk, bulging with jewels.",
        ldesc="There is an old trunk here, bulging with assorted jewels.",
        action_name="TRUNK-F",
        size=35, value=15, tvalue=5)

    obj("TUBE",
        synonyms=["tube", "tooth", "paste"],
        desc="tube",
        flags={TAKEBIT, CONTBIT, READBIT},
        action_name="TUBE-FUNCTION",
        ldesc="There is an object which looks like a tube of toothpaste here.",
        capacity=7, size=5,
        text="---> Frobozz Magic Gunk Company <---\n      All-Purpose Gunk")

    obj("PUTTY",
        synonyms=["material", "gunk"],
        adjectives=["viscous"],
        desc="viscous material",
        flags={TAKEBIT, TOOLBIT},
        size=6,
        action_name="PUTTY-FCN")

    obj("ENGRAVINGS",
        synonyms=["wall", "engravings", "inscription"],
        adjectives=["old", "ancient"],
        desc="wall with engravings",
        flags={READBIT, SACREDBIT},
        ldesc="There are old engravings on the walls here.",
        text="The engravings were incised in the living rock of the cave wall by\nan unknown hand. They depict, in symbolic form, the beliefs of the\nancient Zorkers. Skillfully interwoven with the bas reliefs are excerpts\nillustrating the major religious tenets of that time. Unfortunately, a\nlater age seems to have considered them blasphemous and just as skillfully\nexcised them.")

    obj("OWNERS-MANUAL",
        synonyms=["manual", "piece", "paper"],
        adjectives=["zork", "owners", "small"],
        desc="ZORK owner's manual",
        flags={READBIT, TAKEBIT},
        fdesc="Loosely attached to a wall is a small piece of paper.",
        text="Congratulations!\n\nYou are the privileged owner of ZORK I: The Great Underground Empire,\na self-contained and self-maintaining universe.")

    obj("CLIMBABLE-CLIFF",
        synonyms=["wall", "cliff", "walls", "ledge"],
        adjectives=["rocky", "sheer"],
        desc="cliff",
        action_name="CLIFF-OBJECT",
        flags={NDESCBIT, CLIMBBIT})

    obj("WHITE-CLIFF",
        synonyms=["cliff", "cliffs"],
        adjectives=["white"],
        desc="white cliffs",
        flags={NDESCBIT, CLIMBBIT},
        action_name="WCLIF-OBJECT")

    obj("WRENCH",
        synonyms=["wrench", "tool", "tools"],
        desc="wrench",
        flags={TAKEBIT, TOOLBIT},
        size=10)

    obj("CONTROL-PANEL",
        synonyms=["panel"],
        adjectives=["control"],
        desc="control panel",
        flags={NDESCBIT})

    obj("NEST",
        synonyms=["nest"],
        adjectives=["birds"],
        desc="bird's nest",
        flags={TAKEBIT, BURNBIT, CONTBIT, OPENBIT, SEARCHBIT},
        fdesc="Beside you on the branch is a small bird's nest.",
        capacity=20)

    obj("EGG",
        synonyms=["egg", "treasure"],
        adjectives=["birds", "encrusted", "jeweled"],
        desc="jewel-encrusted egg",
        flags={TAKEBIT, CONTBIT, DOORBIT, SEARCHBIT},
        action_name="EGG-OBJECT",
        value=5, tvalue=5, capacity=6,
        fdesc="In the bird's nest is a large egg encrusted with precious jewels,\napparently scavenged by a childless songbird. The egg is covered with\nfine gold inlay, and ornamented in lapis lazuli and mother-of-pearl.\nUnlike most eggs, this one is hinged and closed with a delicate looking\nclasp. The egg appears extremely fragile.")

    obj("BROKEN-EGG",
        synonyms=["egg", "treasure"],
        adjectives=["broken", "birds", "encrusted", "jewel"],
        desc="broken jewel-encrusted egg",
        flags={TAKEBIT, CONTBIT, OPENBIT},
        capacity=6, tvalue=2,
        ldesc="There is a somewhat ruined egg here.")

    obj("BAUBLE",
        synonyms=["bauble", "treasure"],
        adjectives=["brass", "beauti"],
        desc="beautiful brass bauble",
        flags={TAKEBIT},
        value=1, tvalue=1)

    obj("CANARY",
        synonyms=["canary", "treasure"],
        adjectives=["clockwork", "gold", "golden"],
        desc="golden clockwork canary",
        flags={TAKEBIT, SEARCHBIT},
        action_name="CANARY-OBJECT",
        value=6, tvalue=4,
        fdesc="There is a golden clockwork canary nestled in the egg. It has ruby\neyes and a silver beak. Through a crystal window below its left\nwing you can see intricate machinery inside. It appears to have\nwound down.")

    obj("BROKEN-CANARY",
        synonyms=["canary", "treasure"],
        adjectives=["broken", "clockwork", "gold", "golden"],
        desc="broken clockwork canary",
        flags={TAKEBIT},
        action_name="CANARY-OBJECT",
        tvalue=1,
        fdesc="There is a golden clockwork canary nestled in the egg. It seems to\nhave recently had a bad experience.")
