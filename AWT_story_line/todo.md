# Roundabout: The God-Forsaken Ring — Open Design Questions

Consolidated from all source files. Update this file when items are resolved; record the resolution and the source file where it was written.
Resolved items are removed; their history is in git (last full list: commit 7eec353).

**Policy:** When a new walkthrough test fails, fix the engine. Never adjust the narrative or add state injection to make a test pass. Only fix the walkthrough when the design doc confirms the walkthrough is wrong.

---

## TODO #7 — Stored Room doesn't show as Hole to Below — RESOLVED 2026-10-09

Found in play: after the Stored Room collapses, it showed as the Stored Room instead of the Hole to Below — only after a RESTORE. Cause: a save doesn't keep room names, and the rename was done once, in play. Kevry's House had the same bug (reverted to "A House").
Resolution: renamed rooms take their name from their flag (STORED-ROOM-DUG, KEVRY-MET) through one rule each, applied in play and after every restore, so old saves restore right too. Written to mechanics.md (Save and Restore); built in engine/game.py (register_room_name, apply_room_names) and engine/savegame.py; tests in test_room_names.py, including a guard that refuses any direct room rename in content.

## TODO #8 — Ring messages in ticks 40–50 don't appear every turn — RESOLVED 2026-10-09

Found in play: from tick 40 to 50, no corruption message appeared each turn. The design only had messages at ticks 10, 25 and 40 (the late-stage removal roll shows text only on REMOVE RING).
Resolution: ticks 41–49 each get a line — the player's own voice giving way. Written to mechanics.md (The God-Forsaken Ring — Milestone messages); built in content/corruption.py; tests in test_corruption.py.
