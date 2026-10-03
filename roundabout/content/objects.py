"""
Item and object definitions for Roundabout: The God-Forsaken Ring.
Sourced from AWT_story_line/items.md and locations.md.
Built incrementally — objects added as walkthrough sections require them.
"""

from __future__ import annotations
from engine.world import GameObject, TAKEBIT, CONTBIT, OPENBIT, NDESCBIT, SACREDBIT, ACTORBIT, BURNBIT


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
        flags={TAKEBIT},
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
        fdesc="A weathered man sits hunched over a map.",
        ldesc="Kevry — old sea captain, muttering over charts.",
        synonyms=["kevry", "captain", "man"],
        adjectives=["weathered", "old"],
        flags={ACTORBIT},
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
