"""
May's hints — TIP MAY [#] / TIP MAY [#] ZENNI in the Bar.

Design: mechanics.md (Hint System — tier ranges, May's responses, which hint
a tip buys, one-tier and phased hints, hints before discovery), quests.md
(each quest's hints and when they're sold).

- The amount sets the tier paid for (1–3, 4–6, 7–12). May gives a random hint
  at exactly that tier; if there's none, she steps down a tier at a time.
  Nothing at or below it: a "nothing to share" line, the Zenni comes back.
- A quest's hints are sold in order. One-tier hints are Tier 1. Phased quests
  (17, 32) sell from Tier 1 again in each phase; unbought hints from an
  earlier phase are no longer sold.
- Sold only for discovered, incomplete quests — except 19&30 and 4 (sold
  before discovery; buying one discovers the quest) and 34's late hint (sold
  before discovery; doesn't discover it).
- May's response follows the amount tipped; the hint follows it.

State: HINTS-BOUGHT [hint id], CHUCKLE-VISITED, LOWER-TIER-ENTERED,
       LOWER-TIER-TURNS, LOWER-TIER-SINCE (world.moves on entry, or None)
"""

from __future__ import annotations
import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.world import World, Room

LOWER_TIER = frozenset({
    "PILE-OF-RUBBLE", "LOWER-CRYPT", "THERMAL-VENT-ROOM", "LOWER-ENCAMPMENT",
    "ANTECHAMBER", "LOWER-CROSSING", "NARROW-PASS", "STILL-DEN", "TOOL-ALCOVE",
    "FLOODED-PASSAGE", "FOUNTAIN-ROOM", "DARK-ROOM", "SPIRIT-ROOM", "BURIAL-CHAMBER",
})
CHUCKLE_HOUSE = frozenset({
    "CHUCKLE-ENTRANCE", "REJECTION-MIRROR", "SHATTER-TRAP-MIRROR", "GHOSTS-ROOM",
})
LATE_HINT_TURNS = 50     # Quest 34

# --- May's lines (mechanics.md — Hint System) -------------------------------

_RESPONSE = {
    1: ('May palms the coin without looking at it, leans in, and shares what she '
        'knows. "That\'s worth something," she says.'),
    2: 'May pockets the coins carefully. "That buys you something worth hearing," she says.',
    3: ('May counts the coins once, pockets them, and leans all the way across the '
        'bar. "{name}," she says.'),
}
_NOTHING = (
    'May pushes the Zenni back. "Keep it. I\'ve got nothing worth that right now." '
    'She goes back to wiping the bar.',
    'May looks at the coin and shakes her head slowly. "I\'d be robbing you. Ask me '
    'again when something changes."',
    'May sets the Zenni on the bar and slides it back. "Nothing in here worth '
    'selling today," she says, tapping her temple.',
)
_OVER = ('May looks genuinely uncomfortable. "I appreciate the thought, but no." She '
         'slides it all back. "Ask me something and we\'ll talk."')
_HOW_MUCH = 'May waits. "How much?"'
_ZERO = 'May looks at your empty hand, then at you. "That\'s nothing."'
_SHORT = 'May looks at you evenly. "You\'re short." She goes back to work.'
_NOT_HERE = "May isn't here."

# --- Hints (quests.md) --------------------------------------------------------

_Q4 = ("That jar in the back room of the inn — people say it used to warn about "
       "things. If it's still got something to say, I'd want to hear it before "
       "going any deeper.")
_Q17_BEFORE = (
    "People say the mirrors in the Chuckle House show more than they should. Most "
    "folks don't go back a second time.",
    "Word is a family member of the records room clerk went into the Chuckle House "
    "years ago and never came out. He doesn't talk about it.",
    "The trick with the Chuckle House is that some doors only open for people the "
    "mirrors can't find.",
)
_Q17_AFTER = (
    "Malevolent spirits can only be freed through magic.",
    "Silas Bryne — keeps the lighthouse — mentioned he came across a spell he "
    "couldn't make heads or tails of. Left it on his desk.",
)
_Q17_CHARTER = (
    "Word is the records room clerk had a relative who went into the Chuckle House "
    "years ago and never came back. He doesn't talk about it. He's also the one "
    "sitting on the town charter, and he's not giving it up easily — but something "
    "personal might move him more than an argument would.",
)
_Q19_STATUE = ("Someone was seen tampering with the statue in Roundabout Town Square. "
               "Probably nothing. Probably.")
