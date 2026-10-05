"""
Shared combat rules (content/combat.py; mechanics.md — Combat, Gear bonuses,
Equipping weapons, Bow attacks): the equipped weapon or bow, gloves, the tunic
in every fight, the werewolf's claws, the Finishing Move.
Rolls are fixed by patching the player's level roll and the enemy's dice.
Run with: pytest roundabout/test_combat_rules.py  (from c:\\zork_awt)
"""

import sys
import os
from unittest.mock import patch
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do
from content import combat
from engine.world import WEARBIT


def _world(cls="warrior", **kw):
    return _make_world(cls=cls, **kw)


def _give(w, *names, wear=False):
    for n in names:
        obj = w.objects[n]
        w.move_object(obj, w.player)
        if wear:
            obj.set_flag(WEARBIT)


def _equip(w, name):
    _give(w, name)
    w.globals["EQUIPPED"] = name


# --- weapon_bonus / gloves_bonus -----------------------------------------------

def test_no_weapon_no_bonus():
    w, g = _world()
    assert combat.weapon_bonus(w) == 0


@pytest.mark.parametrize("name,bonus", [("DAGGER", 2), ("MACE", 4), ("BATTLE-AXE", 6)])
def test_equipped_weapon_bonus(name, bonus):
    w, g = _world()
    _equip(w, name)
    assert combat.weapon_bonus(w) == bonus


def test_carried_but_not_equipped_adds_nothing():
    w, g = _world()
    _give(w, "BATTLE-AXE")
    assert combat.weapon_bonus(w) == 0


def test_bow_equipped_means_bare_hands_for_melee():
    w, g = _world()
    _give(w, "MACE")
    _equip(w, "BOW")
    assert combat.weapon_bonus(w) == 0


@pytest.mark.parametrize("cls", ["mage", "rogue"])
def test_untrained_class_gets_no_weapon_bonus(cls):
    w, g = _world(cls=cls)
    w.globals.pop("skill_melee", None)
    _equip(w, "BATTLE-AXE")
    assert combat.weapon_bonus(w) == 0
    w.globals["skill_melee"] = True              # Quest 54 done
    assert combat.weapon_bonus(w) == 6


def test_gloves_only_while_worn():
    w, g = _world()
    _give(w, "APPRENTICE-GLOVES")
    assert combat.gloves_bonus(w) == 0
    w.objects["APPRENTICE-GLOVES"].set_flag(WEARBIT)
    assert combat.gloves_bonus(w) == 3


def test_weapon_and_gloves_add_up():
    w, g = _world()
    _equip(w, "MACE")
    _give(w, "APPRENTICE-GLOVES", wear=True)
    with patch("content.player.roll", return_value=5):
        assert combat.player_roll(w) == 5 + 4 + 3


def test_bow_roll_opening_and_gloves():
    w, g = _world()
    _equip(w, "MACE")
    _give(w, "APPRENTICE-GLOVES", wear=True)
    with patch("content.player.roll", return_value=5):
        assert combat.player_roll(w, shot=True, opening=True) == 5 + 5 + 3
        assert combat.player_roll(w, shot=True) == 5 + 3


# --- EQUIP / UNEQUIP / REMOVE ------------------------------------------------------

def test_equip_lines():
    w, g = _world()
    _give(w, "BOW", "MACE")
    assert "You take up the bow." in _do(g, "equip bow")
    assert "You're already holding the bow." in _do(g, "equip bow")
    assert "You put away the bow and take up the mace." in _do(g, "wield mace")
    assert w.globals["EQUIPPED"] == "MACE"


def test_equip_untrained_refused():
    w, g = _world(cls="mage")
    w.globals.pop("skill_melee", None)
    _give(w, "DAGGER", "BOW")
    out = _do(g, "equip dagger")
    assert "You don't know how to fight with the dagger. The knight in the square teaches that." in out
    assert not w.globals.get("EQUIPPED")
    assert "You take up the bow." in _do(g, "equip bow")


def test_equip_non_weapon():
    w, g = _world()
    _give(w, "ROPE")
    assert "You can't equip the coil of rope." in _do(g, "equip rope")


