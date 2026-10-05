"""
Combat rules shared by every fight (mechanics.md — Combat, Gear bonuses).

Each fight (back_alley, combat_room, trap_side, knight, still_den) keeps its own
dice, hearts, lines and ending; this module owns the player's roll, the round,
damage and death.
"""

from __future__ import annotations

import random
from typing import TYPE_CHECKING

from content import player
from content.experience import award_xp, get_level

if TYPE_CHECKING:
    from engine.world import World

# items.md — Dagger, Mace, Battle Axe
WEAPON_BONUS: dict[str, int] = {"DAGGER": 2, "MACE": 4, "BATTLE-AXE": 6}
GLOVES_BONUS = 3          # items.md — Apprentice's Gloves, while worn
BOW_OPENING_BONUS = 5     # mechanics.md — Bow, first round bonus
EQUIPPABLE = (*WEAPON_BONUS, "BOW")

# A bow shot's own hit and tie lines; a miss keeps the fight's line (mechanics.md)
_BOW_WON = "Your arrow finds its mark. The {enemy} staggers."
_BOW_TIE = "You loose an arrow as it closes on you. Both of you feel it."

# experience.md — Combat
_COMBAT_XP: dict[str, int] = {
    "mugger": 5, "aylora": 2, "apprentice": 8, "warden": 12, "werewolf": 15,
}

# Round results
WIN  = "win"      # the player hits
LOSE = "lose"     # the enemy hits
TIE  = "tie"      # both hit

FINISHED = 99     # enemy hearts lost to the Finishing Move
# Finishing Move odds: all 3d20 at 15+ is (6/20)^3 = 216 in 8000. Checked as one
# roll <= 216 so the always-max test dice never trigger it.
_FINISH_ODDS = (216, 8000)
_FINISH_LINES = (
    '"Finish him."\n'
    "The voice is not yours. It doesn't need to be.\n"
    "You already knew how this was going to end. The voice just said it out loud.\n"
    "Your body is already moving."
)


# ---------------------------------------------------------------------------
# The player's roll
# ---------------------------------------------------------------------------

def _carried(w: "World", obj) -> bool:
    return obj is not None and w.player is not None and obj in w.player.contents


def can_use_weapons(w: "World") -> bool:
    """Weapon Use: Warriors always; Mages and Rogues once Quest 54 is done."""
    return w.globals.get("player_class") == "warrior" or bool(w.globals.get("skill_melee"))


def equipped(w: "World"):
    """The equipped weapon or bow, if the player still has it."""
    name = w.globals.get("EQUIPPED")
    obj = w.objects.get(name) if name else None
    return obj if _carried(w, obj) else None


def equip(w: "World", obj) -> bool:
    """EQUIP X (mechanics.md — Equipping weapons). Prints the line; True if obj
    is equipped afterwards."""
    if obj.name not in EQUIPPABLE:
        print(f"You can't equip the {obj.desc}.")
        return False
    if obj.name in WEAPON_BONUS and not can_use_weapons(w):
        print(f"You don't know how to fight with the {obj.desc}. "
              "The knight in the square teaches that.")
        return False
    current = equipped(w)
    if current is obj:
        print(f"You're already holding the {obj.desc}.")
        return True
    if current is not None:
        print(f"You put away the {current.desc} and take up the {obj.desc}.")
    else:
        print(f"You take up the {obj.desc}.")
    w.globals["EQUIPPED"] = obj.name
    return True


def unequip(w: "World", obj) -> None:
    if equipped(w) is not obj:
        print(f"You aren't holding the {obj.desc}.")
        return
    w.globals["EQUIPPED"] = None
    print(f"You put away the {obj.desc}.")


def weapon_bonus(w: "World") -> int:
    """The equipped melee weapon's bonus. Nothing without Weapon Use
    (Warriors; Mages/Rogues after Quest 54)."""
    obj = equipped(w)
    if obj is None or not can_use_weapons(w):
        return 0
    return WEAPON_BONUS.get(obj.name, 0)


def gloves_bonus(w: "World") -> int:
    gloves = w.objects.get("APPRENTICE-GLOVES")
    return GLOVES_BONUS if _carried(w, gloves) and gloves.has_flag("WEARBIT") else 0


def player_roll(w: "World", *, shot: bool = False, opening: bool = False) -> int:
    """Melee: level dice + equipped weapon + gloves. A bow shot: level dice +
    5 on the fight's opening round + gloves."""
    if shot:
        return player.roll(w) + (BOW_OPENING_BONUS if opening else 0) + gloves_bonus(w)
    return player.roll(w) + weapon_bonus(w) + gloves_bonus(w)


