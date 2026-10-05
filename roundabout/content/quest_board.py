"""
The Quest Board in the Bar of the Tale and Ale.

Design: mechanics.md (Quest Board — postings, rules, board text), quests.md
(Quest Board Cascade), locations.md (Bar).

- LOOK AT / READ / EXAMINE BOARD lists the notices still up, in the order
  they were posted; completed quests are left off.
- Reading the board discovers every quest it shows. Posting alone doesn't.
- Posted at game start: 22, 50. First Kitchen visit: 40. Will's second
  briefing: 17. Town charter received: 24. Timed (worked out when the board is
  read): 7, 20 turns after the ring hand-over; 51, at 100 turns while the
  mugger lives.
- Quest 50's notice comes down for good when Trap 41 is disarmed.

State: BOARD-POSTED {quest_id: move posted}, BOARD-REMOVED [quest_id],
       PYRONICUS-MET-AT (world.moves at the ring hand-over)
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED

if TYPE_CHECKING:
    from engine.world import World, Room

_HEADER = "Notices are pinned to the board, newer ones over older:"
_EMPTY = ("The board holds nothing but pinholes and the corners of notices long "
          "since torn away.")

POSTINGS = {
    "22": ("WANTED: someone to mend the old aqueduct beneath the town. The fountain's "
           "been dry for years. Drinks will be cheaper for it. — May"),
    "50": ("MISSING: a young man, last seen heading toward the dungeon. He may not be "
           "himself. If you find him, bring him out. Please."),
    "40": ("WANTED: bog thyme, and a cooking pot that isn't cracked. Bring both to the "
           "kitchen. There's a stew in it. — Shamus"),
    "7": ("WANTED: a bone flute, somewhere in the middle passages below. Bring it to "
          "the forge beneath the volcano. — Pyronicus"),
    "17": ("MISSING: a relative of mine went into the Chuckle House some years ago and "
           "never came out. If he lives, tell him to come home. If he doesn't, I would "
           "like his pocket watch. — Records Room, Town Hall"),
    "24": ("SWARM LOOSE: my bees have taken up in a hollow tree at the forest edge. "
           "Help wanted bringing the queen home. Honey for your trouble. — the cottage "
           "west of the Old Oak"),
    "51": ("BOUNTY: someone's been robbing people in the back alley. Whoever puts a "
           "stop to it drinks free. — May"),
}

FLUTE_DELAY = 20      # Quest 7: turns after the ring hand-over
BOUNTY_TURN = 100     # Quest 51


def _posted(w: World) -> dict:
    return w.globals.setdefault("BOARD-POSTED", {})


def post(w: World, quest_id: str, at: int | None = None) -> None:
    """Put a notice up (once). `at` is the move it went up; default now."""
    posted = _posted(w)
    if quest_id in posted or quest_id in w.globals.get("BOARD-REMOVED", []):
        return
    posted[quest_id] = w.moves if at is None else at


def remove(w: World, quest_id: str) -> None:
    """Take a notice down for good."""
    removed = w.globals.setdefault("BOARD-REMOVED", [])
    if quest_id not in removed:
        removed.append(quest_id)


def met_pyronicus(w: World) -> None:
    """The ring hand-over: the bone flute notice goes up 20 turns later."""
    if w.get_global("PYRONICUS-MET-AT") is None:
        w.set_global("PYRONICUS-MET-AT", w.moves)


def _post_timed(w: World) -> None:
    met = w.get_global("PYRONICUS-MET-AT")
    if met is not None and w.moves >= met + FLUTE_DELAY:
        post(w, "7", at=met + FLUTE_DELAY)
    if w.moves >= BOUNTY_TURN and not w.get_global("MUGGER-DEAD"):
        post(w, "51", at=BOUNTY_TURN)


def notices(w: World) -> list[str]:
    """Quest IDs on the board now, oldest first."""
    from content import quests
    _post_timed(w)
    removed = w.globals.get("BOARD-REMOVED", [])
    posted = _posted(w)
    return [q for q in sorted(posted, key=lambda q: posted[q])
            if q not in removed and not quests.is_complete(w, q)]


def read(w: World) -> None:
    from content import quests
    shown = notices(w)
    if not shown:
        print(_EMPTY)
        return
    print(_HEADER)
    for q in shown:
        print(POSTINGS[q])
        quests.discover(w, q)


def board_action(w: World) -> int:
    if w.prsa in ("V-EXAMINE", "V-READ", "V-LOOK-INSIDE"):
        read(w)
        return M_HANDLED
    return M_NOT_HANDLED


def on_enter(w: World, room: Room) -> None:
    """Enter hook: Shamus's notice goes up on the first Kitchen visit."""
    if room.name == "KITCHEN":
        post(w, "40")


def setup(w: World) -> None:
    """Game start: the aqueduct and Will's anonymous notice."""
    post(w, "22")
    post(w, "50")
    w.objects["QUEST-BOARD"].action = board_action
