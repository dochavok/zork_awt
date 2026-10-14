# Roundabout: The God-Forsaken Ring — Open Design Questions

Consolidated from all source files. Update this file when items are resolved; record the resolution and the source file where it was written.
Resolved items are removed; their history is in git (last full lists: commit 7eec353 for TODO #1–#6, b9e5feb for #7–#8, fecb0f2 for #9, cfd1724 for #13, 4a4e63c for #12, 337bf02 for #11, 6bbb3e5 for #16).

**Policy:** When a new walkthrough test fails, fix the engine. Never adjust the narrative or add state injection to make a test pass. Only fix the walkthrough when the design doc confirms the walkthrough is wrong.

---

### TODO #10 — Pre-release antivirus steps in operations.md (found 2026-10-12)

A player using ESET couldn't open the v2.5 .exe (permission error, most likely quarantine). The .exe was uploaded to VirusTotal afterwards; waiting to hear whether their next download gets through. Once known, add to operations.md (Antivirus false positives) whichever steps actually helped: e.g. uploading each new build to VirusTotal before announcing it, and submitting false positives to the engines that flag it (ESET: in-product Tools → Submit sample for analysis, or samples@eset.com).

### TODO #14 — Revealed connections are hidden by BRIEF mode (found 2026-10-12)

From the 2026-10 playtest (`roundabout_playtest/feedback-2026-10-12.md`, "Litlock's 'see things differently' reveals a building in the graveyard, but brief mode hides it").
When an exit appears in a room the player has already visited, BRIEF mode (the default) shows only the room name on the next visit, so the line announcing the new way on is never seen.
The Graveyard after Litlock's reveal (the Chuckle House, east) is the reported case.
Others to check: perception-found connections (the volcano stairs, Will's bedroom door in the Wizard Tower, the Dankhaus path, the Hidden Secondary Entrance from the mine side), and state changes that open a way (the Tool Alcove wall, the frozen Flooded Passage, the Stored Room hole, the Rickety Bridge west shortcut, the Keeper's door).
The Wizard Tower's bedroom door (2026-10-13): the find line shows in every mode, but its lasting line (*"A door in the north wall stands where you'd have sworn there wasn't one."*) is in the long description only.
Decide on one rule — e.g. the first visit after a room's exits change shows the full description — and record it in mechanics.md (Description modes).

### TODO #15 — Parser and scenery items noted during the exits pass (found 2026-10-12)

Small items from the 2026-10 playtest, found while fixing room exits (theme 1) and set aside for the parser/scenery pass (theme 2 in `roundabout_playtest/feedback-2026-10-12.md`). Add to this list as more turn up.
- `ENTER MINE` at Roundabout Forest should go down to the Mine Entrance, as `DOWN` does (the playtester tried it first; feedback "'enter mine' fails; 'down' works").
- `EXAMINE ALTAR` in The Altar answers "You see nothing special about the altar." — it should give the altar's own description.
- **Forest shrine, the repaired bowl** (feedback "Where does the repaired bowl go?" and "(ASSISTED) The shrine needs `put bowl on pedestal` then `put zenni on pedestal`"):
  - `PUT BOWL IN SHRINE` takes the bowl back and says *"(Taken) That won't fit in the pedestal."* — a parser bug.
  - `PUT ZENNI IN BOWL` (*"That won't fit in the repaired bowl."*), `OFFER ZENNI` and `DONATE` aren't accepted; only `PUT ZENNI ON PEDESTAL` works. The playtester's suggestion: accept the in-bowl form, the most natural.
  - The placement reply (*"The bowl is placed. The shrine is unmoved. Devotion is appreciated. Contributions pay the bills."*) is the real hint but reads as a stock brush-off; "unmoved" suggests a wrong move. Suggested: something sincere, e.g. *"The bowl sits where it belongs. The shrine seems to be waiting for an offering."*
  - `PRAY` at the shrine answers *"If you pray enough, your prayers may be answered."* (they prayed four times).
  - After a restore, the forest showed *"The repaired bowl sits on the pedestal"* while the bowl was in the inventory (stale state).
  - The underground Shrine Room's plinth and bowl depression, its only features, aren't nouns.
- **`CLIMB STAIRS`, `CLIMB UP STAIRS`, `CLIMB DOWN STAIRS`** should work as `UP` / `DOWN` (requested 2026-10-12).
  - Today all three answer *"You can't see any stairs here!"* — even in the Tale and Ale, whose description has a staircase — because "stairs" isn't an object anywhere.
  - With UP or DOWN given, take that exit.
  - Bare `CLIMB STAIRS` goes whichever way the room's stairs go; where stairs run both ways (the Upper Hall), ask *"Up or down?"* the way `TURN DIAL` asks which way.
  - Rooms with described stairs or steps include the Tale and Ale, Upstairs Hall, Town Hall, Upper Hall, The Tower, the Mausoleum, the Crypt, Charnel Walk, the Kitchen (cellar steps once drained), the Mid-Tier Key Door and Key Door Landing, the Volcano (once found) and Pyronicus's Forge.
  - mechanics.md already has `CLIMB UP [thing]` / `CLIMB DOWN [thing]` = `UP` / `DOWN` — the gap is "stairs" as a noun and the bare form.
- **The Lighthouse** (feedback "The lighthouse stairs and desk are scenery only, and the paperweight vanishes"):
  - The desk and the papers (*"stacked with more care than anything else in the room"*) can't be examined or read — the text invites both.
  - The smooth stone weighting the Unbind Undead scroll vanishes once the scroll is taken, and `TAKE STONE` picks the player's own rune stone instead.
  - The torch burns down inside the lighthouse, a room with a window — a question for the light rules (mechanics.md) rather than this room.

- **From the TODO #16 room notes** (playtest feedback, single-verb solutions and scenery):
  - Collapsed Aqueduct: only `PLACE BLOCK` works; `LIFT BLOCK` / `PUT BLOCK` fail (feedback "The aqueduct repair: `place block` is the only verb that works").
  - Collapsed Gallery: the crowbar's *"You can't get any leverage on that"* pushed the playtester away from levering; the pickaxe is the answer (feedback "The pickaxe was the answer for the timbers").
  - Combat Room: the east door isn't an object, and only `JUMP ON PLATE` triggers the plate (not step, stand, press or trigger).
  - The Still Den: `ATTACK`, `STAB` and `USE` on the werewolf all print *"Your blade finds its mark"*, even with no blade held; only `DRIVE STAKE INTO WEREWOLF` works.
  - The Still Den, after the kill: the text says *"the stake still in him"*, but `TAKE STAKE` answers *"You can't see any stake here!"* Answer instead: *"You dare not remove it."* (wording decided 2026-10-13).
  - Pile of Rubble: the rubble isn't a noun (feedback "Shovel, hole, timber, rope: a good chain, but the rubble isn't a noun").
  - Supply Room: the Trap 17 spotted line (*"…a trip mechanism… Whatever it triggers, it isn't subtle."*) keeps showing after the trap has fired or been disarmed — `TRAP17-SPOTTED` is set whenever perception passes, even when the disarm then botches. It should go (or change) once the trap is resolved.
  - The Encampment (lower tier): the journals (*"Journals open to pages no one finished"*), bedrolls and equipment aren't nouns — `READ JOURNALS` / `EXAMINE BEDROLLS` answer *"You can't see any … here!"*, and `EXAMINE JOURNAL` answers *"You don't have a journal."* (another journal object elsewhere is matched). The room is "lore and context only" — the journals could carry a line of lore.
  - The Rat's Nest: the crates and barrels in the description aren't nouns — `EXAMINE CRATES` / `SEARCH BARRELS` answer *"You can't see any crates here!"* (the playtester tried both).

### TODO #17 — Trap 45 (Ink Corridor) barely fires at the level players reach it (found 2026-10-13)

Level 4 is about the lowest level a player can be on reaching the dungeon.
At level 4 (2d10+3 with Lucky), a warrior without glasses passes the Medium (9) perception check 95.7% of the time and the Medium disarm the same, so the trap inks them only ~8.4% of the time (exact; a 20,000-run engine simulation gave 8.7%).
Rogues and mages, with +3, almost never trigger it. For comparison, a warrior is inked ~83% of the time at level 2 and ~41% at level 3 — levels that don't get here.
Review the trap's difficulty against the levels players actually arrive at (traps.md, Trap 45). The ink is what negates invisibility, so how often it fires matters beyond this room. Check the other upper-tier traps for the same problem.
- **Trap 29 (Combat Room plate) — the auto-disarm locks out the Guardian's Lantern.**
  - Also Medium perception + Medium disarm, so a level-4 warrior without glasses auto-disarms it ~92% of the time.
  - Then the Warden never comes out, the Den door stays shut (*"The door is shut."*), and the Guardian's Lantern (needed for the lower-tier Dark Room) is unreachable unless the player thinks to `JUMP ON PLATE`.
  - Nothing connects the plate to the door: the disarm line is only *"You spot a pressure plate set into the corridor floor and are able to disarm it, neutralizing it."*
  - Same shape as the Flooding Room decision (TODO #16, #20), but it hits nearly every player, not just Rogues.
  - Decide together: e.g. make the auto-disarm a choice (as with Actually Enchanted Glasses), have the disarmed plate or the shut door hint at the link, or let the door be opened another way.
- **Trap 41 (Flooding Room plate) — the auto-disarm locks out the trap side** (moved here from TODO #16 #20, playtest theme 4, feedback "The Flooding Room's levers and its plate").
  - Disarming jams the plate; the levers then give no feedback (left grinds, middle does nothing, right snaps off), so Quest 50 and the gold nugget treasure are locked out.
  - The design's re-arm after the middle lever doesn't help a player who never saw the plate fire.
  - Also Medium + Medium, so ~92% of level-4 warriors (and nearly every Rogue) auto-disarm it — not just Rogues, as first reported.
  - Options: let `JUMP ON PLATE` still fire a jammed plate; make the auto-disarm a choice here; or put a clue on the sluice grate. Settle with Trap 29 so the fix is consistent.
- **Trap 19 (Portcullis Corridor) — a failed check leaves the portcullis charged for good** (found 2026-10-13).
  - Same Medium + Medium odds (~8.4% failure for a level-4 warrior), but the failure is permanent, not a nuisance. `_check_trap19` runs once (`TRAP19-CHECKED`).
  - If perception fails (~4.3%) — or it's spotted and the disarm botches (~4.1%; the player is shocked) — the portcullis stays charged, and nothing can discharge it afterwards.
  - `DISARM PORTCULLIS` gives *"There's nothing here to disarm."*, `SEARCH` doesn't re-check, `EXAMINE PORTCULLIS` gives *"You see nothing special about the portcullis."*, and every `LIFT` shocks (1 heart, a lost turn).
  - The north route to the Shrine Room is then closed for good; only the Quest 38 shortcut (Collapsed Gallery → Rickety Bridge) gets past. traps.md says the disarm check is one of the "ways to pass", which implies it can be retried.
  - Fix with the other two: e.g. allow `DISARM PORTCULLIS` (and SEARCH) to retry once the charge is known — the room text's crackle line already tells every player it's charged.
