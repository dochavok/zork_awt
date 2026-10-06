"""
Item weights (items.md — each item's **Weight:**; mechanics.md — Weight System).

The weights are read from items.md itself, so a wrong weight in the code fails
here even when no puzzle happens to weigh that item. Each items.md heading is
matched to its game object(s) below; a new weighted heading fails until it is
added.
Run with: pytest roundabout/test_item_weights.py  (from c:\\zork_awt)
"""

import os
import re
import sys
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world

_ITEMS_MD = os.path.join(os.path.dirname(__file__), "..", "AWT_story_line", "items.md")

# items.md heading -> the object(s) it describes
OBJECTS = {
    "The Bow": ["BOW"],
    "The God-Forsaken Ring *(Core Quest Item)*": ["RING"],
    "Enchanted Glasses / Actually Enchanted Glasses": ["ENCHANTED-GLASSES"],
    "Dragon-Nip": ["DRAGON-NIP"],
    "Heart Necklace": ["HEART-NECKLACE"],
    "Dagger": ["DAGGER"],
    "Mace": ["MACE"],
    "Battle Axe": ["BATTLE-AXE"],
    "Crowbar": ["CROWBAR"],
    "Guardian's Lantern": ["GUARDIANS-LANTERN"],
    "Torch": ["TORCH"],
    "Apprentice's Gloves": ["APPRENTICE-GLOVES"],
    "Bartender's Boots": ["BARTENDERS-BOOTS"],
    "Cellar Key": ["CELLAR-KEY"],
    "Treasure Map": ["TREASURE-MAP"],
    "Runed Metal": ["RUNED-METAL"],
    "The Pale Blade": ["PALE-BLADE"],
    "Werewolf's Amulet": ["WEREWOLFS-AMULET"],
    "The Crystal Bowl": ["CRYSTAL-BOWL"],
    "Silver Stake": ["SILVER-STAKE"],
    "Consecrated Silver Stake": ["SILVER-STAKE"],       # the same object, blessed
    "Holy Water": ["HOLY-WATER"],
    "Keeper's Key Ring": ["KEY-RING"],
    "Middle Tier Key": ["MIDDLE-TIER-KEY"],
    "Town Charter": ["TOWN-CHARTER"],
    "Vial of Glacier Melt": ["GLACIER-MELT"],
    "Ivory Torch": ["IVORY-TORCH"],
    "Unbind Undead Scroll": ["SCROLL-UNBIND-UNDEAD"],
    "Light Spell Scroll": ["SCROLL-LIGHT"],
    "Incantation Scroll": ["INCANTATION-SCROLL"],
    "Fireball Scroll": ["FIREBALL-SCROLL"],
    "Rope": ["ROPE"],
    "Shovel": ["SHOVEL"],
    "Wax Seal": ["WAX-SEAL"],
    "Silver Dust": ["SILVER-DUST"],
    "Bone Flute": ["BONE-FLUTE"],
    "Rubbing": ["RUBBING"],
    "Diamond Brooch": ["DIAMOND-BROOCH"],
    "Music Box Key": ["MUSIC-BOX-KEY"],
    "Pie Rat Disguise": ["PIE-RAT-DISGUISE"],
    "Pie Rat Coin": ["PIE-RAT-COIN"],
    "Pocket Watch": ["POCKET-WATCH"],
    "Gold Pocket Watch": ["GOLD-WATCH"],
    "Hand Cart": ["HAND-CART"],
    "Gravestone (Calder Finch)": ["GRAVESTONE"],
    "Thin Paper": ["THIN-PAPER"],
    "Charcoal": ["CHARCOAL"],
    "Smoke Jar": ["SMOKE-JAR"],
    "Sack of Salt": ["SACK-OF-SALT"],
    "Portcullis Bar": ["PORTCULLIS-BAR"],
    "Mortar Compound": ["MORTAR"],
    "Support Beam": ["SUPPORT-BEAM"],
    "Pickaxe": ["PICKAXE"],
    "Gunpowder": ["GUNPOWDER"],
    "Flint and Steel": ["FLINT-AND-STEEL"],
    "Fishing Rod": ["FISHING-ROD"],
    "Ship-in-a-Bottle": ["SHIP-IN-A-BOTTLE"],
    "Lockpicks": ["LOCKPICKS"],
    "Fire Clay": ["FIRE-CLAY"],
    "Clay Adhesive": ["CLAY-ADHESIVE"],
    "Repaired Bowl": ["REPAIRED-BOWL"],
    "Verdant Circle Shrine Bowl (3 pieces)": ["BOWL-PIECE-FOREST", "BOWL-PIECE-BOG",
                                              "BOWL-PIECE-SHRINE"],
    "Bee Queen (Glass Vial)": ["QUEEN-VIAL"],
    "Enchanted Honey": ["ENCHANTED-HONEY"],
    "Kite": ["KITE"],
    "Rune Stones (3)": ["OLD-OAK-RUNE-STONE", "BOG-RUNE-STONE", "DUNGEON-RUNE-STONE"],
    "Ivanaar's Tunic": ["IVANAAR-TUNIC"],
    "Bog Thyme": ["BOG-THYME"],
    "Small Clay Pot": ["SMALL-CLAY-POT"],
    "Tip Journal": ["TIP-JOURNAL"],
}