@pytest.mark.parametrize("cmd", ["unequip mace", "remove mace"])
def test_put_away(cmd):
    w, g = _world()
    _equip(w, "MACE")
    assert "You put away the mace." in _do(g, cmd)
    assert not w.globals.get("EQUIPPED")
    assert "You aren't holding the mace." in _do(g, cmd)


def test_dropping_unequips_silently():
    w, g = _world()
    _equip(w, "MACE")
    _do(g, "drop mace")
    assert not w.globals.get("EQUIPPED")
    _do(g, "take mace")
    assert combat.equipped(w) is None


def test_inventory_shows_equipped():
    w, g = _world()
    _equip(w, "MACE")
    _give(w, "DAGGER")
    out = _do(g, "i")
    assert "Mace (equipped)" in out and "Dagger\n" in out


# --- WEAR: wearable things only ------------------------------------------------------

@pytest.mark.parametrize("name,word", [("BOW", "bow"), ("ROPE", "coil of rope"), ("DAGGER", "dagger")])
def test_wear_refuses_non_wearables(name, word):
    w, g = _world()
    _give(w, name)
    assert f"You can't wear the {word}." in _do(g, f"wear {word.split()[-1]}")
    assert not w.objects[name].has_flag(WEARBIT)


def test_disguise_can_be_worn():
    w, g = _world()
    _give(w, "PIE-RAT-DISGUISE")
    _do(g, "wear disguise")
    assert w.objects["PIE-RAT-DISGUISE"].has_flag(WEARBIT)


# --- In the fights ---------------------------------------------------------------

def _mugger(w):
    w.move_object(w.player, w.rooms["BACK-ALLEY"])
    w.here = w.rooms["BACK-ALLEY"]
    w.set_global("MUGGER-SPOTTED", True)
    mugger = w.objects["MUGGER"]
    mugger.flags.discard("INVISIBLE")
    w.move_object(mugger, w.here)


def _round(g, cmd, mine, theirs):
    """One round with the player's level roll and the enemy's dice fixed."""
    faces = iter(theirs)
    with patch("content.player.roll", return_value=mine), \
         patch("content.combat.random.randint", lambda a, b: next(faces)):
        return _do(g, cmd)


def test_equipped_weapon_turns_a_lost_round_into_a_hit():
    w, g = _world()
    _mugger(w)
    _give(w, "MACE")
    _round(g, "kill mugger", 3, [5])           # carried only: 3 loses to 5
    assert w.globals["MUGGER-HEARTS"] == 2
    _do(g, "equip mace")
    _round(g, "kill mugger", 3, [5])           # 3 + 4 beats 5
    assert w.globals["MUGGER-HEARTS"] == 1


def test_kill_with_weapon_equips_it_same_turn():
    w, g = _world()
    _mugger(w)
    _give(w, "DAGGER", "BATTLE-AXE")
    out = _round(g, "kill mugger with dagger", 3, [5])   # 3 + 2 ties 5: both hit
    assert "You take up the dagger." in out
    assert w.globals["EQUIPPED"] == "DAGGER"
    assert w.globals["MUGGER-HEARTS"] == 1


def test_untrained_named_weapon_fights_at_plus_zero():
    w, g = _world(cls="mage")
    w.globals.pop("skill_melee", None)
    _mugger(w)
    _give(w, "BATTLE-AXE")
    out = _round(g, "kill mugger with axe", 3, [5])
    assert w.globals["MUGGER-HEARTS"] == 2           # no refusal, no bonus
    assert "You take up" not in out and "can't" not in out


def test_gloves_count_in_the_warden_fight():
    from content import combat_room
    w, g = _world()
    _give(w, "APPRENTICE-GLOVES", wear=True)
    w.move_object(w.objects["WARDEN"], w.here)
    hearts = w.globals["hearts"]
    with patch("content.player.roll", return_value=10), \
         patch("content.combat.random.randint", lambda a, b: 6):    # 2d10 → 12
        combat_room.fight_round(w)
    assert w.globals["WARDEN-HEARTS"] == combat_room.WARDEN_HEARTS - 1   # 13 beats 12
    assert w.globals["hearts"] == hearts


