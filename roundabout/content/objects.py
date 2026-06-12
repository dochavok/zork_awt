"""
Items and NPCs for Roundabout: The God-Forsaken Ring.

All item/NPC data sourced from AWT_story_line/items.md and npcs.md.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from engine.world import (
    GameObject,
    TAKEBIT, ACTORBIT, ONBIT, INVISIBLE, NDESCBIT, CONTBIT, OPENBIT,
    WEARBIT, DRINKBIT, WEAPONBIT, BURNBIT, READBIT,
)

# FOODBIT = consumable food items (engine uses DRINKBIT for all consumables)
FOODBIT = DRINKBIT
# LIGHTBIT = light sources (engine uses BURNBIT; we track active state in globals)
LIGHTBIT = BURNBIT

if TYPE_CHECKING:
    from engine.world import World


# ---------------------------------------------------------------------------
# Flags not defined in engine (we define local constants here)
# ---------------------------------------------------------------------------

# These flags are tracked in world.globals rather than engine flags for
# Roundabout-specific slot/state management.
RINGBIT  = frozenset({"ringbit"})   # ring slot equip
NECKBIT  = frozenset({"neckbit"})   # neck slot
HEADBIT  = frozenset({"headbit"})   # head slot
CHESTBIT = frozenset({"chestbit"})  # chest slot
LEGSBIT  = frozenset({"legsbit"})   # legs slot (boots = legs slot per design)
HANDSBIT = frozenset({"handsbit"})  # hands slot


def make_objects(world: "World") -> None:
    """Register all items and NPCs. Called by initialize_world()."""
    _make_opening_objects(world)
    _make_equipment(world)
    _make_quest_items(world)
    _make_treasure_items(world)
    _make_consumables(world)
    _make_npcs(world)


def _place(world: "World", obj: "GameObject", loc: str | None) -> None:
    """Register obj and move it to loc room if loc is given."""
    world.register_object(obj)
    if loc:
        room = world.rooms.get(loc)
        if room is not None:
            world.move_object(obj, room)


# ---------------------------------------------------------------------------
# Opening area objects
# ---------------------------------------------------------------------------

def _make_opening_objects(world: "World") -> None:
    # Mailbox in the field (white-house)
    _place(world, GameObject(
        name="mailbox",
        synonyms=frozenset({"mailbox", "mail box", "box", "post box"}),
        desc="a mailbox",
        ldesc="A plain metal mailbox. It has a small flag, currently down.",
        flags=set({CONTBIT, OPENBIT}),
        value=0,
        size=0,
    ), "white-house")

    # Painting in Will's tower
    _place(world, GameObject(
        name="painting",
        synonyms=frozenset({"painting", "picture", "picture of tavern", "portrait",
                            "painting of tavern", "tale and ale painting"}),
        desc="a painting of the Tale and Ale",
        ldesc=(
            "A painting of the Tale and Ale tavern, seen from outside -- "
            "warm light through the windows, a painted sign reading TALE AND ALE. "
            "It hangs slightly crooked. Will has never straightened it."
        ),
        flags=set({NDESCBIT}),  # Not auto-listed in room contents
        value=0,
        size=0,
    ), "wills-tower-main")


# ---------------------------------------------------------------------------
# Equipment
# ---------------------------------------------------------------------------

def _make_equipment(world: "World") -> None:
    # The God-Forsaken Ring
    _place(world, GameObject(
        name="ring",
        synonyms=frozenset({"ring", "god-forsaken ring", "the ring", "cursed ring"}),
        desc="The God-Forsaken Ring",
        ldesc=(
            "A plain band of dark metal, unremarkable in every respect. "
            "You would not look twice at it on a market table. "
            "You also cannot stop looking at it now that you're holding it."
        ),
        flags=set({TAKEBIT, WEARBIT}),
        value=0,
        size=1,
    ), "pyronicus-forge")

    # Enchanted Glasses (regular)
    _place(world, GameObject(
        name="glasses",
        synonyms=frozenset({"glasses", "spectacles", "wire-rimmed glasses", "enchanted glasses"}),
        desc="wire-rimmed glasses",
        ldesc=(
            "Wire-rimmed glasses, plain and unassuming. "
            "There is something slightly off about how the room looks through them."
        ),
        flags=set({TAKEBIT, WEARBIT}),
        value=0,
        size=1,
    ), "wills-bedroom")

    # Actually Enchanted Glasses (upgraded form — starts out of world; created by Kevry)
    _place(world, GameObject(
        name="enchanted-glasses",
        synonyms=frozenset({"enchanted glasses", "actually enchanted glasses",
                            "glowing glasses", "glasses"}),
        desc="slightly glowing wire-rimmed glasses",
        ldesc=(
            "Wire-rimmed glasses, now with a faint luminescence that isn't quite a glow — "
            "more like the way a room looks right before you understand something. "
            "They feel lighter than before, and more certain."
        ),
        flags=set({TAKEBIT, WEARBIT}),
        value=0,
        size=1,
    ), None)

    # Heart Necklace
    _place(world, GameObject(
        name="heart-necklace",
        synonyms=frozenset({"necklace", "heart necklace", "clay charm", "cord"}),
        desc="a heart necklace",
        ldesc=(
            "A simple cord with a clay charm worn smooth at the edges. "
            "Someone has carried this for a long time."
        ),
        flags=set({TAKEBIT, WEARBIT}),
        value=0,
        size=1,
    ), None)

    # Ivanaar's Tunic
    _place(world, GameObject(
        name="ivaanars-tunic",
        synonyms=frozenset({"tunic", "ivanaar's tunic", "brotherhood tunic",
                            "runed tunic", "woven tunic"}),
        desc="Ivanaar's tunic",
        ldesc=(
            "Brotherhood weave, old but not worn. The runes along the hem and collar "
            "glow faintly — restored by Ivanaar's hands. "
            "Whatever is woven into this fabric, it is not entirely decorative."
        ),
        flags=set({TAKEBIT, WEARBIT}),
        value=0,
        size=1,
    ), None)

    # The Bow
    _place(world, GameObject(
        name="bow",
        synonyms=frozenset({"bow", "shortbow", "longbow", "ranged weapon"}),
        desc="a bow",
        ldesc=(
            "A bow, plain and well-maintained, strung tight and balanced. "
            "It has the feeling of something that expects to be used correctly."
        ),
        flags=set({TAKEBIT, WEAPONBIT}),
        value=0,
        size=1,
    ), None)

    # Dagger
    _place(world, GameObject(
        name="dagger",
        synonyms=frozenset({"dagger", "short blade", "knife"}),
        desc="a dagger (+2)",
        ldesc="A short blade, plain-handled and well-balanced. Nothing fancy about it.",
        flags=set({TAKEBIT, WEAPONBIT}),
        value=0,
        size=1,
    ), "tale-and-ale-kitchen")

    # Mace
    _place(world, GameObject(
        name="mace",
        synonyms=frozenset({"mace", "flanged mace", "iron mace"}),
        desc="a mace (+4)",
        ldesc=(
            "A heavy flanged mace, solid iron head, leather-wrapped grip. "
            "It has the look of something that settles arguments."
        ),
        flags=set({TAKEBIT, WEAPONBIT}),
        value=0,
        size=2,
    ), "tale-and-ale-kitchen")

    # Battle Axe
    _place(world, GameObject(
        name="battle-axe",
        synonyms=frozenset({"battle axe", "battleaxe", "axe", "broad axe"}),
        desc="a battle axe (+6)",
        ldesc=(
            "A broad-headed battle axe, balanced for a two-handed swing. "
            "Shamus keeps it behind the counter. It is not subtle."
        ),
        flags=set({TAKEBIT, WEAPONBIT}),
        value=0,
        size=3,
    ), "tale-and-ale-kitchen")

    # Crowbar
    _place(world, GameObject(
        name="crowbar",
        synonyms=frozenset({"crowbar", "bar", "iron bar", "pry bar"}),
        desc="a crowbar",
        ldesc="A heavy iron crowbar, well-balanced and clearly well-used.",
        flags=set({TAKEBIT, WEAPONBIT}),
        value=0,
        size=3,
    ), "prayer-alcove")

    # Guardian's Lantern
    _place(world, GameObject(
        name="lantern",
        synonyms=frozenset({"lantern", "guardian's lantern", "lamp", "special lantern"}),
        desc="the Guardian's Lantern",
        ldesc=(
            "A plain iron lantern, functional and unadorned. The wick is fresh. "
            "It flickers in open air but does not go out. "
            "Something about it feels patient — like it has been waiting to be useful."
        ),
        flags=set({TAKEBIT, LIGHTBIT}),
        value=0,
        size=2,
    ), None)

    # Torch
    _place(world, GameObject(
        name="torch",
        synonyms=frozenset({"torch", "brand", "burning torch"}),
        desc="a torch",
        ldesc="A torch, lit and burning. Handle it carefully in tight spaces.",
        flags=set({TAKEBIT, LIGHTBIT}),
        value=0,
        size=2,
    ), None)

    # Bartender's Boots
    _place(world, GameObject(
        name="boots",
        synonyms=frozenset({"boots", "bartender's boots", "leather boots"}),
        desc="bartender's boots",
        ldesc=(
            "Heavy leather boots, worn in a way that suggests they've done real work. "
            "There's something comforting about the way they grip the ground."
        ),
        flags=set({TAKEBIT, WEARBIT}),
        value=0,
        size=1,
    ), None)

    # Apprentice's Gloves
    _place(world, GameObject(
        name="gloves",
        synonyms=frozenset({"gloves", "apprentice's gloves", "leather gloves"}),
        desc="apprentice's gloves",
        ldesc=(
            "Supple leather gloves, well-fitted. They're broken in exactly right — "
            "they've done this before."
        ),
        flags=set({TAKEBIT, WEARBIT}),
        value=0,
        size=1,
    ), None)


# ---------------------------------------------------------------------------
# Quest Items
# ---------------------------------------------------------------------------

def _make_quest_items(world: "World") -> None:
    # Treasure Map
    _place(world, GameObject(
        name="treasure-map",
        synonyms=frozenset({"treasure map", "map", "old map", "chart"}),
        desc="a treasure map",
        ldesc=(
            "An old map on heavy paper, salt-stained at the edges. "
            "An X is marked on a small island well east of Roundabout's coast. "
            "The notation is Kevry's hand, recognizably cramped and precise."
        ),
        flags=set({TAKEBIT, READBIT}),
        value=0,
        size=1,
    ), None)

    # Runed Metal
    _place(world, GameObject(
        name="runed-metal",
        synonyms=frozenset({"runed metal", "metal", "brotherhood metal", "rune metal"}),
        desc="runed metal",
        ldesc=(
            "Dense, rune-carved, warm to the touch even in open air. "
            "Brotherhood metal, kept since before the encampment. "
            "It does not look like it wants to stay solid forever."
        ),
        flags=set({TAKEBIT}),
        value=0,
        size=3,
    ), None)

    # The Pale Blade
    _place(world, GameObject(
        name="pale-blade",
        synonyms=frozenset({"pale blade", "the pale blade", "blade", "pale sword"}),
        desc="the Pale Blade",
        ldesc=(
            "A blade of unusual metal — pale, almost white, the edge caught in light "
            "in a way that suggests it remembers being something else. "
            "Whatever Pyronicus put into the forging, this is not merely a sword."
        ),
        flags=set({TAKEBIT, WEAPONBIT}),
        value=0,
        size=3,
    ), None)

    # Werewolf's Amulet
    _place(world, GameObject(
        name="werewolf-amulet",
        synonyms=frozenset({"werewolf's amulet", "amulet", "seven-pointed star", "veil amulet"}),
        desc="the Werewolf's Amulet",
        ldesc=(
            "A tarnished amulet bearing the seven-pointed star of The Veil of the Arcane. "
            "Still warm from the werewolf's body."
        ),
        flags=set({TAKEBIT}),
        value=0,
        size=1,
    ), None)

    # The Crystal Bowl
    _place(world, GameObject(
        name="crystal-bowl",
        synonyms=frozenset({"crystal bowl", "bowl", "verdant circle bowl", "clear bowl"}),
        desc="the Crystal Bowl",
        ldesc=(
            "A crystal bowl, clear as still water. A continuous line is etched into the rim "
            "— looping back on itself, no beginning, no end. "
            "It has the feeling of something that has been waiting a long time to be this."
        ),
        flags=set({TAKEBIT}),
        value=0,
        size=2,
    ), None)

    # Silver Stake
    _place(world, GameObject(
        name="silver-stake",
        synonyms=frozenset({"silver stake", "stake", "stake of silver"}),
        desc="a silver stake",
        ldesc=(
            "A stake of solid silver — not decorative, not flimsy. "
            "A note folded beside it bore the Keeper's emerald wax seal. "
            "Someone put this here knowing it would be needed."
        ),
        flags=set({TAKEBIT, WEAPONBIT}),
        value=0,
        size=2,
    ), None)

    # Consecrated Silver Stake
    _place(world, GameObject(
        name="consecrated-stake",
        synonyms=frozenset({"consecrated silver stake", "consecrated stake",
                            "holy stake", "silver stake"}),
        desc="a consecrated silver stake",
        ldesc=(
            "The silver stake has been anointed with holy water. "
            "The metal has a faint sheen to it now that wasn't there before."
        ),
        flags=set({TAKEBIT, WEAPONBIT}),
        value=0,
        size=2,
    ), None)

    # Holy Water
    _place(world, GameObject(
        name="holy-water",
        synonyms=frozenset({"holy water", "vial of holy water", "vial", "water"}),
        desc="a vial of holy water",
        ldesc=(
            "A small glass vial, stoppered tight. The liquid inside is clear. "
            "Whatever makes it holy isn't visible from outside."
        ),
        flags=set({TAKEBIT, DRINKBIT}),
        value=0,
        size=1,
    ), "keepers-chamber")

    # Keeper's Key Ring
    _place(world, GameObject(
        name="keepers-keys",
        synonyms=frozenset({"key ring", "keys", "keeper's keys", "iron keys", "ring of keys"}),
        desc="a ring of keys",
        ldesc=(
            "A ring of keys, old iron, worn smooth from years of use. "
            "They are cold and heavier than they look."
        ),
        flags=set({TAKEBIT}),
        value=0,
        size=1,
    ), "lower-crypt")

    # Middle Tier Key
    _place(world, GameObject(
        name="mid-tier-key",
        synonyms=frozenset({"middle tier key", "mid-tier key", "dungeon key", "key"}),
        desc="the Middle Tier Key",
        ldesc=(
            "A heavy iron key, notched in an unusual pattern. "
            "Someone had it made to open a specific door. "
            "It has been waiting for someone to use it properly."
        ),
        flags=set({TAKEBIT}),
        value=0,
        size=1,
    ), None)

    # Town Charter
    _place(world, GameObject(
        name="town-charter",
        synonyms=frozenset({"town charter", "charter", "document", "official charter"}),
        desc="the Town Charter",
        ldesc=(
            "A formal document bearing the seal of Roundabout. "
            "The text establishes civic rights and obligations in the kind of language "
            "designed to sound permanent."
        ),
        flags=set({TAKEBIT, READBIT}),
        value=0,
        size=1,
    ), None)

    # Vial of Glacier Melt
    _place(world, GameObject(
        name="glacier-melt",
        synonyms=frozenset({"vial of glacier melt", "glacier melt", "cold vial", "vial"}),
        desc="a vial of glacier melt",
        ldesc=(
            "A small sealed vial of water so cold it hurts to hold. "
            "The label, if there was one, is long gone. "
            "Whatever this was collected from was very old and very cold."
        ),
        flags=set({TAKEBIT, DRINKBIT}),
        value=0,
        size=1,
    ), "prayer-alcove")

    # Ivory Torch
    _place(world, GameObject(
        name="ivory-torch",
        synonyms=frozenset({"ivory torch", "white torch", "pale torch", "mounted torch"}),
        desc="an ivory torch",
        ldesc=(
            "A torch mounted in an iron bracket, the handle wrapped in ivory cloth. "
            "It burns with unusual steadiness. The warmth it throws is specific — "
            "more focused than a regular torch."
        ),
        flags=set({TAKEBIT, LIGHTBIT}),
        value=0,
        size=2,
    ), "the-still-den")

    # Unbind Undead Scroll
    _place(world, GameObject(
        name="unbind-scroll",
        synonyms=frozenset({"unbind undead scroll", "scroll", "spell scroll",
                            "cast unbind undead", "unbind scroll"}),
        desc="an Unbind Undead scroll",
        ldesc=(
            "A scroll on parchment yellowed with age, the text in precise careful ink. "
            "The words don't quite resolve into meaning the first time you read them. "
            "The second time, they do."
        ),
        flags=set({TAKEBIT, READBIT}),
        value=0,
        size=1,
    ), "lighthouse")

    # Light Spell Scroll
    _place(world, GameObject(
        name="light-scroll",
        synonyms=frozenset({"light spell scroll", "light scroll", "scroll", "spell scroll"}),
        desc="a Light spell scroll",
        ldesc=(
            "A tightly rolled scroll, sealed with plain wax. "
            "The ink inside describes something that makes no sense until it does."
        ),
        flags=set({TAKEBIT, READBIT}),
        value=0,
        size=1,
    ), None)

    # Incantation Scroll
    _place(world, GameObject(
        name="incantation-scroll",
        synonyms=frozenset({"incantation scroll", "scroll", "archivist's scroll",
                            "quest 34 scroll", "old scroll"}),
        desc="an incantation scroll",
        ldesc=(
            "A scroll on heavy paper, the text a sequence of syllables that reads aloud "
            "better than silently. The archivist couldn't place it. You suspect you know where it belongs."
        ),
        flags=set({TAKEBIT, READBIT}),
        value=0,
        size=1,
    ), None)

    # Fireball Scroll
    _place(world, GameObject(
        name="fireball-scroll",
        synonyms=frozenset({"fireball scroll", "scroll", "fire scroll", "spell scroll"}),
        desc="a Fireball scroll",
        ldesc=(
            "A scroll in a protective iron tube, the text brief and unambiguous. "
            "It smells faintly of sulfur. Pyronicus's handwriting, if you recognized it."
        ),
        flags=set({TAKEBIT, READBIT}),
        value=0,
        size=1,
    ), None)

    # Rope
    _place(world, GameObject(
        name="rope",
        synonyms=frozenset({"rope", "coil of rope", "coil", "climbing rope"}),
        desc="a coil of rope",
        ldesc=(
            "A coil of good rope — heavy, not fraying at the ends, the kind meant for "
            "real work rather than show. Long enough to be useful."
        ),
        flags=set({TAKEBIT}),
        value=0,
        size=3,
    ), "the-docks")

    # Shovel
    _place(world, GameObject(
        name="shovel",
        synonyms=frozenset({"shovel", "spade", "digging shovel"}),
        desc="a shovel",
        ldesc=(
            "A sturdy shovel, slightly salt-pitted. It has clearly spent time at sea."
        ),
        flags=set({TAKEBIT, WEAPONBIT}),
        value=0,
        size=3,
    ), "pie-rat-ship-deck")

    # Wax Seal
    _place(world, GameObject(
        name="wax-seal",
        synonyms=frozenset({"wax seal", "seal", "signet seal", "stamp"}),
        desc="a wax seal",
        ldesc=(
            "A brass signet, the face engraved with a civic crest. "
            "It's been in the display cabinet long enough that the wax is dry. "
            "Still functional."
        ),
        flags=set({TAKEBIT}),
        value=0,
        size=1,
    ), "upper-hall")

    # Silver Dust
    _place(world, GameObject(
        name="silver-dust",
        synonyms=frozenset({"silver dust", "dust", "fine dust", "metallic dust"}),
        desc="a pouch of silver dust",
        ldesc=(
            "A small pouch of silver dust, fine as flour. "
            "Someone refined this carefully — it didn't come from a mine naturally this pure."
        ),
        flags=set({TAKEBIT, INVISIBLE}),  # hidden until perception check
        value=0,
        size=1,
    ), None)

    # Bone Flute
    _place(world, GameObject(
        name="bone-flute",
        synonyms=frozenset({"bone flute", "flute", "carved bone", "flute of bone"}),
        desc="a bone flute",
        ldesc=(
            "A flute carved from a single long bone — origin unclear, "
            "the carving too deliberate to be decorative and too old to be recent."
        ),
        flags=set({TAKEBIT}),
        value=0,
        size=1,
    ), "cave-creature-lair")

    # Music Box Key
    _place(world, GameObject(
        name="music-box-key",
        synonyms=frozenset({"music box key", "small key", "key", "box key"}),
        desc="a small key",
        ldesc=(
            "A small iron key, too small for a door lock — the scale of something "
            "meant for a box or a chest."
        ),
        flags=set({TAKEBIT, INVISIBLE}),
        value=0,
        size=1,
    ), None)

    # Pie Rat Disguise
    _place(world, GameObject(
        name="disguise",
        synonyms=frozenset({"disguise", "pie rat disguise", "costume",
                            "pirate costume", "rat costume"}),
        desc="a Pie Rat disguise",
        ldesc=(
            "A collection of ratty garments and accessories that, assembled correctly, "
            "would pass for a Pie Rat crew member at a distance. "
            "It smells like the mine."
        ),
        flags=set({TAKEBIT, WEARBIT}),
        value=0,
        size=1,
    ), "mine-rats-nest")

    # Town Charter  (already created above — this is a reminder the pocket watch triggers it)

    # Pocket Watch (Ghost's Room drop)
    _place(world, GameObject(
        name="pocket-watch",
        synonyms=frozenset({"pocket watch", "watch", "gold watch", "silver watch"}),
        desc="a pocket watch",
        ldesc=(
            "A pocket watch, stopped. The case is engraved but the engraving has been "
            "worn smooth by a long time of being held. It clicks faintly when you tilt it."
        ),
        flags=set({TAKEBIT}),
        value=0,
        size=1,
    ), None)

    # Gold Pocket Watch (Crevice — Trophy Item — different object)
    _place(world, GameObject(
        name="gold-pocket-watch",
        synonyms=frozenset({"gold pocket watch", "gold watch", "pocket watch"}),
        desc="a gold pocket watch",
        ldesc=(
            "A handsome gold pocket watch, in surprisingly good condition. "
            "It hangs from a single chain. "
            "The kind of object that someone chose to carry, not wear."
        ),
        flags=set({TAKEBIT}),
        value=30,
        size=1,
    ), "the-crevice")

    # Hand Cart
    _place(world, GameObject(
        name="hand-cart",
        synonyms=frozenset({"hand cart", "cart", "trolley", "flat cart"}),
        desc="a hand cart",
        ldesc=(
            "A flat wooden cart on iron wheels, the kind used for moving things too heavy "
            "to carry. One wheel sticks slightly. It will do."
        ),
        flags=set({TAKEBIT}),
        value=0,
        size=5,
    ), "storage-area")

    # Gravestone (Calder Finch)
    _place(world, GameObject(
        name="gravestone",
        synonyms=frozenset({"gravestone", "calder finch gravestone", "headstone", "stone"}),
        desc="Calder Finch's gravestone",
        ldesc=(
            "A heavy marble headstone, face-down in the mud. "
            "The carved surface reads: CALDER FINCH — EXPLORER. ROUNDABOUT'S OWN. "
            "Someone moved this deliberately."
        ),
        flags=set({TAKEBIT, INVISIBLE}),
        value=0,
        size=10,
    ), None)

    # Thin Paper
    _place(world, GameObject(
        name="thin-paper",
        synonyms=frozenset({"thin paper", "paper", "sheet of paper"}),
        desc="a sheet of thin paper",
        ldesc="A sheet of thin, flexible paper — good for taking impressions.",
        flags=set({TAKEBIT}),
        value=0,
        size=1,
    ), None)

    # Charcoal
    _place(world, GameObject(
        name="charcoal",
        synonyms=frozenset({"charcoal", "stick of charcoal", "drawing charcoal"}),
        desc="a stick of charcoal",
        ldesc="A stick of drawing charcoal, not crumbling, usable.",
        flags=set({TAKEBIT}),
        value=0,
        size=1,
    ), "mine-passage")

    # Smoke Jar
    _place(world, GameObject(
        name="smoke-jar",
        synonyms=frozenset({"smoke jar", "jar", "sealed jar", "clay jar"}),
        desc="a smoke jar",
        ldesc=(
            "A sealed clay jar, surprisingly heavy. Something shifts inside it when you "
            "tip it. A faint grey haze drifts from the seam where lid meets base."
        ),
        flags=set({TAKEBIT}),
        value=0,
        size=2,
    ), "supply-room")

    # Sack of Salt
    _place(world, GameObject(
        name="sack-of-salt",
        synonyms=frozenset({"sack of salt", "salt", "salt sack", "bag of salt"}),
        desc="a sack of salt",
        ldesc=(
            "A cloth sack, knotted at the top. Heavy — about the weight of something "
            "that would make a good counterweight for an idol on a pressure pedestal."
        ),
        flags=set({TAKEBIT}),
        value=0,
        size=4,
    ), "supply-room")

    # Portcullis Bar
    _place(world, GameObject(
        name="portcullis-bar",
        synonyms=frozenset({"portcullis bar", "iron bar", "prop", "bar", "support bar"}),
        desc="an iron bar",
        ldesc=(
            "A heavy iron bar, about the right length to serve as a prop. "
            "It looks purpose-made, though for what isn't immediately obvious."
        ),
        flags=set({TAKEBIT}),
        value=0,
        size=3,
    ), "supply-room")

    # Mortar Compound
    _place(world, GameObject(
        name="mortar",
        synonyms=frozenset({"mortar compound", "mortar", "stone compound", "sealant", "compound"}),
        desc="a bucket of mortar compound",
        ldesc=(
            "A small wooden bucket of grey compound, still workable. "
            "The kind of thing someone left here thinking they'd come back for it."
        ),
        flags=set({TAKEBIT}),
        value=0,
        size=2,
    ), "supply-room")

    # Support Beam
    _place(world, GameObject(
        name="support-beam",
        synonyms=frozenset({"support beam", "beam", "timber", "wooden beam"}),
        desc="a support beam",
        ldesc="A heavy timber support beam, solid and dense. It will hold anything you need it to hold.",
        flags=set({TAKEBIT}),
        value=0,
        size=4,
    ), "storage-area")

    # Pickaxe
    _place(world, GameObject(
        name="pickaxe",
        synonyms=frozenset({"pickaxe", "pick", "mining pick", "axe"}),
        desc="a pickaxe",
        ldesc=(
            "A mine pickaxe, the head solid iron, the handle worn smooth. "
            "It leans against the wall like it knows it's still needed."
        ),
        flags=set({TAKEBIT, WEAPONBIT}),
        value=0,
        size=3,
    ), "mine-main-shaft")

    # Gunpowder
    _place(world, GameObject(
        name="gunpowder",
        synonyms=frozenset({"gunpowder", "powder", "explosive", "black powder"}),
        desc="a pouch of gunpowder",
        ldesc=(
            "A cloth pouch, tightly sealed. You can feel the fine grain of the powder "
            "through the cloth. Treat it accordingly."
        ),
        flags=set({TAKEBIT}),
        value=0,
        size=2,
    ), None)

    # Flint and Steel
    _place(world, GameObject(
        name="flint-and-steel",
        synonyms=frozenset({"flint and steel", "flint", "steel", "tinderbox", "fire starter"}),
        desc="flint and steel",
        ldesc=(
            "A piece of flint and a steel striker, bundled together. "
            "Straightforward. Will start a fire if you have something to start."
        ),
        flags=set({TAKEBIT}),
        value=0,
        size=2,
    ), "mine-tunnels")

    # Fishing Rod
    _place(world, GameObject(
        name="fishing-rod",
        synonyms=frozenset({"fishing rod", "rod", "fishing pole", "pole"}),
        desc="a fishing rod",
        ldesc=(
            "A fishing rod — sturdy cane, proper line, an honest hook. "
            "It expects to be used near water."
        ),
        flags=set({TAKEBIT}),
        value=0,
        size=2,
    ), None)

    # Lockpicks
    _place(world, GameObject(
        name="lockpicks",
        synonyms=frozenset({"lockpicks", "picks", "lock picks", "thieves' tools"}),
        desc="a set of lockpicks",
        ldesc=(
            "A slim leather roll containing three picks and a tension wrench. "
            "Used. Someone knew how to use them."
        ),
        flags=set({TAKEBIT}),
        value=0,
        size=1,
    ), None)

    # Fire Clay
    _place(world, GameObject(
        name="fire-clay",
        synonyms=frozenset({"fire clay", "clay", "volcanic clay", "ceiling clay"}),
        desc="a lump of fire clay",
        ldesc=(
            "A lump of clay from the thermal vent ceiling — warm, pliable, dense. "
            "It will set hard if you mix it with water and let it cure."
        ),
        flags=set({TAKEBIT, INVISIBLE}),
        value=0,
        size=1,
    ), None)

    # Verdant Circle Shrine Bowl — Piece 1
    _place(world, GameObject(
        name="bowl-piece-1",
        synonyms=frozenset({"bowl piece", "ceramic piece", "bowl fragment", "shard"}),
        desc="a ceramic bowl fragment",
        ldesc="A curved shard of painted ceramic — part of something larger, clearly. The colors are still visible along the edge.",
        flags=set({TAKEBIT, INVISIBLE}),
        value=0,
        size=1,
    ), None)

    # Verdant Circle Shrine Bowl — Piece 2
    _place(world, GameObject(
        name="bowl-piece-2",
        synonyms=frozenset({"bowl piece", "ceramic piece", "bowl fragment", "shard"}),
        desc="a ceramic bowl fragment",
        ldesc="A curved shard of painted ceramic. The painted lines on this piece continue from something else — they want to connect.",
        flags=set({TAKEBIT, INVISIBLE}),
        value=0,
        size=1,
    ), None)

    # Verdant Circle Shrine Bowl — Piece 3
    _place(world, GameObject(
        name="bowl-piece-3",
        synonyms=frozenset({"bowl piece", "ceramic piece", "bowl fragment", "shard"}),
        desc="a ceramic bowl fragment",
        ldesc="The last piece — you can see how the three fit together before you even try.",
        flags=set({TAKEBIT, INVISIBLE}),  # perception check
        value=0,
        size=1,
    ), "shrine-room")

    # Repaired Bowl (assembled from 3 pieces + fire clay + water)
    _place(world, GameObject(
        name="repaired-bowl",
        synonyms=frozenset({"repaired bowl", "bowl", "ceramic bowl", "restored bowl"}),
        desc="a repaired ceramic bowl",
        ldesc=(
            "The three pieces fit together perfectly — the fire clay joins are almost invisible. "
            "The painted pattern on the surface is a sprouting seed inside a circle of leaves."
        ),
        flags=set({TAKEBIT}),
        value=0,
        size=1,
    ), None)

    # Bee Queen (glass vial)
    _place(world, GameObject(
        name="bee-queen",
        synonyms=frozenset({"bee queen", "queen bee", "vial", "glass vial", "bee"}),
        desc="a glass vial containing the queen bee",
        ldesc=(
            "A small glass vial with a cork, the bee inside moving with slow, deliberate purpose. "
            "She is aware of you. That is apparent."
        ),
        flags=set({TAKEBIT}),
        value=0,
        size=1,
    ), None)

    # Enchanted Honey
    _place(world, GameObject(
        name="enchanted-honey",
        synonyms=frozenset({"enchanted honey", "honey", "magical honey"}),
        desc="a jar of enchanted honey",
        ldesc=(
            "A small jar of honey — golden, thicker than ordinary honey, "
            "and faintly luminescent in the right light. It smells extraordinary."
        ),
        flags=set({TAKEBIT, FOODBIT}),
        value=0,
        size=1,
    ), None)

    # Rune Stones (3)
    _place(world, GameObject(
        name="bog-rune-stone",
        synonyms=frozenset({"rune stone", "grey stone", "bog rune stone", "rune stone 1"}),
        desc="a rune stone",
        ldesc=(
            "A grey stone, heavy for its size, one face worn flat by water. "
            "Faint lines are etched across the surface in no pattern you recognize."
        ),
        flags=set({TAKEBIT, INVISIBLE}),
        value=0,
        size=2,
    ), None)

    _place(world, GameObject(
        name="dungeon-rune-stone",
        synonyms=frozenset({"rune stone", "pale stone", "dungeon rune stone", "rune stone 2"}),
        desc="a rune stone",
        ldesc=(
            "A pale stone, roughly square, with deep natural veins of darker mineral "
            "running through it like old script."
        ),
        flags=set({TAKEBIT, INVISIBLE}),
        value=0,
        size=2,
    ), None)

    _place(world, GameObject(
        name="oak-rune-stone",
        synonyms=frozenset({"rune stone", "flat stone", "oak rune stone", "rune stone 3", "cord stone"}),
        desc="a rune stone",
        ldesc=(
            "A small flat stone, dark and smooth, threaded on a cord. "
            "Mineral veins run through it in a pattern that looks almost intentional."
        ),
        flags=set({TAKEBIT}),
        value=0,
        size=2,
    ), None)

    # Bog Thyme
    _place(world, GameObject(
        name="bog-thyme",
        synonyms=frozenset({"bog thyme", "thyme", "herb", "wild thyme"}),
        desc="a sprig of bog thyme",
        ldesc=(
            "A small herb with tiny purple flowers. It smells exactly like the bog, "
            "which means it smells complicated."
        ),
        flags=set({TAKEBIT, INVISIBLE}),
        value=0,
        size=1,
    ), None)

    # Small Clay Pot
    _place(world, GameObject(
        name="clay-pot",
        synonyms=frozenset({"clay pot", "small pot", "intact pot", "pot"}),
        desc="a small clay pot",
        ldesc=(
            "A small clay pot, somehow intact. The kind you'd keep herbs in. "
            "Everything around it is broken."
        ),
        flags=set({TAKEBIT, CONTBIT}),
        value=0,
        size=1,
    ), "supply-room")

    # Tip Journal
    _place(world, GameObject(
        name="tip-journal",
        synonyms=frozenset({"tip journal", "journal", "notebook", "tips book"}),
        desc="the Tip Journal",
        ldesc=(
            "A small leather-bound journal, Shamus's handwriting throughout. "
            "Observations about the town, the dungeon, the locals. "
            "Useful in the way things are useful when you don't know what you need yet."
        ),
        flags=set({TAKEBIT, READBIT}),
        value=0,
        size=1,
    ), None)

    # Dragon-nip (Quest 58 — hidden under nightstand in Will's Bedroom)
    _place(world, GameObject(
        name="dragon-nip",
        synonyms=frozenset({"dragon-nip", "dragon nip", "sprig", "herb", "nip"}),
        desc="a sprig of dragon-nip",
        ldesc=(
            "A dried sprig of something that smells like nothing you have smelled before — "
            "spicy, sharp, and then suddenly sweet in a way that stops making sense. "
            "It has been here for a while."
        ),
        flags=set({TAKEBIT, INVISIBLE}),
        value=0,
        size=1,
    ), None)

    # Pie Rat Coin
    _place(world, GameObject(
        name="pie-rat-coin",
        synonyms=frozenset({"pie rat coin", "pirate coin", "strange coin", "coin"}),
        desc="a Pie Rat coin",
        ldesc=(
            "An unusual coin — larger than standard Zenni, heavier, the face "
            "stamped with a rat wearing a hat and holding a slice of pie. "
            "Not legal tender in Roundabout. Probably."
        ),
        flags=set({TAKEBIT}),
        value=18,
        size=1,
    ), None)

    # Music Box (in Will's Tower — not takeable; contains Light Scroll)
    _place(world, GameObject(
        name="music-box",
        synonyms=frozenset({"music box", "box", "locked box", "small box"}),
        desc="a music box",
        ldesc=(
            "A small wooden box with a keyhole set into the lid, "
            "the surface inlaid with a simple pattern. "
            "It is locked."
        ),
        flags=set({CONTBIT}),  # not TAKEBIT — fixed in tower
        value=0,
        size=0,
    ), "wills-tower-main")


# ---------------------------------------------------------------------------
# Treasure Items (Trophy Case targets)
# ---------------------------------------------------------------------------

def _make_treasure_items(world: "World") -> None:
    # The Forgotten Blade
    _place(world, GameObject(
        name="forgotten-blade",
        synonyms=frozenset({"forgotten blade", "the forgotten blade", "ceremonial sword", "blade"}),
        desc="the Forgotten Blade",
        ldesc=(
            "A sword of ancient make — the grip wrapped in something dry and crumbling "
            "that was once leather, the guard shaped like a horizon line. "
            "The blade has not been sharpened in centuries and doesn't need to be. "
            "It is ceremonial. It is also real."
        ),
        flags=set({TAKEBIT, WEAPONBIT}),
        value=60,
        size=3,
    ), None)

    # Diamond Brooch
    _place(world, GameObject(
        name="diamond-brooch",
        synonyms=frozenset({"diamond brooch", "brooch", "diamond pin", "jeweled brooch"}),
        desc="a diamond brooch",
        ldesc=(
            "A brooch set with a single large diamond, the metalwork around it fine enough "
            "to be old money. It catches the light differently depending on angle."
        ),
        flags=set({TAKEBIT}),
        value=45,
        size=1,
    ), "magnetic-vault")

    # Funeral Mask of Hammered Gold
    _place(world, GameObject(
        name="funeral-mask",
        synonyms=frozenset({"funeral mask", "gold mask", "hammered gold mask", "mask"}),
        desc="the Funeral Mask of Hammered Gold",
        ldesc=(
            "A funeral mask in hammered gold — the features idealized, the expression "
            "composed in a way that suggests whoever wore it was not at peace with being "
            "memorialized. It is beautiful and slightly uncomfortable to hold."
        ),
        flags=set({TAKEBIT}),
        value=36,
        size=3,
    ), "burial-chamber")

    # Golden Dragon Scale
    _place(world, GameObject(
        name="dragon-scale",
        synonyms=frozenset({"golden dragon scale", "dragon scale", "scale", "gold scale"}),
        desc="a golden dragon scale",
        ldesc=(
            "A single scale, golden and dense, larger than a hand. "
            "The surface has the iridescent quality of very old metal. "
            "Will gave this to you. Draw your own conclusions."
        ),
        flags=set({TAKEBIT}),
        value=36,
        size=1,
    ), None)

    # Chachapoyan Fertility Idol
    _place(world, GameObject(
        name="idol",
        synonyms=frozenset({"idol", "fertility idol", "chachapoyan idol", "stone idol", "figurine"}),
        desc="the Chachapoyan Fertility Idol",
        ldesc=(
            "A stone figurine, palm-sized, with the solemn weight of something that has been "
            "in one place for a very long time. The pedestal it came from clearly missed it. "
            "It is currently missing the pedestal."
        ),
        flags=set({TAKEBIT}),
        value=30,
        size=4,
    ), "idol-room")

    # Ship-in-a-Bottle
    _place(world, GameObject(
        name="ship-in-a-bottle",
        synonyms=frozenset({"ship in a bottle", "ship in bottle", "bottle ship", "bottle"}),
        desc="a ship-in-a-bottle",
        ldesc=(
            "A glass bottle, sealed with wax, a fully-rigged ship inside — "
            "masts, lines, the works. Impossible to say how it got in there. "
            "No one has ever satisfactorily explained how these work."
        ),
        flags=set({TAKEBIT}),
        value=24,
        size=2,
    ), None)

    # Gold Nugget
    _place(world, GameObject(
        name="gold-nugget",
        synonyms=frozenset({"gold nugget", "nugget", "gold", "lump of gold"}),
        desc="a gold nugget",
        ldesc="A heavy irregular chunk of gold, smooth-edged from years in rubble.",
        flags=set({TAKEBIT}),
        value=21,
        size=2,
    ), "supply-cache")


# ---------------------------------------------------------------------------
# Consumables / Misc
# ---------------------------------------------------------------------------

def _make_consumables(world: "World") -> None:
    # Strongbox (dropped by Boggart on bridge)
    _place(world, GameObject(
        name="strongbox",
        synonyms=frozenset({"strongbox", "strong box", "iron box", "chest"}),
        desc="a strongbox",
        ldesc="A small iron box, heavy for its size, the lock broken open from inside.",
        flags=set({TAKEBIT, CONTBIT}),
        value=0,
        size=3,
    ), None)

    # Trophy Case (fixed in Tower; not takeable)
    _place(world, GameObject(
        name="trophy-case",
        synonyms=frozenset({"trophy case", "display case", "glass case", "case"}),
        desc="the Trophy Case",
        ldesc=(
            "A glass-fronted case of old wood, built into the stone of the Tower. "
            "The placard below reads: CALDER FINCH — EXPLORER. DONATED IN PERPETUITY "
            "FOR THE GLORY OF ROUNDABOUT. The case is empty. "
            "For now."
        ),
        flags=set({CONTBIT, OPENBIT}),  # always open / accessible
        value=0,
        size=0,
    ), "the-tower")

    # The Fountain (Town Square) — not takeable, interactable
    _place(world, GameObject(
        name="fountain",
        synonyms=frozenset({"fountain", "stone fountain", "dry fountain", "basin"}),
        desc="a stone fountain",
        ldesc=(
            "A stone fountain, the basin cracked at one edge. It is dry — "
            "the stonework has the patient look of something that has been waiting a long time "
            "to be fixed."
        ),
        flags=set(),
        value=0,
        size=0,
    ), "town-square")

    # Town Square Statue
    _place(world, GameObject(
        name="statue",
        synonyms=frozenset({"statue", "stone statue", "civic statue", "figure"}),
        desc="a stone statue",
        ldesc=(
            "A stone statue of a civic figure, the plaque below worn to illegibility. "
            "The base is solid — or appears to be. "
            "Something about the weight distribution is subtly off."
        ),
        flags=set(),
        value=0,
        size=0,
    ), "town-square")


# ---------------------------------------------------------------------------
# NPCs
# ---------------------------------------------------------------------------

def _make_npcs(world: "World") -> None:
    # Will Passion
    _place(world, GameObject(
        name="will",
        synonyms=frozenset({"will", "will passion", "wizard", "old man", "man"}),
        desc="Will Passion",
        ldesc=(
            "Will Passion sits with the unhurried stillness of a man who has seen "
            "centuries compressed into a single lifetime. "
            "His long dark robes of deep violet, trimmed in crimson cord, hang from broad "
            "weathered shoulders. His dark hair, streaked with silver, falls untamed past "
            "his shoulders. The wire-rimmed spectacles on his nose are an odd contrast "
            "to everything else about him."
        ),
        flags=set({ACTORBIT}),
        value=0,
        size=0,
    ), "wills-tower-main")

    # May
    _place(world, GameObject(
        name="may",
        synonyms=frozenset({"may", "bartender", "barkeep", "woman behind the bar"}),
        desc="May",
        ldesc=(
            "A woman behind the bar — shoulder-length red hair, "
            "late thirties, the appraisal done in about a second and apparently satisfactory. "
            "She works the bar with the efficiency of someone who has answered every question "
            "before and will answer them all again without complaint."
        ),
        flags=set({ACTORBIT}),
        value=0,
        size=0,
    ), "tale-and-ale-bar")

    # Shamus
    _place(world, GameObject(
        name="shamus",
        synonyms=frozenset({"shamus", "cook", "chef", "short man"}),
        desc="Shamus",
        ldesc=(
            "Short, wide, shaved head, untrimmed grey beard. "
            "He moves through the kitchen without wasted motion. "
            "The kind of man you'd go to if you needed something that wasn't on any official list."
        ),
        flags=set({ACTORBIT}),
        value=0,
        size=0,
    ), "tale-and-ale-kitchen")

    # Lynds
    _place(world, GameObject(
        name="lynds",
        synonyms=frozenset({"lynds", "strong man", "arm wrestler"}),
        desc="Lynds",
        ldesc=(
            "A broad man, relaxed in his chair with the ease of someone "
            "who has never seriously worried about any physical situation. "
            "His drink is in front of him. His elbow is not on the table, for once."
        ),
        flags=set({ACTORBIT}),
        value=0,
        size=0,
    ), "tale-and-ale-main")

    # Ty
    _place(world, GameObject(
        name="ty",
        synonyms=frozenset({"ty", "casino man", "dice man", "gambler"}),
        desc="Ty",
        ldesc=(
            "Ty sits at the head of the table — or what he has decided is the head — "
            "presiding over the dice with the calm of a man who has never once worried "
            "about the outcome."
        ),
        flags=set({ACTORBIT}),
        value=0,
        size=0,
    ), "tys-casino-corner")

    # Raznak
    _place(world, GameObject(
        name="raznak",
        synonyms=frozenset({"raznak", "archer", "viking archer", "ranger"}),
        desc="Raznak",
        ldesc=(
            "A Viking, lean and quiet in the way of someone who has spent a great deal of "
            "time outdoors not being noticed. He looks at you the way he'd look at an arrow "
            "with bad fletching — not hostile, just certain."
        ),
        flags=set({ACTORBIT}),
        value=0,
        size=0,
    ), "archery-range")

    # The Redcrosse Knight
    _place(world, GameObject(
        name="knight",
        synonyms=frozenset({"knight", "redcrosse knight", "red cross knight", "knight of faith"}),
        desc="the Redcrosse Knight",
        ldesc=(
            "The Knight stands at ease in the town square — armored in battered plate "
            "with a red cross on the breast, a sword at his side, watching the town "
            "go about its business. Formally warm. A teacher first."
        ),
        flags=set({ACTORBIT}),
        value=0,
        size=0,
    ), "town-square")

    # Ivanaar Stormbringer
    _place(world, GameObject(
        name="ivanaar",
        synonyms=frozenset({"ivanaar", "ivanaar stormbringer", "viking chief", "chief"}),
        desc="Ivanaar Stormbringer",
        ldesc=(
            "A broad-shouldered man with the bearing of someone who has been in charge "
            "long enough to stop thinking about it. A banner bearing four symbols in "
            "sequence hangs above his longhouse."
        ),
        flags=set({ACTORBIT}),
        value=0,
        size=0,
    ), "viking-encampment")

    # Haalvar
    _place(world, GameObject(
        name="haalvar",
        synonyms=frozenset({"haalvar", "riddle man", "stone keeper"}),
        desc="Haalvar",
        ldesc=(
            "A man with the satisfied air of someone who administers tests and takes it personally "
            "when others pass them. He stands near the Riddle Stone."
        ),
        flags=set({ACTORBIT}),
        value=0,
        size=0,
    ), "haalvar-hut")

    # Aylora
    _place(world, GameObject(
        name="aylora",
        synonyms=frozenset({"aylora", "viking woman", "drinking champion"}),
        desc="Aylora",
        ldesc=(
            "A broad, calm woman with a cup of something dark in one hand. "
            "She looks at you the way athletes look at things they are about to defeat."
        ),
        flags=set({ACTORBIT}),
        value=0,
        size=0,
    ), "fire-pit")

    # Unnamed Viking Child (Ritual Circle)
    _place(world, GameObject(
        name="ritual-child",
        synonyms=frozenset({"child", "unnamed child", "boy", "girl", "viking child"}),
        desc="an unnamed child",
        ldesc=(
            "A small child, standing to one side of the ritual circle, watching. "
            "Does not speak."
        ),
        flags=set({ACTORBIT, NDESCBIT}),  # not auto-described in room ldesc
        value=0,
        size=0,
    ), "ritual-circle")

    # Councilman Rowan Finch
    _place(world, GameObject(
        name="rowan-finch",
        synonyms=frozenset({"rowan finch", "councilman", "councilman finch", "finch"}),
        desc="Councilman Rowan Finch",
        ldesc=(
            "A man at the far end of the council table with the bearing of someone "
            "who has inherited both the title and the furniture. "
            "He looks up when you enter with the expression of someone who expects to be interrupted."
        ),
        flags=set({ACTORBIT}),
        value=0,
        size=0,
    ), "council-chamber")

    # Records Room Worker
    _place(world, GameObject(
        name="records-worker",
        synonyms=frozenset({"records worker", "clerk", "worker", "records clerk"}),
        desc="the Records Room Worker",
        ldesc=(
            "A clerk at a desk near the window, surrounded by ledgers and folded documents. "
            "He looks up when you enter with the expression of a man who was hoping you wouldn't."
        ),
        flags=set({ACTORBIT}),
        value=0,
        size=0,
    ), "records-room")

    # The Librarian
    _place(world, GameObject(
        name="librarian",
        synonyms=frozenset({"librarian", "half-elf", "kenku", "woman at desk"}),
        desc="the Librarian",
        ldesc=(
            "A woman behind the desk — emerald cuffs, the features of two different lineages "
            "held in one face, her eyes meeting yours with the attentiveness of someone "
            "who has been waiting for exactly this conversation."
        ),
        flags=set({ACTORBIT}),
        value=0,
        size=0,
    ), "library-main-hall")

    # The Archivist
    _place(world, GameObject(
        name="archivist",
        synonyms=frozenset({"archivist", "old scholar", "scholar", "ink-stained man"}),
        desc="the Archivist",
        ldesc=(
            "An older man, slight, with ink on both hands. "
            "He works at a large table buried under rolled maps, open books held flat by stones, "
            "and sheets of careful notation. He does not look up immediately."
        ),
        flags=set({ACTORBIT}),
        value=0,
        size=0,
    ), "the-stacks")

    # Pyronicus
    _place(world, GameObject(
        name="pyronicus",
        synonyms=frozenset({"pyronicus", "forge master", "smith", "man at the forge"}),
        desc="Pyronicus",
        ldesc=(
            "A man at the forge — measured, slightly aloof, economical with words. "
            "He is not surprised to see you. Will told him to expect someone."
        ),
        flags=set({ACTORBIT}),
        value=0,
        size=0,
    ), "pyronicus-forge")

    # Litlock
    _place(world, GameObject(
        name="litlock",
        synonyms=frozenset({"litlock", "jovial man", "bog man"}),
        desc="Litlock",
        ldesc=(
            "A man who fills whatever room he's in without trying to. "
            "He is near the fireplace. He looks up with the alertness of someone "
            "who was hoping for company without admitting it to himself."
        ),
        flags=set({ACTORBIT}),
        value=0,
        size=0,
    ), "dankhaus-common-room")

    # Boggart
    _place(world, GameObject(
        name="boggart",
        synonyms=frozenset({"boggart", "troll", "bridge keeper", "toll collector"}),
        desc="the Boggart",
        ldesc=(
            "A small, dense figure planted at the center of the bridge with "
            "the unmistakable air of someone who has never once been successfully argued with. "
            "He eyes you with the satisfaction of a man in an excellent position."
        ),
        flags=set({ACTORBIT}),
        value=0,
        size=0,
    ), "toll-bridge")

    # Beekeeper
    _place(world, GameObject(
        name="beekeeper",
        synonyms=frozenset({"beekeeper", "bee woman", "beekeeper woman"}),
        desc="the Beekeeper",
        ldesc=(
            "A broad woman with patience in her posture and a concerning number of "
            "sting marks on her forearms. She looks at you over the top of her hive boxes "
            "with polite interest."
        ),
        flags=set({ACTORBIT}),
        value=0,
        size=0,
    ), "beekeeper-cottage")

    # Kevry Talborn
    _place(world, GameObject(
        name="kevry",
        synonyms=frozenset({"kevry", "kevry talborn", "old sailor", "island man"}),
        desc="Kevry Talborn",
        ldesc=(
            "A weathered man, hunched over a map in the back room of a small island house. "
            "When he looks up, his face does something complicated — then widens into "
            "a genuine grin."
        ),
        flags=set({ACTORBIT}),
        value=0,
        size=0,
    ), "kevry-captains-quarters")

    # The Warden (drops Guardian's Lantern; Combat Room / Creature Den)
    _place(world, GameObject(
        name="warden",
        synonyms=frozenset({"warden", "the warden", "dungeon warden", "guardian"}),
        desc="the Warden",
        ldesc=(
            "A large figure in rusted armor, moving with the patient purpose "
            "of something that has been waiting in this dark room for a very long time."
        ),
        flags=set({ACTORBIT}),
        value=0,
        size=0,
    ), "combat-room")

    # Undead Werewolf (The Still Den, lower tier)
    _place(world, GameObject(
        name="werewolf",
        synonyms=frozenset({"werewolf", "undead werewolf", "creature", "wolf-creature"}),
        desc="the undead werewolf",
        ldesc=(
            "A werewolf — wrong. Wrong size, wrong posture, wrong silence. "
            "It moves like something working from memory. "
            "The wounds on its flanks have not healed and never will."
        ),
        flags=set({ACTORBIT}),
        value=0,
        size=0,
    ), "the-still-den")

    # Aurix the Kobold child
    _place(world, GameObject(
        name="aurix",
        synonyms=frozenset({"aurix", "kobold", "kobold child", "child"}),
        desc="Aurix",
        ldesc=(
            "A small kobold child, watching from the doorway with round, serious eyes."
        ),
        flags=set({ACTORBIT, NDESCBIT}),
        value=0,
        size=0,
    ), "dankhaus-common-room")
