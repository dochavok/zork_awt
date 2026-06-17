"""
Character creation / opening sequence for Roundabout: The God-Forsaken Ring.

run_opening(world, game) is called by the White House mailbox action.
Places the player in Will's Wizard Tower after class and name selection.
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
A figure appears at the edge of the field — unhurried, as if he’d been\
 there the whole time and you simply hadn’t noticed.

He is tall, older, wearing the kind of clothes that suggest someone who\
 stopped caring about appearances a long time ago and is entirely comfortable\
 with that decision. He carries a staff that looks more like a walking stick\
 that got ideas above its station.

“Ah,” he says. “Good. I was wondering when you’d show up.”

He introduces himself as Will Passion. He has a job for you — a ring needs\
 returning, a wrong needs setting right, and you seem like the sort of person\
 who can manage both without making things significantly worse. Probably.

The mailbox opens. Inside: a letter. It reads: *Are you up for an adventure?*
"""

_BRIEFING_TEXT = """\
Will hands you a ring — plain, dark metal, heavier than it looks.

“Don’t wear it,” he says. Then: “Well. Don’t wear it *much*.\
 There are things it can do that will be useful. There are also things it’ll\
 do to you if you let it. The two facts are related. Be sensible.”

He produces ten Zenni from somewhere and sets them on the desk.

“For expenses. The painting on the wall is the way out. Come back when you’ve\
 finished, or when you need help, or when something has gone interestingly wrong.\
 I’ll be here.”
"""


def _pause() -> None:
    input()


def _prompt_class() -> str:
    print("Choose your class:")
    print("  warrior  — 6 hearts, starts with melee skill")
    print("  mage     — 4 hearts, starts with spell casting")
    print("  rogue    — 5 hearts, starts with bow skill")
    choice = input("Your choice: ").strip().lower()
    return choice


def _prompt_name() -> str:
    return input("What is your name, adventurer? ").strip()


def run_opening(world: World, game: Game) -> None:
    """Fire the full opening sequence. Called once when player opens the mailbox."""
    print(_OPENING_TEXT)
    _pause()

    # Class selection
    while True:
        choice = _prompt_class()
        if choice in _CLASSES:
            break
        print("Please choose warrior, mage, or rogue.")

    cls = _CLASSES[choice]
    print(f"\nYou have chosen: {choice.capitalize()}")
    print(f"Hearts: {cls['hearts']}  Starting skill: {cls['skill']}")
    _pause()

    # Name
    name = _prompt_name()
    if not name:
        name = "Adventurer"

    # Store on player
    player = world.player
    if player is not None:
        player.desc = name
        world.set_global("PLAYER-NAME", name)
        world.set_global("PLAYER-CLASS", choice)
        world.set_global("PLAYER-HEARTS", cls["hearts"])
        world.set_global("PLAYER-HEARTS-MAX", cls["hearts"])
        world.set_global("PLAYER-SKILL", cls["skill"])
        world.set_global("ZENNI", 10)

    print(f"\nWelcome, {name}.")
    _pause()

    # Move player to Tower
    tower = world.rooms.get("WIZARDS-TOWER")
    if tower is not None:
        game.enter_room(tower)

    print(_BRIEFING_TEXT)
    _pause()

    # Give the ring
    ring = world.objects.get("RING")
    if ring is not None and player is not None:
        world.move_object(ring, player)

    _pause()  # sendoff pause
