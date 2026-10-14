# Roundabout: The God-Forsaken Ring — Open Design Questions

Consolidated from all source files. Update this file when items are resolved; record the resolution and the source file where it was written.
Resolved items are removed; their history is in git (last full lists: commit 7eec353 for TODO #1–#6, b9e5feb for #7–#8, fecb0f2 for #9, cfd1724 for #13, 4a4e63c for #12, 337bf02 for #11).

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

### TODO #16 — Exits in room descriptions: the remaining rooms (found 2026-10-12)

Playtest theme 1 (`roundabout_playtest/feedback-2026-10-12.md`: exits and rooms the text never mentions). The surface world is done (2026-10-12; `roundabout/test_room_exits.py`). This is the rest, prepared so each room is a quick review: approve or change the proposed text, settle any note, then update locations.md and the engine and add the room to test_room_exits.py.

**How to read an entry.** *Current* is what the game prints now; long descriptions quote only the part that changes (the rest stays as it is). In *Proposed*, new or changed words are in bold. *Notes* are decisions beyond a text change. Rooms marked "No change" already name their exits.

**Summary**

| # | Room | Change | Decision needed |
|---|------|--------|-----------------|
| 1 | Mine Tunnels | Exits; restore dropped design lines | — |
| 2 | The Rat's Nest | Exit; restore dropped clause | — |
| 3 | Hidden Secondary Entrance | Exits | — |
| 4 | The Forgotten Shaft | South | — |
| 5 | The Undercroft | Exits | — |
| 6 | The Junction | Exits; drop "back" | — |
| 7 | The Bone Passage | West | Black oak door drowning warning |
| 8 | Cellar | Up | — |
| 9 | The Toll Bridge | Exits; bridge text lost after the Boggart | — |
| 10 | Dungeon Entrance | North | — |
| 11 | Ink Corridor | North | — |
| 12 | Supply Room | East | — |
| 13 | Storage Area | West | — |
| 14 | Collapsed Aqueduct | North; south when sealed | — |
| 15 | Collapsed Gallery | North; cleared text | Wording of the cleared state |
| 16 | Narrow Passageway | "behind you" → north | — |
| 17 | Idol Room | Exits | — |
| 18 | Combat Room | North, south | Rogue auto-disarm (see #19, #20) |
| 19 | Creature Den | West | — |
| 20 | Flooding Room | No change | Rogue auto-disarm locks out the trap side |
| 21 | Prayer Alcove | Exits; "dead end" is wrong | Confirm the geometry |
| 22 | Portcullis Corridor | Exits (by state) | — |
| 23 | Shrine Room | Exits | — |
| 24 | Mid-Tier Key Door | North | — |
| 25 | Key Door Landing | North; "deposits you" | — |
| 26 | Stored Room / Hole to Below | Exits (by state) | Warn before the dig loses the watch? |
| 27 | The Crevice | West | — |
| 28 | Inscription Chamber | North, south | — |
| 29 | Cave Creature's Lair | West | — |
| 30 | Echo Alcove | No change | — |
| 31 | Magnetic Vault | Exits | — |
| 32 | Deep Lock Door | North | Purpose of a door that never opens |
| 33 | The Spillway | No change | — |
| 34 | Dream Corridor | No change | — |
| 35 | Lost Apprentice's Cell | No change | — |
| 36 | Supply Cache | No change | — |
| 37 | Flood Sump | North | — |
| 38 | Pile of Rubble | The rope (up) | — |
| 39 | Lower Crypt | Exits | — |
| 40 | The Encampment | North | — |
| 41 | Thermal Vent Room | No change | — |
| 42 | Antechamber | No change | Warnings for the bone floor and the south door |
| 43 | Skeleton Room | — (death on entry) | Same as #42 |
| 44 | The Narrow Pass | West | — |
| 45 | The Still Den | West (two states) | — |
| 46 | Tool Alcove | South; north when open | — |
| 47 | The Flooded Passage | South | — |
| 48 | The Fountain Room | South | — |
| 49 | Dark Room | North, before the lantern | Break the total dark with one direction? |
| 50 | Spirit Room | Directions (visible state) | — |
| 51 | Burial Chamber | North | — |
| 52 | The Stacks | West | — |
| 53 | Will's Wizard Tower | Bedroom door once found | Hint the painting is the way out? |
| 54 | Will Passion's Bedroom | South | — |
| 55 | West of House | No change | — |

#### Tunnels and the mine

**1. Mine Tunnels** (`MINE-TUNNELS`). Exits: up → Main Shaft, north → The Rat's Nest.
- Current: *The working tunnels branch off the main shaft. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The floor is rutted with cart tracks.*
- Proposed: *The working tunnels branch off the main shaft, following veins of ore that may or may not have been the point. Torch sconces are fixed to the walls at intervals — the torches in them are real and lit. The smell of fresh-cut rock is strongest here.* ***The cart tracks rutting the floor run off to the north; the shaft climbs back up to the main level.***
- Notes: restores the design's dropped lines, minus "in two directions" (north is the only way on besides up). The weak-point lines are unchanged.

**2. The Rat's Nest** (`RATS-NEST`). Exit: south → Mine Tunnels.
- Current: *…The Pie Rats keep their surplus here.*
- Proposed: *…The Pie Rats keep their surplus here:* ***things that aren't ore, things that don't show up on manifests, things that would raise questions on a dock. The tunnel runs back south.***
- Notes: the colon clause is the design's, dropped by the engine.

**3. Hidden Secondary Entrance** (`HIDDEN-SECONDARY-ENTRANCE`). Exits: west → Assay Room, east → The Forgotten Shaft.
- Current: *The gap in the assay room wall opens into a rough passage that connects to the tunnel network below. It does not appear on any official plan of the mine. It would not.*
- Proposed: *The gap in the assay room wall,* ***back to the west,*** *opens into a rough passage that* ***runs east toward*** *the tunnel network below. It does not appear on any official plan of the mine. It would not.*
- Notes: arriving from the tunnel side, this is how the player learns the Assay Room exists — fine as a reveal.

**4. The Forgotten Shaft** (`FORGOTTEN-SHAFT`). Exits: south → The Undercroft, west → Hidden Secondary Entrance (named).
- Current: *…To the west, a rougher passage breaks off and climbs toward the mine.*
- Proposed: *…To the west, a rougher passage breaks off and climbs toward the mine.* ***Southward, the passage widens again.***

**5. The Undercroft** (`UNDERCROFT`). Exits: north → The Forgotten Shaft, south → The Junction.
- Current: *…The floor is uneven underfoot. The air is heavier here, deeper-smelling.*
- Proposed: *…The air is heavier here, deeper-smelling.* ***It runs north toward older, narrower stone, and south to where the tunnels meet.***

**6. The Junction** (`JUNCTION`). Exits: east → The Bone Passage, north → The Undercroft, south → The Toll Bridge.
- Current: *…Passages branch three ways. The one to the east runs back toward the cellar. …*
- Proposed: *…Passages branch three ways:* ***east toward the cellar, north toward the old mine workings, and south, where the floor drops away toward a ravine.*** *…*
- Notes: "back toward the cellar" assumed the player came from there; most first arrive from the mine side.

**7. The Bone Passage** (`BONE-PASSAGE`). Exits: south → Charnel Walk, west → The Junction, east → Cellar (black oak door).
- Current: *…The passage runs south. Whatever built this part…* (door line follows)
- Proposed: *…The passage runs south****, and west toward the junction.*** *Whatever built this part…*
- Notes: **Decision (theme 3):** opening the door before the cellar is drained drowns the player with no warning (feedback "Instant death behind the black oak door, with no fair warning").
  - The design says "no warning sign" on purpose. Options: keep; or add a pre-drain clue to the door line (cold seeping under it, the wood dark and wet).
  - Recommendation: add the clue — the drowning stays, but it becomes fair.

**8. Cellar** (`CELLAR`). Exits: up → Kitchen, west → The Bone Passage (door, named).
- Current: *…The drain gurgles now and then, like it's still thinking about it. In the west wall is a low door of black oak that nobody upstairs has mentioned.*
- Proposed: *…like it's still thinking about it.* ***Steps climb back up to the kitchen.*** *In the west wall is a low door of black oak that nobody upstairs has mentioned.*

**9. The Toll Bridge** (`TOLL-BRIDGE`). Exits: north → The Junction, south → Dungeon Entrance.
- Current (Boggart there): *A narrow stone bridge spans a ravine in the tunnel floor — the drop below is deep enough that the bottom isn't visible. The bridge looks solid.* + the two Boggart lines. After he leaves the whole description becomes one line: *The bridge is empty now. The strongbox sits where he was.* (or *…The open strongbox sits where he was, lid thrown back.*)
- Proposed: the bridge sentence prints in every state, extended: *…The bridge looks solid.* ***It carries the tunnel south; the junction is back to the north.*** Then the state line: the Boggart lines, or the strongbox line, or the looted line (unchanged).
- Notes: engine change in tunnels.bridge_action (today the post-Boggart states replace the bridge sentence).

**10. Dungeon Entrance** (`DUNGEON-ENTRANCE`). Exits: north → The Toll Bridge, south → Ink Corridor (named).
- Current: *The tunnel ends at a threshold — stone floor, stone walls, a passage leading south into darkness. Whatever is ahead…*
- Proposed: *…a passage leading south into darkness.* ***The bridge is back to the north.*** *Whatever is ahead…*

#### Dungeon, upper tier

**11. Ink Corridor** (`INK-CORRIDOR`). Exits: north → Dungeon Entrance, west → Supply Room, east → Storage Area, south → Narrow Passageway.
- Current: *…The passage splits ahead — west, east, and on to the south.*
- Proposed: *…The passage splits ahead — west, east, and on to the south****; the dungeon entrance is back to the north.***
- Notes: both states (the spotted-trap state adds the cord sentence after it).

**12. Supply Room** (`SUPPLY-ROOM`). Exit: east → Ink Corridor.
- Current: *…It smells of old wood and something chemical underneath.*
- Proposed: *…It smells of old wood and something chemical underneath.* ***The doorway back to the corridor is east.***
- Notes: both states (the trap-spotted state's trip-mechanism line follows).

**13. Storage Area** (`STORAGE-AREA`). Exits: west → Ink Corridor, south → Collapsed Aqueduct (named).
- Current: *…The east wall is solid. A passage leads south, and from somewhere down it comes the sound of water.*
- Proposed: *…and from somewhere down it comes the sound of water.* ***The corridor is back to the west.***
- Notes: all four equipment-sentence states.

**14. Collapsed Aqueduct** (`COLLAPSED-AQUEDUCT`). Exits: north → Storage Area, south → Collapsed Gallery.
- Current: the unsealed states end *…away down the passage south.*; the sealed state ends *…Water moves through it quietly, on its way to somewhere it's needed.* (no exits).
- Proposed: every state adds ***The storage chamber is back to the north.*** The sealed state also adds ***A passage leads on south.***
- Notes: the playtester found `PLACE BLOCK` the only working verb (`LIFT` / `PUT` failed) — for TODO #15.

**15. Collapsed Gallery** (`COLLAPSED-GALLERY`). Exits: north → Collapsed Aqueduct, east → Rickety Bridge (gated).
- Current: north is named only by the flood line (*Water from the passage north…*), which goes once the aqueduct is sealed. Cleared state: *The passage runs east, clear now. The timbers that blocked it are gone, the support beam holding the way open. The shortcut saves time — significant time.*
- Proposed: every state adds ***The aqueduct room is back to the north.*** Cleared state: replace the last sentence with ***Beyond, the passage runs on toward a narrow stone bridge.***
- Notes: **Decision:** "The shortcut saves time — significant time." reads like a designer's note; the replacement names where it leads. The playtester's pickaxe/crowbar "no leverage" confusion is for TODO #15.

**16. Narrow Passageway** (`NARROW-PASSAGEWAY`). Exits: north → Ink Corridor, south → Idol Room.
- Current: *A short passage, plain stone, lower-ceilinged than the corridor behind you. It goes south and ends at a doorway. …*
- Proposed: *…lower-ceilinged than the corridor* ***to the north****. It goes south and ends at a doorway. …*
- Notes: "behind you" is wrong coming back from the Idol Room.

**17. Idol Room** (`IDOL-ROOM`). Exits: north → Narrow Passageway (the slab can block it), south → Combat Room.
- Current: *The room is small and oddly formal — the stonework here is more deliberate than the corridors outside, the walls smoothed, the floor level.*
- Proposed: *…the walls smoothed, the floor level.* ***Doorways lead north and south.***
- Notes: the slab line (*A stone slab fills the north doorway.*) already covers the blocked state.

**18. Combat Room** (`COMBAT-ROOM`). Exits: north → Idol Room, east → Creature Den (door), south → Prayer Alcove.
- Current: *…At the east end a heavy door is set into the stone, shut. Whatever happened in here happened more than once.*
- Proposed: *…At the east end a heavy door is set into the stone, shut.* ***Doorways lead north and south.*** *Whatever happened in here happened more than once.* (Same in the door-open state.)
- Notes: playtester: the door isn't an object, and `JUMP ON PLATE` is the only verb that works — TODO #15. The Rogue's auto-disarm leaves the Den door shut; see #20.

**19. Creature Den** (`CREATURE-DEN`). Exits: west → Combat Room, north → Flooding Room (named).
- Current: *…A passage leads on to the north.*
- Proposed: *…A passage leads on to the north****; the combat room is back through the door to the west.***

**20. Flooding Room** (`FLOODING-ROOM`). Exits: south → Creature Den (down → The Spillway only when the flood takes you). **No change** — *The only way out is back south.*
- Notes: **Decision (playtest theme 4):** a Rogue's automatic disarm jams the plate, and the levers then give no feedback (left grinds, middle does nothing, right snaps off).
  - So the trap side — Quest 50 and the gold nugget treasure — is locked out (feedback "The Flooding Room's levers and its plate").
  - Options: let `JUMP ON PLATE` still fire a jammed plate; make the auto-disarm a choice here (as with Actually Enchanted Glasses); or put a clue on the sluice grate.
  - The design says the plate re-arms after the middle lever, which doesn't help a player who never saw it fire.

**21. Prayer Alcove** (`PRAYER-ALCOVE`). Exits: north → Combat Room, south → Portcullis Corridor (always open).
- Current: *A low stone alcove, barely deep enough to stand in. A carved niche is set into the back wall, its edges worn smooth by hands. It looks like a dead end.*
- Proposed: *A low stone alcove* ***off a passage that runs north and south****, barely deep enough to stand in. A carved niche is set into the back wall, its edges worn smooth by hands.* (drop "It looks like a dead end.")
- Notes: **Decision:** the critical path goes south from here, so "dead end" is wrong for the room. The design's "looks like a dead end until examined" seems to mean the niche (which hides the crowbar and vial). Confirm, and if the alcove itself is meant to be a dead end, the south exit is the mistake.

**22. Portcullis Corridor** (`PORTCULLIS-CORRIDOR`). Exits: north → Prayer Alcove, south → Shrine Room (only the side you came in on, until propped).
- Current: *A straight corridor, closed off halfway along by an iron portcullis. The air around the bars has a faint, dry crackle…* (propped: *…The portcullis is propped open with an iron bar.*)
- Proposed: not propped — add ***The corridor runs north and south; the bars stand between you and the far end.*** Propped — add ***The corridor runs north and south, the way through open now.***

**23. Shrine Room** (`SHRINE-ROOM`). Exits: north → Portcullis Corridor, south → Rickety Bridge.
- Current: *…The air is stiller here than in the corridors outside, as if the room has been holding its breath for a long time.*
- Proposed: *…holding its breath for a long time.* ***A corridor leads north; to the south, the floor gives way to a narrow stone bridge.***
- Notes: both states (the bowl-piece line follows). Plinth and depression as nouns are already in TODO #15.

**24. Mid-Tier Key Door** (`MID-TIER-KEY-DOOR`). Exits: north → Rickety Bridge, south → Key Door Landing (locked until the Middle Tier Key).
- Current: locked — *The door is iron, set deep into the stone. The lock is substantial — no amount of forcing will open this. It wants a key.* Open — *The iron door stands open, the finch key still in its lock. Stone stairs lead down to the south.*
- Proposed: both states add ***The bridge is back to the north.***

#### Dungeon, middle tier

**25. Key Door Landing** (`KEY-DOOR-LANDING`). Exits: north → Mid-Tier Key Door (stairs), south → Mine Passage.
- Current: *The staircase deposits you in a rough cave at the bottom — low ceiling, unworked stone, … The passage continues south.*
- Proposed: *The staircase* ***ends*** *in a rough cave — low ceiling, unworked stone, … The passage continues south****, and the stairs climb back north to the iron door.***
- Notes: "deposits you" only reads right coming down the stairs.

**26. Stored Room / Hole to Below** (`STORED-ROOM`). Exits: west → Mine Passage; east → The Crevice (until the dig); down → Pile of Rubble (after the dig, with the rope).
- Current: before — *The floor is packed tight with rubble — not the chaotic scatter of a cave-in, but deliberate, careful fill. Someone put this here on purpose.* After — *Apparently the "something" being covered was a giant hole. …* + the timber and rope lines.
- Proposed: before — add ***A narrow passage carries on east beyond it; the mine passage is back to the west.*** After — add ***The passage east is out of reach across the gap now. The mine passage is back to the west.***
- Notes: **Decision:** digging loses the Crevice's gold watch for good (a missable treasure). Naming the east passage gives players a fair chance to see it first. Also consider a hint before the dig (e.g. the fill sounds hollow underfoot), so the player knows the floor will go.

**27. The Crevice** (`THE-CREVICE`). Exit: west → Stored Room.
- Current: *The passage pinches down to a crack in the far wall, and a skeleton is wedged into it… One arm hangs back toward you…*
- Proposed: both states end with ***The only way out is back west.***

**28. Inscription Chamber** (`INSCRIPTION-CHAMBER`). Exits: north → Mine Passage, south → Echo Alcove, east → Cave Creature's Lair (crawlspace, perception-gated).
- Current: *A cave room, wider than the passage leading to it. One wall has been worked…*
- Proposed: *A cave room, wider than the* ***passages running north and south from it.*** *One wall has been worked…*
- Notes: the crawlspace stays undirected until found (its found line names east) — the same rule as the Assay Room gap.

**29. Cave Creature's Lair** (`CAVE-CREATURES-LAIR`). Exit: west → Inscription Chamber.
- Current: *…Whatever lives here isn't home. It hasn't been for a while, or it's only just left.*
- Proposed: *…or it's only just left.* ***The crawlspace leads back west.***

**30. Echo Alcove** (`ECHO-ALCOVE`). **No change** — *The passage runs north and south.*

**31. Magnetic Vault** (`MAGNETIC-VAULT`). Exits: north → Echo Alcove, south → Deep Lock Door.
- Current: *A square room, stone walls, a single chest at the center on a low stone platform. …*
- Proposed: *A square room, stone walls, a single chest at the center on a low stone platform.* ***Passages lead north and south.*** *…*
- Notes: all three states.

**32. Deep Lock Door** (`DEEP-LOCK-DOOR`). Exit: north → Magnetic Vault.
- Current: *…This door does not open. The passage ends here.*
- Proposed: *…This door does not open. The passage ends here****; the only way is back north.***
- Notes: **Decision:** the playtester listed it among things they missed. By design it never opens. Keep it as a deliberate dead end (the text is already firm), or give it a purpose later?

#### Dungeon, trap side

**33. The Spillway** (`SPILLWAY`). **No change** — *There's no way back up. The passage continues south.*

**34. Dream Corridor** (`DREAM-CORRIDOR`). **No change** — the numbered decision tree is the navigation (mechanics.md).

**35. Lost Apprentice's Cell** (`LOST-APPRENTICES-CELL`). **No change** — names the tunnel up and *Passages lead north and south.*

**36. Supply Cache** (`SUPPLY-CACHE`). **No change** — *Passages lead north and south.*

**37. Flood Sump** (`FLOOD-SUMP`). Exit: north → Supply Cache.
- Current: *…This is the lowest point down here, and it feels like it.*
- Proposed: *…and it feels like it.* ***The only way out is back north.***

#### Dungeon, lower tier

**38. Pile of Rubble** (`PILE-OF-RUBBLE`). Exits: up → Stored Room (rope), north, east, south (named).
- Current: *…Passages lead north, east, and south.*
- Proposed: *…Passages lead north, east, and south.* ***Your rope hangs down through the hole above.***
- Notes: the player can only be here with the rope tied, so the line is always true. Rubble as a noun is for TODO #15.

**39. Lower Crypt** (`LOWER-CRYPT`). Exits: south → Pile of Rubble, north → Thermal Vent Room.
- Current: *…Whatever the Keeper came down here to do, this is as far as he got.*
- Proposed: *…this is as far as he got.* ***A passage leads on north; the rubble is back to the south.***

**40. The Encampment** (`LOWER-ENCAMPMENT`). Exit: north → Pile of Rubble.
- Current: *…Journals open to pages no one finished. Whatever happened here, no one saw it coming.*
- Proposed: *…no one saw it coming.* ***The only way out is back north, to the rubble.***

**41. Thermal Vent Room** (`THERMAL-VENT-ROOM`). **No change** — *The only way out is back south.* (Says nothing about the ceiling on purpose.)

**42. Antechamber** (`ANTECHAMBER`). **No change** — *Doorways lead east and south; the way you came is west.*
- Notes: **Decision (theme 3):** walking on the bones and entering the south doorway are both instant deaths. The warning is there (*silence is not optional here*), but the playtester asked whether the south room was unwinnable — it is, by design (#43). Options: keep; or make `SOUTH` after clearing give one more warning before the fatal step.

**43. Skeleton Room** — not a room in the engine: `SOUTH` from the Antechamber (after clearing the bones) is the death message. Nothing to describe. See #42.

**44. The Narrow Pass** (`NARROW-PASS`). Exits: west → The Lower Crossing, east → The Still Den (implied by "as you move east").
- Current: *…Somewhere ahead, something breathes — slow and irregular, like sleep that isn't quite sleep.*
- Proposed: *…like sleep that isn't quite sleep.* ***The crossing is back to the west.***

**45. The Still Den** (`STILL-DEN`). Exit: west → The Narrow Pass.
- Current: three states — first visit (it rises), werewolf up (*…It hasn't taken its eyes off you.*), after the kill (*…The scholar lies where the creature fell, the stake still in him.*).
- Proposed: werewolf up and after the kill each end with ***The narrow pass is back to the west.*** The first-visit text stays as it is (the rising is the moment).
- Notes: the playtester's attack-verb issues (every attack says "Your blade finds its mark", even unarmed; only `DRIVE STAKE INTO WEREWOLF` works) are for TODO #15.

**46. Tool Alcove** (`TOOL-ALCOVE`). Exits: south → The Lower Crossing; north → The Flooded Passage once the wall opens.
- Current: before — *…The back wall is flat and featureless.* Open — *The passage ends at a shallow recess lined with empty iron brackets. The back wall stands open. It has nothing left to ask.*
- Proposed: before (and the found states) — add ***The crossing is back to the south.*** Open — *…The back wall stands open* ***onto a passage north****. It has nothing left to ask.* ***The crossing is back to the south.***

**47. The Flooded Passage** (`FLOODED-PASSAGE`). Exits: south → Tool Alcove, north → The Fountain Room (named).
- Current: both states end with the passage north.
- Proposed: both states add ***The alcove is back to the south.***

**48. The Fountain Room** (`FOUNTAIN-ROOM`). Exit: south → The Flooded Passage.
- Current: *…A person. Standing. Composed.* (after the thaw: *…a few sheets of ice melting at its edges.*)
- Proposed: both states add ***The flooded passage is back to the south.***

**49. Dark Room** (`DARK-ROOM`). Exits: north → The Lower Crossing (always open), south → Spirit Room (needs the lantern).
- Current (before the lantern): *You cannot see anything. This is not like being in the dark. This is something the dark is doing on purpose.* Lit: names north and south (no change).
- Proposed (before the lantern): add ***Behind you, to the north, the way you came is still there.***
- Notes: **Decision:** the total dark is the point. "Behind you" is safe (before the lantern the only way in is from the north). Keep the dark absolute, or allow this one line?

**50. Spirit Room** (`SPIRIT-ROOM`). Exits: north → Dark Room, south → Burial Chamber (both blocked while visible).
- Current (visible): *…The passages on either side are visible. Getting to them is another matter.* Invisible: *…Passages lead north and south.* (no change)
- Proposed (visible): *…The passages* ***north and south*** *are visible. Getting to them is another matter.*
- Notes: the trapped-player game over was decided 2026-10-12; this is text only.

**51. Burial Chamber** (`BURIAL-CHAMBER`). Exit: north → Spirit Room.
- Current: *…Everything in this room was arranged deliberately, long ago, by people who are not coming back.*
- Proposed: *…by people who are not coming back.* ***The only way out is back north, through the spirits.***

#### Elsewhere

**52. The Stacks** (`STACKS`). Exit: west → Library (Main Hall).
- Current: *The passage from the Main Hall opens into something that shouldn't fit inside this building.*
- Proposed: *The passage from the Main Hall****, back to the west,*** *opens into something that shouldn't fit inside this building.*

**53. Will's Wizard Tower** (`WIZARDS-TOWER`). Exits: north → Will's Bedroom (perception-gated); the painting teleports to the Tale and Ale.
- Current: *…A painting hangs on the wall, slightly crooked. …* Once the door is found, *You notice a door to the north you hadn't seen before.* prints once and is never mentioned again.
- Proposed: once found, add a lasting line ***A door in the north wall stands where you'd have sworn there wasn't one.*** (like the Volcano's staircase line).
- Notes: **Decision:** the tower has no ordinary way out — the painting is it (`EXAMINE PAINTING`). Hint its subject (*A painting of a tavern hangs on the wall, slightly crooked.*)? Related to TODO #14 (revealed ways in BRIEF mode).

**54. Will Passion's Bedroom** (`WIZARDS-BEDROOM`). Exit: south → Will's Wizard Tower.
- Current: *…A nightstand holds a half-melted candle…* then *The rest of the room is Will's business and clearly has been for a very long time.*
- Proposed: before the closing line, add ***The door back to the tower is south.***

**55. West of House** (`WHITE-HOUSE`). **No change** — the opening; the mailbox is the way in, by design.

#### Proposed additions (beyond the rooms)

- **Record the rule in mechanics.md** (a new "Room descriptions name their exits" entry):
  - Every room names each exit the player can use now.
  - Perception-hidden exits get no direction until found (the Assay Room gap, the Inscription Chamber crawlspace).
  - Deliberate exceptions: the bog's interior, the Open Ocean, and the Dark Room before the lantern.
  - A way the text shows but the player can't take gets its own refusal (the Lighthouse chain, the Rickety Bridge west, the guest-room doors).
- **Make it a test.** Turn the scratch sweep used for this pass into a test over every room, with the exceptions above listed explicitly, so a new room can't ship without its exits.
- **The reverse check.** Sweep for directions the text names that have no exit (the Lighthouse stair was one) and give each a refusal message. Noted during the pass: the Crevice's crack in the far wall (`EAST`: default refusal; e.g. *"The crack is far too narrow. He found that out."*); the Collapsed Aqueduct's channel running "east to west" (probably fine as is — it's waist-high, not a passage).
- **Engine-versus-design drift.** Several rooms had lines the engine had silently dropped from the design (the Wasteland, Pipe Room, Mine Entrance sign, Empty Beach; Mine Tunnels and the Rat's Nest above). A check comparing each room's engine text with its locations.md description would catch the rest.- **Text that assumes where the player came from** ("behind you", "back toward", "deposits you"): fixed where found; worth one grep across all room text once the pass is done.
