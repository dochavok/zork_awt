"""
Ty's Casino Corner — Cargo (Ship, Captain, and Crew).

Design: mechanics.md (Ty's Casino Corner — Cargo), npcs.md (Ty).

- Five fair d6 (no level dice, no Lucky), up to three rolls. 6, then 5, then 4
  lock automatically; the last two dice are the Cargo (2–12). No full
  sequence by the third roll scores 0.
- Ty rolls first. He keeps any cargo die showing 4–6 and rerolls 1–3 while
  rolls remain. The player then rolls; once the sequence is done with rolls
  left, they choose: REROLL BOTH, REROLL <n> (the die showing n), or STAND.
  A reroll must be kept.
- Stakes: the player sets them, Ty matches from his bankroll (30 Zenni to
  start; his winnings go back into it). Ties push. Cleaned out = the table
  closes for good. Play again right away as long as there's Zenni.

Stakes, die faces and the reroll choice are numbers, so commands are read from
the raw input line (an input hook), like TIP MAY.

State: TY-BANKROLL, TY-CLEANED-OUT,
       CARGO-ROUND (None, or {stake, ty, a, b, left} while the player chooses)
"""

from __future__ import annotations
import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.world import World

BANKROLL = 30
_ROOM = "CASINO-CORNER"
_ORDINALS = ("First", "Second", "Third")
_NAMES = {6: "six", 5: "five", 4: "four"}
_SLOTS = ((6, "ship"), (5, "captain"), (4, "crew"))

_INTRO = ('Ty doesn\'t look up from the dice. "Cargo. Six, five, four — whatever\'s '
          'left is your load. You put up Zenni, I match it." He nods at the empty chair.')
_STAKE_FIRST = 'Ty taps the table in front of you. "Stake first."'
_ZERO = '"Zero\'s not a bet."'
_SHORT = 'Ty glances at your purse. "You don\'t have that."'
_CAN_MATCH = '"I can match {x}." He sets the Zenni on the table. "That\'s what I\'ve got."'
_CLOSED = 'Ty raises his drink an inch. "Table\'s closed. You saw to that."'

# Ty's roll (mechanics.md)
_TY_ALL_AT_ONCE = ('Ty looks at the dice for a moment without touching them. "Six, five, '
                   'four." He sets three aside with two fingers, unhurried. "Cargo." He '
                   'rolls the remaining two. He doesn\'t look surprised.')
_TY_SIX_ON_TWO = ('The first roll comes up without a six. Ty considers the dice the way a '
                  'man considers weather — not concerned, just noting it. He sweeps them '
                  'up. The second roll produces the six. He sets it aside. "There it is." '
                  'As if it were never in doubt.')
_TY_FAILS = ('The dice don\'t cooperate. Ty watches the last roll settle. No four. He looks '
             'at the table for a moment, then at you. "Happens." He gathers the dice. '
             '"Your turn."')
_TY_ROLLS = "Ty rolls, sets the dice aside as they come, and rolls again."
_TY_KEEPS_ONE = "Ty keeps the {keep} and rolls the {roll} again."
_TY_REROLLS_BOTH = "Ty sweeps up both cargo dice and rolls again."
_TY_CARGO = "Ty's cargo: {n}."
_TY_LOW = '"Not much cargo on that ship." He records the score without ceremony.'
_TY_HIGH = '"Full load." A pause. "That\'ll be hard to beat."'

# The player's roll
_CHOOSE = "Reroll one, both, or stand?"
_SEQUENCE = "Ship, Captain and Crew. Your cargo: {a} and {b} — {n}."
_NO_SLOT = "No {slot}. Your score: 0."
_REROLL_ONE = "You roll the {old} again: {new}. Your cargo: {a} and {b} — {n}."
_REROLL_BOTH = "You roll the cargo again: {a} and {b} — {n}."
_WHICH = 'Ty waits. "Both, or just the {low}?" (REROLL BOTH, REROLL {low}, or STAND)'
_WAITING = 'Ty waits. "Reroll or stand?" (REROLL BOTH, REROLL {low}, or STAND)'

