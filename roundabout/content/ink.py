"""
Inked player (traps.md — Trap 45; npcs.md, each NPC's "Inked player" line).

While INKED, the refusing NPCs won't deal with the player at all — TALK, GIVE
(the item is kept), BUY, PAY / GIVE Zenni, CHALLENGE / FIGHT, the trials. No
Zenni taken. May is in tavern.py (rooms only); Litlock's door line is in
dankhaus.py. Will still engages: the first thing done with him while inked
gets his disdainful line, then goes ahead; TALK TO WILL gets it every time.
Quest givers' unprompted arrival lines hold until the player is clean
(vikings.py, old_oak.py). Renting a room clears the ink (tavern.py).

State: INKED, WILL-DISDAIN-SHOWN
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional

from engine.game import M_HANDLED, M_NOT_HANDLED

if TYPE_CHECKING:
    from engine.world import World, GameObject

_OWN_LINES = {
    "SHAMUS": ('Shamus looks up from the stove, takes in the ink, and points the '
               'ladle at the door. "Not in my kitchen."'),
    "RAZNAK": 'Raznak lowers his bow and studies you. "Wash," he says. "Then we talk."',
    "KNIGHT": ('The knight looks you over, slowly. "I teach those who present '
               'themselves properly. Come back clean."'),
    "RECORDS-WORKER": ('The clerk glances up, sees the ink, and slides the ledger out '
                       'of your reach. "Not near the records. Not like that."'),
    "LIBRARIAN": ('The Librarian takes one look at you and moves, quietly, between '
                  'you and the shelves. "Not with those hands."'),
}
QUEST_GIVERS = ("ARCHIVIST", "OAK-CHILD", "BEEKEEPER", "IVANAAR", "HAALVAR", "AYLORA",
                "PYRONICUS", "ROWAN-FINCH", "LYNDS")
_SHARED = "{name} takes one look at the ink and wants nothing to do with you until it's gone."

LITLOCK_DOOR = ("The air near the door shifts as you approach, then settles, firmly. "
                'From inside, Litlock\'s voice: "Not like that, you\'re not."')
_WILL = ("Will peers over his spectacles. \"And you found the thread,\" he says, and "
         "pauses. \"Everyone finds the thread.\" He turns back to his work. \"The inn "
         'has a bath. Use it. Twice."')

# Everything done *with* an NPC. Looking at one, or listening, is not.
_GATED = frozenset({
    "V-TALK", "V-HELLO", "V-GIVE", "V-BUY", "V-PAY", "V-CHALLENGE", "V-MELEE",
    "V-SHOOT", "V-TIP", "V-SAY", "V-ANSWER", "V-REPLY",
})


def inked(w: World) -> bool:
    return bool(w.get_global("INKED"))


def refusal(w: World, name: str) -> Optional[str]:
    """The NPC's refusal line while the player is inked, else None."""
    if not inked(w):
        return None
    if name in _OWN_LINES:
        return _OWN_LINES[name]
    if name in QUEST_GIVERS:
        from content.verbs import _npc_subject
        return _SHARED.format(name=_npc_subject(w.objects[name]))
    return None


def refuse(w: World, name: str) -> bool:
    """Print the refusal and return True if `name` won't deal with an inked player."""
    line = refusal(w, name)
    if line:
        print(line)
        return True
    return False


def player_action(w: World) -> int:
    """First in the PERFORM chain: the refusing NPCs, and Will's disdain."""
    if not inked(w) or w.prsa not in _GATED and w.prsa != "V-READ":
        return M_NOT_HANDLED
    for obj in (w.prso, w.prsi):
        if obj is None:
            continue
        if w.prsa in _GATED and refuse(w, obj.name):
            return M_HANDLED
    return M_HANDLED if _will_disdain(w) else M_NOT_HANDLED


def _will_disdain(w: World) -> bool:
    """TALK TO WILL: the line, every time (True — that's the whole turn).
    Anything else with him (GIVE, READ a spell scroll in his presence): the
    line once, then it goes ahead (False)."""
    names = {o.name for o in (w.prso, w.prsi) if o is not None}
    if w.prsa in ("V-TALK", "V-HELLO") and "WILL" in names:
        print(_WILL)
        return True
    if w.get_global("WILL-DISDAIN-SHOWN"):
        return False
    from content import will
    teaching = w.prsa == "V-READ" and w.prso is not None \
        and w.prso.name in will.SPELL_SCROLLS and will._will_present(w) \
        and w.globals.get("player_class") != "mage"   # a Mage reads it alone
    if (w.prsa == "V-GIVE" and "WILL" in names) or teaching:
        print(_WILL)
        w.set_global("WILL-DISDAIN-SHOWN", True)
    return False


def cleaned(w: World) -> None:
    """The bath: ink gone, Will's line can show again if inked again."""
    w.set_global("INKED", False)
    w.set_global("WILL-DISDAIN-SHOWN", False)