def _enemy_roll(dice: tuple[int, int]) -> int:
    return sum(random.randint(1, dice[1]) for _ in range(dice[0]))


# ---------------------------------------------------------------------------
# A round
# ---------------------------------------------------------------------------

def fight_round(w: "World", dice: tuple[int, int], won: str, lost: str, tie: str,
                *, lethal: bool = True, finishing: bool = True) -> int:
    """One round: higher roll hits for 1 heart; ties hit both. Prints the
    fight's line, applies the player's damage, and returns the hearts the enemy
    loses (0, 1, or FINISHED). lethal=False: the player's hearts can reach 0
    without death (the mugger handles that himself). finishing=False: no
    Finishing Move (the knight's trial)."""
    opening = not w.globals.get("FIGHT-OPENED")
    w.globals["FIGHT-OPENED"] = True
    if finishing and _finishing_move(w):
        return FINISHED
    shot = w.prsa == "V-SHOOT"
    if shot and w.prso is not None:
        won, tie = _BOW_WON.format(enemy=w.prso.desc), _BOW_TIE
    mine = player_roll(w, shot=shot, opening=opening)
    theirs = _enemy_roll(dice)
    if mine > theirs:
        print(won)
        return 1
    if theirs > mine:
        print(lost)
        take_damage(w, 1, lethal=lethal)
        return 0
    print(tie)
    take_damage(w, 1, lethal=lethal)
    return 1


def on_enter(w: "World", room) -> None:
    """Enter hook: every fight resets when the player comes back into its room,
    so the next round is a fight's opening round (the bow's +5)."""
    w.globals["FIGHT-OPENED"] = False


def _finishing_move(w: "World") -> bool:
    """Level 8, secret and silent: ~2.7% per round, the enemy falls at once
    (mechanics.md — Finishing Move)."""
    if get_level(w) < 8 or random.randint(1, _FINISH_ODDS[1]) > _FINISH_ODDS[0]:
        return False
    print(_FINISH_LINES)
    return True


def defend(w: "World", dice: tuple[int, int], hit: str) -> None:
    """An enemy that can't be hurt this way (the werewolf): the roll, with every
    bonus, only decides whether its blow lands."""
    if _enemy_roll(dice) > player_roll(w):
        print(hit)
        take_damage(w, 1)


# ---------------------------------------------------------------------------
# Damage and death
# ---------------------------------------------------------------------------

_TUNIC_LINES = (
    "The threads along the hem pulse faintly. Whatever just happened, the tunic had something to do with it.",
    "For a moment the fabric stiffens — then relaxes, as if it exhaled. The blow that should have landed didn't.",
    "The runes along the collar catch the light briefly. You are less hurt than you expected to be.",
    "Something in the weave absorbed it. You felt the impact — and then didn't.",
)


def take_damage(w: "World", amount: int, *, lethal: bool = True) -> None:
    """The player is hit: Ivanaar's Tunic may turn it (1d10 7+, while worn);
    otherwise hearts drop, and at 0 the player dies (Nobu's Favor may intercept)."""
    tunic = w.objects.get("IVANAAR-TUNIC")
    if _carried(w, tunic) and tunic.has_flag("WEARBIT") and random.randint(1, 10) >= 7:
        print(random.choice(_TUNIC_LINES))
        return
    w.globals["hearts"] = w.globals.get("hearts", 1) - amount
    if lethal and w.globals["hearts"] <= 0:
        _handle_death(w)


_take_damage = take_damage      # older callers (traps, hazards)


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

    print("Your last heart gives out. The dark closes in, and this time it keeps you.\n\n"
          "*** GAME OVER ***")
    world.set_global("GAME-OVER", True)   # permanent death (mechanics.md)
    world.game.quit()


# ---------------------------------------------------------------------------
# XP
# ---------------------------------------------------------------------------

def award_combat_xp(world: "World", enemy_key: str, kill: bool = True) -> None:
    """
    Award XP on enemy defeat (experience.md — Combat). Warriors get +10 per
    combat kill (experience.md — Class XP Adjustments); kill=False for
    defeats that aren't kills (Aylora passes out).
    """
    xp = _COMBAT_XP.get(enemy_key, 0)
    if kill and world.globals.get("player_class") == "warrior":
        xp += 10
    award_xp(world, xp)
