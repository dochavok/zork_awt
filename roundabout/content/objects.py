"""
Item and object definitions for Roundabout: The God-Forsaken Ring.
Sourced from AWT_story_line/items.md and locations.md.
Built incrementally — objects added as walkthrough sections require them.
"""

from __future__ import annotations
from engine.world import (
    GameObject, TAKEBIT, CONTBIT, OPENBIT, NDESCBIT, SACREDBIT, ACTORBIT, BURNBIT,
    CLIMBBIT, INVISIBLE, SURFACEBIT, TRYTAKEBIT,
)


# npcs.md — Will Passion: Appearance. Shown on EXAMINE WILL.
WILL_APPEARANCE = (
    "Will Passion sits with the unhurried stillness of a man who has "
    "seen centuries compressed into a single lifetime.\n"
    "His long dark robes of deep violet — trimmed in crimson cord that "
    "winds like a binding spell — hang loosely from broad, weathered "
    "shoulders.\n"
    "His hair, dark as a raven's wing but streaked with the silver of "
    "hard-won wisdom, falls long and untamed past his shoulders.\n"
    "His beard is full and commanding, the kind that seems to grow with "
    "intent.\n"
    "Thin, almost delicate wire-rimmed spectacles rest upon his nose — "
    "an odd contrast to everything else about him, as if he borrowed "
    "them from a much more ordinary man.\n"
    "On his wrist sits a leather cuff, dark and worn.\n"
    "Around his neck, a crimson cord from which hangs... something. "
    "You can't quite make it out."
)


def make_objects(world) -> None:
    _make_opening_objects(world)
    _make_tower_objects(world)
    _make_mine_objects(world)
    _make_sea_objects(world)
    _make_npcs(world)
    _make_viking_objects(world)
    _make_town_objects(world)
    _make_scrolls(world)
    _make_old_oak_objects(world)
    _make_bog_objects(world)
    _make_alley_objects(world)
    _make_lynds_objects(world)
    _make_dankhaus_objects(world)
    _make_chuckle_objects(world)
    _make_town_hall_objects(world)
    _make_tunnel_objects(world)
    _make_upper_tier_objects(world)
    _make_combat_room_objects(world)
    _make_shrine_path_objects(world)
    _make_statue_objects(world)
    _make_cellar_objects(world)
    _make_mid_tier_objects(world)
    _set_weights(world)


# ---------------------------------------------------------------------------
# Opening area objects
# ---------------------------------------------------------------------------

def _make_opening_objects(world) -> None:
    mailbox = GameObject(
        name="MAILBOX-WHITE-HOUSE",
        desc="small mailbox",
        fdesc="There is a small mailbox here.",
        ldesc="There is a small mailbox here.",
        synonyms=["mailbox", "box"],
        adjectives=["small"],
        flags={CONTBIT, SACREDBIT},
    )
    mailbox.set_flag(NDESCBIT)   # suppressed from room listing (covered by ldesc above)
    world.register_object(mailbox)


# ---------------------------------------------------------------------------
# Tower objects
# ---------------------------------------------------------------------------

def _make_tower_objects(world) -> None:
    # Painting — teleports to Tale and Ale on EXAMINE
    painting = GameObject(
        name="PAINTING",
        desc="painting",
        fdesc=(
            "A painting hangs on the wall, slightly crooked — a tavern scene, "
            "warm light, people who look comfortable."
        ),
        ldesc="A painting of the Tale and Ale hangs on the wall, slightly crooked.",
        synonyms=["painting", "picture", "portrait"],
        flags={SACREDBIT, NDESCBIT},
    )
    world.register_object(painting)

    # Tower mailbox — teleports to Tale and Ale on OPEN; also present in tavern
    mailbox_tower = GameObject(
        name="MAILBOX-TOWER",
        desc="mailbox",
        fdesc="A mailbox sits near the door, entirely out of place.",
        ldesc="A mailbox sits near the door, entirely out of place.",
        synonyms=["mailbox", "box"],
        flags={CONTBIT, SACREDBIT, NDESCBIT},
    )
    world.register_object(mailbox_tower)

    # WEARABLE is a string flag defined in content/syntax.py
    _WEARABLE = "WEARABLE"

    # Enchanted Glasses — in bedroom, on nightstand
    glasses = GameObject(
        name="ENCHANTED-GLASSES",
        desc="wire-rimmed glasses",
        fdesc=(
            "A pair of wire-rimmed glasses sit on the nightstand. "
            "They look perfectly ordinary."
        ),
        ldesc="A pair of wire-rimmed glasses rests on the nightstand.",
        synonyms=["glasses", "spectacles", "specs"],
        adjectives=["wire-rimmed", "enchanted", "actually"],
        flags={TAKEBIT, _WEARABLE},
        value=0,
    )
    world.register_object(glasses)

    # The Ring — given to player after briefing
    ring = GameObject(
        name="RING",
        desc="plain dark ring",
        ldesc="A plain dark ring.",
        synonyms=["ring"],
        adjectives=["plain", "dark", "god-forsaken"],
        flags={TAKEBIT, "WEARABLE"},
    )
    world.register_object(ring)


