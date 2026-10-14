# Roundabout: The God-Forsaken Ring — Open Design Questions

Consolidated from all source files. Update this file when items are resolved; record the resolution and the source file where it was written.
Resolved items are removed; their history is in git (last full lists: commit 7eec353 for TODO #1–#6, b9e5feb for #7–#8, fecb0f2 for #9, cfd1724 for #13, 4a4e63c for #12, 337bf02 for #11, 6bbb3e5 for #16, 8084dfa for #14).

**Policy:** When a new walkthrough test fails, fix the engine. Never adjust the narrative or add state injection to make a test pass. Only fix the walkthrough when the design doc confirms the walkthrough is wrong.

---

### TODO #10 — Pre-release antivirus steps in operations.md (found 2026-10-12)

A player using ESET couldn't open the v2.5 .exe (permission error, most likely quarantine).
The .exe was uploaded to VirusTotal afterwards; waiting to hear whether their next download gets through.
Once known, add to operations.md (Antivirus false positives) whichever steps actually helped: e.g. uploading each new build to VirusTotal before announcing it, and submitting false positives to the engines that flag it (ESET: in-product Tools → Submit sample for analysis, or samples@eset.com).

### TODO #15 — Parser and scenery items noted during the exits pass (found 2026-10-12)

Small items from the 2026-10 playtest, found while fixing room exits (theme 1) and set aside for the parser/scenery pass (theme 2 in `roundabout_playtest/feedback-2026-10-12.md`). Add to this list as more turn up.

- **Found during the scenery pass** (2026-10-14):

### TODO #17 — Trap 45 (Ink Corridor) barely fires at the level players reach it (found 2026-10-13)

Level 4 is about the lowest level a player can be on reaching the dungeon.
At level 4 (2d10+3 with Lucky), a warrior without glasses passes the Medium (9) perception check 95.7% of the time and the Medium disarm the same, so the trap inks them only ~8.4% of the time (exact; a 20,000-run engine simulation gave 8.7%).
Rogues and mages, with +3, almost never trigger it. For comparison, a warrior is inked ~83% of the time at level 2 and ~41% at level 3 — levels that don't get here.
Review the trap's difficulty against the levels players actually arrive at (traps.md, Trap 45). The ink is what negates invisibility, so how often it fires matters beyond this room. Check the other upper-tier traps for the same problem.
- **Trap 29 (Combat Room plate) and Trap 41 (Flooding Room plate)** — the auto-disarm locked out the Guardian's Lantern and the trap side for ~92% of level-4 warriors and nearly every Rogue. Decided 2026-10-14: neither plate can be spotted or disarmed any more; both fire on entry. Moved to TODO #21 (Combat Room) and TODO #22 (Flooding Room and the apprentice).
- **Trap 19 (Portcullis Corridor) — a failed check leaves the portcullis charged for good** (found 2026-10-13).
  - Same Medium + Medium odds (~8.4% failure for a level-4 warrior), but the failure is permanent, not a nuisance. `_check_trap19` runs once (`TRAP19-CHECKED`).
  - If perception fails (~4.3%) — or it's spotted and the disarm botches (~4.1%; the player is shocked) — the portcullis stays charged, and nothing can discharge it afterwards.
  - `DISARM PORTCULLIS` gives *"There's nothing here to disarm."*, `SEARCH` doesn't re-check, `EXAMINE PORTCULLIS` gives *"You see nothing special about the portcullis."*, and every `LIFT` shocks (1 heart, a lost turn).
  - The north route to the Shrine Room is then closed for good; only the Quest 38 shortcut (Collapsed Gallery → Rickety Bridge) gets past. traps.md says the disarm check is one of the "ways to pass", which implies it can be retried.
  - Fix: e.g. allow `DISARM PORTCULLIS` (and SEARCH) to retry once the charge is known — the room text's crackle line already tells every player it's charged.

### TODO #18 — The ring: warnings come too late to budget invisibility (found 2026-10-13)

From the 2026-10 playtest (`roundabout_playtest/feedback-2026-10-12.md`: "The ring's growing 'presence' is good foreshadowing", "The ring's countdown on the way out was excellent", "The ring's 'you can't take it off' game over is random").
The playtester didn't get enough early warning, didn't take the ring off soon enough, and ran short of corruption ticks in the end game, where invisibility is needed (the Spirit Room).
- What they saw: the first hint is at tick 10 of 50 and the next at 25. They couldn't tell whether there was a real cost, or that the timer pauses but never resets (feedback: "I'd still like a hint that the timer doesn't reset when I take the ring off").
- The removal rolls at ticks 41–49 felt random: the same `REMOVE RING` from the same save gave a game over about 2 times in 3 ("A random game over isn't something a player can learn from").
- **Constraint:** corruption is sacred (mechanics.md — The God-Forsaken Ring). Nothing here may reduce, slow or mitigate it; the 50-tick budget stays. Only what the player is told, and when, is open.
- Options to weigh: an early, explicit warning that each wearing spends from one budget (Will, before or after the ring is handed over: e.g. "each time you wear it, it takes less time to take hold"); earlier or more frequent milestone lines; a line on each `REMOVE RING` that hints how far it has gone; and whether the 41–49 window should end on a clear point of no return rather than a roll.
- Also review where the game needs invisibility (Chuckle House, Spirit Room and back, the Burial Chamber) against 50 ticks, so a careful player can plan the budget.
- **Likely fix** (2026-10-13): more frequent milestone lines — e.g. warnings at ticks 20 and 30 in place of the single midpoint line at 25 (so 10, 20, 30, 40, then the 41–49 slide). New lines need writing and review; mechanics.md's milestone table changes with them.

### TODO #19 — Puzzles and rules the scene doesn't signal (found 2026-10-14)

From the 2026-10 playtest (theme 2 and the session 4 entries), set aside from TODO #15 because each needs a design decision, not just a noun or a synonym.
- **Kitchen cellar — nothing suggests `CLEAR DRAIN`** (feedback "(ASSISTED) The cellar needed `clear drain`, and I missed it"). After `PRY DRAIN` (*"The cover comes up with a jolt and slides off into the dark."*) the room still says the water fills the stairwell, and nothing hints at a second step; the playtester waited, went down and drowned.
  - May's *"it's yours to clear"* read as the goal, not the verb. Their suggestion: one line after the cover comes off, e.g. *"Below the cover, the drain mouth is packed solid with silt and roots. The water isn't going anywhere."*
- **The Whispering Jar — nothing links the silver dust to the letters** (feedback "(ASSISTED) The Whispering Jar"). Before dusting, `READ JAR` reads the letters in full (*"Around the base, worn almost smooth: 'Hold what was heard. Speak what was held.' You say the words aloud. The jar hums on, unchanged."*), so nothing seems missing.
  - Suggested: make the letters unreadable until dusted (*"worn almost to nothing; you can make out the shape of words but not the words"*), and let the dust's description or May's tip lean that way.
  - The same entry reports the in-between states as stale: after sealing (and before speaking) the room and `EXAMINE JAR` still say "cracked".
- **The Lighthouse — the torch burns down in a room with a window** (moved from TODO #15). A question for the light rules (mechanics.md): does a windowed room count as lit, and should a torch burn there?

### TODO #20 — The hand cart sometimes missing from room listings (found 2026-10-14)

The 2026-10 playtest summary ("Also worth fixing — Display") says dropped items sometimes don't appear in room listings: *the hand cart, the bowl*.
The bowl was fixed in TODO #15 (2026-10-14): an implicit "(Taken)" off the shrine pedestal left it with NDESCBIT, so it vanished wherever it was dropped.
The hand cart hasn't been reproduced yet. Check whether it keeps a hidden flag the same way (e.g. after loading or unloading the gravestone) and where it fails to list.

### TODO #23 — ENTER for the other buildings and places (found 2026-10-14)

TODO #15 made `ENTER` / `GO INTO` / `GO IN` / `GO THROUGH [place]` work for the mine (Roundabout Forest) and the crypt and arch (Charnel Walk) — mechanics.md, Stairs and places.
The 2026-10 playtest summary lists `enter <place>` among the commands the parser refuses. Extend the same table to the other places a room names as a way in: e.g. the tavern from the Town Square, the lighthouse from the beach, the church, the Town Hall, the library, the mausoleum, the Chuckle House, the beekeeper's cottage.
Each is a noun and a direction (no new text unless the noun needs an `EXAMINE` line). Check each noun against objects already in that room first.

### TODO #21 — Combat Room redesign: the plate fires on entry (decided 2026-10-14)

Replaces Trap 29's spot-and-disarm plate (moved from TODO #17). The auto-disarm left ~92% of level-4 warriors, and nearly every Rogue, with the Den door shut and no idea why; the Guardian's Lantern behind it is needed for the lower-tier Dark Room.
The room's name only makes sense if the fight happens, so the fight now always happens.
- **First entry, from either side** (the Quest 38 shortcut brings some players up from the south first):
  - No perception check, no disarm, no Actually Enchanted Glasses choice. The plate isn't "just inside the doorway" any more; the text is *as you enter the room you trigger…*.
  - Then the bell and the door beginning to open (an "uh-oh" moment), then *[Press ENTER to continue]*, then the Warden comes through and the fight begins.
- **The Warden blocks EAST only.** `NORTH` and `SOUTH` stay open (the critical path runs through this room). `EAST` while he lives needs a refusal line.
  - Fleeing and returning: the trigger doesn't replay; he's there, back at full hearts (as now), with his presence line.
  - **Ring:** an invisible player can slip past him east (decided 2026-10-14; the ring is dangerous enough). Use the Chuckle House rule — invisible means wearing the ring and not inked (`chuckle.py`).
- **XP:** the plate's 3 disarm XP (+5 Rogue) goes; raise the Warden's kill XP (12, experience.md) slightly to make up for it. Rogues lose more (8 here) than a flat boost returns — accepted 2026-10-14.
- **From TODO #15 (Combat Room row):** the east door becomes an object (`EXAMINE` / `OPEN` / `KNOCK` / `PUSH` / `PRY DOOR`, shut and open states), and the plate gets an `EXAMINE` line. The plate verbs (`STEP ON` / `PRESS` / `TRIGGER`…) are no longer needed.
- **New text to write and approve:** the trigger line, the door opening before the pause, the `EAST` refusal, the door and plate examine lines.
- **Docs:** traps.md Trap 29 becomes a scripted event (keep the number); locations.md (Combat Room, Creature Den connections); experience.md (Trap 29 row, Warden XP); items.md glasses text if it mentions the plates.
- **Tests and walkthroughs:** remove `JUMP ON PLATE` / `DISARM PLATE` and the glasses-choice tests for this plate; walkthrough_fullscore.txt and walkthrough_ring.txt both pass through this room. The Press-ENTER pause is fine — the walkthrough feed answers bare pauses with "".

### TODO #22 — Flooding Room and the Lost Apprentice redesign (decided 2026-10-14)

Replaces Trap 41's spot-and-disarm plate and its two-turn flood (moved from TODO #17). Anyone who walks into the Flooding Room is now sent down to the trap side; the apprentice finishes his own tunnel, so no shovel is needed to get out.
- **Entry (every player, first and only visit):**
  - The plate fires on entry, with a cheeky nod (e.g. whoever designed this dungeon sure liked pressure plates).
  - A new **slab** drops behind the player, sealing the way south; the room is suddenly half full of water. A softened urgency line (not "you may not have much time" — there's no timer, and the line mustn't be a promise the game breaks).
  - No perception check, no disarm, no glasses choice, no timer. The thin paper is still destroyed by the sweep (accepted).
- **The levers** (no hint needed — after the middle one, the only thing left to do is pull the others):
  - **Right:** snaps off, and more water rushes in.
  - **Middle:** stops the water; the room stays half full.
  - **Left:** opens the sluice — the player goes down to the Spillway (the existing sweep text). It used to grind and stick; its pull text is new.
  - Each is one pull, then *"You already tried that one."* The room description needs a water-level line per state (half full, more water, stopped).
  - The sluice becomes a noun (moved from TODO #15, 2026-10-14: `EXAMINE SLUICE` answers *"You can't see any sluice here!"*; playtest theme 2).
- **The Creature Den, once the player has entered the Flooding Room:** `NORTH` is refused (the slab — *the way is blocked…*), and the Den description loses "A passage leads on to the north". That's a change of ways, so the Den shows its full description next time. No later visits to the Flooding Room.
- **The apprentice (Lost Apprentice's Cell):**
  - More narrative when he's freed from the affliction, and he finishes the tunnel himself. `USE SHOVEL` / `DIG` there needs a new reply (or none); the shovel's uses in items.md drop from three to two.
  - He gives the player the gloves in the cell (he doesn't need them), and his departure text comes before he climbs out; the cell description changes once he's gone. The Bog-NW surfacing line changes (he's already gone).
  - Quest 50 completes at the handover, not on reaching the bog (12 XP, 5 Zenni).
  - **Ring:** if the player is still invisible on reaching him, that interaction needs designing (he crouches "between you and the tunnel"; today nothing checks the ring here).
  - Check Will's homecoming line (npcs.md — Quest 50) for anything tied to the bog.
- **Quest 50 stays missable** (a player who never enters the Flooding Room). The Quest Board notice comes down when the apprentice is freed, not when Trap 41 is disarmed.
- **The gold nugget** stays missable: leaving up the tunnel before searching the Supply Cache leaves it behind for good. Add it to mechanics.md's missable treasures (four, not three) and recheck the tier sentence there.
- **XP:** Trap 41's 5 disarm XP (+5 Rogue) goes; raise the apprentice's XP (8, experience.md) slightly.
- **Docs:** traps.md Trap 41 (keep the number); locations.md (Flooding Room, Creature Den, Spillway, Lost Apprentice's Cell, Supply Cache); quests.md Quest 50 (missability, prerequisites — no shovel, steps); npcs.md (The Afflicted Apprentice); items.md (Shovel, Thin Paper — still accurate); experience.md; mechanics.md (missable treasures).
- **Tests and walkthroughs:** remove `JUMP ON PLATE` / `DISARM PLATE`, the glasses-choice, two-turn flood, re-arm and bog-completion tests; fix walkthrough_fullscore.txt (Quest 50 route) and any walkthrough that disarms or jumps on this plate.
- **New text to write and approve:** the entry trigger, the slab, the water lines, the three lever lines, the Den's blocked north, the apprentice's freeing, digging and farewell, the cell after he's gone, the new Bog-NW arrival.
