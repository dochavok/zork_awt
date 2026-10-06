"""
Progression (experience.md — Leveling Curve, Dice Progression, Quest Completion,
Class XP Adjustments; mechanics.md — Difficulty tiers, Lucky).

Every expected number is the design's, written out here — not read from the
code — so a change to the code that drifts from the design fails a test.
Run with: pytest roundabout/test_progression.py  (from c:\\zork_awt)
"""

import sys
import os
import io
import random
from unittest.mock import patch
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do
from content.experience import award_xp
from content import player, quests

# experience.md — Leveling Curve: level -> cumulative XP
THRESHOLDS = {2: 20, 3: 45, 4: 85, 5: 145, 6: 225, 7: 320, 8: 420}
# experience.md — Dice Progression: level -> (dice, sides, bonus)
DICE = {1: (1, 6, 0), 2: (2, 6, 1), 3: (2, 8, 2), 4: (2, 10, 3),
        5: (3, 10, 4), 6: (3, 12, 5), 7: (2, 20, 6), 8: (3, 20, 7)}
# experience.md — Quest Completion (XP); quests.md — each quest's Reward (Zenni)
QUEST_REWARDS = {
    "4": (10, 5), "7": (6, 3), "12": (10, 5), "17": (17, 8), "19": (11, 5),
    "22": (10, 5), "24": (10, 5), "25": (10, 5), "27": (6, 3), "28": (6, 3),
    "30": (11, 5), "32": (12, 5), "34": (17, 8), "38": (8, 5), "40": (6, 3),
    "41": (4, 3), "42": (12, 5), "49": (17, 8), "50": (12, 5), "51": (6, 3),
    "52": (6, 3), "53": (10, 5), "54": (8, 0), "55": (6, 0), "57": (12, 5),
    "58": (15, 5), "59": (5, 3),
}


def _quiet(fn, *a, **kw):
    with patch("sys.stdout", io.StringIO()):
        return fn(*a, **kw)


def _fresh(cls="warrior", **kw):
    return _make_world(cls=cls, level=1, **kw)


# --- Leveling curve ---------------------------------------------------------------

@pytest.mark.parametrize("level,xp", sorted(THRESHOLDS.items()))
def test_level_thresholds(level, xp):
    w, g = _fresh()
    _quiet(award_xp, w, xp - 1)
    assert w.globals["level"] == level - 1
    _quiet(award_xp, w, 1)
    assert w.globals["level"] == level


def test_level_up_message():
    w, g = _fresh()
    buf = io.StringIO()
    with patch("sys.stdout", buf):
        award_xp(w, 20)
    assert "You hear music — a familiar melody. You have reached level 2!" in buf.getvalue()


def test_hearts_at_levels_three_five_seven_only():
    w, g = _fresh(hearts=6)
    gained = {}
    for level in range(2, 9):
        before = w.globals["max_hearts"]
        _quiet(award_xp, w, THRESHOLDS[level] - w.globals["xp"])
        gained[level] = w.globals["max_hearts"] - before
    assert gained == {2: 0, 3: 1, 4: 0, 5: 1, 6: 0, 7: 1, 8: 0}


def test_rest_granted_at_level_six():
    w, g = _fresh()
    _quiet(award_xp, w, 224)
    assert not w.globals.get("spell_rest")
    buf = io.StringIO()
    with patch("sys.stdout", buf):
        award_xp(w, 1)
    assert w.globals.get("spell_rest")
    assert "You can now REST to recover when the fighting stops." in buf.getvalue()


# --- Dice progression ---------------------------------------------------------------

@pytest.mark.parametrize("level,dice", sorted(DICE.items()))
def test_dice_by_level(level, dice):
    n, sides, bonus = dice
    w, g = _make_world(level=level)
    with patch("random.randint", lambda a, b: b):
        assert player.roll(w) == n * sides + bonus           # max
    with patch("random.randint", lambda a, b: a):
        assert player.roll(w) == n + bonus                   # min (Lucky rerolls 1s into 1s)


def _mean_roll(level, n=40000):
    w, g = _make_world(level=level)
    rng = random.Random(3)
    with patch("random.randint", rng.randint):
        return sum(player.roll(w) for _ in range(n)) / n