def test_tunic_turns_the_muggers_blow():
    w, g = _world()
    _mugger(w)
    _give(w, "IVANAAR-TUNIC", wear=True)
    hearts = w.globals["hearts"]
    out = _round(g, "kill mugger", 1, [6, 10])  # mugger 6; tunic 1d10 → 10
    assert any(line in out for line in combat._TUNIC_LINES)
    assert w.globals["hearts"] == hearts


def test_losing_to_the_mugger_is_still_not_death():
    w, g = _world(hearts=1)
    _mugger(w)
    _round(g, "kill mugger", 1, [6])
    assert not w.get_global("GAME-OVER")
    assert w.globals["hearts"] == 1


# --- Bow attacks --------------------------------------------------------------------

def test_shoot_without_bow():
    w, g = _world()
    _mugger(w)
    assert "You've nothing to shoot with." in _do(g, "shoot mugger")


def test_shoot_with_something_else():
    w, g = _world()
    _mugger(w)
    _give(w, "BOW", "ROPE")
    assert "That won't shoot anything." in _do(g, "shoot mugger with rope")


def test_shoot_non_enemy():
    w, g = _world()
    _give(w, "BOW")
    w.move_object(w.player, w.rooms["BAR"])
    w.here = w.rooms["BAR"]
    assert "You can't fight the" in _do(g, "shoot may")
    assert not w.globals.get("EQUIPPED")


def test_shoot_equips_bow_and_opening_bonus_once():
    w, g = _world()
    _mugger(w)
    _give(w, "BOW")
    _equip(w, "MACE")
    out = _round(g, "shoot mugger", 1, [5])     # 1 + 5 beats 5: opening shot
    assert "You put away the mace and take up the bow." in out
    assert w.globals["MUGGER-HEARTS"] == 1
    _round(g, "shoot mugger", 1, [5])           # no bonus now: 1 loses
    assert w.globals["MUGGER-HEARTS"] == 1


def test_swing_first_then_shoot_gets_no_bonus():
    w, g = _world()
    _mugger(w)
    _give(w, "BOW")
    _round(g, "kill mugger", 1, [5])            # lost; fight opened
    _round(g, "shoot mugger", 1, [5])           # 1, no +5: lost again
    assert w.globals["MUGGER-HEARTS"] == 2


def test_reentering_resets_opening_round():
    w, g = _world()
    _mugger(w)
    _give(w, "BOW")
    _round(g, "kill mugger", 1, [5])
    combat.on_enter(w, w.here)                        # came back into the alley
    _round(g, "shoot mugger", 1, [5])
    assert w.globals["MUGGER-HEARTS"] == 1


def test_shot_lines_hit_tie_and_miss():
    from content import back_alley
    w, g = _world()
    _mugger(w)
    _give(w, "BOW")
    out = _round(g, "shoot mugger", 1, [5])          # opening: 1 + 5 beats 5
    assert "Your arrow finds its mark. The mugger staggers." in out
    assert back_alley._ROUND_WON not in out
    out = _round(g, "shoot mugger", 1, [1])          # 1 ties 1
    assert "You loose an arrow as it closes on you. Both of you feel it." in out
    assert back_alley._ROUND_TIE not in out


def test_shot_miss_keeps_the_fights_line():
    from content import combat_room
    w, g = _world()
    _give(w, "BOW")
    room = w.rooms["COMBAT-ROOM"]
    w.move_object(w.player, room)
    w.here = room
    warden = w.objects["WARDEN"]
    warden.flags.discard("INVISIBLE")
    w.move_object(warden, room)
    out = _round(g, "shoot warden", 1, [10, 10])     # 6 against 20
    assert combat_room._ROUND_LOST in out


def test_warden_hit_line_names_the_warden():
    w, g = _world()
    _give(w, "BOW")
    room = w.rooms["COMBAT-ROOM"]
    w.move_object(w.player, room)
    w.here = room
    warden = w.objects["WARDEN"]
    warden.flags.discard("INVISIBLE")
    w.move_object(warden, room)
    out = _round(g, "shoot warden", 10, [1, 1])
    assert "Your arrow finds its mark. The Warden staggers." in out


