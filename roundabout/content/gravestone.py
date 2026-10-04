"""
Quest 32 — The Missing Gravestone (Middle Tier Key).

Design: quests.md (Quest 32), npcs.md (Councilman Rowan Finch), items.md
(Hand Cart, Gravestone, Middle Tier Key), locations.md (Bog-SE, Graveyard).
- Discovery: reaching the Rickety Bridge (shrine_path.py).
- Bog-SE: Easy perception every visit until the gravestone is found.
- LOAD STONE ONTO CART puts the stone in the hand cart. A loaded cart goes
  anywhere on the level but not UP or DOWN.
- UNLOAD STONE at the Graveyard sets the stone back and leaves the cart
  there; anywhere else it tips the stone onto the ground.
- Rowan: first interaction / Trophy Case line until the quest is discovered,
  then start → in progress → reward (quest completes, key held out) → after.

State: ROWAN-MET, ROWAN-QUEST-STARTED, GRAVESTONE-FOUND, GRAVESTONE-RETURNED,
       CART-ROLLED
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from engine.world import World, Room

_SPOTTED = (
    "Half-sunk in the mud at the water's edge, a slab of dressed stone lies "
    "face-down — too square to be anything the bog made. Someone dumped it here."
)
LISTING_MUD = "A gravestone lies face-down in the mud."
_LISTING_GROUND = "A gravestone lies face-down on the ground."
EXAMINE_STONE = "You tip up one edge far enough to read it: CALDER FINCH — EXPLORER."
_TAKE_STONE = "It doesn't budge. Whatever carried this out here didn't carry it by hand."
_NO_CART = "You'll need something to put it on."
_LOADED = (
    "You tip the gravestone up out of the mud and walk it, corner by corner, "
    "onto the cart. The axle complains. The bog lets go of the stone with a "
    "sound you'd rather not have heard. The gravestone is loaded."
)
_ROLLING = "The cart takes some getting started. Once it's rolling, it wants to keep going."
_NO_STAIRS = "Not with that on it."
_EXAMINE_LOADED = "The cart sits low on its axle under Calder Finch's gravestone."
_PLACED = (
    "You wheel the cart to the empty plot — a rectangle of disturbed earth with "
    "a broken stub of mortar at its head — and tip the gravestone back into "
    "place. It settles as if it remembers the spot. You leave the cart beside "
    "it; it's done its job."
)
_TIPPED_OFF = "You tip the gravestone off the cart. It lands face-down, which seems to be its preference."
_GRAVEYARD_STONE = (
    "One headstone near the path stands straighter than the others, newly "
    "scrubbed of mud: CALDER FINCH — EXPLORER."
)
_GRAVEYARD_CART = "An empty hand cart stands beside it."

_ROWAN_FIRST = (
    "He looks up from his papers with the expression of someone who has been "
    "interrupted before and expects to be interrupted again. \"Can I help you?\" "
    "It is not entirely a question."
)
_ROWAN_TROPHY = (
    "\"My grandfather built this town as much as anyone. He explored the "
    "passages beneath it too — donated whatever he found to the Trophy Case "
    "upstairs. It's been empty for years. I don't know what that says about "
    "the state of adventure in Roundabout.\""
)
_ROWAN_START = (
    "Rowan looks up from his papers, then looks again — at your boots, and the "
    "tunnel dust on them. \"You've been under the town.\" It isn't a question. "
    "\"So did my grandfather. Calder Finch. Half the passages down there are in "
    "his notebooks.\"\n"
    "He sets the pen down. \"Someone stole his gravestone out of the cemetery. "
    "Pried it up and carried it off, and nobody saw a thing. The town has other "
    "priorities.\" A pause. \"You go places other people don't. If you find it, "
    "bring it home. I'd consider it a personal favor.\""
)
_ROWAN_WAITING = (
    "\"Any word on the gravestone?\" Rowan asks, before you can say anything. He "
    "reads the answer on your face and goes back to his papers."
)
_ROWAN_REWARD = (
    "\"I went out to the cemetery this morning,\" Rowan says. \"Grandfather's "
    "stone is back where it belongs.\" Then, flatly: \"That cart you left by the "
    "grave came from the dungeon. Don't bother denying it — I've seen it before, "
    "in my grandfather's papers.\" He studies you for a moment. \"He left a key. "
    "Said it led to a lower level — wouldn't say what was down there.\" He holds "
    "it out. \"Take it. It was never meant for me.\""
)
_ROWAN_AFTER = (
    "\"Grandfather's stone is standing straight for the first time in a year,\" "
    "Rowan says. \"I went and looked. Twice.\" He goes back to his papers."
)

_BOG_ROOMS = ("BOG-SE", "BOG-NE", "BOG-SW", "BOG-NW")


def _stone(w: World):
    return w.objects["GRAVESTONE"]


def _cart(w: World):
    return w.objects["HAND-CART"]


def cart_loaded(w: World) -> bool:
    return _stone(w).location is _cart(w)


# ---------------------------------------------------------------------------
# Bog-SE perception (called from dankhaus.bog_se_action)
# ---------------------------------------------------------------------------

def bog_se_enter(w: World) -> None:
    if w.get_global("GRAVESTONE-FOUND") or _stone(w).location is not w.rooms["BOG-SE"]:
        return
    from content.player import check_perception
    from content.perception import EASY
    if check_perception(w, EASY):
        w.set_global("GRAVESTONE-FOUND", "pending")


def bog_se_end(w: World) -> None:
    """The stone is revealed after the room description, with the find line."""
    if w.get_global("GRAVESTONE-FOUND") == "pending":
        w.set_global("GRAVESTONE-FOUND", True)
        _stone(w).clear_flag("INVISIBLE")
        print(_SPOTTED)


# ---------------------------------------------------------------------------
# Verbs
# ---------------------------------------------------------------------------

def take_stone(w: World) -> None:
    if w.get_global("GRAVESTONE-RETURNED"):
        print("The gravestone is fixed in place.")   # engine's standard SACREDBIT line
    else:
        print(_TAKE_STONE)


def examine(w: World, obj) -> bool:
    """Examine text for the stone and the loaded cart. True if handled."""
    if obj.name == "GRAVESTONE":
        print(EXAMINE_STONE)
        return True
    if obj.name == "HAND-CART" and cart_loaded(w):
        print(_EXAMINE_LOADED)
        return True
    return False


def load(w: World) -> None:
    stone, cart = _stone(w), _cart(w)
    if stone.location is cart:
        print("It's already on the cart.")
        return
    if stone.location is not w.here:
        print("There's nothing here to load.")
        return
    if cart not in w.player.contents and cart.location is not w.here:
        print(_NO_CART)
        return
    if cart.location is w.here:
        w.move_object(cart, w.player)   # you take the handles to push it
    print(_LOADED)
    w.move_object(stone, cart)
    w.set_global("CART-ROLLED", False)


def unload(w: World) -> None:
    stone, cart = _stone(w), _cart(w)
    if not cart_loaded(w):
        print("There's nothing on the cart.")
        return
    here = w.here
    if here.name == "GRAVEYARD":
        print(_PLACED)
        w.move_object(stone, here)
        stone.set_flag("NDESCBIT")      # described by the Graveyard line
        stone.set_flag("SACREDBIT")
        w.move_object(cart, here)
        w.set_global("GRAVESTONE-RETURNED", True)
        return
    print(_TIPPED_OFF)
    stone.ldesc = LISTING_MUD if here.name in _BOG_ROOMS else _LISTING_GROUND
    stone.touched = True
    w.move_object(stone, here)


def drop_cart(w: World) -> bool:
    """DROP CART while loaded: at the Graveyard it unloads. True if handled."""
    if cart_loaded(w) and w.here.name == "GRAVEYARD":
        unload(w)
        return True
    return False


# ---------------------------------------------------------------------------
# Pushing the cart: walk check (no stairs) and enter hook (first move)
# ---------------------------------------------------------------------------

def stairs_block(w: World, destination: Room) -> Optional[str]:
    if w.walk_dir in ("up", "down") and cart_loaded(w) and _cart(w) in w.player.contents:
        return _NO_STAIRS
    return None


def on_enter(w: World, room: Room) -> None:
    if cart_loaded(w) and _cart(w) in w.player.contents and not w.get_global("CART-ROLLED"):
        w.set_global("CART-ROLLED", True)
        print(_ROLLING)


# ---------------------------------------------------------------------------
# Graveyard description line (called from chuckle.graveyard_action)
# ---------------------------------------------------------------------------

def graveyard_lines(w: World) -> None:
    if not w.get_global("GRAVESTONE-RETURNED"):
        return
    line = _GRAVEYARD_STONE
    if _cart(w).location is w.rooms["GRAVEYARD"]:
        line += " " + _GRAVEYARD_CART
    print(line)


# ---------------------------------------------------------------------------
# Councilman Rowan Finch
# ---------------------------------------------------------------------------

def talk_rowan(w: World) -> None:
    from content import quests
    if quests.is_complete(w, "32"):
        print(_ROWAN_AFTER)
    elif not quests.is_discovered(w, "32"):
        print(_ROWAN_TROPHY if w.get_global("ROWAN-MET") else _ROWAN_FIRST)
    elif w.get_global("GRAVESTONE-RETURNED"):
        print(_ROWAN_REWARD)
        quests.complete(w, "32")
        w.move_object(w.objects["MIDDLE-TIER-KEY"], w.here)   # held out — TAKE KEY
    elif w.get_global("ROWAN-QUEST-STARTED"):
        print(_ROWAN_WAITING)
    else:
        print(_ROWAN_START)
        w.set_global("ROWAN-QUEST-STARTED", True)
        quests.start(w, "32")
    w.set_global("ROWAN-MET", True)


_SET_NOUNS = ("stone", "gravestone", "headstone")


def set_stone_input_hook(w: World, text: str) -> bool:
    """SET STONE — "set" isn't a parser verb (SET SAIL must reach "sail")."""
    words = [x for x in text.lower().split() if x not in ("the", "down")]
    if len(words) >= 2 and words[0] == "set" and words[1] in _SET_NOUNS:
        unload(w)
        return True
    return False
