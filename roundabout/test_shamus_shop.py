"""
Shamus's stock (npcs.md — Shamus; locations.md — Kitchen: no items).

The stock isn't in the world until it's bought, so nothing in the Kitchen can be
taken for free. BUY X in the Kitchen sells it. Each test starts a fresh game;
the player is moved to the Kitchen directly and every command goes through
game.do_turn().

Run with (from c:\\zork_awt\\roundabout):
    py -m pytest test_shamus_shop.py -v
"""

import io
import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(__file__))

import test_walkthrough_fullscore_v2 as fullscore

_STOCK = {"GUNPOWDER": 5, "TORCH": 3, "FISHING-ROD": 8, "THIN-PAPER": 2}


class TestShamusShop(unittest.TestCase):

    def setUp(self):
        self._patches = [
            patch("random.randint", fullscore._always_max),
            patch("content.char_create.input", fullscore._make_input_feed()),
        ]
        for p in self._patches:
            p.start()
        self.game, self.w = fullscore._make_game()
        self.w.globals["zenni"] = 50
        with patch("sys.stdout", io.StringIO()):
            self.game.enter_room(self.w.rooms["KITCHEN"])

    def tearDown(self):
        for p in self._patches:
            p.stop()

    def do(self, cmd):
        buf = io.StringIO()
        with patch("sys.stdout", buf):
            self.game.do_turn(cmd)
        return buf.getvalue()

    def held(self, name):
        return self.w.objects[name] in self.w.player.contents

    def test_stock_not_on_the_kitchen_floor(self):
        out = self.do("look")
        for text in ("gunpowder", "A torch", "fishing rod", "thin paper"):
            self.assertNotIn(text, out)

    def test_nothing_taken_for_free(self):
        for cmd in ("take torch", "take gunpowder", "take rod", "take paper", "take all"):
            with self.subTest(cmd=cmd):
                self.do(cmd)
                for name in _STOCK:
                    self.assertFalse(self.held(name))
        self.assertEqual(self.w.globals["zenni"], 50)

    def test_buy_each_item(self):
        for cmd, name in (("buy gunpowder", "GUNPOWDER"), ("buy torch", "TORCH"),
                          ("buy fishing rod", "FISHING-ROD"), ("buy thin paper", "THIN-PAPER")):
            with self.subTest(cmd=cmd):
                before = self.w.globals["zenni"]
                self.assertIn("Anything else?", self.do(cmd))
                self.assertTrue(self.held(name))
                self.assertEqual(self.w.globals["zenni"], before - _STOCK[name])

    def test_short_names(self):
        self.do("buy rod")
        self.do("buy the paper")
        self.assertTrue(self.held("FISHING-ROD"))
        self.assertTrue(self.held("THIN-PAPER"))

    def test_bought_torch_is_lit(self):
        self.do("buy torch")
        self.assertTrue(self.w.objects["TORCH"].has_flag("ONBIT"))

    def test_short_of_zenni(self):
        self.w.globals["zenni"] = 4
        self.assertIn("You don't have enough Zenni", self.do("buy gunpowder"))
        self.assertFalse(self.held("GUNPOWDER"))
        self.assertEqual(self.w.globals["zenni"], 4)

    def test_buy_torch_while_carrying_one_is_the_exchange(self):
        self.do("buy torch")
        zenni = self.w.globals["zenni"]
        out = self.do("buy torch")
        self.assertNotIn("Anything else?", out)          # not a second torch
        self.assertEqual(self.w.globals["zenni"], zenni)   # fresh torch: swap refused
        self.assertTrue(self.held("TORCH"))

    def test_already_holding_one(self):
        for cmd in ("buy gunpowder", "buy fishing rod", "buy thin paper"):
            with self.subTest(cmd=cmd):
                self.do(cmd)
                zenni = self.w.globals["zenni"]
                self.assertIn("You've already got one.", self.do(cmd))
                self.assertEqual(self.w.globals["zenni"], zenni)

    def test_not_sold_outside_the_kitchen(self):
        with patch("sys.stdout", io.StringIO()):
            self.game.enter_room(self.w.rooms["BAR"])
        self.do("buy torch")
        self.assertFalse(self.held("TORCH"))
        self.assertEqual(self.w.globals["zenni"], 50)


if __name__ == "__main__":
    unittest.main(verbosity=2)