_Q19 = (
    "The Keeper of the Faiths has gone missing. No one's seen him in some time.",
    "There's talk of a scholar who went into the deep passages and never came back. "
    "The Librarian might know something about it.",
    "No one can get into his office at the Church. Locked tight. You'd need his key "
    "to find out what he knew.",
)
_Q24 = ("Bees aren't aggressive by nature — beekeepers have known for centuries how "
        "to calm them. Something about smoke. Ask me why it works and I couldn't tell "
        "you, but it does.")
_Q25 = ("There's water behind more than one door near the inn. Best to sort that out "
        "from the top before you go wandering underneath.")
_Q27 = ("There's something in the town charter about public bridges and rights of "
        "way. Might be worth a look.")
_Q32 = (
    "There's a locked door down in the tunnels, they say. Heavy thing — needs a "
    "proper key. Word is someone in town might know something about it.",
    "The Finch family goes back a long way in Roundabout. Rowan's grandfather was "
    "quite the explorer, from what I hear. Rowan works up at the Town Hall if you "
    "want to ask him about it.",
    "Old Calder Finch — now there was an explorer. Spent more time underground than "
    "above it. Whatever he knew about that door went with him to the cemetery. Rowan "
    "might point you in the right direction.",
)
_Q32_CART = "I've heard carts are good for moving heavy things. Stones, for instance."
_Q34 = ("There are rooms in the deep passages that aren't finished. Sometimes a room "
        "that looks like a dead end is asking you something.")
_Q42 = ("Rushing through a place and knowing a place aren't the same thing. I've "
        "learned that much.")
_Q49 = (
    "Something about that shrine bowl needs water — clean, running water. Check the "
    "Quest Board; there may be something relevant posted.",
    "The town fountain hasn't run in years. Word is the aqueduct beneath the dungeon "
    "needs repair — it's on the Quest Board if you haven't seen it.",
)
_Q59 = ("I've seen plenty of people try Lynds. The ones who come back and win aren't "
        "the same people who first sat down across from him.")


def _open(w: World, q: str) -> bool:
    from content import quests
    return quests.is_discovered(w, q) and not quests.is_complete(w, q)


def _phase(w: World, q: str):
    """(phase id, hint texts) on sale for quest q now, or None."""
    from content import quests
    g = w.get_global
    if q == "4":
        if g("LOWER-TIER-ENTERED") and not quests.is_complete(w, "4"):
            return "4", (_Q4,)
    elif q == "17":
        if not _open(w, "17"):
            return None
        if g("GHOST-FREED"):
            return "17c", _Q17_CHARTER
        if g("CHUCKLE-VISITED"):
            return "17b", _Q17_AFTER
        return "17a", _Q17_BEFORE
    elif q == "19":
        if not quests.is_complete(w, "19"):
            first = _Q19[0] if g("STATUE-EXAMINED") else _Q19_STATUE
            return "19", (first,) + _Q19[1:]
    elif q == "32":
        if not _open(w, "32") or g("GRAVESTONE-RETURNED"):
            return None
        if g("ROWAN-QUEST-STARTED"):
            return "32b", (_Q32_CART,)
        return "32a", _Q32
    elif q == "34":
        if (quests.is_complete(w, "28") and not quests.is_discovered(w, "34")
                and lower_tier_turns(w) >= LATE_HINT_TURNS):
            return "34", (_Q34,)
    elif q == "49":
        if _open(w, "49") and not quests.is_complete(w, "22"):
            return "49", _Q49
    else:
        text = {"24": _Q24, "25": _Q25, "27": _Q27, "42": _Q42, "59": _Q59}[q]
        if _open(w, q):
            return q, (text,)
    return None


_QUESTS = ("4", "17", "19", "24", "25", "27", "32", "34", "42", "49", "59")


def _bought(w: World) -> list:
    return w.globals.setdefault("HINTS-BOUGHT", [])


def _next_hints(w: World) -> list[tuple[int, str, str, str]]:
    """(tier, quest, hint id, text) — each quest's next unbought hint now."""
    out = []
    bought = _bought(w)
    for q in _QUESTS:
        on_sale = _phase(w, q)
        if on_sale is None:
            continue
        phase, texts = on_sale
        for i, text in enumerate(texts):
            hint_id = f"{phase}.{i + 1}"
            if hint_id not in bought:
                out.append((i + 1, q, hint_id, text))
                break
    return out


