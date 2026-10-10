"""
May's hints — TIP MAY [#] (mechanics.md — Hint System; quests.md per quest).

Each test starts a fresh game (seed 7, always-max rolls, so May's random pick
is the last candidate in quest-number order). Every tip goes through
game.do_turn(). Quest states and story flags the hints depend on are set
directly unless a cheap command triggers them; the player is moved between
rooms directly.

Run with (from c:\\zork_awt\\roundabout):
    py -m pytest test_may_hints.py -v
"""

import io
import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(__file__))

import test_walkthrough_fullscore_v2 as fullscore
from content import quests
from content import may_hints as mh

_RESP = {1: "That's worth something", 2: "That buys you something worth hearing",
         3: '"Tester," she says'}


class MayHintsBase(unittest.TestCase):

    def setUp(self):
        # Some tests call setUp() again mid-test for a fresh game; stop the
        # patches already running first, or they outlive this file.
        self.tearDown()
        self._patches = [
            patch("random.randint", fullscore._always_max),
            patch("content.char_create.input", fullscore._make_input_feed()),
        ]
        for p in self._patches:
            p.start()
        self.fresh()

    def fresh(self):
        """A new game in the Bar (patches stay as set up)."""
        self.game, self.w = fullscore._make_game()
        self.w.globals["zenni"] = 100
        self.w.globals["player_name"] = "Tester"
        # Quests 19&30 are sold from the start of the game (before discovery), so
        # May always has them. Mark them bought; the 19&30 tests clear this.
        mh._bought(self.w).extend(["19.1", "19.2", "19.3"])
        self.go("BAR")

    def tearDown(self):
        for p in getattr(self, "_patches", []):
            p.stop()
        self._patches = []

    def go(self, room):
        with patch("sys.stdout", io.StringIO()):
            self.game.enter_room(self.w.rooms[room])

    def do(self, cmd):
        buf = io.StringIO()
        with patch("sys.stdout", buf):
            self.game.do_turn(cmd)
        return buf.getvalue()

    def tip(self, amount):
        return self.do(f"tip may {amount}")

    def assertNothing(self, out):
        self.assertIn(mh._NOTHING[-1], out)     # always-max picks the third line


class TestTipping(MayHintsBase):

    def test_not_in_the_bar(self):
        quests.discover(self.w, "59")
        self.go("TALE-AND-ALE")
        self.assertIn("May isn't here.", self.tip(3))
        self.assertEqual(self.w.globals["zenni"], 100)

    def test_no_amount_zero_over_and_short(self):
        quests.discover(self.w, "59")
        self.assertIn('"How much?"', self.do("tip may"))
        self.assertIn("That's nothing", self.tip(0))
        self.assertIn("I appreciate the thought, but no", self.tip(13))
        self.w.globals["zenni"] = 2
        self.assertIn("You're short", self.tip(3))
        self.assertEqual(self.w.globals["zenni"], 2)
        self.assertEqual(mh._bought(self.w), ["19.1", "19.2", "19.3"])   # nothing new

    def test_number_words_and_zenni_suffix(self):
        quests.discover(self.w, "59")
        self.assertIn(mh._Q59, self.do("tip may three zenni"))
        self.assertEqual(self.w.globals["zenni"], 97)

    def test_tip_without_her_name_tips_may(self):
        quests.discover(self.w, "59")
        self.assertIn(mh._Q59, self.do("tip 2"))
        self.assertIn('"How much?"', self.do("tip"))

    def test_nothing_to_share_refunds(self):
        self.assertNothing(self.tip(5))
        self.assertEqual(self.w.globals["zenni"], 100)

    def test_response_follows_amount_and_zenni_taken(self):
        for amount, tier in ((1, 1), (3, 1), (4, 2), (6, 2), (7, 3), (12, 3)):
            with self.subTest(amount=amount):
                self.setUp()
                quests.discover(self.w, "32")
                out = self.tip(amount)
                self.assertIn(_RESP[tier], out)
                self.assertIn(mh._Q32[0], out)          # first hint; tiers in order
                self.assertEqual(self.w.globals["zenni"], 100 - amount)
                self.tearDown()

    def test_low_tip_never_buys_a_higher_tier(self):
        quests.discover(self.w, "32")
        self.assertIn(mh._Q32[0], self.tip(3))
        self.assertNothing(self.tip(3))                  # next is Tier 2
        self.assertEqual(self.w.globals["zenni"], 97)
        self.assertIn(mh._Q32[1], self.tip(4))

    def test_exact_tier_first_then_next_lower(self):
        quests.discover(self.w, "32")
        quests.discover(self.w, "59")
        mh._bought(self.w).extend(["32a.1", "32a.2"])   # 32's next hint is Tier 3
        self.assertIn(mh._Q32[2], self.tip(7))
        self.assertIn(mh._Q59, self.tip(7))              # no Tier 3 or 2 left: Tier 1
        self.assertNothing(self.tip(7))

    def test_steps_down_to_tier_2_before_tier_1(self):
        quests.discover(self.w, "32")
        quests.discover(self.w, "59")
        mh._bought(self.w).append("32a.1")               # 32 next: Tier 2; 59: Tier 1
        self.assertIn(mh._Q32[1], self.tip(7))

    def test_random_pick_among_the_tier(self):
        quests.discover(self.w, "24")
        quests.discover(self.w, "59")
        self.assertIn(mh._Q59, self.tip(2))              # always-max: last in order
        self.assertIn(mh._Q24, self.tip(2))
        self.assertNothing(self.tip(2))                  # never re-sold

    def test_undiscovered_and_complete_quests_get_nothing(self):
        self.assertNothing(self.tip(2))                  # 24 undiscovered
        quests.complete(self.w, "24")
        self.assertNothing(self.tip(2))