def test_lucky_from_level_four():
    # Level 3 (2d8+2, no Lucky): mean 11.0. Level 4 (2d10+3) without Lucky would be
    # 14.0; rerolling 1s once raises each d10 by 0.45, so 14.9.
    assert abs(_mean_roll(3) - 11.0) < 0.1
    assert abs(_mean_roll(4) - 14.9) < 0.1


# --- Difficulty tiers (Medium, 9) through real checks --------------------------------

def _blocks(cls, roll):
    """PLACE BLOCKS at the Collapsed Aqueduct (quests.md — Quest 22: Medium strength)."""
    w, g = _make_world(cls=cls)
    w.move_object(w.player, w.rooms["COLLAPSED-AQUEDUCT"])
    w.here = w.rooms["COLLAPSED-AQUEDUCT"]
    with patch("content.player.roll", return_value=roll):
        _do(g, "place blocks")
    return w.get_global("BLOCKS-PLACED") or 0


def test_medium_strength_check_is_nine():
    assert _blocks("mage", 8) == 0
    assert _blocks("mage", 9) == 1


def test_warrior_strength_bonus_counts():
    assert _blocks("warrior", 5) == 0                       # 5 + 3 = 8
    assert _blocks("warrior", 6) == 1                       # 6 + 3 = 9


def _alley(roll):
    """Enter the Back Alley (locations.md: mugger perception, Medium 9) as a Warrior."""
    w, g = _make_world(cls="warrior", zenni=10)
    with patch("content.player.roll", return_value=roll):
        _quiet(g.enter_room, w.rooms["BACK-ALLEY"])
        _do(g, "look")
    return w


def test_medium_perception_check_is_nine():
    assert not _alley(8).get_global("MUGGER-SPOTTED")
    assert _alley(9).get_global("MUGGER-SPOTTED")


# --- Quest, ritual and teaching rewards ------------------------------------------------

@pytest.mark.parametrize("quest,reward", sorted(QUEST_REWARDS.items(), key=lambda kv: int(kv[0])))
def test_quest_rewards(quest, reward):
    xp, zenni = reward
    w, g = _fresh(zenni=0)
    _quiet(quests.complete, w, quest)
    assert (w.globals["xp"], w.globals["zenni"]) == (xp, zenni)
    _quiet(quests.complete, w, quest)                       # paid once
    assert (w.globals["xp"], w.globals["zenni"]) == (xp, zenni)


def test_teaching_is_free_and_pays_four_xp():
    # quests.md — Quest 56: no Zenni either way, 4 XP per spell; an empty purse is fine
    w, g = _fresh(cls="rogue", zenni=0)
    w.move_object(w.player, w.rooms["WIZARDS-TOWER"])
    w.here = w.rooms["WIZARDS-TOWER"]
    w.move_object(w.objects["WILL"], w.here)
    for n, scroll in enumerate(("SCROLL-LIGHT", "SCROLL-UNBIND-UNDEAD"), 1):
        w.objects[scroll].flags.discard("INVISIBLE")         # the Light scroll starts in the music box
        w.move_object(w.objects[scroll], w.player)
        out = _do(g, "give scroll to will")
        assert "The knowing, I mean." in out
        assert w.objects[scroll].location is not w.player    # consumed
        assert w.globals["zenni"] == 0
        assert w.globals["xp"] == 4 * n


def test_binding_ritual_pays_five_xp():
    w, g = _fresh()
    room = w.rooms["ALTAR"]
    w.move_object(w.player, room)
    w.here = room
    w.move_object(w.objects["RING"], w.player)
    for art, noun in (("PALE-BLADE", "blade"), ("WEREWOLFS-AMULET", "amulet"),
                      ("CRYSTAL-BOWL", "bowl")):
        w.move_object(w.objects[art], w.player)
        _do(g, f"put {noun} on altar")
    for _ in range(7):                                        # once round the dial
        _do(g, "turn dial right")
    before = w.globals["xp"]
    out = _do(g, "put ring on altar")
    assert "The ring is bound." in out
    assert w.globals["xp"] - before == 5
