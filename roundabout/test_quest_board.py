"""
Quest Board — postings, reading, discovery, removal (mechanics.md — Quest Board).

Each test starts a fresh game (the full-score walkthrough's setup: seed 7,
always-max rolls). The player is moved between rooms directly; every trigger
and every read of the board goes through game.do_turn().

Run with (from c:\\zork_awt\\roundabout):
    py -m pytest test_quest_board.py -v
"""

import io
import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(__file__))

import walkthrough_runner as wt
from content import quests
from content.quest_board import POSTINGS     # notice text — verbatim in mechanics.md

BOUNTY_TURN = 100      # mechanics.md — Quest 51 bounty at 100 turns
FLUTE_DELAY = 20       # mechanics.md — Quest 7, 20 turns after the ring hand-over

_HEADER = "Notices are pinned to the board, newer ones over older:"
_EMPTY = "The board holds nothing but pinholes"


class TestQuestBoard(unittest.TestCase):

    def setUp(self):
        self._patches = [
            patch("random.randint", wt._always_max),
            patch("content.char_create.input", wt._make_input_feed()),
        ]
        for p in self._patches:
            p.start()
        self.game, self.w = wt._make_game()

    def tearDown(self):
        for p in self._patches:
            p.stop()

    def go(self, room):
        with patch("sys.stdout", io.StringIO()):
            self.game.enter_room(self.w.rooms[room])

    def do(self, cmd):
        buf = io.StringIO()
        with patch("sys.stdout", buf):
            self.game.do_turn(cmd)
        return buf.getvalue()

    def read_board(self):
        self.go("BAR")
        return self.do("look at board")

    def wait(self, turns):
        for _ in range(turns):
            self.do("wait")

    # --- the board itself ---------------------------------------------------

    def test_bar_description_mentions_board(self):
        self.go("BAR")
        self.assertIn("things people want found or done", self.do("look"))

    def test_read_examine_and_nouns_all_list_the_board(self):
        self.go("BAR")
        for cmd in ("look at board", "read board", "examine notices",
                    "read notice", "look at quest board", "read notice board"):
            with self.subTest(cmd=cmd):
                self.assertIn(_HEADER, self.do(cmd))

    def test_game_start_notices_in_order(self):
        out = self.read_board()
        self.assertIn(_HEADER, out)
        self.assertLess(out.index(POSTINGS["22"]), out.index(POSTINGS["50"]))
        for q in ("40", "7", "17", "24", "51"):
            self.assertNotIn(POSTINGS[q], out)

    def test_empty_board(self):
        quests.complete(self.w, "22")
        from content import quest_board
        quest_board.remove(self.w, "50")
        out = self.read_board()
        self.assertIn(_EMPTY, out)
        self.assertNotIn(_HEADER, out)

    # --- discovery ----------------------------------------------------------

    def test_posting_alone_does_not_discover(self):
        self.assertFalse(quests.is_discovered(self.w, "22"))
        self.assertFalse(quests.is_discovered(self.w, "50"))

    def test_reading_discovers_what_it_shows(self):
        self.read_board()
        self.assertTrue(quests.is_discovered(self.w, "22"))
        self.assertTrue(quests.is_discovered(self.w, "50"))
        self.assertFalse(quests.is_discovered(self.w, "40"))

    def test_completed_quest_drops_off(self):
        quests.complete(self.w, "22")
        out = self.read_board()
        self.assertNotIn(POSTINGS["22"], out)
        self.assertIn(POSTINGS["50"], out)

    # --- postings by trigger ------------------------------------------------

    def test_kitchen_visit_posts_shamus(self):
        self.go("KITCHEN")
        out = self.read_board()
        self.assertLess(out.index(POSTINGS["50"]), out.index(POSTINGS["40"]))

    def test_flute_notice_twenty_turns_after_pyronicus(self):
        self.go("PYRONICUS-FORGE")
        self.assertIn("fell through my ceiling", self.do("talk to pyronicus"))
        self.wait(FLUTE_DELAY - 2)          # the talk was one turn, reading is another
        self.assertNotIn(POSTINGS["7"], self.read_board())
        self.wait(1)
        self.assertIn(POSTINGS["7"], self.read_board())

    def test_second_briefing_posts_records_worker(self):
        self.w.move_object(self.w.objects["RING"], self.w.player)
        self.go("WIZARDS-TOWER")
        self.do("give ring to will")
        self.assertTrue(self.w.get_global("SECOND-BRIEFING-DONE"))
        self.assertIn(POSTINGS["17"], self.read_board())

    def test_charter_posts_beekeeper(self):
        self.w.move_object(self.w.objects["POCKET-WATCH"], self.w.player)
        self.go("RECORDS-ROOM")
        self.do("give watch to clerk")
        self.assertTrue(quests.is_complete(self.w, "17"))
        self.assertIn(POSTINGS["24"], self.read_board())

    def test_bounty_at_100_turns(self):
        self.wait(BOUNTY_TURN - self.w.moves - 2)
        self.assertNotIn(POSTINGS["51"], self.read_board())
        self.wait(1)
        self.assertIn(POSTINGS["51"], self.read_board())

    def test_no_bounty_once_the_mugger_is_dead(self):
        self.w.set_global("MUGGER-DEAD", True)
        self.wait(BOUNTY_TURN)
        self.assertNotIn(POSTINGS["51"], self.read_board())

    # --- Quest 50's notice stays up until the quest is done -----------------
    # (Until 2026-10-14 it came down when Trap 41 was disarmed; the plate
    # can't be disarmed any more.)

    def test_the_flooding_room_leaves_the_apprentice_notice_up(self):
        self.go("FLOODING-ROOM")
        self.do("wait")
        self.assertTrue(self.w.get_global("FLOOD-FIRED"))
        self.assertIn(POSTINGS["50"], self.read_board())

    def test_freeing_the_apprentice_takes_the_notice_down(self):
        from content import trap_side
        self.read_board()                    # discovered
        self.go("LOST-APPRENTICES-CELL")
        with patch("sys.stdout", io.StringIO()):
            trap_side._freed(self.w)         # he digs out; Quest 50 completes
        self.assertNotIn(POSTINGS["50"], self.read_board())


if __name__ == "__main__":
    unittest.main(verbosity=2)