# The result
_WIN = 'Ty looks at the scores. He slides the pot across without comment. "Well played."'
_LOSE = 'Ty looks at the scores. He pulls the pot in. "Better luck." He means it plainly — no gloating.'
_PUSH = 'Ty looks at the scores. "Push." He slides your stake back.'
_CLEANED_OUT = ('Ty doesn\'t say anything for a moment. He looks at the table, then at '
                'you, then back at the table. "You cleaned me out." A small nod, as if '
                'confirming something to himself. "I don\'t play on credit." He reaches '
                'for his drink and doesn\'t reach for the dice.')

_NUMBERS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
    "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "zero": 0,
}
_PASS_THROUGH = {"save", "restore", "quit", "q"}   # meta commands during the choice


def _d6() -> int:
    return random.randint(1, 6)


def _here(w: World) -> bool:
    return w.here is not None and w.here.name == _ROOM


def _bankroll(w: World) -> int:
    b = w.get_global("TY-BANKROLL")
    return BANKROLL if b is None else b


# ---------------------------------------------------------------------------
# Rolling the sequence
# ---------------------------------------------------------------------------

def _roll_sequence():
    """Roll up to three times. Returns (rolls, locked count, cargo, rolls left), where
    rolls is a list of (faces rolled, values locked from them)."""
    rolls, locked, free = [], 0, 5
    for r in range(3):
        faces = [_d6() for _ in range(free)]
        rest, got = list(faces), []
        while locked < 3 and _SLOTS[locked][0] in rest:
            rest.remove(_SLOTS[locked][0])
            got.append(_SLOTS[locked][0])
            locked += 1
            free -= 1
        rolls.append((faces, got))
        if locked == 3:
            return rolls, locked, rest, 2 - r
    return rolls, locked, None, 0


# ---------------------------------------------------------------------------
# Ty's turn
# ---------------------------------------------------------------------------

def _ty_turn() -> int:
    rolls, _, cargo, left = _roll_sequence()
    first_six = 6 in rolls[0][1]
    if cargo is not None and len(rolls) == 1:
        print(_TY_ALL_AT_ONCE)
    elif not first_six and len(rolls) >= 2 and 6 in rolls[1][1]:
        print(_TY_SIX_ON_TWO)
        if cargo is None:
            print(_TY_FAILS)
    elif cargo is None:
        print(_TY_FAILS)
    else:
        print(_TY_ROLLS)
    if cargo is None:
        return 0
    a, b = cargo
    while left > 0 and (a < 4 or b < 4):     # keeps 4–6, rerolls 1–3
        if a < 4 and b < 4:
            print(_TY_REROLLS_BOTH)
            a, b = _d6(), _d6()
        else:
            keep, roll = (a, b) if b < 4 else (b, a)
            print(_TY_KEEPS_ONE.format(keep=keep, roll=roll))
            a, b = keep, _d6()
        left -= 1
    score = a + b
    print(_TY_CARGO.format(n=score))
    print(_TY_LOW if score <= 6 else _TY_HIGH)
    return score


# ---------------------------------------------------------------------------
# The player's turn
# ---------------------------------------------------------------------------

def _set_aside(got) -> str:
    if not got:
        return "Nothing to set aside."
    names = [f"the {_NAMES[v]}" for v in got]
    if len(names) == 1:
        return f"You set aside {names[0]}."
    return f"You set aside {', '.join(names[:-1])} and {names[-1]}."


def _player_turn(w: World, stake: int, ty: int) -> None:
    rolls, locked, cargo, left = _roll_sequence()
    for i, (faces, got) in enumerate(rolls):
        print(f"{_ORDINALS[i]} roll: {', '.join(str(f) for f in faces)}. {_set_aside(got)}")
    if cargo is None:
        print(_NO_SLOT.format(slot=_SLOTS[locked][1]))
        _settle(w, stake, ty, 0)
        return
    a, b = cargo
    if left == 0 or ty == 0:                 # Ty missed 6-5-4: the sequence wins outright
        print(_SEQUENCE.format(a=a, b=b, n=a + b))
        _settle(w, stake, ty, a + b)
        return
    print(_SEQUENCE.format(a=a, b=b, n=a + b) + " " + _CHOOSE)
    w.set_global("CARGO-ROUND", {"stake": stake, "ty": ty, "a": a, "b": b, "left": left})


