"""
Floor listings and the torch (mechanics.md):
- Plural and mass names: "There are lockpicks here." / "There is some charcoal here."
- Anything reaching the player's hands (bought, handed over) is touched, so a
  dropped item shows its own line, not its first-sight one.
- A burnt-out torch dropped leaves the game (back in Shamus's stock); BUY TORCH
  sells a fresh one. A lit torch left elsewhere is replaced by the fresh one.
Run with: pytest roundabout/test_floor_listing.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do
from content import init, light


def _hold(w, name):
    obj = w.objects[name]
    obj.flags.discard("INVISIBLE")
    w.move_object(obj, w.player)
    return obj


def _goto(w, name):
    w.move_object(w.player, w.rooms[name])
    w.here = w.rooms[name]


def test_plural_and_mass_listings():
    w, g = _make_world(cls="warrior")
    for name, article in init._ARTICLES.items():
        obj = _hold(w, name)
        assert "You drop" in _do(g, f"drop {obj.synonyms[0]}"), name
        out = _do(g, "look")
        if article == "plural":
            assert f"There are {obj.desc} here." in out, name
        else:
            assert f"There is some {obj.desc} here." in out, name
        w.move_object(obj, None)


def test_ordinary_item_keeps_a_or_an():
    w, g = _make_world(cls="warrior")
    _hold(w, "BOW")
    _do(g, "drop bow")
    assert "There is a bow here." in _do(g, "look")


def test_bought_torch_dropped_lit_shows_its_own_line():
    w, g = _make_world(cls="warrior")
    _goto(w, "KITCHEN")
    _do(g, "buy torch")
    _do(g, "drop torch")
    out = _do(g, "look")
    assert "A lit torch." in out
    assert "A torch.\n" not in out


def test_burnt_out_torch_dropped_leaves_the_game():
    w, g = _make_world(cls="warrior")
    _goto(w, "KITCHEN")
    _do(g, "buy torch")
    light._burn_out(w)
    out = _do(g, "drop torch")
    assert "You toss the burnt-out torch aside. It's no good to anyone now." in out
    torch = w.objects["TORCH"]
    assert torch.location is None
    assert "burnt-out torch" not in _do(g, "look")
    # Shamus sells a fresh one
    zenni = w.globals["zenni"]
    out = _do(g, "buy torch")
    assert "slides the torch across the counter" in out
    assert torch.location is w.player and torch.has_flag("ONBIT")
    assert torch.desc == "torch" and torch.ldesc == "A lit torch."
    assert w.globals["zenni"] == zenni - 3


def test_burnt_out_torch_dropped_with_drop_all():
    w, g = _make_world(cls="warrior")
    _goto(w, "KITCHEN")
    _do(g, "buy torch")
    light._burn_out(w)
    _hold(w, "BOW")
    out = _do(g, "drop all")
    assert "You toss the burnt-out torch aside." in out
    assert w.objects["TORCH"].location is None


def test_lit_torch_left_elsewhere_is_replaced():
    w, g = _make_world(cls="warrior")
    _goto(w, "KITCHEN")
    _do(g, "buy torch")
    _goto(w, "TOWN-SQUARE")
    _do(g, "drop torch")
    _goto(w, "KITCHEN")
    out = _do(g, "buy torch")
    assert "slides the torch across the counter" in out
    torch = w.objects["TORCH"]
    assert torch.location is w.player
    assert torch not in w.rooms["TOWN-SQUARE"].contents
    assert w.get_global("TORCH-LIT-TIMER") is None


def test_carried_torch_still_goes_to_the_exchange():
    w, g = _make_world(cls="warrior")
    _goto(w, "KITCHEN")
    _do(g, "buy torch")
    assert "plenty of life left" in _do(g, "buy torch")


# A torch left lying in another room burns down unseen: no warnings, no
# burnout line, no stranded check. Carried or on the floor of the player's
# room, it gets them all (mechanics.md — Torch).

def _tick(w, g, left, where):
    import io
    from unittest.mock import patch
    _goto(w, "KITCHEN")
    _do(g, "buy torch")
    torch = w.objects["TORCH"]
    if where != "carried":
        w.move_object(torch, w.rooms[where])
    w.set_global("TORCH-LIT-TIMER", left)
    light._ensure_clock(w)
    buf = io.StringIO()
    with patch("sys.stdout", buf):
        light._torch_demon(w)
    return buf.getvalue(), torch


def test_carried_torch_still_warns_and_burns_out():
    w, g = _make_world(cls="warrior")
    out, _ = _tick(w, g, 51, "carried")
    assert light._WARNINGS[50] in out
    w, g = _make_world(cls="warrior")
    out, torch = _tick(w, g, 1, "carried")
    assert light._BURNOUT_SAFE in out
    assert not torch.has_flag("ONBIT")


def test_torch_left_lying_warns_nobody():
    for left in light._WARNINGS:
        w, g = _make_world(cls="warrior")
        out, _ = _tick(w, g, left + 1, "TOWN-SQUARE")
        assert out == "", left


def test_torch_left_lying_burns_out_silently():
    w, g = _make_world(cls="warrior")
    out, torch = _tick(w, g, 1, "TOWN-SQUARE")
    assert out == ""
    assert not torch.has_flag("ONBIT") and torch.desc == "burnt-out torch"
    assert w.get_global("TORCH-LIT-TIMER") is None


def test_torch_left_lying_is_no_game_over_in_the_dark():
    # The player is in a dark room with no light; the torch is elsewhere.
    w, g = _make_world(cls="warrior")
    _goto(w, "KITCHEN")
    _do(g, "buy torch")
    w.move_object(w.objects["TORCH"], w.rooms["TOWN-SQUARE"])
    _goto(w, "COMBAT-ROOM")
    w.set_global("TORCH-LIT-TIMER", 1)
    import io
    from unittest.mock import patch
    buf = io.StringIO()
    with patch("sys.stdout", buf):
        light._torch_demon(w)
    assert buf.getvalue() == ""
    assert not w.get_global("GAME-OVER")


def test_torch_on_the_floor_here_still_warns():
    w, g = _make_world(cls="warrior")
    out, _ = _tick(w, g, 51, "KITCHEN")      # dropped where the player stands
    assert light._WARNINGS[50] in out
    w, g = _make_world(cls="warrior")
    out, torch = _tick(w, g, 1, "KITCHEN")
    assert light._BURNOUT_SAFE in out
    assert not torch.has_flag("ONBIT")


def test_torch_on_the_floor_here_goes_out_in_the_dark():
    # Dropped in a dark room and left there: the same as holding it.
    import io
    from unittest.mock import patch
    w, g = _make_world(cls="warrior")
    _goto(w, "KITCHEN")
    _do(g, "buy torch")
    _goto(w, "COMBAT-ROOM")
    w.move_object(w.objects["TORCH"], w.here)
    w.set_global("TORCH-LIT-TIMER", 1)
    buf = io.StringIO()
    with patch("sys.stdout", buf):
        light._torch_demon(w)
    assert light._BURNOUT_FATAL in buf.getvalue()
    assert w.get_global("GAME-OVER")
