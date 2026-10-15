# Roundabout: The God-Forsaken Ring — Open Design Questions

Consolidated from all source files. Update this file when items are resolved; record the resolution and the source file where it was written.
Resolved items are removed; their history is in git (last full lists: commit 7eec353 for TODO #1–#6, b9e5feb for #7–#8, fecb0f2 for #9, cfd1724 for #13, 4a4e63c for #12, 337bf02 for #11, 6bbb3e5 for #16, 8084dfa for #14, 6cb6920 for #15, 9130035 for #20, 26df3b1 for #23, 536aab4 for #21, cb0b094 for #22).

**Policy:** When a new walkthrough test fails, fix the engine. Never adjust the narrative or add state injection to make a test pass. Only fix the walkthrough when the design doc confirms the walkthrough is wrong.

---

### TODO #10 — Pre-release antivirus steps in operations.md (found 2026-10-12)

A player using ESET couldn't open the v2.5 .exe (permission error, most likely quarantine).
The .exe was uploaded to VirusTotal afterwards; waiting to hear whether their next download gets through.
Once known, add to operations.md (Antivirus false positives) whichever steps actually helped: e.g. uploading each new build to VirusTotal before announcing it, and submitting false positives to the engines that flag it (ESET: in-product Tools → Submit sample for analysis, or samples@eset.com).

### TODO #17 — Trap 45 (Ink Corridor) barely fires at the level players reach it (found 2026-10-13)

- **Difficulty tiers renamed and extended** (2026-10-15): Easy / Medium / Hard / Very Hard are now Level 1–4 checks (same targets), and Level 5–8 were added (24 / 28 / 32 / 44). A Level N check is passed about a third of the time by a level-N player. Written in mechanics.md (Difficulty tiers); the old names below are kept as found.
- **Arrival level** (checked 2026-10-15): both walkthroughs reach the Ink Corridor at level 5 (ring route 159 XP, full score 187), where Level 2 / Level 2 traps fire 0% of the time.
- ~~**Trap 45**~~ **resolved 2026-10-15:** Level 5 perception, Level 4 disarm — inks about half of level-5 Warriors, 20% of Rogues (traps.md, Trap 45).
- ~~**Traps 16 and 17**~~ **resolved 2026-10-15:** Trap 17 (Supply Room) Level 5 / Level 4, like Trap 45; Trap 16 (Chuckle House) Level 4 / Level 4, since most players arrive there at level 4 (traps.md). The Ghost's Room 50% exit roll stays as it is (decided 2026-10-15).
- ~~**Mid and lower tiers**~~ **resolved 2026-10-15:** Trap 8 (snare) Level 6 perception, Level 4 pull free; Trap 15 (Magnetic Vault) Level 6 perception, Level 5 disarm, Level 4 pry. Strength checks stay at Level 4 so a level-4 Mage or Rogue can always get free. No other lower-tier trap rolls (36 has no check; 29 and 41 are scripted). The dungeon's Level 2 item finds are left as they are.
- ~~**Traps 19 and 33**~~ **resolved 2026-10-15:** Trap 19 Level 4 perception / disarm / lift (no higher: it guards the north route); Trap 33 Level 5 plate perception, Level 4 pry (traps.md).

Level 4 is about the lowest level a player can be on reaching the dungeon.
At level 4 (2d10+3 with Lucky), a warrior without glasses passes the Medium (9) perception check 95.7% of the time and the Medium disarm the same, so the trap inks them only ~8.4% of the time (exact; a 20,000-run engine simulation gave 8.7%).
Rogues and mages, with +3, almost never trigger it. For comparison, a warrior is inked ~83% of the time at level 2 and ~41% at level 3 — levels that don't get here.
Review the trap's difficulty against the levels players actually arrive at (traps.md, Trap 45). The ink is what negates invisibility, so how often it fires matters beyond this room. Check the other upper-tier traps for the same problem.
- **Trap 29 (Combat Room plate) and Trap 41 (Flooding Room plate)** — the auto-disarm locked out the Guardian's Lantern and the trap side for ~92% of level-4 warriors and nearly every Rogue. Decided 2026-10-14: neither plate can be spotted or disarmed any more; both fire on entry. Moved to TODO #21 (Combat Room) and TODO #22 (Flooding Room and the apprentice).
- ~~**Trap 19 (Portcullis Corridor) — a failed check leaves the portcullis charged for good**~~ (found 2026-10-13). **Resolved 2026-10-15:** perception every visit until spotted, plus SEARCH; `DISARM PORTCULLIS` / `MECHANISM` retries once spotted (a failure costs only the turn); `TOUCH` shocks like `LIFT`; new mechanism object and examine text.
  Written in traps.md (Trap 19), locations.md (Portcullis Corridor) and mechanics.md (SEARCH, Parser Verbs).
- ~~**Trap 19 — walking through the held portcullis**~~ (found 2026-10-15). With it lifted and held, `SOUTH` said *"The portcullis is down."* and then *"You let go. The portcullis slams back down."*
  **Resolved 2026-10-15:** no leaving while it's held (*You'll have to drop the portcullis first.*, still held); `DROP` / `RELEASE` / `LOWER PORTCULLIS` and `LET GO` let it drop. Written in locations.md (Portcullis Corridor, Let go) and mechanics.md (Parser Verbs).

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

