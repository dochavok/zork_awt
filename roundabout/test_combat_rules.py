"""
Shared combat rules (content/combat.py; mechanics.md — Combat, Gear bonuses):
weapon and glove bonuses, the tunic in every fight, the werewolf's claws.
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
    w, g = _make_world(cls=cls, **kw)
    return w, g


def _give(w, *names, wear=False):
    for n in names:
        obj = w.objects[n]
        w.move_object(obj, w.player)
        if wear:
            obj.set_flag(WEARBIT)


# --- weapon_bonus / gloves_bonus -----------------------------------------------

def test_no_weapon_no_bonus():
    w, g = _world()
    assert combat.weapon_bonus(w) == 0


@pytest.mark.parametrize("names,best", [
    (["DAGGER"], 2), (["MACE"], 4), (["BATTLE-AXE"], 6),
    (["DAGGER", "MACE"], 4), (["MACE", "BATTLE-AXE"], 6),
])
def test_best_weapon_carried(names, best):
    w, g = _world()
    _give(w, *names)
    assert combat.weapon_bonus(w) == best


def test_named_weapon_is_used():
    w, g = _world()
    _give(w, "DAGGER", "BATTLE-AXE")
    assert combat.weapon_bonus(w, w.objects["DAGGER"]) == 2


def test_named_non_weapon_gives_nothing():
    w, g = _world()
    _give(w, "BATTLE-AXE", "ROPE")
    assert combat.weapon_bonus(w, w.objects["ROPE"]) == 0


@pytest.mark.parametrize("cls", ["mage", "rogue"])
def test_untrained_class_gets_no_weapon_bonus(cls):
    w, g = _world(cls=cls)
    w.globals.pop("skill_melee", None)
    _give(w, "BATTLE-AXE")
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
    _give(w, "MACE")
    _give(w, "APPRENTICE-GLOVES", wear=True)
    with patch("content.player.roll", return_value=5):
        assert combat.player_roll(w) == 5 + 4 + 3


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


def test_weapon_turns_a_lost_round_into_a_hit():
    w, g = _world()
    _mugger(w)
    out = _round(g, "kill mugger", 3, [5])
    assert w.globals["MUGGER-HEARTS"] == 2           # lost: 3 against 5
    _give(w, "MACE")
    _round(g, "kill mugger", 3, [5])
    assert w.globals["MUGGER-HEARTS"] == 1           # 3 + 4 beats 5


def test_kill_with_named_weapon_uses_it():
    w, g = _world()
    _mugger(w)
    _give(w, "DAGGER", "BATTLE-AXE")
    _round(g, "kill mugger with dagger", 3, [5])     # 3 + 2 ties 5: both hit
    assert w.globals["MUGGER-HEARTS"] == 1


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
    out = _round(g, "kill mugger", 1, [6, 10])        # mugger 6; tunic 1d10 → 10
    assert any(line in out for line in combat._TUNIC_LINES)
    assert w.globals["hearts"] == hearts


def test_losing_to_the_mugger_is_still_not_death():
    w, g = _world(hearts=1)
    _mugger(w)
    _round(g, "kill mugger", 1, [6])
    assert not w.get_global("GAME-OVER")
    assert w.globals["hearts"] == 1


# --- The werewolf: bonuses decide whether its claws land -------------------------

def test_werewolf_claws_miss_with_bonuses():
    w, g = _world()
    hearts = w.globals["hearts"]
    with patch("content.player.roll", return_value=10), \
         patch("content.combat.random.randint", lambda a, b: 5):   # 3d10 → 15
        combat.defend(w, (3, 10), "CLAWS")
    assert w.globals["hearts"] == hearts - 1                        # 10 against 15
    _give(w, "BATTLE-AXE")
    _give(w, "APPRENTICE-GLOVES", wear=True)
    with patch("content.player.roll", return_value=10), \
         patch("content.combat.random.randint", lambda a, b: 5):
        combat.defend(w, (3, 10), "CLAWS")
    assert w.globals["hearts"] == hearts - 1                        # 19 against 15


def test_still_den_round_uses_shared_defend():
    from content import still_den
    w, g = _world()
    _give(w, "BATTLE-AXE")
    _give(w, "APPRENTICE-GLOVES", wear=True)
    hearts = w.globals["hearts"]
    with patch("content.player.roll", return_value=10), \
         patch("content.combat.random.randint", lambda a, b: 5):
        still_den._werewolf_round(w)
    assert w.globals["hearts"] == hearts


def test_untrained_named_weapon_fights_at_plus_zero():
    w, g = _world(cls="mage")
    w.globals.pop("skill_melee", None)
    _mugger(w)
    _give(w, "BATTLE-AXE")
    out = _round(g, "kill mugger with axe", 3, [5])
    assert w.globals["MUGGER-HEARTS"] == 2           # 3 + 0 loses to 5: no refusal, no bonus
    assert "can't" not in out


# --- The Finishing Move (Level 8, secret) ------------------------------------------

def _finish(g, cmd, level_roll=1):
    """randint always 1: the 216-in-8000 draw succeeds."""
    with patch("content.combat.random.randint", lambda a, b: level_roll):
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
    assert w.globals["KNIGHT-HEARTS"] >= knight.KNIGHT_HEARTS - 1