class TestQuestHints(MayHintsBase):

    def test_one_tier_quests(self):
        for q, text in (("24", mh._Q24), ("25", mh._Q25), ("27", mh._Q27),
                        ("42", mh._Q42), ("59", mh._Q59)):
            with self.subTest(quest=q):
                self.setUp()
                quests.discover(self.w, q)
                self.assertIn(text, self.tip(9))
                self.tearDown()

    def test_19_and_30_sold_before_discovery_and_discover(self):
        mh._bought(self.w).clear()
        self.assertIn(mh._Q19_STATUE, self.tip(1))
        self.assertTrue(quests.is_discovered(self.w, "19"))
        self.assertTrue(quests.is_discovered(self.w, "30"))
        self.assertIn(mh._Q19[1], self.tip(4))           # Path A: the Librarian
        self.assertIn(mh._Q19[2], self.tip(7))
        self.assertNothing(self.tip(7))

    def test_19_tier_1_after_the_statue_is_examined(self):
        mh._bought(self.w).clear()
        self.go("TOWN-SQUARE")
        self.do("look at statue")
        self.go("BAR")
        self.assertIn(mh._Q19[0], self.tip(1))           # the Keeper has gone missing

    def test_19_stops_when_the_werewolf_dies(self):
        mh._bought(self.w).clear()
        quests.complete(self.w, "19")
        self.assertNothing(self.tip(1))

    def test_4_from_the_first_lower_tier_descent(self):
        self.assertNothing(self.tip(1))
        self.go("PILE-OF-RUBBLE")
        self.go("BAR")
        self.assertIn(mh._Q4, self.tip(1))
        self.assertTrue(quests.is_discovered(self.w, "4"))

    def test_34_late_hint(self):
        quests.complete(self.w, "28")
        mh._bought(self.w).append("4.1")                 # the descent unlocks Quest 4's too
        self.go("PILE-OF-RUBBLE")
        for _ in range(mh.LATE_HINT_TURNS - 1):
            self.do("wait")
        self.go("BAR")
        self.assertNothing(self.tip(1))                  # 49 turns down there
        self.go("PILE-OF-RUBBLE")
        self.do("wait")
        self.go("BAR")
        self.assertIn(mh._Q34, self.tip(1))
        self.assertFalse(quests.is_discovered(self.w, "34"))

    def test_34_not_once_the_door_is_found(self):
        quests.complete(self.w, "28")
        self.w.set_global("LOWER-TIER-TURNS", 60)
        quests.discover(self.w, "34")
        self.assertNothing(self.tip(1))

    def test_17_phases(self):
        quests.discover(self.w, "17")
        self.assertIn(mh._Q17_BEFORE[0], self.tip(1))
        self.go("CHUCKLE-ENTRANCE")
        self.go("BAR")
        self.assertIn(mh._Q17_AFTER[0], self.tip(1))     # Tier 1 again; before-visit 2–3 gone
        self.assertIn(mh._Q17_AFTER[1], self.tip(4))
        self.assertNothing(self.tip(7))
        self.w.set_global("GHOST-FREED", True)
        self.assertIn(mh._Q17_CHARTER[0], self.tip(2))
        self.assertNothing(self.tip(2))

    def test_32_phases(self):
        quests.discover(self.w, "32")
        self.assertIn(mh._Q32[0], self.tip(1))
        self.w.set_global("ROWAN-QUEST-STARTED", True)
        self.assertIn(mh._Q32_CART, self.tip(5))         # one-tier: Tier 1
        self.assertNothing(self.tip(5))
        self.setUp()
        quests.discover(self.w, "32")
        self.w.set_global("ROWAN-QUEST-STARTED", True)
        self.w.set_global("GRAVESTONE-RETURNED", True)
        self.assertNothing(self.tip(1))

    def test_49_only_while_the_aqueduct_is_broken(self):
        quests.discover(self.w, "49")
        self.assertIn(mh._Q49[0], self.tip(1))
        quests.complete(self.w, "22")
        self.assertNothing(self.tip(4))


class TestGiveZenniAsTip(MayHintsBase):
    """GIVE / HAND / PAY Zenni to May is a tip (mechanics.md — TIP MAY)."""

    def test_give_forms_tip(self):
        for cmd in ("give 3 zenni to may", "give may 3 zenni", "hand may three zenni",
                    "pay may 3", "give the bartender 3 zenni"):
            self.fresh()
            quests.discover(self.w, "59")
            out = self.do(cmd)
            self.assertIn(_RESP[1], out, cmd)
            self.assertEqual(self.w.globals["zenni"], 97, cmd)

    def test_no_amount_asks_how_much(self):
        self.assertIn('"How much?"', self.do("give zenni to may"))
        self.assertIn('"How much?"', self.do("pay may"))
        self.assertEqual(self.w.globals["zenni"], 100)

    def test_short_and_over(self):
        self.assertIn("I appreciate the thought, but no", self.do("give 13 zenni to may"))
        self.w.globals["zenni"] = 2
        self.assertIn("You're short", self.do("give 3 zenni to may"))
        self.assertEqual(self.w.globals["zenni"], 2)

    def test_away_from_may_is_not_a_tip(self):
        self.go("TALE-AND-ALE")
        out = self.do("give 3 zenni to may")
        self.assertNotIn("May isn't here.", out)
        self.assertEqual(self.w.globals["zenni"], 100)

    def test_giving_an_item_is_still_give(self):
        out = self.do("give note to may")
        self.assertNotIn('"How much?"', out)
        self.assertEqual(self.w.globals["zenni"], 100)


if __name__ == "__main__":
    unittest.main(verbosity=2)
