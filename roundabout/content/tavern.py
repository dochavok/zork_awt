"""
Tale and Ale — May at the Bar, and the guest rooms upstairs.

Design: npcs.md (May). First visit to the Bar fires her introduction once.
Quest 51's reward (one free drink, 1 heart) is served on TALK TO MAY.
- BUY / ORDER / PURCHASE DRINK, FOOD or STEW (1 heart; stew 2, after Quest
  40): 2 Zenni, 1 after Quest 22. Refused at full hearts.
- RENT / BUY ROOM: 5 Zenni, full heal, a random guest room (locations.md),
  woken with its wake-up text. Refused at full hearts unless inked — the
  room's bath clears the ink (traps.md — Trap 45).
- Inked, renting a room is the only thing May will do.

State: MAY-MET, INKED, FOOD-DISCOUNT (Quest 22), HEARTY-STEW (Quest 40),
       GUEST-WAKING, GUEST-BATH
"""

from __future__ import annotations
import random
from typing import TYPE_CHECKING

from engine.game import M_NOT_HANDLED, M_HANDLED, M_END, M_LOOK
from engine.world import Room, Exit, ONBIT

if TYPE_CHECKING:
    from engine.world import World

_MAY_FIRST_VISIT = (
    "A woman behind the bar glances up as you come in — shoulder-length red "
    "hair, appraisal done in about a second, apparently satisfactory.\n"
    '"New face," she says, not unkindly. "I\'m May. Drinks are two Zenni, '
    "food's the same — keeps you on your feet longer than you'd think. Rooms "
    'are upstairs if you need to sleep it off properly."\n'
    "She sets a glass down and leans one hand on the bar.\n"
    '"If you get stuck on something and want a nudge in the right direction, '
    "money talks. Shamus is in the kitchen if you need supplies — he keeps "
    'more than recipes back there."\n'
    "She picks the glass back up and goes back to work. The conversation is "
    "over when she decides it is."
)
_MAY_BUSY = (
    "She picks the glass back up and goes back to work. The conversation is "
    "over when she decides it is."
)
_MAY_MUGGER_REWARD = (
    'May glances up. "Heard the back alley\'s gone quiet." She sets a glass '
    'on the bar. "That one\'s on the house."'
)


def bar_action(w: World, msg: int = M_NOT_HANDLED) -> int:
    if msg == M_END and not w.get_global("MAY-MET"):
        w.set_global("MAY-MET", True)
        print(_MAY_FIRST_VISIT)
    return M_NOT_HANDLED


def talk_may(w: World) -> None:
    g = w.globals
    if w.get_global("INKED"):
        print(MAY_INKED)   # the free drink and quest hand-overs wait
        return
    if w.get_global("FREE-DRINK-PENDING"):
        print(_MAY_MUGGER_REWARD)
        w.set_global("FREE-DRINK-PENDING", False)
        g["hearts"] = min(g.get("max_hearts", g.get("hearts", 1)), g.get("hearts", 1) + 1)
        return
    from content import cellar
    if not cellar.talk_may(w):
        print(_MAY_BUSY)


# ---------------------------------------------------------------------------
# Food, drink, stew and rooms at the Bar (npcs.md — May)
# ---------------------------------------------------------------------------

MAY_INKED = (
    'May looks at the ink, then at you. "Rooms are upstairs. That\'s all '
    'you\'re getting from me until you\'ve used one."'
)
_NO_SELLER = "There's no one here to sell you that."
_SHORT = 'May looks at you evenly. "You\'re short." She goes back to work.'
_FULL = ('May glances at you and sets the glass back down. "You don\'t need it. '
         'Come back when you do."')
_FULL_ROOM = 'May stops halfway to the key. "You\'re fine. Come back when you\'re not."'
_NO_STEW = '"Not on the menu," May says. "Ask Shamus."'

# {price} is "Two" or "One" (Quest 22)
_SERVED = {
    "drink": ("May sets a glass on the bar and fills it without being asked what "
              "you want. {price} Zenni."),
    "food":  ("May calls back to the kitchen and a plate appears shortly after. "
              'She sets it in front of you. "{price} Zenni."'),
    "stew":  ("May calls back to the kitchen. Shamus brings the bowl out himself "
              'and sets it down without a word. "{price} Zenni," May says.'),
}
_HEALS = {"drink": 1, "food": 1, "stew": 2}

_ROOM_PRICE = 5
_RENT = '"Five Zenni," May says, and slides a key across the bar. "Sleep well."'
_RENT_INKED = (
    'May looks at the ink for a long moment. "Five Zenni," she says, and slides '
    'a key across the bar. "There\'s a bath up there. Use it."'
)
_BATH = "The ink takes three changes of water and most of the soap. It comes off."

_ORDER_VERBS = ("buy", "order", "purchase", "rent")
_ITEMS = {"drink": "drink", "food": "food", "stew": "stew", "room": "room"}


