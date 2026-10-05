"""
Game-logic actions for Roundabout: The God-Forsaken Ring.

Contains: combat loop, altar ritual, Cargo dice game, and other complex
multi-step logic. May's hints: content/may_hints.py.

Called from verbs.py and room action handlers.
"""

from __future__ import annotations

import random
from typing import TYPE_CHECKING

from engine.game import M_HANDLED, M_NOT_HANDLED

if TYPE_CHECKING:
    from engine.world import World, GameObject


# ---------------------------------------------------------------------------
# Combat loop
# ---------------------------------------------------------------------------

def start_combat(world: "World", npc: "GameObject", weapon: str = "melee") -> int:
    """
    Begin (or continue) combat with an NPC.
    Returns M_HANDLED in all cases.
    """
    from content.combat import (
        resolve_round, init_enemy, enemy_dead, award_combat_xp, WIN, LOSE, TIE,
    )
    from content.experience import award_xp

    npc_key = npc.name
    g = world.globals

    # Werewolf: conventional weapons useless
    if npc_key == "werewolf" and weapon not in ("fireball",):
        print(
            "You attack the werewolf. The blow connects -- and the werewolf reassembles "
            "around it as if you'd thrown water at a fog. It doesn't even flinch.\n"
            "You'll need something consecrated for this."
        )
        return M_HANDLED

    # Fresh combat: initialize enemy
    if g.get("current_enemy") != npc_key:
        init_enemy(world, npc_key)

    # Round narration
    is_first = g.get(f"combat_rounds_{npc_key}", 0) == 0
    g[f"combat_rounds_{npc_key}"] = g.get(f"combat_rounds_{npc_key}", 0) + 1

    result = resolve_round(world, npc_key, weapon, is_first_round=is_first)

    # Fireball cooldown
    if weapon == "fireball":
        g["fireball_cooldown"] = 10

    # Print round result
    _combat_narrate(world, result, npc_key, weapon)

    # Check enemy death
    if enemy_dead(world):
        _enemy_defeated(world, npc_key)
        return M_HANDLED

    # Check player death (handled inside _take_damage → jigs_up, but if still alive here)
    if g.get("hearts", 1) <= 0:
        return M_HANDLED  # jigs_up was already called

    return M_HANDLED


def _combat_narrate(world: "World", result: str, npc_key: str, weapon: str) -> None:
    from content.combat import WIN, LOSE, TIE

    npc_name = _npc_display_name(npc_key)

    if weapon == "fireball":
        print(f"The fireball engulfs {npc_name}. It recoils, badly scorched.")
        return

    win_msgs = [
        f"Your attack connects. {npc_name} staggers.",
        f"You land a solid blow on {npc_name}.",
        f"A clean hit. {npc_name} is hurt.",
    ]
    lose_msgs = [
        f"{npc_name} strikes back. You take a hit.",
        f"You move too slowly. {npc_name} gets through your guard.",
        f"{npc_name} lands a blow. You wince.",
    ]
    tie_msgs = [
        f"You trade blows with {npc_name}. Both of you take damage.",
        f"A messy exchange. You both suffer for it.",
    ]

    if result == WIN:
        print(random.choice(win_msgs))
    elif result == LOSE:
        print(random.choice(lose_msgs))
    else:
        print(random.choice(tie_msgs))


def _enemy_defeated(world: "World", npc_key: str) -> None:
    from content.combat import award_combat_xp

    award_combat_xp(world, npc_key)
    world.globals.pop("current_enemy", None)
    world.globals.pop(f"combat_rounds_{npc_key}", None)
    world.globals[f"hostile_{npc_key}"] = False

    npc_name = _npc_display_name(npc_key)

    defeat_msgs = {
        "mugger": (
            f"The mugger goes down. They don't get up. "
            f"You catch your breath. The alley is quiet again."
        ),
        "aylora": (
            "The aylora falls. Its glow fades as it does, "
            "leaving nothing but a cooling patch of darkness."
        ),
        "apprentice": (
            "The apprentice collapses. The grimoire hits the floor beside them. "
            "The silence that follows is immediate and complete."
        ),
        "warden": (
            "The warden stumbles and falls. Whatever animated it is gone. "
            "The armor rattles once, then settles."
        ),
    }

    print(defeat_msgs.get(npc_key, f"{npc_name} is defeated."))

    # Move defeated NPC out of room
    npc_obj = world.objects.get(npc_key)
    if npc_obj:
        world.move_object(npc_obj, None)


