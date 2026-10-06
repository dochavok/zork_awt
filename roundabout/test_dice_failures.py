"""
Every dice check needs a test of what happens when it fails.

The walkthroughs force every roll to its maximum (_always_max), so they only
ever see checks succeed: a perception check that never misses, a disarm that
never botches, a strength check that never slips. The failure side has to be
tested on purpose, with the roll fixed low.

This file scans content/ for every call to a dice check (CHECKS below) and
requires each call site to be listed in exactly one of:

  FAILURE_TESTS  — the test that fixes that check low and asserts the
                   designed outcome of failing it, or
  NOT_YET_TESTED — a known gap, with what the failure does.

So a new trap, hidden item or strength check fails this file until someone
writes its failure test (or, knowingly, lists it as a gap). A site is
"module.function: check" — the function that makes the call, and the call.

Run with: pytest roundabout/test_dice_failures.py  (from c:\\zork_awt)
"""

import ast
import glob
import os
import pytest

_HERE = os.path.dirname(__file__)

# content/player.py and content/perception.py — the level roll behind each
CHECKS = {
    "check_perception", "check_strength", "check_trap_disarm", "check_fishing",
    "roll_class_bonus", "reveal_if_found", "reveal_exit_if_found",
}
_DEFINED_IN = ("player", "perception")

FAILURE_TESTS = {
    "back_alley.back_alley_action: check_perception": "test_perception.py::test_class_perception_bonus",
    "bedroom.check_sprig: check_perception": "test_sprig_check.py::test_seventeen_misses",
    "chuckle.shatter_action: check_perception": "test_traps.py::test_trap16_crossbow_once_for_one_heart",
    "chuckle.shatter_action: roll_class_bonus": "test_traps.py::test_trap16_crossbow_once_for_one_heart",
    "combat_room._plate_on_arrival: check_perception": "test_traps.py::test_trap29_missed_plate_rings_the_bell_and_opens_the_den",
    "combat_room._plate_on_arrival: roll_class_bonus": "test_traps.py::test_trap29_botched_disarm_rings_the_bell",
    "combat_room.disarm_plate: roll_class_bonus": "test_traps.py::test_trap29_glasses_then_botched_disarm_fires",
    "flooding._on_arrival: check_perception": "test_traps.py::test_trap41_missed_plate_floods_the_room",
    "flooding._on_arrival: roll_class_bonus": "test_traps.py::test_trap41_botched_disarm_on_arrival_floods",
    "flooding.disarm_plate: roll_class_bonus": "test_traps.py::test_trap41_glasses_then_botched_disarm_floods",
    "gravestone.bog_se_enter: check_perception": "test_cellar_gravestone.py::test_gravestone_hidden_until_perception_easy",
    "inscription._disarm: check_trap_disarm": "test_traps.py::test_trap15_failed_disarm_leaves_the_lodestone_and_pays_nothing",
    "inscription._hanging_turn: check_strength": "test_traps.py::test_trap8_snare_fires_and_holds_until_pulled_free",
    "inscription.chamber_action: check_perception": "test_traps.py::test_trap8_snare_fires_and_holds_until_pulled_free",
    "inscription.vault_action: check_perception": "test_traps.py::test_trap15_unspotted_cannot_be_disarmed",
    "rooms.volcano_action: reveal_exit_if_found": "test_perception.py::test_hidden_exit_blocked_until_found",
    "shrine_path._check_trap19: check_perception": "test_traps.py::test_trap19_unnoticed_charge_shocks_on_lift_and_costs_a_turn",
    "shrine_path._check_trap19: roll_class_bonus": "test_traps.py::test_trap19_botched_discharge_shocks",
    "shrine_path.alcove_action: check_perception": "test_perception.py::test_tier_targets",
    "shrine_path.lift: roll_class_bonus": "test_traps.py::test_trap19_discharged_lift_needs_medium_strength",
    "tool_alcove.alcove_action: check_perception": "test_perception.py::test_tier_targets",
    "upper_tier.idol_action: check_perception": "test_traps.py::test_trap33_plate_described_only_once_spotted",
    "upper_tier.ink_corridor_action: check_perception": "test_traps.py::test_trap45_thread_inks_the_player",
    "upper_tier.ink_corridor_action: roll_class_bonus": "test_traps.py::test_trap45_thread_inks_the_player",
    "upper_tier.pry_idol_door: check_strength": "test_traps.py::test_trap33_pry_needs_crowbar_and_medium_strength_with_retries",
    "upper_tier.supply_action: check_perception": "test_traps.py::test_trap17_smoke_costs_a_heart_but_the_jar_is_still_there",
    "upper_tier.supply_action: roll_class_bonus": "test_traps.py::test_trap17_botched_disarm_still_smokes",
}

