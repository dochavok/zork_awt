"""
Character creation for Roundabout: The God-Forsaken Ring.

run_opening(world) fires once at game start, before the main loop.
Places the player in Will's Tower and runs steps 1-6. The game then
starts normally with the player still in the tower.

Steps run automatically:
  1. Opening monologue (mailbox)
  2. Class selection (Warrior / Mage / Rogue)
  3. Name entry
  4. Ring quest briefing
  5. Zenni handoff (10 Z)
  6. Send-off (describes painting, player must interact with it)

Steps triggered by player:
  7. Trailing warning (interrupted) -- fires when player examines/enters painting
  8. Transition text -> move to tale-and-ale-main
"""

from __future__ import annotations

import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine.world import World


def run_opening(world: "World") -> None:
    """Run steps 1-6. Player starts in Will's Tower; painting interaction triggers 7-8."""
    g = world.globals

    # Place player in Will's tower for the opening scene
    tower = world.rooms.get("wills-tower-main")
    if tower and world.player:
        world.move_object(world.player, tower)
        world.here = tower

    _step1_mailbox(world)
    _step2_class_selection(world)
    _step3_name_entry(world)
    _step4_ring_briefing(world)
    _step5_zenni_handoff(world)
    _step6_sendoff(world)

    # Apply class starting equipment now so it's ready when the player arrives
    _apply_class_start(world)

    g["opening_complete"] = True
    g["ring_quest_started"] = True
    g["painting_ready"] = True  # Painting interaction now armed


# ---------------------------------------------------------------------------
# Steps
# ---------------------------------------------------------------------------

def _step1_mailbox(world: "World") -> None:
    print(
        "\n\n"
        "Will appears without ceremony, straightening his cuffs as though he merely stepped from one room to another.\n\n"
        "\"You opened the mailbox,\" he says. \"I wasn't entirely certain you would.\"\n\n"
        "He takes you in -- the particular look of a man who has spent years reading people and still occasionally finds one opaque.\n\n"
        "\"Interesting,\" he says, finally.\n\n"
        "There is a great deal happening in that one word."
    )
    _pause()


def _step2_class_selection(world: "World") -> None:
    g = world.globals
    print(
        "\n\"I have read destinies in the lines of a man's palm, in the pattern of stars, "
        "in the way smoke rises from a candle. And yet here you stand, entirely unreadable.\"\n\n"
        "He sighs.\n\n"
        "\"Just tell me -- Warrior, Mage, or Rogue?\"\n\n"
        "  1) Warrior\n"
        "  2) Mage\n"
        "  3) Rogue"
    )

    cls = _prompt_class()
    g["player_class"] = cls

    if cls == "warrior":
        print(
            "\n\"A Warrior. Yes. I can see it now, actually.\"\n\n"
            "He seems mildly embarrassed to have missed it.\n\n"
            "\"Good. You'll need that in you before this is done.\""
        )
        g["max_hearts"] = 6
        g["hearts"] = 6
        g["skill_melee"] = True
    elif cls == "mage":
        print(
            "\n\"A Mage. Yes -- I almost had it.\"\n\n"
            "He says this as though he's been working on a puzzle and just found the missing piece.\n\n"
            "\"Good. You'll see things others miss. Pay attention to that instinct.\""
        )
        g["max_hearts"] = 4
        g["hearts"] = 4
        g["skill_spell"] = True
        g["spell_fireball"] = True
    else:  # rogue
        print(
            "\n\"A Rogue. Yes.\"\n\n"
            "He seems to find this amusing in a quiet way.\n\n"
            "\"You know, I should have seen that. Something about the way you looked at the door when you came in.\"\n\n"
            "He shakes his head.\n\n"
            "\"Pay attention to everything. You already know how. Just keep doing it.\""
        )
        g["max_hearts"] = 5
        g["hearts"] = 5
        g["skill_bow"] = True

    _pause()


def _step3_name_entry(world: "World") -> None:
    g = world.globals
    print("\n\"And your name?\"")
    name = _prompt_name()
    g["player_name"] = name
    if name:
        print(f"\nWill nods once. \"{name}.\"\n\nHe seems to file it away.")
    else:
        print("\nWill nods once, accepting the silence.")
    _pause()


def _step4_ring_briefing(world: "World") -> None:
    print(
        "\n\"There is a ring in Roundabout.\"\n\n"
        "He pauses as though giving that sentence time to settle.\n\n"
        "\"It belongs to no one and everyone, depending on how you look at it -- "
        "which is part of the problem.\"\n\n"
        "He stands and moves to the window.\n\n"
        "\"It fell through the roof of a man named Pyronicus. "
        "He's holding it in good faith, completely unaware of what it is. "
        "He'll give it up without a fight.\"\n\n"
        "He turns back.\n\n"
        "\"I need you to retrieve it. Bring it to me, or keep it close -- "
        "but understand this: the ring is useful. It is also patient. "
        "And patient things have a way of getting what they want eventually.\""
    )
    _pause()


