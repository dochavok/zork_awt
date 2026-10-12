# Roundabout: The God-Forsaken Ring — Open Design Questions

Consolidated from all source files. Update this file when items are resolved; record the resolution and the source file where it was written.
Resolved items are removed; their history is in git (last full lists: commit 7eec353 for TODO #1–#6, b9e5feb for #7–#8).

**Policy:** When a new walkthrough test fails, fix the engine. Never adjust the narrative or add state injection to make a test pass. Only fix the walkthrough when the design doc confirms the walkthrough is wrong.

---

### TODO #9 — Syntax actions with no default handler (found 2026-10-12)

`PUT X IN Y` printed nothing because `V-PUT-IN` was in the syntax table with no registered verb handler; when no object or room action takes such a command, the engine prints nothing (`engine/game.py`, `_perform_chain` step 7). `V-PUT-IN` is fixed. These actions are still in `content/syntax.py` with no default handler:

`V-BOARD`, `V-BREATHE`, `V-BRUSH`, `V-BURN`, `V-CAST`, `V-CLIMB-DOWN`, `V-CLIMB-UP`, `V-CLOSE`, `V-COUNT`, `V-CROSS`, `V-CUT`, `V-ENCHANT`, `V-FILL`, `V-FOLLOW`, `V-HOLD-NEAR`, `V-INFLATE`, `V-KICK`, `V-KNOCK`, `V-LAMP-OFF`, `V-LEAN`, `V-LOCK`, `V-LOOK-INSIDE`, `V-LOOK-UNDER`, `V-LOWER`, `V-LUBRICATE`, `V-MAKE`, `V-MELT`, `V-PICK`, `V-PLUG`, `V-PUMP`, `V-PUT`, `V-REST`, `V-RING`, `V-ROLL`, `V-RUB`, `V-SHAKE`, `V-SPIN`, `V-SQUEEZE`, `V-SWING`, `V-TAKE-FROM`, `V-THROW`, `V-TIE`, `V-TIP`, `V-TURN`, `V-TURN-OFF`, `V-UNTIE`, `V-WIND`.

Some work through input hooks or object/room actions (e.g. `CAST`), so not all are silent in play. For each: check whether it can print nothing; if so, give it a default line (design text in `mechanics.md` — Parser Verbs) or drop the syntax rule. Then add a guard test that every syntax action answers with an object (`test_system_verbs.py` only checks bare verbs today).