# ---------------------------------------------------------------------------
# Mine objects
# ---------------------------------------------------------------------------

def _make_mine_objects(world) -> None:
    pickaxe = GameObject(
        name="PICKAXE",
        desc="pickaxe",
        fdesc="A pickaxe leans against the wall.",
        ldesc="A sturdy mining pickaxe.",
        synonyms=["pickaxe", "pick", "axe"],
        flags={TAKEBIT},
    )
    world.register_object(pickaxe)

    disguise = GameObject(
        name="PIE-RAT-DISGUISE",
        desc="Pie Rat disguise",
        fdesc="A Pie Rat disguise sits among the contraband.",
        ldesc="A convincing Pie Rat disguise — hat, coat, the works.",
        synonyms=["disguise", "costume", "hat", "coat"],
        adjectives=["pie", "rat", "pie-rat"],
        flags={TAKEBIT},
    )
    world.register_object(disguise)

    gunpowder = GameObject(
        name="GUNPOWDER",
        desc="gunpowder",
        fdesc="A paper packet of gunpowder.",
        ldesc="A paper packet of gunpowder.",
        synonyms=["gunpowder", "powder", "packet"],
        flags={TAKEBIT, BURNBIT},
    )
    world.register_object(gunpowder)

    torch = GameObject(
        name="TORCH",
        desc="torch",
        fdesc="A torch.",
        ldesc="A lit torch.",
        synonyms=["torch"],
        flags={TAKEBIT},
    )
    world.register_object(torch)

    flint = GameObject(
        name="FLINT-AND-STEEL",
        desc="flint and steel",
        fdesc="Flint and steel sit in the torch sconce.",
        ldesc="A flint and steel striker.",
        synonyms=["flint", "steel", "striker"],
        adjectives=["flint", "and"],
        flags={TAKEBIT},
    )
    world.register_object(flint)


# ---------------------------------------------------------------------------
# Sea objects
# ---------------------------------------------------------------------------

def _make_npcs(world) -> None:
    shamus = GameObject(
        name="SHAMUS",
        desc="Shamus",
        fdesc="Shamus works the kitchen with practiced efficiency.",
        ldesc="Shamus the cook, short and wide, shaved head and untrimmed grey beard.",
        synonyms=["shamus", "cook"],
        adjectives=["shamus"],
        flags={ACTORBIT},
    )
    world.register_object(shamus)

    kevry = GameObject(
        name="KEVRY",
        desc="Kevry",
        synonyms=["kevry", "captain", "man"],
        adjectives=["weathered", "old"],
        flags={ACTORBIT, NDESCBIT},   # described in the Captain's Quarters text
    )
    world.register_object(kevry)

    # Will Passion — in the tower (npcs.md: Will Passion)
    _WILL_PRESENCE = "Will Passion sits at his desk, pen in hand."
    will = GameObject(
        name="WILL",
        desc="Will Passion",
        fdesc=_WILL_PRESENCE,
        ldesc=_WILL_PRESENCE,
        synonyms=["will", "passion", "wizard"],
        adjectives=["will"],
        flags={ACTORBIT},
    )
    world.register_object(will)

    # Pyronicus — holds the ring until TALK TO (npcs.md: Pyronicus)
    _PYRONICUS_PRESENCE = (
        "Pyronicus works at the forge, unhurried, as though he has been "
        "expecting company and sees no reason to stop for it."
    )
    pyronicus = GameObject(
        name="PYRONICUS",
        desc="Pyronicus",
        fdesc=_PYRONICUS_PRESENCE,
        ldesc=_PYRONICUS_PRESENCE,
        synonyms=["pyronicus", "dragon", "smith"],
        flags={ACTORBIT},
    )
    world.register_object(pyronicus)


def _make_sea_objects(world) -> None:
    shovel = GameObject(
        name="SHOVEL",
        desc="shovel",
        fdesc="A shovel is lashed to the rail near the bow.",
        ldesc="A sturdy iron-headed shovel.",
        synonyms=["shovel", "spade"],
        flags={TAKEBIT},
    )
    world.register_object(shovel)

    rope = GameObject(
        name="ROPE",
        desc="coil of rope",
        fdesc="A coil of rope sits loose on a bollard.",
        ldesc="A coil of sturdy rope.",
        synonyms=["rope", "coil", "line"],
        adjectives=["coil", "coiled"],
        flags={TAKEBIT},
    )
    world.register_object(rope)


# ---------------------------------------------------------------------------
# Archery Range & Viking Encampment (locations.md, npcs.md)
# ---------------------------------------------------------------------------

