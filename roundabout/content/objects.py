"""
Item and object definitions for Roundabout: The God-Forsaken Ring.
Sourced from AWT_story_line/items.md and locations.md.
Built incrementally — objects added as walkthrough sections require them.
"""

from __future__ import annotations
from engine.world import GameObject, TAKEBIT, CONTBIT, OPENBIT, NDESCBIT, SACREDBIT, ACTORBIT, BURNBIT


def make_objects(world) -> None:
    _make_opening_objects(world)
    _make_tower_objects(world)
    _make_mine_objects(world)
    _make_sea_objects(world)
    _make_npcs(world)


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
        ldesc="A pair of wire-rimmed glasses sit on the nightstand.",
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
        fdesc="A plain dark ring sits on the desk.",
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
