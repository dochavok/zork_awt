# Roundabout: The God-Forsaken Ring — Open Design Questions

Consolidated from all source files. Update this file when items are resolved; record the resolution and the source file where it was written.
Resolved items are removed; their history is in git (last full lists: commit 7eec353 for TODO #1–#6, b9e5feb for #7–#8).

**Policy:** When a new walkthrough test fails, fix the engine. Never adjust the narrative or add state injection to make a test pass. Only fix the walkthrough when the design doc confirms the walkthrough is wrong.

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

---

### TODO #9 — Syntax actions with no default handler (found 2026-10-12)

`PUT X IN Y` printed nothing because `V-PUT-IN` was in the syntax table with no registered verb handler; when no object or room action takes such a command, the engine prints nothing (`engine/game.py`, `_perform_chain` step 7). `V-PUT-IN` is fixed. These actions are still in `content/syntax.py` with no default handler:

Every action on the original list is done (below).

Done so far (2026-10-12): `V-BOARD`, `V-BREATHE`, `V-INFLATE` dropped; `V-BRUSH` given Zork's line; `V-BURN` dropped (`BURN` is a synonym of `LIGHT`); `V-CAST` dropped (the spells hook answers every CAST line); `V-CLIMB-UP` / `V-CLIMB-DOWN` walk up / down; `V-CLOSE` — *You can't close that.* (bar the Trophy Case); `V-COUNT` (purse line for COUNT ZENNI, else Zork's line); `V-CROSS` given Zork's line; `V-CUT` (attack an enemy, refuse an NPC, Zork's line; `CUT ROPE` once tied keeps it; "You can't fight May." fixed); `V-ENCHANT` given a line; `V-FILL` given a line; `V-FOLLOW` removed with its words; `V-HOLD-NEAR` — *Nothing happens.* (a torch near the gunpowder is refused); `V-KICK` as `V-CUT`, `TAUNT` dropped; `V-KNOCK` (+ `KNOCK ON`; doors, the speaking wall, the Dankhaus, the White House); `V-LEAN` (+ `LEAN ON` / `AGAINST`) Zork's line; `V-LOCK` given lines; `V-LOOK-INSIDE` = EXAMINE; `V-LOOK-UNDER` (dust; the nightstand finds the dragon-nip); `V-LOWER` (Zork's line; `LOWER ROPE` at the hole); `V-LUBRICATE` removed with its words; `V-MAKE` Zork's line; `V-MELT` (Zork's line; `MELT ICE` with no tool or the wrong one); `V-PICK` (the chest, keyed doors, TAKE); `V-PLUG` (aqueduct = SEAL, the jar's seal step, GLUE/PATCH BOWL, else a line; `SEAL` default too); `V-PUMP` removed with its word; `V-PUT` (only `APPLY X TO Y` used it — now `V-APPLY`, routed by item); `V-REST` rule removed (`rest.py`'s hook reads REST; signpost comment in `syntax.py`); `V-RING` removed with its words; `V-ROLL` (Zork's line; `ROLL [DICE]` at Ty's is `PLAY`); `V-RUB` (+ `WITH`; the rubbing from the paper or charcoal; NPCs; Zork's line); `V-SHAKE` removed with its word; `V-SPIN` → `TURN` synonym; `V-SQUEEZE` and `V-WIND` removed with their words; `V-SWING` (`AT` = ATTACK WITH, else *Whoosh!*); `V-TAKE-FROM` (TAKE if it's there, else Zork's line; no stray implicit take); `V-THROW` (DROP; AT anything — kept hold of); `V-TIE` / `V-UNTIE` given lines (NPCs aren't tied up); `V-TIP` (tip over; only May takes tips); `V-TURN` (+ `TURN DIAL` asks which way; `SHUT` moved to `CLOSE`). `V-LAMP-OFF` / `V-TURN-OFF` given lines, and `V-TURN-ON` (registered, but silent for anything but the lantern). Registered handlers that return without printing are silent too; the guard test should catch those as well.

Still to do (found by a guard script, 2026-10-12): registered handlers that give up in silence on an ordinary object — `V-DESTROY`, `V-DRIVE-STAKE` (no target), `V-EAT`, `V-POUR`, `V-PROP`, `V-MIX`. Then the guard test itself.

Related: some rules only look at the room (`_og_ir`), so naming a carried item gives "You can't see any X here!" — fixed for `CROSS`, `HOLD NEAR`, `SEAL`, `SWING`, `THROW`, `TIP`; still so for `ATTACK` / `KILL` / `STAB` / `SHOOT`, `EXORCISE`, `DISARM`, `JUMP ON`, `WALK` (and `TALK` / `PAY` / `CHALLENGE` / `GIVE … TO`, where wanting a person here is reasonable).

Some work through input hooks or object/room actions (e.g. `CAST`), so not all are silent in play. For each: check whether it can print nothing; if so, give it a default line (design text in `mechanics.md` — Parser Verbs) or drop the syntax rule. Then add a guard test that every syntax action answers with an object (`test_system_verbs.py` only checks bare verbs today).