def _make_viking_objects(world) -> None:
    def npc(name, desc, presence, synonyms, adjectives=()):
        o = GameObject(
            name=name, desc=desc, fdesc=presence, ldesc=presence,
            synonyms=list(synonyms), adjectives=list(adjectives),
            flags={ACTORBIT},
        )
        world.register_object(o)
        return o

    npc("RAZNAK", "Raznak",
        "Raznak stands at the near end of the range, watching the targets.",
        ["raznak", "viking", "archer"])
    npc("IVANAAR", "Ivanaar Stormbringer",
        "Ivanaar Stormbringer sits by the central fire, watching you with the "
        "patience of someone who expects to be impressed or disappointed, and "
        "has not decided which.",
        ["ivanaar", "stormbringer", "viking"], ["ivanaar"])
    npc("HAALVAR", "Haalvar",
        "Haalvar lounges beside the stone, looking pleased with himself.",
        ["haalvar", "viking"])
    npc("CHILD", "child",
        "A child stands at the edge of the circle, watching you without a word.",
        ["child", "kid", "boy"], ["unnamed", "silent"])
    npc("AYLORA", "Aylora",
        "Aylora sits by the fire, a cup in hand.",
        ["aylora", "champion", "viking"])

    banner = GameObject(
        name="BANNER", desc="banner",
        ldesc="Four runes are stitched along the banner, left to right: "
              "Earth, Air, Fire, Water.",
        synonyms=["banner", "flag", "pole", "runes"],
        flags={NDESCBIT, SACREDBIT},
    )
    world.register_object(banner)

    riddle_stone = GameObject(
        name="RIDDLE-STONE", desc="riddle stone",
        ldesc="The stone is carved with runes — solid to the touch, but its "
              "surface moves like dark water.",
        synonyms=["stone", "rock"], adjectives=["riddle", "runic", "carved"],
        flags={NDESCBIT, SACREDBIT},
    )
    world.register_object(riddle_stone)

    # Ritual Circle stones — order Earth, Air, Fire, Water, Heart
    for key, extra in (("EARTH", []), ("AIR", []), ("FIRE", []),
                       ("WATER", []), ("HEART", ["love", "life"])):
        stone = GameObject(
            name=f"{key}-STONE", desc=f"{key.lower()} stone",
            synonyms=["stone", "rune"],
            adjectives=[key.lower(), *extra],
            flags={NDESCBIT, SACREDBIT},
        )
        world.register_object(stone)

    world.register_object(GameObject(
        name="RUNED-METAL", desc="runed metal",
        ldesc="A length of dark metal — dense, rune-carved, warm to the touch "
              "even in the open air.",
        synonyms=["metal", "runes"], adjectives=["runed", "dark", "brotherhood"],
        flags={TAKEBIT},
    ))
    world.register_object(GameObject(
        name="PALE-BLADE", desc="Pale Blade",
        ldesc="The blade is pale, almost white, and thin in the way of "
              "something that doesn't need to be heavy to do what it does.",
        synonyms=["blade", "sword"], adjectives=["pale", "white"],
        flags={TAKEBIT},
    ))
    world.register_object(GameObject(
        name="FORGE", desc="forge",
        synonyms=["forge", "fire"], adjectives=["ancient", "enormous"],
        flags={NDESCBIT, SACREDBIT},
    ))


# ---------------------------------------------------------------------------
# Town Square
# ---------------------------------------------------------------------------

def _make_town_objects(world) -> None:
    # Hollow base: seam visible on LOOK AT STATUE (no perception check);
    # crowbar opens it (Quests 19 & 30). Text in content/verbs.py.
    world.register_object(GameObject(
        name="STATUE", desc="statue",
        synonyms=["statue", "base", "seam", "plaque", "figure"],
        adjectives=["stone", "civic", "hollow"],
        flags={NDESCBIT, SACREDBIT},
    ))


# ---------------------------------------------------------------------------
# Spell scrolls (items.md — Unbind Undead Scroll). Teaching: content/will.py
# ---------------------------------------------------------------------------

def _make_scrolls(world) -> None:
    world.register_object(GameObject(
        name="SCROLL-UNBIND-UNDEAD", desc="Unbind Undead scroll",
        fdesc="A scroll lies on the desk, weighted at one corner with a smooth stone.",
        ldesc="A spell scroll headed Unbind Undead, in a cramped, careful hand.",
        synonyms=["scroll", "spell"], adjectives=["unbind", "undead", "spell"],
        flags={TAKEBIT},
    ))


# ---------------------------------------------------------------------------
# The Old Oak area (locations.md, npcs.md, items.md). Logic: content/old_oak.py
# ---------------------------------------------------------------------------

def _make_old_oak_objects(world) -> None:
    from content.old_oak import CHILD_WAITING
    world.register_object(GameObject(
        name="OAK-CHILD", desc="child", fdesc=CHILD_WAITING, ldesc=CHILD_WAITING,
        synonyms=["child", "kid"], flags={ACTORBIT},
    ))
    world.register_object(GameObject(
        name="OAK-TREE", desc="oak", synonyms=["oak", "tree", "branches"],
        adjectives=["old", "large"], flags={CLIMBBIT, NDESCBIT, SACREDBIT},
    ))
    world.register_object(GameObject(
        name="KITE", desc="kite",
        synonyms=["kite"], flags={TAKEBIT},
    ))
    world.register_object(GameObject(
        name="OLD-OAK-RUNE-STONE", desc="rune stone",
        fdesc="A small flat stone on a cord lies in the grass.",
        ldesc="A small flat stone, dark and smooth, threaded on a cord. Mineral "
              "veins run through it in a pattern that looks almost intentional.",
        synonyms=["stone", "rune", "cord"], adjectives=["rune", "flat", "small"],
        flags={TAKEBIT},
    ))
    # Beekeeper is described in the cottage's room description
    world.register_object(GameObject(
        name="BEEKEEPER", desc="beekeeper", synonyms=["beekeeper", "woman", "keeper"],
        adjectives=["broad"], flags={ACTORBIT, NDESCBIT},
    ))
    # Forest bowl piece — hidden until an Easy perception check finds it
    world.register_object(GameObject(
        name="BOWL-PIECE-FOREST", desc="bowl piece",
        fdesc="Among the shards on the pedestal, one piece is larger than the "
              "rest — a curved section of the rim, still whole.",
        ldesc="A curved piece of ceramic from the shrine bowl, part of the rim. "
              "A faint etched line runs along its edge.",
        synonyms=["piece", "shard", "bowl"], adjectives=["bowl", "curved", "ceramic"],
        flags={TAKEBIT, INVISIBLE},
    ))