def _step5_zenni_handoff(world: "World") -> None:
    world.globals["zenni"] = world.globals.get("zenni", 0) + 10
    print(
        "\nAlmost as an afterthought, Will pulls a small pouch from somewhere in his robes and holds it out.\n\n"
        "\"Here,\" he says. \"Ten Zenni. Don't spend it all on drinks.\""
    )
    _pause()


def _step6_sendoff(world: "World") -> None:
    name = world.globals.get("player_name", "")
    closer = f"\"{name},\" " if name else ""
    print(
        f"\n{closer}\"When you're ready,\" Will says, settling back into his chair, "
        "\"Roundabout awaits.\"\n\n"
        "He picks up his pen. The conversation, it seems, is over.\n\n"
        "Against the far wall, a large painting shows a tavern from outside -- "
        "warm light through the windows, a painted sign reading TALE AND ALE."
    )
    _pause()


def enter_painting(world: "World") -> bool:
    """
    Called by the verb handler when the player interacts with the painting.
    Returns True if the transition fired, False if the painting isn't ready yet.
    """
    if not world.globals.get("painting_ready"):
        print("It's just a painting.")
        return False

    if world.globals.get("painting_used"):
        print("The painting shows the Tale and Ale, but it's just a painting now.")
        return False

    _step7_trailing_warning(world)
    _step8_transition(world)
    world.globals["painting_used"] = True
    return True


def _step7_trailing_warning(world: "World") -> None:
    print(
        "\nYou move toward the painting.\n\n"
        "\"One more thing,\" Will says, rising from his chair. "
        "\"The ring -- I should have told you, it--\""
    )


def _step8_transition(world: "World") -> None:
    print(
        "\nThe painting is larger than it looked. Or you are smaller.\n\n"
        "The tavern in the frame tilts toward you, and then you are simply there -- "
        "the smell of woodsmoke and ale arriving before anything else does."
    )

    # Move player to tavern
    tavern = world.rooms.get("tale-and-ale-main")
    if tavern and world.player:
        world.move_object(world.player, tavern)
        world.here = tavern

    print()
    # Auto-describe the arrival room
    if world.here and world.here.desc:
        print(world.here.desc)


# ---------------------------------------------------------------------------
# Class starting equipment
# ---------------------------------------------------------------------------

def _apply_class_start(world: "World") -> None:
    """Place class-specific starting item in player inventory."""
    cls = world.globals.get("player_class", "")

    if cls == "warrior":
        pass  # Warriors buy weapons from Shamus; no starting weapon
    elif cls == "mage":
        # Fireball granted via spell_fireball=True; mages start with no extra item
        # but get the spell scroll as a reminder object if present
        pass
    elif cls == "rogue":
        lockpick = world.objects.get("lockpick")
        if lockpick:
            world.move_object(lockpick, world.player)
        bow = world.objects.get("bow")
        if bow:
            world.move_object(bow, world.player)


# ---------------------------------------------------------------------------
# Input helpers
# ---------------------------------------------------------------------------

def _prompt_class() -> str:
    """Block until player gives a valid class choice."""
    _ALIASES = {
        "warrior": "warrior", "1": "warrior", "w": "warrior",
        "fighter": "warrior", "knight": "warrior",
        "mage": "mage", "2": "mage", "m": "mage",
        "wizard": "mage", "sorcerer": "mage", "witch": "mage",
        "rogue": "rogue", "3": "rogue", "r": "rogue",
        "thief": "rogue", "ranger": "rogue", "scout": "rogue",
    }
    while True:
        raw = input("\n> ").strip().lower()
        if raw in _ALIASES:
            return _ALIASES[raw]
        print(
            "\nWill waits. The options haven't changed: Warrior, Mage, or Rogue.\n"
            "  1) Warrior\n"
            "  2) Mage\n"
            "  3) Rogue"
        )


def _prompt_name() -> str:
    """Prompt for a name; blank is accepted (Will accepts silence)."""
    raw = input("\n> ").strip()
    # Strip any parser-style prefix the player might type
    for prefix in ("my name is ", "i am ", "call me ", "name "):
        if raw.lower().startswith(prefix):
            raw = raw[len(prefix):]
    return raw.title() if raw else ""


def _pause() -> None:
    """Brief pause so the player can read before the next beat."""
    input("\n[Press Enter to continue]")