def bar_input_hook(w: World, text: str) -> bool:
    """BUY / ORDER / PURCHASE DRINK, FOOD or STEW; RENT / BUY ROOM. None of
    these are parser objects — match the words here."""
    words = [x for x in text.lower().split() if x not in ("a", "an", "the", "some")]
    if words[:1] and words[0] in _ORDER_VERBS and words[1:2] == ["hearty"]:
        words = [words[0]] + words[2:]
    if len(words) != 2 or words[0] not in _ORDER_VERBS or words[1] not in _ITEMS:
        return False
    item = words[1]
    if words[0] == "rent" and item != "room":
        return False
    if w.here is None or w.here.name != "BAR":
        print(_NO_SELLER)
    elif item == "room":
        rent_room(w)
    else:
        _serve(w, item)
    return True


def _price(w: World) -> int:
    return 1 if w.get_global("FOOD-DISCOUNT") else 2


def _serve(w: World, item: str) -> None:
    g = w.globals
    if w.get_global("INKED"):
        print(MAY_INKED)
        return
    if item == "stew" and not w.get_global("HEARTY-STEW"):
        print(_NO_STEW)
        return
    hearts, max_hearts = g.get("hearts", 1), g.get("max_hearts", 1)
    if hearts >= max_hearts:
        print(_FULL)
        return
    price = _price(w)
    if g.get("zenni", 0) < price:
        print(_SHORT)
        return
    g["zenni"] -= price
    print(_SERVED[item].format(price="One" if price == 1 else "Two"))
    g["hearts"] = min(max_hearts, hearts + _HEALS[item])


def rent_room(w: World) -> None:
    g = w.globals
    inked = bool(w.get_global("INKED"))
    if not inked and g.get("hearts", 1) >= g.get("max_hearts", 1):
        print(_FULL_ROOM)
        return
    if g.get("zenni", 0) < _ROOM_PRICE:
        print(_SHORT)
        return
    g["zenni"] -= _ROOM_PRICE
    print(_RENT_INKED if inked else _RENT)
    g["hearts"] = g.get("max_hearts", g.get("hearts", 1))
    w.set_global("GUEST-WAKING", True)
    w.set_global("GUEST-BATH", inked)
    if inked:
        from content import chuckle, ink
        ink.cleaned(w)
        chuckle.update_ghost_visibility(w)
    room = w.rooms[f"GUEST-ROOM-{random.randint(1, 3)}"]
    game = w.game
    game.desc_mode_override = True      # the wake-up text shows every time
    try:
        game.enter_room(room)
    finally:
        game.desc_mode_override = False
        w.set_global("GUEST-WAKING", False)
        w.set_global("GUEST-BATH", False)


# ---------------------------------------------------------------------------
# Guest rooms (locations.md) — entered only by renting; one-way out
# ---------------------------------------------------------------------------

_GUEST_ROOMS = {
    1: ("east",
        "A plain room, honestly kept. Bed, washstand, a window that looks out "
        "over the street. The kind of room that asks nothing of you.",
        "You come around slowly. The bed is better than it had any reason to "
        "be. Light comes through the window — enough to know you slept. You "
        "feel considerably more capable than you did."),
    2: ("west",
        "A corner room, slightly larger than it needs to be. Two windows, a "
        "wardrobe that doesn't quite close, a rag rug that was once a specific "
        "color. Comfortable in an unassuming way.",
        "The wardrobe door has drifted open in the night. You close it out of "
        "habit. Whatever was wrong with you yesterday, sleep has addressed most "
        "of it."),
    3: ("south",
        "The smallest of the three rooms, tucked at the end of the hall. Low "
        "ceiling, narrow bed, a single candle on the nightstand burned to "
        "nothing. Quiet in a way the other rooms aren't.",
        "You wake in the small room at the end of the hall. The candle is out. "
        "You are rested — properly, completely rested. That will do."),
}


def _guest_action(n: int):
    _, ldesc, wake = _GUEST_ROOMS[n]

    def action(w: World, msg: int = M_NOT_HANDLED) -> int:
        if msg == M_LOOK:
            if w.get_global("GUEST-WAKING"):
                if w.get_global("GUEST-BATH"):
                    print(_BATH)
                print(wake)
            else:
                print(ldesc)
            return M_HANDLED
        return M_NOT_HANDLED
    return action


def make_guest_rooms(world) -> None:
    """Three guest rooms off the Upstairs Hall. 0 XP; not in the Zenni pool."""
    for n, (exit_dir, _ldesc, _wake) in _GUEST_ROOMS.items():
        r = Room(name=f"GUEST-ROOM-{n}", desc=f"Guest Room {n}", ldesc="", value=0)
        r.set_flag(ONBIT)
        r.action = _guest_action(n)
        r.exits[exit_dir] = Exit(destination="UPSTAIRS-HALL")
        world.register_room(r)