# ---------------------------------------------------------------------------
# Bog of Eternal Stench
# ---------------------------------------------------------------------------

def _make_bog_objects(world) -> None:
    # Bog-SW shrine bowl piece — hidden until an Easy perception check finds it
    world.register_object(GameObject(
        name="BOWL-PIECE-BOG", desc="bowl piece",
        fdesc="Half-sunk in the mud at the edge of the reeds, a curved shard of "
              "pale ceramic catches what light there is.",
        ldesc="A piece of the shrine bowl, caked with bog mud. Under the mud, a "
              "faint etched line.",
        synonyms=["piece", "shard", "bowl"], adjectives=["bowl", "curved", "ceramic"],
        flags={TAKEBIT, INVISIBLE},
    ))


# ---------------------------------------------------------------------------
# The Back Alley & the Bar (logic: content/back_alley.py, content/tavern.py)
# ---------------------------------------------------------------------------

def _make_alley_objects(world) -> None:
    from content.back_alley import MUGGER_PRESENCE
    # Hidden until the Medium perception check spots him
    world.register_object(GameObject(
        name="MUGGER", desc="mugger", fdesc=MUGGER_PRESENCE, ldesc=MUGGER_PRESENCE,
        synonyms=["mugger", "figure", "thief"], adjectives=["shadowy"],
        flags={ACTORBIT, INVISIBLE},
    ))
    world.register_object(GameObject(
        name="LOCKPICKS", desc="lockpicks",
        fdesc="A roll of lockpicks lies on the cobbles.",
        synonyms=["lockpicks", "picks", "roll"], adjectives=["lock"],
        flags={TAKEBIT},
    ))
    # May is described in the Bar's room description
    world.register_object(GameObject(
        name="MAY", desc="May", synonyms=["may", "bartender", "barkeep", "woman"],
        flags={ACTORBIT, NDESCBIT},
    ))


# ---------------------------------------------------------------------------
# Lynds & the Heart Necklace (logic: content/lynds.py)
# ---------------------------------------------------------------------------

def _make_lynds_objects(world) -> None:
    from content.lynds import LYNDS_PRESENCE
    world.register_object(GameObject(
        name="LYNDS", desc="Lynds", fdesc=LYNDS_PRESENCE, ldesc=LYNDS_PRESENCE,
        synonyms=["lynds"], flags={ACTORBIT},
    ))
    world.register_object(GameObject(
        name="HEART-NECKLACE", desc="heart necklace",
        ldesc="A simple cord with a clay charm, worn smooth.",
        synonyms=["necklace", "charm", "cord"], adjectives=["heart", "clay"],
        flags={TAKEBIT, "WEARABLE"},
    ))


# ---------------------------------------------------------------------------
# The Dankhaus (logic: content/dankhaus.py)
# ---------------------------------------------------------------------------

def _make_dankhaus_objects(world) -> None:
    # The yurt seen from Bog-SE — hidden until the path is found
    world.register_object(GameObject(
        name="DANKHAUS", desc="yurt", synonyms=["dankhaus", "yurt", "path", "house"],
        adjectives=["low", "round"], flags={NDESCBIT, SACREDBIT, INVISIBLE},
    ))
    # Litlock is described in the Common Room's room description
    world.register_object(GameObject(
        name="LITLOCK", desc="Litlock", synonyms=["litlock"], flags={ACTORBIT, NDESCBIT},
    ))
    presence = ("A small kobold sits cross-legged among the chalk marks, absorbed "
                "in something only they can see.")
    world.register_object(GameObject(
        name="AURIX", desc="Aurix", fdesc=presence, ldesc=presence,
        synonyms=["aurix", "kobold", "child"], adjectives=["small"], flags={ACTORBIT},
    ))


# ---------------------------------------------------------------------------
# The Chuckle House (logic: content/chuckle.py)
# ---------------------------------------------------------------------------