def _tier_paid(amount: int) -> int:
    return 1 if amount <= 3 else 2 if amount <= 6 else 3


def tip(w: World, amount: int | None) -> None:
    from content import quests
    if w.here is None or w.here.name != "BAR":
        print(_NOT_HERE)
        return
    if amount is None:
        print(_HOW_MUCH)
        return
    if amount <= 0:
        print(_ZERO)
        return
    if amount > 12:
        print(_OVER)
        return
    if amount > w.globals.get("zenni", 0):
        print(_SHORT)
        return

    paid = _tier_paid(amount)
    available = _next_hints(w)
    for tier in range(paid, 0, -1):
        choices = [h for h in available if h[0] == tier]   # quest-number order
        if choices:
            break
    else:
        print(_NOTHING[random.randint(1, len(_NOTHING)) - 1])
        return

    _tier, q, hint_id, text = choices[random.randint(1, len(choices)) - 1]
    w.globals["zenni"] -= amount
    _bought(w).append(hint_id)
    name = w.globals.get("player_name", "")
    print(_RESPONSE[paid].format(name=name))
    print(f'"{text}"')
    if q == "19":
        quests.discover(w, "19")
        quests.discover(w, "30")
    elif q == "4":
        quests.discover(w, "4")


# --- TIP MAY input hook --------------------------------------------------------

_NUMBERS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
    "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "zero": 0,
}
_MAY = ("may", "bartender", "barkeep")


def tip_input_hook(w: World, text: str) -> bool:
    """TIP MAY [#] / TIP MAY [#] ZENNI — the amount isn't a parser object.
    May is the only one who takes tips, so TIP [#] without her name tips her too."""
    words = text.lower().split()
    if not words or words[0] != "tip":
        return False
    others = [x for x in words[1:]
              if x not in _MAY and x not in _NUMBERS and not x.isdigit()
              and x not in ("zenni", "coin", "coins", "to")]
    if others:
        return False
    tip(w, _amount(words[1:]))
    return True


def _amount(words) -> int | None:
    amount = None
    for x in words:
        if x.isdigit():
            amount = int(x)
        elif x in _NUMBERS:
            amount = _NUMBERS[x]
    return amount


def give_zenni_input_hook(w: World, text: str) -> bool:
    """GIVE 3 ZENNI TO MAY / GIVE MAY 3 ZENNI / PAY MAY 3 — a tip, while May
    is here. Zenni isn't a parser object."""
    words = [x for x in text.lower().split() if x not in ("the", "a")]
    if not words or words[0] not in ("give", "hand", "pay"):
        return False
    if not any(x in _MAY for x in words[1:]):
        return False
    others = [x for x in words[1:]
              if x not in _MAY and x not in _NUMBERS and not x.isdigit()
              and x not in ("zenni", "coin", "coins", "to", "her")]
    if others:
        return False                     # GIVE NOTE TO MAY etc. — the normal GIVE
    if words[0] != "pay" and "zenni" not in words and "coin" not in words \
            and "coins" not in words and _amount(words[1:]) is None:
        return False                     # GIVE MAY — let the parser ask "what?"
    may = w.objects.get("MAY")
    if may is None or may.location is not w.here:
        return False
    tip(w, _amount(words[1:]))
    return True


# --- Tracking for hint conditions ------------------------------------------

def lower_tier_turns(w: World) -> int:
    turns = w.get_global("LOWER-TIER-TURNS") or 0
    since = w.get_global("LOWER-TIER-SINCE")
    return turns + (w.moves - since if since is not None else 0)


def on_enter(w: World, room: Room) -> None:
    """Enter hook: first lower-tier descent, lower-tier time, Chuckle House visit."""
    since = w.get_global("LOWER-TIER-SINCE")
    if room.name in LOWER_TIER:
        w.set_global("LOWER-TIER-ENTERED", True)
        if since is None:
            w.set_global("LOWER-TIER-SINCE", w.moves)
    elif since is not None:
        w.set_global("LOWER-TIER-TURNS", lower_tier_turns(w))
        w.set_global("LOWER-TIER-SINCE", None)
    if room.name in CHUCKLE_HOUSE:
        w.set_global("CHUCKLE-VISITED", True)