def _npc_display_name(npc_key: str) -> str:
    names = {
        "mugger":     "the mugger",
        "aylora":     "the aylora",
        "apprentice": "the dark apprentice",
        "warden":     "the warden",
        "werewolf":   "the werewolf",
    }
    return names.get(npc_key, npc_key.replace("-", " "))


# ---------------------------------------------------------------------------
# Altar ritual
# ---------------------------------------------------------------------------

def altar_ritual(world: "World", dial_setting: str) -> int:
    """
    Place ring on Church of All altar for binding ritual.
    Called from V-PUT-ON when target is altar.
    """
    g = world.globals

    ring = world.objects.get("ring")
    if not ring or ring.location is not world.player:
        print("You don't have the ring.")
        return M_HANDLED

    if not g.get("blessing_complete"):
        print(
            "The altar sits inert. "
            "Something is missing -- a proper blessing, perhaps, "
            "or the right words spoken at the right moment."
        )
        return M_HANDLED

    # Check correct religious alignment for binding
    required_dial = g.get("required_ritual_dial", "the-unnamed")
    if dial_setting != required_dial:
        print(
            "You set the ring on the altar stone. "
            f"The dial reads {dial_setting.replace('-', ' ').title()}. "
            "The ring rests there, patient, unimpressed. Nothing happens."
        )
        return M_HANDLED

    # Execute binding ritual
    _execute_binding(world)
    return M_HANDLED


def _execute_binding(world: "World") -> None:
    g = world.globals
    ring = world.objects.get("ring")

    print(
        "You place the ring on the altar stone.\n\n"
        "The dial clicks. A sound not quite sound fills the space -- "
        "the way air fills a room when a door is opened from outside.\n\n"
        "The ring does not move. But something that was in it is gone.\n\n"
        "You reach out and take it back. It is lighter than it was. "
        "Not in weight. In the other way.\n\n"
        "May was right. The God-Forsaken Ring is God-Forsaken once more."
    )

    g["ring_bound"] = True
    g["ring_worn"] = False

    # Disable corruption clock permanently
    event = world.game.clock.get("ring-corruption-clock")
    if event:
        event.enabled = False

    # Trophy: place bound ring in player inventory (no further corruption ticks)
    if ring:
        world.move_object(ring, world.player)

    from content.quests import complete
    complete(world, "49", xp_override=17)  # The Ruined Shrine -- binding quest


def altar_pray(world: "World", dial_setting: str) -> int:
    """PRAY at altar -- may grant blessing required for binding ritual."""
    g = world.globals
    here = world.here.name if world.here else ""

    if here != "the-altar":
        return M_HANDLED

    if g.get("altar_blessing_prayer_used"):
        print("You have already offered the prayer. The altar has heard you.")
        return M_HANDLED

    # Check: blessing scroll in hand
    scroll = world.objects.get("blessing-scroll")
    if not scroll or scroll.location is not world.player:
        print(
            "You bow your head. The altar is attentive in the way a locked door is attentive. "
            "There may be words that open this, but you don't know them yet."
        )
        return M_HANDLED

    g["altar_blessing_prayer_used"] = True
    g["blessing_complete"] = True

    from content.quests import discover
    discover(world, "49")

    print(
        "You read from the blessing scroll. The words are not difficult -- they are, in fact, "
        "suspiciously simple, like directions to a place everyone already knows how to get to.\n\n"
        "The altar pulses once. The scroll crumbles. "
        "You feel something settle into place, the way a key feels in a lock that was "
        "designed for it specifically.\n\n"
        "The altar is ready."
    )

    return M_HANDLED


# ---------------------------------------------------------------------------
# Ty's Cargo dice game
# ---------------------------------------------------------------------------
#
# Rules (from reference-cargo-game.md):
# Player rolls 5d6. After each roll, may keep any dice and re-roll the rest
# (up to 2 re-rolls total).
# Winning hand in descending order of value:
#   Ship (6) + Captain (5) + Crew (4) = 15+ remaining = win
#   Otherwise house wins.
# Bet: 1-5 Zenni. Win pays 2x bet.
#
# ---------------------------------------------------------------------------