def _make_chuckle_objects(world) -> None:
    from content.chuckle import GHOST_PRESENCE
    world.register_object(GameObject(
        name="TICKET-BOOTH", desc="ticket booth",
        ldesc="The ticket window is cracked but intact. A small wooden sign on the "
              "ledge reads: ADMISSION. Below it, in smaller text: EVERYONE GETS IN. "
              "The booth is empty. Whoever collected the tickets isn't collecting "
              "anymore.",
        synonyms=["booth", "window", "sign"], adjectives=["ticket"],
        flags={NDESCBIT, SACREDBIT},
    ))
    world.register_object(GameObject(
        name="CHUCKLE-HOOKS", desc="hooks",
        ldesc="Empty brackets where something square once hung — the right shape "
              "for mirrors, though whatever was here is long gone. The hooks in the "
              "deeper rooms still have their tenants.",
        synonyms=["hooks", "brackets"], flags={NDESCBIT, SACREDBIT},
    ))
    # Seen only while the ring is worn — hostility is atmosphere only
    world.register_object(GameObject(
        name="GHOST", desc="ghost", fdesc=GHOST_PRESENCE, ldesc=GHOST_PRESENCE,
        synonyms=["ghost", "spirit", "figure"], adjectives=["grey"],
        flags={ACTORBIT, INVISIBLE},
    ))
    world.register_object(GameObject(
        name="POCKET-WATCH", desc="pocket watch",
        fdesc="A pocket watch lies on the floor where the ghost stood.",
        ldesc="A plain silver pocket watch, stopped. The inside of the lid is "
              "engraved, but too worn to read.",
        synonyms=["watch"], adjectives=["pocket", "silver"], flags={TAKEBIT},
    ))


# ---------------------------------------------------------------------------
# Town Hall (logic: content/town_hall.py)
# ---------------------------------------------------------------------------

def _make_town_hall_objects(world) -> None:
    # Both are described in their room descriptions
    world.register_object(GameObject(
        name="RECORDS-WORKER", desc="clerk", synonyms=["clerk", "worker"],
        adjectives=["records", "room"], flags={ACTORBIT, NDESCBIT},
    ))
    world.register_object(GameObject(
        name="ROWAN-FINCH", desc="Councilman Rowan Finch",
        synonyms=["rowan", "finch", "councilman", "man"], adjectives=["councilman"],
        flags={ACTORBIT, NDESCBIT},
    ))
    # Quest 32 (logic: content/gravestone.py). Rowan puts the key in the room
    # when he holds it out.
    world.register_object(GameObject(
        name="MIDDLE-TIER-KEY", desc="Middle Tier Key",
        ldesc="A heavy iron key, its bow worked into the shape of a finch in flight. "
              "The teeth are worn smooth at the tips.",
        synonyms=["key"], adjectives=["middle", "tier", "iron", "heavy", "calder's"],
        size=1, flags={TAKEBIT, NDESCBIT},
    ))
    from content.gravestone import LISTING_MUD
    world.register_object(GameObject(
        name="GRAVESTONE", desc="gravestone", fdesc=LISTING_MUD, ldesc=LISTING_MUD,
        synonyms=["gravestone", "stone", "headstone", "slab"],
        adjectives=["calder", "finch's"], size=10,
        flags={INVISIBLE, TAKEBIT, TRYTAKEBIT},   # TAKE refuses it (gravestone.take_stone)
    ))
    world.register_object(GameObject(
        name="GRAVE", desc="grave", synonyms=["grave", "plot"], adjectives=["empty", "calder's"],
        flags={NDESCBIT, SACREDBIT, SURFACEBIT},
    ))
    world.register_object(GameObject(
        name="TOWN-CHARTER", desc="town charter",
        ldesc="A rolled document tied with faded ribbon. The town seal is pressed "
              "into the wax at the bottom, and the handwriting is the careful kind "
              "that expects to be read for a long time.",
        synonyms=["charter", "document"], adjectives=["town", "rolled"], flags={TAKEBIT},
    ))


# ---------------------------------------------------------------------------
# Secret Tunnels (logic: content/tunnels.py)
# ---------------------------------------------------------------------------

def _make_tunnel_objects(world) -> None:
    # Both described by the Toll Bridge's stateful room description
    world.register_object(GameObject(
        name="BOGGART", desc="Boggart", synonyms=["boggart", "figure", "squatter"],
        adjectives=["small", "dense"], flags={ACTORBIT, NDESCBIT},
    ))
    world.register_object(GameObject(
        name="STRONGBOX", desc="strongbox", synonyms=["strongbox", "box", "lid"],
        adjectives=["battered"], flags={NDESCBIT, SACREDBIT, CONTBIT},
    ))


# ---------------------------------------------------------------------------
# Dungeon upper tier (logic: content/upper_tier.py). Sizes are items.md weights.
# ---------------------------------------------------------------------------