# items.md — Treasure Items (Trophy Case) table: | **Item** | Location | Weight | ...
TREASURES = {
    "The Forgotten Blade": "FORGOTTEN-BLADE",
    "Diamond Brooch": "DIAMOND-BROOCH",
    "Funeral Mask of Hammered Gold": "FUNERAL-MASK",
    "Golden Dragon Scale": "GOLDEN-DRAGON-SCALE",
    "Chachapoyan Fertility Idol": "IDOL",
    "Gold Pocket Watch": "GOLD-WATCH",
    "Ship-in-a-Bottle": "SHIP-IN-A-BOTTLE",
    "Gold Nugget": "GOLD-NUGGET",
    "Pie Rat Coin": "PIE-RAT-COIN",
}


def _design_weights():
    """{heading: weight} for every items.md heading with a **Weight:** line,
    and {treasure: weight} from the Treasure Items table."""
    weights, treasures, heading = {}, {}, None
    with open(_ITEMS_MD, encoding="utf-8") as fh:
        for line in fh:
            m = re.match(r"^### (.+)", line)
            if m:
                heading = m.group(1).strip()
                continue
            m = re.match(r"^\*\*Weight:\*\*\s*(\d+)", line)
            if m and heading:
                weights[heading] = int(m.group(1))
                heading = None
                continue
            m = re.match(r"^\| \*\*(.+?)\*\* \|[^|]*\|\s*(\d+)\s*\|", line)
            if m:
                treasures[m.group(1)] = int(m.group(2))
    return weights, treasures


DESIGN, DESIGN_TREASURES = _design_weights()


def test_every_weighted_item_is_matched():
    assert DESIGN, f"no weights read from {_ITEMS_MD}"
    assert sorted(set(DESIGN) - set(OBJECTS)) == []        # new items.md entries
    assert sorted(set(OBJECTS) - set(DESIGN)) == []        # renamed or removed entries


@pytest.mark.parametrize("heading", sorted(OBJECTS))
def test_weight_matches_items_md(heading):
    w, _g = _make_world()
    sizes = {name: w.objects[name].size for name in OBJECTS[heading]}
    assert sizes == {name: DESIGN[heading] for name in OBJECTS[heading]}


def test_every_treasure_row_is_matched():
    assert sorted(DESIGN_TREASURES) == sorted(TREASURES)


@pytest.mark.parametrize("treasure", sorted(TREASURES))
def test_treasure_weight_matches_items_md(treasure):
    w, _g = _make_world()
    assert w.objects[TREASURES[treasure]].size == DESIGN_TREASURES[treasure]


def test_idol_weighs_the_same_as_the_salt():
    # items.md — Sack of Salt: "looks like it weighs as much as a Chachapoyan
    # Fertility Idol" — the safe swap depends on it (traps.md — Trap 33)
    assert DESIGN_TREASURES["Chachapoyan Fertility Idol"] == DESIGN["Sack of Salt"]
