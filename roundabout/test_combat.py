"""
Combat (mechanics.md — Combat, Fireball, Ivanaar's Tunic, Finishing Move,
Nobu's Favor, Undead Werewolf Chain). Bow and gear bonuses: test_combat_rules.py.

Expected numbers and text are the design's, written out here.
Run with: pytest roundabout/test_combat.py  (from c:\\zork_awt)
"""

import sys
import os
import io
from unittest.mock import patch
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do
from content import combat
from content.experience import award_xp

# mechanics.md / ring-rituals.md text
CLAWS = "The werewolf's claws find you."
PLAIN_STAKE = ("The stake pierces flesh. The werewolf snarls — pain, but not the right kind. "
               "It pulls free and the wound closes. You need something more than silver.")
REVERTS = ("The creature drops. Between one moment and the next, it is not the creature "
           "anymore. The scholar lies on the floor of the cave he came down here to find.")
FINISH = '"Finish him."'
NOBU = '"But did you die?"'
DEATH = "Your last heart gives out. The dark closes in, and this time it keeps you."
TUNIC_LINES = (
    "The threads along the hem pulse faintly. Whatever just happened, the tunic had something to do with it.",
    "For a moment the fabric stiffens — then relaxes, as if it exhaled. The blow that should have landed didn't.",
    "The runes along the collar catch the light briefly. You are less hurt than you expected to be.",
    "Something in the weave absorbed it. You felt the impact — and then didn't.",
)


def _quiet(fn, *a, **kw):
    with patch("sys.stdout", io.StringIO()):
        return fn(*a, **kw)


# ---------------------------------------------------------------------------
# Fireball: guaranteed 1 heart, no roll
# ---------------------------------------------------------------------------

def _warden_fight():
    """The Warden out in the Combat Room, the player facing him, Fireball known."""
    w, g = _make_world(cls="warrior", level=1, hearts=5)
    w.globals["skill_melee"] = True
    w.globals["spell_fireball"] = True
    room = w.rooms["COMBAT-ROOM"]
    w.move_object(w.player, room)
    w.here = room
    w.move_object(w.objects["WARDEN"], room)
    w.set_global("WARDEN-OUT", True)
    w.set_global("WARDEN-HEARTS", 5)
    return w, g


def test_fireball_deals_guaranteed_damage():
    # Even with every roll lost, the fireball lands and the Warden doesn't hit back
    w, g = _warden_fight()
    buf = io.StringIO()
    with patch("sys.stdout", buf), patch("random.randint", lambda a, b: a):
        g.do_turn("cast fireball at warden")
    out = buf.getvalue()

    assert "takes the Warden full on" in out, out
    assert w.get_global("WARDEN-HEARTS") == 4
    assert w.globals["hearts"] == 5


def test_fireball_cooldown_blocks_reuse():
    # A second cast within 10 turns isn't ready, and doesn't use a turn
    w, g = _warden_fight()
    with patch("sys.stdout", io.StringIO()), patch("random.randint", lambda a, b: b):
        g.do_turn("cast fireball at warden")
    moves = w.moves
    out = _do(g, "cast fireball at warden")

    assert "isn't ready yet" in out, out
    assert w.moves == moves
    assert w.get_global("WARDEN-HEARTS") == 4


# ---------------------------------------------------------------------------
# Ivanaar's Tunic: a hidden 1d10, 7-10 turns the blow (40%)
# ---------------------------------------------------------------------------

def _tunic_hit(face):
    """One blow against a player wearing the tunic, the tunic's d10 showing `face`."""
    w, g = _make_world(cls="warrior", hearts=5)
    tunic = w.objects["IVANAAR-TUNIC"]
    w.move_object(tunic, w.player)
    tunic.set_flag("WEARBIT")
    buf = io.StringIO()
    with patch("sys.stdout", buf), patch("content.combat.random.randint", return_value=face):
        combat.take_damage(w, 1)
    return w, buf.getvalue()


def test_tunic_turns_the_blow_on_seven_to_ten():
    for face in (7, 8, 9, 10):
        w, out = _tunic_hit(face)
        assert w.globals["hearts"] == 5, face
        assert any(line in out for line in TUNIC_LINES), face


def test_tunic_does_nothing_on_one_to_six():
    for face in (1, 6):
        w, out = _tunic_hit(face)
        assert w.globals["hearts"] == 4, face
        assert not any(line in out for line in TUNIC_LINES), face


def test_tunic_only_while_worn():
    w, g = _make_world(cls="warrior", hearts=5)
    w.move_object(w.objects["IVANAAR-TUNIC"], w.player)          # carried, not worn
    with patch("content.combat.random.randint", return_value=10):
        _quiet(combat.take_damage, w, 1)
    assert w.globals["hearts"] == 4


# ---------------------------------------------------------------------------
# Finishing Move: Level 8, all 3d20 at 15+ — 216 in 8,000
# ---------------------------------------------------------------------------