# Known gaps: the failure side runs in no test that checks it. Move an entry to
# FAILURE_TESTS when its test is written.
NOT_YET_TESTED = {
    "aqueduct.place_blocks: roll_class_bonus": "a block slips; nothing placed",
    "aqueduct.strike_timber: check_strength": "the timber holds",
    "bog.reveal: reveal_if_found": "bog log / thyme stay hidden this visit",
    "dankhaus.bog_se_action: check_perception": "the path to the Dankhaus stays hidden",
    "inscription._pry: check_strength": "a magnet-stuck item stays on the chest",
    "inscription.chamber_action: reveal_if_found": "dungeon rune stone stays hidden",
    "lynds.challenge: roll_class_bonus": "Lynds wins the arm-wrestle",
    "mid_tier.mine_action: reveal_if_found": "silver dust stays hidden",
    "mine.on_enter: check_perception": "the mine's weak point stays hidden",
    "mine_branch.on_enter: check_perception": "the Assay Room gap stays hidden",
    "old_oak.forest_action: reveal_if_found": "forest bowl piece stays hidden",
    "pond.fish: check_fishing": "the bottle slips off the hook",
    "pond.on_enter: check_perception": "the bottle in the pond goes unseen",
    "rooms.bog_sw_action: reveal_if_found": "bog bowl piece stays hidden",
    "rooms.tower_action: check_perception": "the bedroom door stays unseen",
    "ship._map_demon: check_perception": "the treasure map stays unfound; the check repeats",
    "shrine_path.shrine_action: reveal_if_found": "shrine bowl piece stays hidden",
    "tunnels.bridge_action: check_perception": "the Toll Bridge seal unseen; Quest 27 undiscovered",
    "tunnels.open_strongbox: roll_class_bonus": "the strongbox lid holds (locations.md — Strongbox stuck)",
    "vikings.archery_action: roll_class_bonus": "an arrow hits on the range",
    "vikings.drink_contest: roll_class_bonus": "Aylora wins a round",
    "whispering_jar._read: check_perception": "the jar's writing reads as worn",
    "zenni_rooms.on_enter: check_perception": "a room's Zenni stays unfound",
}


def _scan():
    """{site: count} for every dice-check call in content/."""
    sites = {}
    for path in sorted(glob.glob(os.path.join(_HERE, "content", "*.py"))):
        module = os.path.basename(path)[:-3]
        if module in _DEFINED_IN:
            continue
        with open(path, encoding="utf-8") as fh:
            tree = ast.parse(fh.read())

        def visit(node, func):
            for child in ast.iter_child_nodes(node):
                inner = child.name if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)) else func
                if isinstance(child, ast.Call):
                    f = child.func
                    name = f.id if isinstance(f, ast.Name) else f.attr if isinstance(f, ast.Attribute) else None
                    if name in CHECKS:
                        site = f"{module}.{func}: {name}"
                        sites[site] = sites.get(site, 0) + 1
                visit(child, inner)

        visit(tree, None)
    return sites


SITES = _scan()


def test_scan_finds_the_checks():
    # If this drops sharply, the scan (not the game) has broken
    assert len(SITES) >= 40


def test_every_dice_check_is_accounted_for():
    listed = set(FAILURE_TESTS) | set(NOT_YET_TESTED)
    new = sorted(set(SITES) - listed)
    assert not new, ("New dice checks — write a test that fixes the roll low and checks the "
                     "designed failure, then add it to FAILURE_TESTS:\n  " + "\n  ".join(new))
    gone = sorted(listed - set(SITES))
    assert not gone, "Listed sites no longer in content/ — remove them:\n  " + "\n  ".join(gone)


def test_no_site_is_both_tested_and_a_gap():
    assert sorted(set(FAILURE_TESTS) & set(NOT_YET_TESTED)) == []


def test_each_site_called_once_per_function():
    # Two calls of the same check in one function share a site and one test;
    # split the function (or extend the key) if that ever happens.
    assert {s: n for s, n in SITES.items() if n > 1} == {}


def _test_names(filename):
    with open(os.path.join(_HERE, filename), encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    return {n.name for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}


@pytest.mark.parametrize("site", sorted(FAILURE_TESTS))
def test_named_failure_test_exists(site):
    filename, test = FAILURE_TESTS[site].split("::")
    assert test.startswith("test_")
    assert test in _test_names(filename), f"{site}: {FAILURE_TESTS[site]} not found"
