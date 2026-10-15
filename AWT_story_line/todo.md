# Roundabout: The God-Forsaken Ring — Open Design Questions

Consolidated from all source files. Update this file when items are resolved; record the resolution and the source file where it was written.
Resolved items are removed; their history is in git (last full lists: commit 7eec353 for TODO #1–#6, b9e5feb for #7–#8, fecb0f2 for #9, cfd1724 for #13, 4a4e63c for #12, 337bf02 for #11, 6bbb3e5 for #16, 8084dfa for #14, 6cb6920 for #15, 9130035 for #20, 26df3b1 for #23, 536aab4 for #21, cb0b094 for #22, 213bcd6 for #17).

**Policy:** When a new walkthrough test fails, fix the engine. Never adjust the narrative or add state injection to make a test pass. Only fix the walkthrough when the design doc confirms the walkthrough is wrong.

---

### TODO #10 — Pre-release antivirus steps in operations.md (found 2026-10-12)

A player using ESET couldn't open the v2.5 .exe (permission error, most likely quarantine).
The .exe was uploaded to VirusTotal afterwards; waiting to hear whether their next download gets through.
Once known, add to operations.md (Antivirus false positives) whichever steps actually helped: e.g. uploading each new build to VirusTotal before announcing it, and submitting false positives to the engines that flag it (ESET: in-product Tools → Submit sample for analysis, or samples@eset.com).

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

### TODO #24 — A warning when the player drops to 1 heart (found 2026-10-15)

Traps 16, 17 and 45 now fire far more often (TODO #17), and trap damage may go up, so a player can reach 1 heart without noticing.
Today nothing marks it: hearts drop silently until the game-over line (mechanics.md — Death: *Your last heart gives out…*).
- Craft a line shown when damage leaves the player on exactly 1 heart. Needs writing and review (2–3 options).
- Engine: `combat.take_damage` is the one place every trap, hazard and fight deducts hearts, so the line can live there.
- To decide: every time it happens, or once until healed; whether it differs for combat versus traps; whether the mugger knock-out (which leaves 1 heart) shows it; and where it sits relative to the damage line.