def test_kill_with_bow_is_a_shot():
    w, g = _world()
    _mugger(w)
    _give(w, "BOW")
    out = _round(g, "kill mugger with bow", 1, [5])
    assert "You take up the bow." in out
    assert w.globals["MUGGER-HEARTS"] == 1


def test_shoot_werewolf():
    from content import still_den
    w, g = _world()
    _give(w, "BOW")
    den = w.rooms["STILL-DEN"]
    w.move_object(w.player, den)
    w.here = den
    w.move_object(w.objects["WEREWOLF"], den)
    out = _do(g, "shoot werewolf")
    assert still_den._BOW_FAILS in out


@pytest.mark.parametrize("cmd", ["shoot knight", "kill knight with bow"])
def test_shoot_knight_no_turn(cmd):
    from content import knight
    w, g = _world(cls="mage")
    _give(w, "BOW")
    square = w.rooms["TOWN-SQUARE"]
    w.move_object(w.player, square)
    w.here = square
    w.move_object(w.objects["KNIGHT"], square)
    moves = w.moves
    assert knight.BOW_REFUSED in _do(g, cmd)
    assert w.moves == moves


# --- The werewolf: bonuses decide whether its claws land -------------------------

def test_werewolf_claws_miss_with_bonuses():
    w, g = _world()
    hearts = w.globals["hearts"]
    with patch("content.player.roll", return_value=10), \
         patch("content.combat.random.randint", lambda a, b: 5):   # 3d10 → 15
        combat.defend(w, (3, 10), "CLAWS")
    assert w.globals["hearts"] == hearts - 1                        # 10 against 15
    _equip(w, "BATTLE-AXE")
    _give(w, "APPRENTICE-GLOVES", wear=True)
    with patch("content.player.roll", return_value=10), \
         patch("content.combat.random.randint", lambda a, b: 5):
        combat.defend(w, (3, 10), "CLAWS")
    assert w.globals["hearts"] == hearts - 1                        # 19 against 15


def test_still_den_round_uses_shared_defend():
    from content import still_den
    w, g = _world()
    _equip(w, "BATTLE-AXE")
    _give(w, "APPRENTICE-GLOVES", wear=True)
    hearts = w.globals["hearts"]
    with patch("content.player.roll", return_value=10), \
         patch("content.combat.random.randint", lambda a, b: 5):
        still_den._werewolf_round(w)
    assert w.globals["hearts"] == hearts


# --- The Finishing Move (Level 8, secret) ------------------------------------------

def _finish(g, cmd):
    """randint always 1: the 216-in-8000 draw succeeds."""
    with patch("content.combat.random.randint", lambda a, b: 1):
        return _do(g, cmd)


def test_finishing_move_fells_the_mugger():
    w, g = _world(level=8)
    _mugger(w)
    hearts = w.globals["hearts"]
    out = _finish(g, "kill mugger")
    assert combat._FINISH_LINES in out
    assert w.get_global("MUGGER-DEAD")
    assert w.globals["hearts"] == hearts


def test_finishing_move_frees_the_apprentice():
    from content import trap_side
    w, g = _world(level=8)
    with patch("content.combat.random.randint", lambda a, b: 1):
        trap_side.fight_round(w)
    assert w.get_global("APPRENTICE-FREED")


def test_no_finishing_move_below_level_8():
    w, g = _world(level=7)
    _mugger(w)
    assert combat._FINISH_LINES not in _finish(g, "kill mugger")


def test_max_dice_never_finish():
    w, g = _world(level=8)
    _mugger(w)
    with patch("content.player.roll", return_value=1), \
         patch("content.combat.random.randint", lambda a, b: b):
        out = _do(g, "kill mugger")
    assert combat._FINISH_LINES not in out


def test_no_finishing_move_on_the_knight():
    from content import knight
    w, g = _world(cls="mage", level=8)
    w.globals.pop("skill_melee", None)
    w.set_global("KNIGHT-FIGHTING", True)
    w.globals["KNIGHT-HEARTS"] = knight.KNIGHT_HEARTS
    with patch("content.player.roll", return_value=1), \
         patch("content.combat.random.randint", lambda a, b: 1):
        knight._round(w)
    assert w.globals["KNIGHT-HEARTS"] == knight.KNIGHT_HEARTS
