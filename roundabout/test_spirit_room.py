"""
The Spirit Room (locations.md — Spirit Room): visible there with no way to turn
invisible — no ring, a bound ring, or ink — is GAME OVER, with the first reason
that applies. A working ring carried but not worn is safe.
Run with: pytest roundabout/test_spirit_room.py  (from c:\\zork_awt)
"""

import sys
import os
import pytest
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do
from content.dark_branch import (
    _TRAPPED_NO_RING, _TRAPPED_BOUND, _TRAPPED_INKED, _TRAPPED_END, _SPIRITS_SEE,
    _SPIRITS_IGNORE, _BLOCKED,
)


def _walk_in(ring=True, worn=False, bound=False, inked=False):
    """From the Burial Chamber, north into the Spirit Room."""
    w, g = _make_world()
    w.set_global("LIGHT-SPELL-ACTIVE", True)
    if ring:
        w.move_object(w.objects["RING"], w.player)
    w.globals["ring_worn"] = worn
    w.globals["ring_bound"] = bound
    w.set_global("INKED", inked)
    w.move_object(w.player, w.rooms["BURIAL-CHAMBER"])
    w.here = w.rooms["BURIAL-CHAMBER"]
    return w, g, _do(g, "north")


@pytest.mark.parametrize("kwargs,reason", [
    (dict(ring=False), _TRAPPED_NO_RING),
    (dict(ring=False, inked=True), _TRAPPED_NO_RING),         # no ring comes first
    (dict(bound=True), _TRAPPED_BOUND),
    (dict(bound=True, inked=True), _TRAPPED_BOUND),           # then the bound ring
    (dict(inked=True), _TRAPPED_INKED),
    (dict(worn=True, inked=True), _TRAPPED_INKED),            # ink cancels a worn ring
])
def test_trapped_is_game_over_with_the_first_reason(kwargs, reason):
    w, g, out = _walk_in(**kwargs)
    assert _SPIRITS_SEE in out
    assert out.index(_SPIRITS_SEE) < out.index(reason) < out.index(_TRAPPED_END)
    for other in (_TRAPPED_NO_RING, _TRAPPED_BOUND, _TRAPPED_INKED):
        if other != reason:
            assert other not in out
    assert "*** GAME OVER ***" in out
    assert w.get_global("GAME-OVER") is True


def test_working_ring_carried_is_safe_then_wearing_it_lets_you_through():
    w, g, out = _walk_in()
    assert _SPIRITS_SEE in out and _TRAPPED_END not in out
    assert not w.get_global("GAME-OVER")
    assert _BLOCKED in _do(g, "south")
    _do(g, "wear ring")
    _do(g, "north")
    assert w.here.name == "DARK-ROOM"


def test_ring_on_the_floor_here_is_still_in_reach():
    w, g, out = _walk_in(worn=True)
    assert _SPIRITS_IGNORE in out
    _do(g, "remove ring")
    _do(g, "drop ring")
    assert not w.get_global("GAME-OVER")