def _make_upper_tier_objects(world) -> None:
    def item(name, desc, fdesc, ldesc, synonyms, adjectives, size, flags=None):
        world.register_object(GameObject(
            name=name, desc=desc, fdesc=fdesc, ldesc=ldesc, synonyms=synonyms,
            adjectives=adjectives, size=size, flags=flags or {TAKEBIT},
        ))
    item("PORTCULLIS-BAR", "portcullis bar",
         "A heavy iron bar leans in the corner, notched at one end — the kind of "
         "thing made to hold something open.",
         "A length of iron as thick as your wrist, notched at one end. Heavy, and "
         "built to take weight.", ["bar"], ["portcullis", "iron", "heavy"], 3)
    item("MORTAR", "mortar compound",
         "A sealed tub of mortar compound sits on a low shelf.",
         "A tub of grey mortar compound, still workable under the lid. Someone "
         "meant to fix something down here.", ["mortar", "compound", "tub"], ["grey"], 2)
    item("SACK-OF-SALT", "sack of salt",
         "A fat sack of salt slumps against the shelves.",
         "It looks like it weighs as much as a Chachapoyan Fertility Idol.",
         ["sack", "salt"], [], 4)
    # The Storage Area's description mentions both; examine text only
    # Open container so the parser can reach the gravestone on it (Quest 32)
    item("HAND-CART", "hand cart", "",
         "A sturdy two-wheeled cart, the handles worn smooth. Built to carry more "
         "than a person could.", ["cart"], ["hand", "two-wheeled"], 5,
         {TAKEBIT, NDESCBIT, CONTBIT, OPENBIT})
    item("SUPPORT-BEAM", "support beam", "",
         "A heavy timber beam, squared and solid. Something meant to hold up a "
         "ceiling.", ["beam", "timber"], ["support", "heavy"], 4, {TAKEBIT, NDESCBIT})
    # Trap 33 deferred: the idol stays on its pedestal for now
    world.register_object(GameObject(
        name="IDOL", desc="figurine", synonyms=["idol", "figurine", "pedestal"],
        adjectives=["chachapoyan", "fertility", "stone"], flags={NDESCBIT, SACREDBIT},
    ))


# ---------------------------------------------------------------------------
# Combat Room & Creature Den (logic: content/combat_room.py)
# ---------------------------------------------------------------------------

def _make_combat_room_objects(world) -> None:
    from content.combat_room import WARDEN_PRESENCE
    world.register_object(GameObject(
        name="WARDEN", desc="Warden", fdesc=WARDEN_PRESENCE, ldesc=WARDEN_PRESENCE,
        synonyms=["warden", "guard", "thing"], flags={ACTORBIT},
    ))
    world.register_object(GameObject(
        name="PRESSURE-PLATE", desc="pressure plate", synonyms=["plate", "flagstone"],
        adjectives=["pressure"], flags={NDESCBIT, SACREDBIT, INVISIBLE},
    ))
    world.register_object(GameObject(
        name="GUARDIANS-LANTERN", desc="Guardian's Lantern",
        fdesc="An old lantern lies on the floor, its glass faintly green.",
        ldesc="A guard's lantern, heavy brass, the glass tinted a faint green. It "
              "flickers when you lift it, as if it wants to light and can't decide where.",
        synonyms=["lantern"], adjectives=["guardian's", "guardians", "old", "brass"],
        size=2, flags={TAKEBIT},
    ))
    world.register_object(GameObject(
        name="INSIGNIA", desc="insignia",
        ldesc="Pinned to the wall, almost lost under the grime: a faded insignia and "
              "the rags of a uniform. This was a guard post once.",
        synonyms=["insignia", "uniform", "rags"], adjectives=["faded"],
        flags={NDESCBIT, SACREDBIT},
    ))


# ---------------------------------------------------------------------------
# Prayer Alcove → Mid-Tier Key Door (logic: content/shrine_path.py)
# ---------------------------------------------------------------------------

def _make_shrine_path_objects(world) -> None:
    from content.shrine_path import SHRINE_PIECE
    world.register_object(GameObject(
        name="CROWBAR", desc="crowbar",
        fdesc="A crowbar lies in the recess, one end flattened from use.",
        ldesc="A heavy iron crowbar, one end flattened to a lip. Made for getting into things.",
        synonyms=["crowbar", "bar"], adjectives=["iron", "heavy"], size=3,
        flags={TAKEBIT, INVISIBLE},
    ))
    world.register_object(GameObject(
        name="GLACIER-MELT", desc="vial of glacier melt",
        fdesc="A small stoppered vial sits beside it, the glass frosted despite the damp.",
        ldesc="A stoppered vial of water so cold the glass has frosted. It doesn't warm in your hand.",
        synonyms=["vial", "melt"], adjectives=["glacier", "frosted", "stoppered"], size=1,
        flags={TAKEBIT, INVISIBLE},
    ))
    world.register_object(GameObject(
        name="BOWL-PIECE-SHRINE", desc="bowl piece", fdesc=SHRINE_PIECE,
        synonyms=["piece", "shard", "fragment", "bowl"], adjectives=["bowl", "curved", "stone"],
        size=1, flags={TAKEBIT, INVISIBLE},
    ))
    world.register_object(GameObject(
        name="PORTCULLIS", desc="portcullis", synonyms=["portcullis", "gate", "bars"],
        adjectives=["iron"], flags={NDESCBIT, SACREDBIT},
    ))
    world.register_object(GameObject(
        name="MID-TIER-DOOR", desc="iron door", synonyms=["door", "lock"],
        adjectives=["iron", "heavy"], flags={NDESCBIT, SACREDBIT},
    ))


# ---------------------------------------------------------------------------
# Dungeon middle tier, key side (logic: content/mid_tier.py)
# ---------------------------------------------------------------------------

