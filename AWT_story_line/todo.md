# Roundabout: The God-Forsaken Ring — Open Design Questions

Consolidated from all source files. Update this file when items are resolved; record the resolution and the source file where it was written.
Resolved items are removed; their history is in git (last full lists: commit 7eec353 for TODO #1–#6, b9e5feb for #7–#8, fecb0f2 for #9).

**Policy:** When a new walkthrough test fails, fix the engine. Never adjust the narrative or add state injection to make a test pass. Only fix the walkthrough when the design doc confirms the walkthrough is wrong.

---

### TODO #13 — Rules that only look in the room (found 2026-10-12)

Some rules only look at the room (`_og_ir`), so naming a carried item gives "You can't see any X here!" — fixed for `CROSS`, `HOLD NEAR`, `SEAL`, `SWING`, `THROW`, `TIP`; still so for `ATTACK` / `KILL` / `STAB` / `SHOOT`, `EXORCISE`, `DISARM`, `JUMP ON`, `WALK` (and `TALK` / `PAY` / `CHALLENGE` / `GIVE … TO`, where wanting a person here is reasonable).

For each: should a carried item be accepted (most should — then the action needs a sensible line for it), or is "not here" the right answer (a person to talk to, pay or challenge)? Then widen the rule's locations and extend the guard test to cover held objects.

---

### TODO #12 — Let a verb handler skip the turn (found 2026-10-12)

The engine skips the turn only for whole actions (`_SKIP_CLOCK` in `engine/game.py`). Commands whose refusals take no turn but whose success does — `REST`, `CAST`, `COUNT ZENNI`, `CROSS` on a bridge — are therefore input hooks that read the raw line, not verbs, and have no syntax rule (signpost comments in `content/syntax.py`). Fix: let a verb handler return a "no turn" result (like `HOOK_NO_TURN`), then make these ordinary verbs and retire the hooks. Engine change; tests for each command's turn use already exist.

---

### TODO #11 — Pathing issues (found 2026-10-12)

1. Up through the mine after the explosion.
2. Aqueduct corridor clearing through the Portcullis room.

Details to be gathered from play; check each route against locations.md.

---

### TODO #10 — Pre-release antivirus steps in operations.md (found 2026-10-12)

A player using ESET couldn't open the v2.5 .exe (permission error, most likely quarantine). The .exe was uploaded to VirusTotal afterwards; waiting to hear whether their next download gets through. Once known, add to operations.md (Antivirus false positives) whichever steps actually helped: e.g. uploading each new build to VirusTotal before announcing it, and submitting false positives to the engines that flag it (ESET: in-product Tools → Submit sample for analysis, or samples@eset.com).