def _choice(w: World, words: list[str]) -> bool:
    """REROLL / STAND. True if it acted (a turn); False if Ty only waited."""
    rnd = w.get_global("CARGO-ROUND")
    a, b = rnd["a"], rnd["b"]
    low = min(a, b)
    if words[0] == "stand":
        w.set_global("CARGO-ROUND", None)
        _settle(w, rnd["stake"], rnd["ty"], a + b)
        return True
    target = words[1:]
    if not target:
        print(_WHICH.format(low=low))
        return False
    if target == ["both"]:
        a, b = _d6(), _d6()
        print(_REROLL_BOTH.format(a=a, b=b, n=a + b))
    else:
        n = _number(target)
        if n is None or n not in (a, b):
            print(_WAITING.format(low=low))
            return False
        new = _d6()
        old = n
        if a == n:
            a = new
        else:
            b = new
        print(_REROLL_ONE.format(old=old, new=new, a=a, b=b, n=a + b))
    rnd.update(a=a, b=b, left=rnd["left"] - 1)
    if rnd["left"] > 0:
        print(_CHOOSE)
        w.set_global("CARGO-ROUND", rnd)
        return True
    w.set_global("CARGO-ROUND", None)
    _settle(w, rnd["stake"], rnd["ty"], a + b)
    return True


# ---------------------------------------------------------------------------
# Stakes and settling
# ---------------------------------------------------------------------------

def _settle(w: World, stake: int, ty: int, mine: int) -> None:
    g = w.globals
    if mine > ty:
        print(_WIN)
        g["zenni"] = g.get("zenni", 0) + stake
        w.set_global("TY-BANKROLL", _bankroll(w) - stake)
        if _bankroll(w) <= 0:
            print(_CLEANED_OUT)
            w.set_global("TY-CLEANED-OUT", True)
    elif mine < ty:
        print(_LOSE)
        g["zenni"] = g.get("zenni", 0) - stake
        w.set_global("TY-BANKROLL", _bankroll(w) + stake)
    else:
        print(_PUSH)


def _play(w: World, stake: int | None) -> None:
    if w.get_global("TY-CLEANED-OUT"):
        print(_CLOSED)
        return
    if stake is None:
        print(_STAKE_FIRST)
        return
    if stake <= 0:
        print(_ZERO)
        return
    if stake > w.globals.get("zenni", 0):
        print(_SHORT)
        return
    if stake > _bankroll(w):
        stake = _bankroll(w)
        print(_CAN_MATCH.format(x=stake))
    ty = _ty_turn()
    _player_turn(w, stake, ty)


def talk(w: World) -> None:
    """TALK TO TY."""
    print(_CLOSED if w.get_global("TY-CLEANED-OUT") else _INTRO)


# ---------------------------------------------------------------------------
# Input hook
# ---------------------------------------------------------------------------

def _number(words) -> int | None:
    n = None
    for x in words:
        if x.isdigit():
            n = int(x)
        elif x in _NUMBERS:
            n = _NUMBERS[x]
    return n


def input_hook(w: World, text: str) -> bool:
    """PLAY [CARGO] [n] / BET n / WAGER n; REROLL / STAND while choosing."""
    from engine.game import HOOK_NO_TURN
    words = [x for x in text.lower().replace(",", " ").split()
             if x not in ("the", "a", "zenni", "coin", "coins", "die", "dice")]
    rnd = w.get_global("CARGO-ROUND")
    if rnd is not None:
        if not _here(w):                     # can't happen while choosing; be safe
            w.set_global("CARGO-ROUND", None)
            return False
        if words and words[0] in ("reroll", "stand"):
            return True if _choice(w, words) else HOOK_NO_TURN
        if words and words[0] in _PASS_THROUGH:
            return False
        print(_WAITING.format(low=min(rnd["a"], rnd["b"])))
        return HOOK_NO_TURN
    if not _here(w) or not words:
        return False
    if words[0] == "play":
        rest = [x for x in words[1:] if x not in ("cargo", "for", "with", "ty")]
        if any(x not in _NUMBERS and not x.isdigit() for x in rest):
            return False                     # PLAY something else — the parser
        _play(w, _number(rest))
        return True
    if words[0] in ("bet", "wager", "stake"):
        rest = words[1:]
        if any(x not in _NUMBERS and not x.isdigit() for x in rest):
            return False
        _play(w, _number(rest))
        return True
    return False