def _make_mid_tier_objects(world) -> None:
    world.register_object(GameObject(
        name="MINE-CHEST", desc="iron chest", synonyms=["chest"],
        adjectives=["large", "iron", "bolted"], flags={NDESCBIT, SACREDBIT},
    ))
    # Lower tier, west end (logic: content/lower_tier.py)
    world.register_object(GameObject(
        name="KEY-RING", desc="key ring",
        fdesc="The skeleton's fingers are curled loosely around a ring of keys.",
        ldesc="A ring of keys, old iron, worn smooth from years of use.",
        synonyms=["keys", "key", "keyring"], adjectives=["iron", "old", "keeper's", "keepers"],
        size=1, flags={TAKEBIT},
    ))
    world.register_object(GameObject(
        name="SKELETON", desc="skeleton",
        ldesc="The robes have rotted at the seams, but the cord around the skeleton's "
              "neck has held. On it hangs a disc of emerald-green wax.",
        synonyms=["skeleton", "keeper", "robes", "bones"], adjectives=["robed"],
        flags={NDESCBIT, SACREDBIT},
    ))
    world.register_object(GameObject(
        name="KEEPER-SEAL", desc="emerald seal",
        ldesc="A disc of emerald-green wax on a cord — the same seal as the note in "
              "the statue's base.",
        synonyms=["seal", "wax", "cord", "disc"], adjectives=["emerald", "green", "wax"],
        flags={NDESCBIT, SACREDBIT},
    ))
    world.register_object(GameObject(
        name="PENDULUM-BLADE", desc="pendulum blade",
        ldesc="The blade hangs dead still, a curved length of iron as wide as a man. "
              "The edge is dark with old blood.",
        synonyms=["blade", "pendulum"], adjectives=["pendulum", "curved"],
        flags={NDESCBIT, SACREDBIT},
    ))
    world.register_object(GameObject(
        name="FIRE-CLAY", desc="fire clay",
        fdesc="A seam of reddish clay is pressed into the overhang above you.",
        ldesc="A lump of reddish fire clay, dense and faintly warm. It takes the print "
              "of your fingers.",
        synonyms=["clay", "seam"], adjectives=["fire", "reddish"],
        size=1, flags={TAKEBIT, INVISIBLE},
    ))
    from content.lower_tier import ceiling_action
    world.register_object(GameObject(
        name="VENT-CEILING", desc="ceiling", synonyms=["ceiling", "overhang", "roof"],
        adjectives=["low"], flags={NDESCBIT, SACREDBIT}, action=ceiling_action,
    ))
    # Keeper's Chamber (logic: content/keeper.py)
    world.register_object(GameObject(
        name="KEEPER-DOOR", desc="narrow door", synonyms=["door", "lock"],
        adjectives=["narrow", "dark", "wood", "wooden", "west"], flags={NDESCBIT, SACREDBIT},
    ))
    world.register_object(GameObject(
        name="HOLY-WATER", desc="vial of holy water",
        ldesc="A small glass vial of clear water, stoppered and sealed with a dab of green wax.",
        synonyms=["water", "vial", "liquid"], adjectives=["holy", "clear", "glass", "small"],
        size=1, flags={TAKEBIT, NDESCBIT},
    ))
    world.register_object(GameObject(
        name="KEEPER-NOTE", desc="Keeper's note",
        ldesc="A note in a careful hand, sealed at the bottom with green wax.",
        text=('"If you are reading this, I did not come back. The scholar of the Veil '
              "went down to the lower caves and did not come back as himself. What paces "
              "down there now is undead, and silver alone will not end it. The stake must "
              "be consecrated — pour the holy water on this desk over it. It is the last I "
              'blessed. I hid the stake where the town would keep it safe."'),
        synonyms=["note"], adjectives=["keeper's", "keepers", "careful"],
        flags={NDESCBIT, SACREDBIT},
    ))
    # The Still Den (logic: content/still_den.py)
    world.register_object(GameObject(
        name="BONES", desc="bones", synonyms=["bones", "floor"], adjectives=["dry"],
        flags={NDESCBIT, SACREDBIT},
    ))
    world.register_object(GameObject(
        name="WEREWOLF", desc="werewolf", synonyms=["werewolf", "creature", "wolf"],
        adjectives=["undead"], flags={ACTORBIT, NDESCBIT, SACREDBIT},
    ))
    world.register_object(GameObject(
        name="SCHOLAR", desc="scholar", synonyms=["scholar", "body"],
        flags={NDESCBIT, SACREDBIT},
    ))
    world.register_object(GameObject(
        name="WEREWOLFS-AMULET", desc="Werewolf's Amulet",
        fdesc="A tarnished amulet lies beside the scholar, a seven-pointed star on its face.",
        ldesc="A tarnished amulet bearing the seven-pointed star of The Veil of the Arcane.",
        synonyms=["amulet"], adjectives=["werewolf's", "werewolfs", "tarnished"],
        size=1, flags={TAKEBIT},
    ))
    # Collapsed Aqueduct, Quest 22 (logic: content/aqueduct.py)
    world.register_object(GameObject(
        name="AQUEDUCT-BLOCKS", desc="stone blocks",
        synonyms=["blocks", "block", "stones", "stone"], adjectives=["stone", "fallen"],
        flags={NDESCBIT, SACREDBIT},
    ))
    world.register_object(GameObject(
        name="AQUEDUCT", desc="aqueduct",
        synonyms=["aqueduct", "channel", "joints", "joint", "gap"], adjectives=["stone"],
        flags={NDESCBIT, SACREDBIT},
    ))
    # Over the edge of the hole once the Stored Room floor is dug out
    world.register_object(GameObject(
        name="SUPPORT-TIMBER", desc="support timber", synonyms=["timber", "beam"],
        adjectives=["support", "old"], flags={NDESCBIT, SACREDBIT, INVISIBLE},
    ))