def _mugger_round(level, finish_draw):
    """One round at the mugger; the Finishing Move draw (1..8000) is fixed."""
    w, g = _make_world(cls="warrior", level=level, hearts=5)
    w.move_object(w.player, w.rooms["BACK-ALLEY"])
    w.here = w.rooms["BACK-ALLEY"]
    w.set_global("MUGGER-SPOTTED", True)
    mugger = w.objects["MUGGER"]
    mugger.flags.discard("INVISIBLE")
    w.move_object(mugger, w.here)

    def randint(a, b):
        return finish_draw if b == 8000 else 1   # mugger's 1d6 shows 1
    with patch("content.player.roll", return_value=1), \
         patch("content.combat.random.randint", randint):
        out = _do(g, "kill mugger")
    return w, out


def test_finishing_move_odds_edge():
    w, out = _mugger_round(8, 216)
    assert FINISH in out and w.get_global("MUGGER-DEAD")
    w, out = _mugger_round(8, 217)
    assert FINISH not in out


def test_finishing_move_needs_level_8():
    w, out = _mugger_round(7, 1)
    assert FINISH not in out


def test_finishing_move_rate_is_about_2_7_percent():
    # Measured over many rounds with seeded dice: 216/8000 = 2.7%
    import random
    from content import combat as c
    w, g = _make_world(cls="warrior", level=8)
    rng = random.Random(1)
    hits = 0
    n = 40000
    with patch("content.combat.random.randint", rng.randint), patch("sys.stdout", io.StringIO()):
        for _ in range(n):
            hits += c._finishing_move(w)
    assert 0.024 < hits / n < 0.030


# ---------------------------------------------------------------------------
# Nobu's Favor: granted silently at Level 7; once per game
# ---------------------------------------------------------------------------

def test_nobus_favor_saves_once_then_death_is_final():
    w, g = _make_world(cls="warrior", level=1, hearts=6)
    _quiet(award_xp, w, 320)                    # experience.md — Level 7 at 320 XP
    assert w.globals["level"] == 7

    w.globals["hearts"] = 1
    buf = io.StringIO()
    with patch("sys.stdout", buf):
        combat.take_damage(w, 1)
    assert NOBU in buf.getvalue()
    assert w.globals["hearts"] == 1
    assert w.here.name == "TALE-AND-ALE"
    assert not w.get_global("GAME-OVER")

    buf = io.StringIO()
    with patch("sys.stdout", buf):
        combat.take_damage(w, 1)
    assert NOBU not in buf.getvalue()
    assert DEATH in buf.getvalue()
    assert w.get_global("GAME-OVER") is True


def test_no_nobus_favor_below_level_7():
    w, g = _make_world(cls="warrior", level=1, hearts=6)
    _quiet(award_xp, w, 319)
    w.globals["hearts"] = 1
    buf = io.StringIO()
    with patch("sys.stdout", buf):
        combat.take_damage(w, 1)
    assert DEATH in buf.getvalue()
    assert w.get_global("GAME-OVER") is True


# ---------------------------------------------------------------------------
# The Undead Werewolf: 3d10; only the consecrated stake harms it
# ---------------------------------------------------------------------------

def _den(hearts=6):
    """In The Still Den with the werewolf up (one turn after entering), stake carried."""
    w, g = _make_world(cls="warrior", hearts=hearts)
    w.move_object(w.objects["TORCH"], w.player)                # bought torches are lit
    w.move_object(w.objects["SILVER-STAKE"], w.player)
    _quiet(g.enter_room, w.rooms["STILL-DEN"])
    _do(g, "wait")                                             # the entry turn: it rises
    return w, g


def test_werewolf_rolls_three_d10():
    # Player's roll 25. The werewolf's dice all show 10: 3d10 = 30 beats 25.
    w, g = _den()
    with patch("content.player.roll", return_value=25), \
         patch("content.combat.random.randint", lambda a, b: 10):
        out = _do(g, "wait")
    assert CLAWS in out
    assert w.globals["hearts"] == 5


def test_plain_stake_does_not_kill():
    w, g = _den()
    with patch("content.player.roll", return_value=99):
        out = _do(g, "drive stake into werewolf")
    assert PLAIN_STAKE in out
    assert not w.get_global("WEREWOLF-DEAD")
    assert w.objects["WEREWOLF"].location is w.here


def test_conventional_weapons_do_not_harm_it():
    w, g = _den()
    w.globals["skill_melee"] = True
    w.move_object(w.objects["BATTLE-AXE"], w.player)
    with patch("content.player.roll", return_value=99):
        _do(g, "kill werewolf with axe")
    assert not w.get_global("WEREWOLF-DEAD")


def test_consecrated_stake_kills_and_drops_the_amulet():
    w, g = _den()
    w.set_global("STAKE-CONSECRATED", True)
    out = _do(g, "drive stake into werewolf")
    assert REVERTS in out
    assert w.get_global("WEREWOLF-DEAD") is True
    assert w.objects["WEREWOLFS-AMULET"].location is w.here
