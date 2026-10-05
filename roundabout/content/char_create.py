"""
Character creation / opening sequence for Roundabout: The God-Forsaken Ring.

run_opening(world, game) is called by the White House mailbox action.
Text is from AWT_story_line/npcs.md — Will Passion: Opening scene and
Tower visit sequence. Will does not hand over the ring; Pyronicus has it.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.world import World
    from engine.game import Game


_CLASSES = {
    "warrior": {"hearts": 6, "skill": "melee"},
    "mage":    {"hearts": 4, "skill": "spell"},
    "rogue":   {"hearts": 5, "skill": "bow"},
}

_OPENING_TEXT = """\
Will appears without ceremony, straightening his cuffs as though he merely\
 stepped from one room to another.

"You opened the mailbox," he says. "I wasn't entirely certain you would."

He studies you for a moment.

"I have a small errand for you. It involves a town called Roundabout, an\
 object that has a habit of ending up where it doesn't belong, and someone who\
 is holding it quite innocently and will give it up without a fuss."

He pauses. "The object itself is another matter."
"""

_DECLINE_TEXT = """\
Will pauses. "No," he repeats, tasting the word. "Interesting." He waves a\
 hand, not unkindly. "Off you go, then." And he is gone. The field is quiet.\
 The mailbox stands closed in the morning light, as though it never opened.\
 As though none of this happened.

*** GAME OVER ***"""

_ACCEPT_TEXT = """\
Will straightens to his full height. Something changes in the air — a\
 pressure, a stillness, the sense of a page turning. "Then we begin," he says.\
 The field vanishes. The tower arrives around you like a cloak settling onto\
 broad shoulders.
"""

_CLASS_PROMPT_TEXT = """\
"I have read destinies in the lines of a man's palm, in the pattern of stars,\
 in the way smoke rises from a candle. And yet here you stand, entirely\
 unreadable." He sighs. "Just tell me — Warrior, Mage, or Rogue?\""""

_CLASS_RESPONSE = {
    "warrior": (
        '"A Warrior. Yes. I can see it now, actually." He seems mildly '
        'embarrassed to have missed it. "Good. You\'ll need that in you '
        'before this is done."'
    ),
    "mage": (
        '"A Mage. Yes — I almost had it." He says this as though he\'s been '
        'working on a puzzle and just found the missing piece. "Good. You\'ll '
        'see things others miss. Pay attention to that instinct."'
    ),
    "rogue": (
        '"A Rogue. Yes." He seems to find this amusing in a quiet way. "You '
        'know, I should have seen that. Something about the way you looked at '
        'the door when you came in." He shakes his head. "Pay attention to '
        'everything. You already know how. Just keep doing it."'
    ),
}

_BRIEFING_TEXT = """\
"There is a ring in Roundabout. It belongs to no one and everyone, depending\
 on how you look at it — which is part of the problem."

He stands and moves to the window.

"It fell through the roof of a man named Pyronicus. He's holding it in good\
 faith, completely unaware of what it is. He'll give it up without a fight."

He turns back.

"I need you to retrieve it. Bring it to me, or keep it close — but understand\
 this: the ring is useful. It is also patient. And patient things have a way\
 of getting what they want eventually."
"""

_ZENNI_TEXT = """\
Almost as an afterthought, Will pulls a small pouch from somewhere in his\
 robes and holds it out. "Here," he says. "Ten Zenni. Don't spend it all on\
 drinks."
"""

_SENDOFF_TEXT = """\
"When you're ready," Will says, settling back into his chair, "Roundabout\
 awaits." He picks up his pen. The conversation, it seems, is over.
"""


_PAUSE_CUE = "[Press ENTER to continue] "


def _pause() -> None:
    """One of the opening's two stops (npcs.md — Will Passion, Pauses)."""
    input(_PAUSE_CUE)


def _prompt_adventure() -> bool:
    while True:
        answer = input('"Are you up for an adventure?" (yes/no) ').strip().lower()
        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False
        print("Please answer yes or no.")


def _prompt_class() -> str:
    print(_CLASS_PROMPT_TEXT)
    while True:
        choice = input("Your choice (warrior/mage/rogue): ").strip().lower()
        if choice in _CLASSES:
            return choice
        print("Please choose warrior, mage, or rogue.")


def _prompt_name() -> str:
    return input('"And your name?" ').strip()


def run_opening(world: World, game: Game) -> None:
    """Fire the full opening sequence. Called once when player opens the mailbox."""
    # Step 0 — West of House: Will appears and asks
    print(_OPENING_TEXT)
    if not _prompt_adventure():
        print(_DECLINE_TEXT)
        world.set_global("GAME-OVER", True)
        game.quit()
        return

    print(_ACCEPT_TEXT)
    _pause()                      # stop 1: before the tower appears

    # Step 1 — Player arrives: tower first impression
    tower = world.rooms.get("WIZARDS-TOWER")
    if tower is not None:
        game.enter_room(tower)

    # Step 2 — Class selection
    choice = _prompt_class()
    cls = _CLASSES[choice]
    print(_CLASS_RESPONSE[choice])
    print(f"\nYou have chosen: {choice.capitalize()}")
    print(f"Hearts: {cls['hearts']}  Starting skill: {cls['skill']}")
    print()

    # Step 3 — Name entry
    name = _prompt_name() or "Adventurer"

    player = world.player
    if player is not None:
        player.desc = name
        g = world.globals
        g["player_name"]  = name
        g["player_class"] = choice
        g["hearts"]       = cls["hearts"]
        g["max_hearts"]   = cls["hearts"]
        g[f"skill_{cls['skill']}"] = True

    print(f"\nWelcome, {name}.\n")

    # Step 4 — Ring quest briefing (no ring handed over; Pyronicus has it)
    print(_BRIEFING_TEXT)
    _pause()                      # stop 2: after the briefing

    # Step 5 — Zenni handoff
    print(_ZENNI_TEXT)
    world.globals["zenni"] = world.globals.get("zenni", 0) + 10

    # Step 6 — Send-off, straight into the game's > prompt. Step 7 (trailing
    # warning) and step 8 (transition) fire on the first EXAMINE PAINTING —
    # see verbs.v_examine.
    print(_SENDOFF_TEXT.rstrip("\n"))