# items.md weights — used by the Rickety Bridge (limit 12). Engine default is 5.
_WEIGHTS = {
    "RING": 1, "ENCHANTED-GLASSES": 1, "HEART-NECKLACE": 1, "TORCH": 2, "PICKAXE": 3,
    "PIE-RAT-DISGUISE": 1, "GUNPOWDER": 2, "FLINT-AND-STEEL": 2, "SHOVEL": 3, "ROPE": 3,
    "KITE": 1, "OLD-OAK-RUNE-STONE": 2, "SCROLL-UNBIND-UNDEAD": 1, "BOWL-PIECE-FOREST": 1,
    "BOWL-PIECE-BOG": 1, "RUNED-METAL": 3, "PALE-BLADE": 3, "TOWN-CHARTER": 1,
    "POCKET-WATCH": 1, "LOCKPICKS": 1, "GUARDIANS-LANTERN": 2, "HAND-CART": 5,
    "SUPPORT-BEAM": 4, "PORTCULLIS-BAR": 3, "MORTAR": 2, "SACK-OF-SALT": 4,
}


def _set_weights(world) -> None:
    for name, weight in _WEIGHTS.items():
        world.objects[name].size = weight


# ---------------------------------------------------------------------------
# Town Square statue contents (logic: content/statue.py)
# ---------------------------------------------------------------------------

def _make_statue_objects(world) -> None:
    world.register_object(GameObject(
        name="SILVER-STAKE", desc="silver stake",
        fdesc="A silver stake lies in the hollow of the statue's base.",
        ldesc="A slim stake of solid silver, the point still sharp. Someone hid this deliberately.",
        synonyms=["stake"], adjectives=["silver", "slim"], size=2, flags={TAKEBIT},
    ))
    world.register_object(GameObject(
        name="STATUE-NOTE", desc="folded note",
        fdesc="A folded note lies beside it, sealed with green wax.",
        ldesc="A folded note, unsigned, closed with a seal of emerald-green wax.",
        text=('"Kept here for whoever comes after me. I hope it\'s someone careful." '
              "There's no name — only the green wax seal."),
        synonyms=["note", "paper"], adjectives=["folded", "sealed"], size=1, flags={TAKEBIT},
    ))


# ---------------------------------------------------------------------------
# Quest 25 — the flooded cellar (logic: content/cellar.py)
# ---------------------------------------------------------------------------

def _make_cellar_objects(world) -> None:
    def fixed(name, desc, synonyms, adjectives, flags=None):
        world.register_object(GameObject(
            name=name, desc=desc, synonyms=synonyms, adjectives=adjectives,
            flags=flags or {NDESCBIT, SACREDBIT},
        ))
    world.register_object(GameObject(
        name="CELLAR-KEY", desc="cellar key",
        ldesc="An iron key, rust-bloomed, on a loop of string gone grey.",
        synonyms=["key"], adjectives=["cellar", "iron"], size=1, flags={TAKEBIT},
    ))
    fixed("CELLAR-DOOR", "cellar door", ["door", "trapdoor", "lock"], ["cellar"])
    # In the Kitchen (reached from the top step) until the cellar drains
    fixed("DRAIN", "drain", ["drain", "cover", "grate", "clog"], ["drain", "iron", "square"])
    fixed("TUNNEL-DOOR-CELLAR", "black oak door", ["door"], ["black", "oak", "low", "tunnel"])
    fixed("TUNNEL-DOOR-BONE", "black oak door", ["door"], ["black", "oak", "low", "tunnel"])
    world.register_object(GameObject(
        name="CASHBOX", desc="cashbox",
        fdesc="A rusted tin cashbox sits on a high shelf, above the old waterline.",
        ldesc="A rusted tin cashbox sits on a high shelf, above the old waterline.",
        synonyms=["cashbox", "box", "cache"], adjectives=["rusted", "tin", "cash"],
        flags={SACREDBIT, INVISIBLE},
    ))
    world.register_object(GameObject(
        name="BARTENDERS-BOOTS", desc="Bartender's Boots",
        ldesc="Tall leather boots, salt-stained, soft at the ankle. Someone wore these "
              "into worse than a cellar and walked back out.",
        synonyms=["boots"], adjectives=["bartender's", "bartenders", "leather", "tall"],
        size=1, flags={TAKEBIT, "WEARABLE"},
    ))
