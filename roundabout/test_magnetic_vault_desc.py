"""
Magnetic Vault room description (locations.md — Magnetic Vault): default,
spotted, and after the trap (lodestone out or pulse fired).
Run with: pytest roundabout/test_magnetic_vault_desc.py  (from c:\\zork_awt)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world, _do
from content import inscription as ins


def _vault():
    w, g = _make_world(cls="warrior")
    w.move_object(w.player, w.rooms["MAGNETIC-VAULT"])
    w.here = w.rooms["MAGNETIC-VAULT"]
    w.set_global("LIGHT-SPELL-ACTIVE", True)
    return w, g


def test_default_description():
    w, g = _vault()
    out = _do(g, "look")
    assert ins._VAULT_DEFAULT in out
    assert ins._VAULT_AFTER not in out


def test_spotted_description():
    w, g = _vault()
    w.set_global("VAULT-SPOTTED", True)
    out = _do(g, "look")
    assert ins._VAULT_SPOTTED in out
    assert ins._VAULT_DEFAULT not in out


def test_after_lodestone_removed():
    w, g = _vault()
    w.set_global("VAULT-SPOTTED", True)
    w.set_global("LODESTONE-STATE", "removed")
    out = _do(g, "look")
    assert ins._VAULT_AFTER in out
    assert "faint ring" not in out
    assert ins._VAULT_SPOTTED not in out


def test_after_pulse_fired_keeps_stuck_line():
    w, g = _vault()
    w.move_object(w.objects["SHOVEL"], w.player)
    _do(g, "open chest")
    out = _do(g, "look")
    assert ins._VAULT_AFTER in out
    assert "faint ring" not in out
    assert "Stuck fast to the side of the chest" in out and "shovel" in out
