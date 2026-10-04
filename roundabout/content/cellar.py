"""
Quest 25 — The Flooded Cellar.

Design: quests.md (Quest 25), npcs.md (May), items.md (Cellar Key, Cashbox,
Bartender's Boots), locations.md (Kitchen, Cellar/Storeroom, The Bone Passage).
- TALK TO MAY while carrying the crowbar: cellar key (Quest 25 discovered).
  After the drain, the next TALK TO MAY gives the Bartender's Boots.
- Kitchen: UNLOCK DOOR WITH KEY (the key stays in the lock), OPEN DOOR. From
  the top step: USE CROWBAR ON DRAIN (cover off), CLEAR DRAIN → the cellar
  drains and Quest 25 completes.
- DOWN before the drain, or opening the tunnel door from the Bone Passage
  before the drain: instant drowning, GAME OVER.
- Cellar (lit): cashbox (10 Zenni), tunnel door west to the Bone Passage.

State: CELLAR-KEY-GIVEN, CELLAR-DOOR-UNLOCKED, CELLAR-DOOR-OPEN,
       DRAIN-COVER-OFF, CELLAR-DRAINED, TUNNEL-DOOR-OPEN, CASHBOX-OPEN,
       BOOTS-GIVEN
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED, M_LOOK
from engine.world import Room, Exit, ONBIT, RLANDBIT

if TYPE_CHECKING:
    from engine.world import World

CACHE_ZENNI = 10

_MAY_KEY = (
    "May's eyes drop to the crowbar and stay there. \"Now that's useful.\" She "
    "reaches under the bar and sets an iron key on the counter. \"Cellar. It "
    "flooded years back — the drain clogged, and we shut the door and stopped "
    "thinking about it. If you can get the cover off that drain, it's yours to "
    "clear.\" She slides the key over. \"Do it from the top of the stairs. Nobody "
    "goes down into that water.\""
)
_MAY_BOOTS = (
    "May looks you over — the wet sleeves, the silt. \"You got the cellar dry.\" "
    "She ducks under the bar and comes up with a pair of tall leather boots, "
    "salt-stained and broken in. \"Forgot I had these. Should have given them to "
    "you BEFORE you cleaned up the cellar.\""
)

_KITCHEN = (
    "The kitchen is warm and loud in the way that working kitchens are — pots, "
    "fire, the particular authority of someone who knows exactly what they're "
    "doing.\n"
    "Shamus moves through it without wasted motion, cooking and selling in equal "
    "measure — if you need something, he's worth asking.\n"
    "Dried herbs hang from the ceiling in loose bundles. A scarred wooden table "
    "dominates the center."
)
_DOOR_LOCKED = (
    "The cellar door is set into the floor near the far wall; a faint smell of "
    "damp rises from it even when it's shut. The bartender keeps the key."
)
_DOOR_UNLOCKED = "The cellar door is set into the floor near the far wall, May's key in its lock."
_DOOR_OPEN_FLOODED = (
    "The cellar door stands open near the far wall, May's key still in the lock. "
    "Below it, water fills the stairwell almost to the top step."
)
_DOOR_OPEN_DRAINED = (
    "The cellar door stands open near the far wall, May's key still in the lock. "
    "Stone steps lead down into the cellar."
)

_UNLOCKED = (
    "The key turns stiffly. The lock hasn't been asked to do anything in years. "
    "You leave it where it is."
)
_OPENED_FLOODED = (
    "The cellar door comes up on a breath of cold, wet air. Stone steps lead down "
    "— three of them, then water, still and clear, filling the cellar nearly to "
    "the beams. At the foot of the steps, through the water, you can make out "
    "the square iron cover of a drain."
)
_COVER_OFF = (
    "You lie flat on the top step and reach the crowbar down through the water, "
    "feeling along the bottom step until the lip catches the edge of the grate. "
    "You lean on it. The cover comes up with a jolt and slides off into the dark."
)
_DRAINED = (
    "You work the crowbar down into the open drain and lever. Something gives — "
    "a fist of rotted sacking and root comes up through the water — and the whole "
    "cellar starts to turn. The water drops a step, then another, then goes all "
    "at once with a long, sucking roar you feel through the kitchen floor. When "
    "it's quiet again, the stairs go all the way down."
)
_DROWN_STAIRS = (
    "You start down the steps. On the fourth there isn't a step — only water, "
    "colder than it has any right to be. The kitchen's light shrinks to a square "
    "above you, and then it doesn't."
)
_DROWN_TUNNEL = (
    "You lift the latch. The door doesn't open so much as leave — the water "
    "behind it takes it off its hinges and you with it. The Bone Passage fills in "
    "the time it takes to understand what's happening."
)

_CELLAR = (
    "The cellar is still wet — the walls dark to shoulder height, a tide line of "
    "silt marking where the water stood for years. Barrels lie where the flood "
    "left them, staves sprung. The drain gurgles now and then, like it's still "
    "thinking about it. In the west wall is a low door of black oak that nobody "
    "upstairs has mentioned."
)
_TUNNEL_OPENED_CELLAR = (
    "The door swings inward onto dark stone. Cold air comes through it, and the "
    "smell of old earth."
)
_TUNNEL_OPENED_BONE = "The door swings open onto the tavern cellar. Somewhere above, someone is cooking."
_CASHBOX_OPENED = (
    "The lid gives on the third try. Inside, wrapped in oilcloth and perfectly "
    f"dry: {CACHE_ZENNI} Zenni. Somebody planned for the flood better than they "
    "planned for the drain."
)


def _game_over(w: World, text: str) -> None:
    print(text + "\n\n*** GAME OVER ***")
    w.set_global("GAME-OVER", True)
    w.game.quit()


# ---------------------------------------------------------------------------
# May
# ---------------------------------------------------------------------------

def talk_may(w: World) -> bool:
    """Quest 25 lines on TALK TO MAY (after the free drink). True if handled."""
    if w.get_global("CELLAR-DRAINED") and not w.get_global("BOOTS-GIVEN"):
        print(_MAY_BOOTS)
        w.set_global("BOOTS-GIVEN", True)
        w.move_object(w.objects["BARTENDERS-BOOTS"], w.player)
        return True
    if not w.get_global("CELLAR-KEY-GIVEN") and w.objects["CROWBAR"] in w.player.contents:
        from content import quests
        print(_MAY_KEY)
        w.set_global("CELLAR-KEY-GIVEN", True)
        w.move_object(w.objects["CELLAR-KEY"], w.player)
        quests.discover(w, "25")
        return True
    return False


# ---------------------------------------------------------------------------
# Kitchen: the cellar door and the drain
# ---------------------------------------------------------------------------

def kitchen_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_LOOK:
        print(_KITCHEN)
        if not w.get_global("CELLAR-DOOR-UNLOCKED"):
            print(_DOOR_LOCKED)
        elif not w.get_global("CELLAR-DOOR-OPEN"):
            print(_DOOR_UNLOCKED)
        elif not w.get_global("CELLAR-DRAINED"):
            print(_DOOR_OPEN_FLOODED)
        else:
            print(_DOOR_OPEN_DRAINED)
        return M_HANDLED
    return M_NOT_HANDLED


def unlock_cellar_door(w: World) -> None:
    if w.get_global("CELLAR-DOOR-UNLOCKED"):
        print("It's already unlocked. The key is still in the lock.")
        return
    key = w.objects["CELLAR-KEY"]
    if key not in w.player.contents:
        print("You don't have the key to it.")
        return
    print(_UNLOCKED)
    w.set_global("CELLAR-DOOR-UNLOCKED", True)
    w.move_object(key, w.objects["CELLAR-DOOR"])   # stays in the lock


def open_cellar_door(w: World) -> None:
    if not w.get_global("CELLAR-DOOR-UNLOCKED"):
        print("The cellar door is locked.")
        return
    if w.get_global("CELLAR-DOOR-OPEN"):
        print("It's already open.")
        return
    w.set_global("CELLAR-DOOR-OPEN", True)
    if w.get_global("CELLAR-DRAINED"):
        print("The cellar door comes up. Stone steps lead down into the cellar.")
    else:
        print(_OPENED_FLOODED)


def pry_drain(w: World) -> None:
    if w.here.name != "KITCHEN" or not w.get_global("CELLAR-DOOR-OPEN") \
            or w.get_global("CELLAR-DRAINED"):
        print("You can't reach the drain from here.")
        return
    if w.objects["CROWBAR"] not in w.player.contents:
        print("You'd need something with leverage — and reach.")
        return
    if w.get_global("DRAIN-COVER-OFF"):
        print("The cover's already off.")
        return
    print(_COVER_OFF)
    w.set_global("DRAIN-COVER-OFF", True)


def clear_drain(w: World) -> None:
    if w.get_global("CELLAR-DRAINED"):
        print("The drain is clear. It gurgles, unhelpfully.")
        return
    if w.here.name != "KITCHEN" or not w.get_global("CELLAR-DOOR-OPEN"):
        print("You can't reach the drain from here.")
        return
    if not w.get_global("DRAIN-COVER-OFF"):
        print("The cover's still on it.")
        return
    if w.objects["CROWBAR"] not in w.player.contents:
        print("You can't reach it from the top step with your bare hands.")
        return
    from content import quests
    print(_DRAINED)
    w.set_global("CELLAR-DRAINED", True)
    w.move_object(w.objects["DRAIN"], w.rooms["CELLAR"])
    w.objects["CASHBOX"].clear_flag("INVISIBLE")
    quests.complete(w, "25")


class _CellarStairs(Exit):
    """Kitchen DOWN: closed/locked door blocks; before the drain, drowning."""

    def resolve(self, world):
        if not world.get_global("CELLAR-DOOR-OPEN"):
            return None, "The cellar door is closed."
        if not world.get_global("CELLAR-DRAINED"):
            _game_over(world, _DROWN_STAIRS)
            return None, None
        return super().resolve(world)


# ---------------------------------------------------------------------------
# Tunnel door (cellar west ↔ Bone Passage east)
# ---------------------------------------------------------------------------

class _TunnelDoor(Exit):
    def resolve(self, world):
        if not world.get_global("TUNNEL-DOOR-OPEN"):
            return None, "The door is closed."
        return super().resolve(world)


def open_tunnel_door(w: World) -> None:
    if w.get_global("TUNNEL-DOOR-OPEN"):
        print("It's already open.")
        return
    if w.here.name == "BONE-PASSAGE" and not w.get_global("CELLAR-DRAINED"):
        _game_over(w, _DROWN_TUNNEL)
        return
    w.set_global("TUNNEL-DOOR-OPEN", True)
    print(_TUNNEL_OPENED_BONE if w.here.name == "BONE-PASSAGE" else _TUNNEL_OPENED_CELLAR)


def open_cashbox(w: World) -> None:
    if w.get_global("CASHBOX-OPEN"):
        print("The cashbox is open, and empty.")
        return
    print(_CASHBOX_OPENED)
    w.set_global("CASHBOX-OPEN", True)
    w.globals["zenni"] = w.globals.get("zenni", 0) + CACHE_ZENNI


# ---------------------------------------------------------------------------
# Rooms
# ---------------------------------------------------------------------------

def make_rooms(world) -> None:
    cellar = Room(name="CELLAR", desc="Cellar", ldesc=_CELLAR, value=1)
    cellar.set_flag(ONBIT)       # part of the inn — not on the dark room list
    cellar.set_flag(RLANDBIT)
    world.register_room(cellar)

    kitchen = world.rooms["KITCHEN"]
    kitchen.ldesc = ""
    kitchen.action = kitchen_action
    kitchen.exits["down"] = _CellarStairs(destination="CELLAR")
    cellar.exits.update(up=Exit(destination="KITCHEN"), west=_TunnelDoor(destination="BONE-PASSAGE"))
    world.rooms["BONE-PASSAGE"].exits["east"] = _TunnelDoor(destination="CELLAR")
