"""
Combat resolution for Roundabout: The God-Forsaken Ring.

Sourced from AWT_story_line/mechanics.md — Combat section.
"""

from __future__ import annotations

import random
from typing import TYPE_CHECKING

from content.player import roll, roll_bonus
from content.experience import award_xp, get_level

if TYPE_CHECKING:
    from engine.world import World

# Melee weapon bonus by object name
_WEAPON_BONUS: dict[str, int] = {
    "dagger":     2,
    "mace":       4,
    "battle-axe": 6,
}

# Enemy stats: (dice_num, die_sides, hearts, xp_reward)
_ENEMY_STATS: dict[str, tuple[int, int, int, int]] = {
    "mugger":    (1, 6,  2,  5),
    "aylora":    (2, 6,  3,  2),
    "apprentice":(2, 8,  3,  8),
    "warden":    (2, 10, 5, 12),
    "werewolf":  (3, 10, 0, 15),  # hearts=0: cannot be harmed conventionally
}

# Combat result constants
WIN    = "win"
LOSE   = "lose"
TIE    = "tie"
FLEE   = "flee"
DEAD   = "dead"


def _enemy_roll(dice_num: int, die_sides: int) -> int:
    return sum(random.randint(1, die_sides) for _ in range(dice_num))


def resolve_round(
    world: "World",
    enemy_key: str,
    weapon: str = "melee",
    is_first_round: bool = False,
) -> str:
    """
    Resolve one combat round. Returns WIN/LOSE/TIE.
    Updates world.globals["hearts"] on player damage.
    Enemies' hearts are tracked in world.globals["enemy_hearts"].
    """
    g = world.globals
    dice_num, die_sides, _, _ = _ENEMY_STATS.get(enemy_key, (1, 6, 2, 0))

    # Player roll
    if weapon == "fireball":
        player_result = 999  # guaranteed win this round
    elif weapon == "bow" and is_first_round:
        player_result = roll_bonus(world, 5)
    else:
        bonus = _WEAPON_BONUS.get(weapon, 0)
        player_result = roll_bonus(world, bonus) if bonus else roll(world)

    # Finishing Move (Level 8): all 3d20 ≥ 15
    if get_level(world) >= 8 and g.get("finishing_move_available"):
        if _check_finishing_move(world):
            _finishing_move_narrative(world)
            return WIN

    enemy_result = _enemy_roll(dice_num, die_sides)

    if player_result > enemy_result:
        # Player deals 1 heart to enemy
        enemy_hp = g.get("enemy_hearts", _ENEMY_STATS.get(enemy_key, (0, 0, 2, 0))[2])
        g["enemy_hearts"] = max(0, enemy_hp - 1)
        return WIN
    elif enemy_result > player_result:
        # Enemy deals 1 heart to player (tunic may negate)
        _take_damage(world, 1)
        return LOSE
    else:
        # Tie: both take 1 heart
        enemy_hp = g.get("enemy_hearts", _ENEMY_STATS.get(enemy_key, (0, 0, 2, 0))[2])
        g["enemy_hearts"] = max(0, enemy_hp - 1)
        _take_damage(world, 1)
        return TIE


def _take_damage(world: "World", amount: int) -> None:
    """Deal damage to player, checking tunic avoidance and Nobu's Favor."""
    g = world.globals

    # Ivanaar's Tunic: 40% chance to negate damage (1d10 ≥ 7)
    if g.get("ivaanars_tunic_worn"):
        roll_val = random.randint(1, 10)
        if roll_val >= 7:
            _tunic_message(world)
            return

    g["hearts"] = g.get("hearts", 1) - amount

    if g["hearts"] <= 0:
        _handle_death(world)


def _tunic_message(world: "World") -> None:
    import random
    msgs = [
        "The threads along the hem pulse faintly. Whatever just happened, the tunic had something to do with it.",
        "For a moment the fabric stiffens — then relaxes, as if it exhaled. The blow that should have landed didn't.",
        "The runes along the collar catch the light briefly. You are less hurt than you expected to be.",
        "Something in the weave absorbed it. You felt the impact — and then didn't.",
    ]
    print(random.choice(msgs))


def _handle_death(world: "World") -> None:
    g = world.globals

    # Nobu's Favor: silent death intercept (once per game, Level 7+)
    if g.get("nobus_favor_available") and not g.get("nobus_favor_used"):
        g["nobus_favor_used"] = True
        g["nobus_favor_available"] = False
        g["hearts"] = 1
        print(
            "The world goes dark. Not the dungeon dark — something older than that. Quieter.\n\n"
            "You are somewhere else.\n\n"
            "A voice, close and unhurried, as if it has all the time there is: \"But did you die?\"\n\n"
            "The Main Room of the Tale and Ale materializes around you. The fire is going. "
            "Someone left a drink on the table. The chair nearest the hearth looks like it was made for exactly this moment.\n\n"
            "You are alive. You are not sure how. You are quite sure you could use a rest."
        )
        tavern = world.rooms.get("TALE-AND-ALE")
        if tavern:
            world.move_object(world.winner, tavern)
            world.here = tavern
            world.game.describe_room()
        return

    world.game.jigs_up("You have run out of hearts.")


def _check_finishing_move(world: "World") -> bool:
    """Level 8: all 3d20 ≥ 15 (~2.7% chance)."""
    rolls = [random.randint(1, 20) for _ in range(3)]
    return all(r >= 15 for r in rolls)


def _finishing_move_narrative(world: "World") -> None:
    print(
        '"Finish him."\n'
        "The voice is not yours. It doesn't need to be.\n"
        "You already knew how this was going to end. The voice just said it out loud.\n"
        "Your body is already moving."
    )


def init_enemy(world: "World", enemy_key: str) -> None:
    """Set up enemy hearts for a new combat encounter."""
    _, _, hearts, _ = _ENEMY_STATS.get(enemy_key, (1, 6, 2, 0))
    world.globals["enemy_hearts"] = hearts
    world.globals["current_enemy"] = enemy_key


def enemy_dead(world: "World") -> bool:
    return world.globals.get("enemy_hearts", 1) <= 0


def award_combat_xp(world: "World", enemy_key: str, kill: bool = True) -> None:
    """
    Award XP on enemy defeat (experience.md — Combat). Warriors get +10 per
    combat kill (experience.md — Class XP Adjustments); kill=False for
    defeats that aren't kills (Aylora passes out).
    """
    _, _, _, xp = _ENEMY_STATS.get(enemy_key, (0, 0, 0, 0))
    if kill and world.globals.get("player_class") == "warrior":
        xp += 10
    award_xp(world, xp)
