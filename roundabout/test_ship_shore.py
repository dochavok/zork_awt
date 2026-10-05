"""
Ship and shore (locations.md — Pie Rat Ship, The Sea, Desert Island, Kevry's
Island). Ship and shore connect only by LAND / DOCK and BOARD SHIP. Land, Ho!
is the last sea square, off Kevry's island; the Empty Beach is the shore.

Each test starts a fresh game; the player is moved directly to the starting
room and every command goes through game.do_turn().

Run with (from c:\\zork_awt\\roundabout):
    py -m pytest test_ship_shore.py -v
"""

import io
import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(__file__))

import test_walkthrough_fullscore_v2 as fullscore

_INTO_SEA = "The ocean offers no opinion on that idea"


class TestShipShore(unittest.TestCase):

    def setUp(self):
        self._patches = [
            patch("random.randint", fullscore._always_max),
            patch("content.char_create.input", fullscore._make_input_feed()),
        ]
        for p in self._patches:
            p.start()
        self.game, self.w = fullscore._make_game()
        self.w.set_global("PIE-RATS-GONE", True)

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

    def at(self, room):
        self.assertEqual(self.w.here.name, room)

    # --- no walking between ship and shore ------------------------------------

    def test_empty_beach_west_is_the_sea(self):
        self.go("EMPTY-BEACH")
        self.assertIn(_INTO_SEA, self.do("west"))
        self.at("EMPTY-BEACH")

    def test_desert_island_north_is_the_sea(self):
        self.go("DESERT-ISLAND")
        self.assertIn(_INTO_SEA, self.do("north"))
        self.at("DESERT-ISLAND")

    def test_no_sailing_onto_desert_island(self):
        self.go("SEA-EAST")
        self.do("south")
        self.at("SEA-EAST")

    def test_land_ho_east_needs_landing(self):
        self.go("LAND-HO")
        self.assertIn("You'll have to land the ship.", self.do("east"))
        self.at("LAND-HO")

    # --- Land, Ho! is at sea ----------------------------------------------------

    def test_sail_east_from_69_reaches_land_ho_at_sea(self):
        self.go("OPEN-OCEAN-69")
        self.w.set_global("AT-SEA", True)
        self.assertIn("Land, Ho!", self.do("go east"))
        self.at("LAND-HO")
        self.assertIn("There's no ship to board here.", self.do("board ship"))

    def test_no_landing_at_69(self):
        self.go("OPEN-OCEAN-69")
        self.assertIn("There's no place to land here.", self.do("land"))

    def test_land_at_land_ho_puts_you_on_the_beach(self):
        self.go("LAND-HO")
        self.assertIn("Empty Beach", self.do("land"))
        self.at("EMPTY-BEACH")

    def test_board_at_the_beach_and_sail_home(self):
        self.go("EMPTY-BEACH")
        self.do("board ship")
        self.at("SHIP-DECK")
        self.assertIn("Empty Beach", self.do("land"))   # moored off Land, Ho!
        self.do("board ship")
        self.do("set sail")
        self.do("go west")
        self.at("OPEN-OCEAN-69")

    def test_desert_island_by_land_and_board(self):
        self.go("SEA-EAST")
        self.assertIn("Desert Island", self.do("land"))
        self.do("board ship")
        self.at("SHIP-DECK")
        self.assertIn("Desert Island", self.do("land"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