def play_cargo(world: "World") -> int:
    g = world.globals

    if not g.get("ty_met"):
        print("Ty watches you approach. \"You want to play, talk to me first.\"")
        return M_HANDLED

    # Get bet amount
    bet = g.pop("cargo_bet", None)
    if bet is None:
        bet_obj = getattr(world, "prso", None)
        if bet_obj is not None:
            try:
                bet = int(bet_obj.value)
            except (ValueError, TypeError, AttributeError):
                bet = None
        if bet is None:
            print("Ty looks up. \"How much are you betting? One to five Zenni.\"")
            return M_HANDLED

    bet = max(1, min(5, int(bet)))

    if g.get("zenni", 0) < bet:
        print("Ty shakes his head slowly. \"You don't have it.\"")
        return M_HANDLED

    print(f"\nTy sweeps the table clear. You put up {bet} Zenni.\n")

    # Initial roll: 5d6
    dice = [random.randint(1, 6) for _ in range(5)]
    _show_dice(dice, roll_num=1)

    kept = []
    # Auto-keep ship/captain/crew as they're found
    dice, kept = _auto_keep(dice, kept)

    if len(kept) < 3:
        # Re-roll 1
        remaining = [d for d in dice if d not in kept]
        new_roll = [random.randint(1, 6) for _ in range(len(remaining))]
        dice = kept + new_roll
        _show_dice(dice, roll_num=2)
        dice, kept = _auto_keep(dice, kept)

    if len(kept) < 3:
        # Re-roll 2
        remaining = [d for d in dice if d not in kept]
        new_roll = [random.randint(1, 6) for _ in range(len(remaining))]
        dice = kept + new_roll
        _show_dice(dice, roll_num=3)
        dice, kept = _auto_keep(dice, kept)

    # Evaluate
    has_ship    = 6 in kept
    has_captain = 5 in kept
    has_crew    = 4 in kept

    if has_ship and has_captain and has_crew:
        cargo_dice = [d for d in dice if d not in [6, 5, 4]]
        cargo_total = sum(cargo_dice)
        if cargo_total >= 15:
            # Win
            g["zenni"] = g.get("zenni", 0) + bet
            print(
                f"Ship. Captain. Crew. Cargo sums to {cargo_total}.\n"
                f"Ty counts out {bet} Zenni and slides them across without ceremony. \"Well played.\""
            )
        else:
            # Have the hand but cargo too low
            g["zenni"] = g.get("zenni", 0) - bet
            print(
                f"Ship. Captain. Crew -- but cargo only totals {cargo_total}. Needs fifteen.\n"
                "Ty sweeps the Zenni off the table. \"Close.\""
            )
    else:
        missing = []
        if not has_ship:    missing.append("ship (6)")
        if not has_captain: missing.append("captain (5)")
        if not has_crew:    missing.append("crew (4)")
        g["zenni"] = g.get("zenni", 0) - bet
        print(
            f"No {'or '.join(missing)}.\n"
            "Ty collects the Zenni. \"Better luck next roll.\""
        )

    return M_HANDLED


def _show_dice(dice: list[int], roll_num: int) -> None:
    sorted_d = sorted(dice, reverse=True)
    print(f"Roll {roll_num}: [{', '.join(str(d) for d in sorted_d)}]")


def _auto_keep(dice: list[int], kept: list[int]) -> tuple[list[int], list[int]]:
    """Keep 6 (ship) then 5 (captain) then 4 (crew) if not already kept."""
    for value, label in [(6, "Ship"), (5, "Captain"), (4, "Crew")]:
        if value not in kept and value in dice:
            kept.append(value)
            dice = [d for d in dice if d != value or d in kept]
            print(f"  Keeping {label} ({value}).")
    return dice, kept


# ---------------------------------------------------------------------------
# Cooldown tick -- called from main game clock each turn
# ---------------------------------------------------------------------------

def tick_cooldowns(world: "World") -> bool:
    """Decrement spell and rest cooldowns each turn. Returns False (always)."""
    g = world.globals
    for key in ("fireball_cooldown", "unbind_cooldown", "light_spell_cooldown", "rest_cooldown"):
        if g.get(key, 0) > 0:
            g[key] -= 1

    # Light spell active turns
    if g.get("light_spell_active_turns", 0) > 0:
        g["light_spell_active_turns"] -= 1
        if g["light_spell_active_turns"] == 0:
            g["light_spell_active"] = False
            print("The light spell flickers and fades.")

    return False  # never consume the event
