# Roundabout: The God-Forsaken Ring — Open Design Questions

Consolidated from all source files. Update this file when items are resolved; record the resolution and the source file where it was written.

---

## TODO #1 — Narrative-Driven Test Rewrite

**Status:** In progress — the ring walkthrough (`walkthrough_ring.txt`, `test_walkthrough_ring_v2.py`) passes end to end, A–U (2026-10-04). Next: the full-score walkthrough (`walkthrough_fullscore.txt`, `test_walkthrough_fullscore_v2.py`), section by section from A.

**Goal:** Both walkthroughs — ring quest and full score — passing with zero state injection. The narrative rewrite is complete only when the full-score walkthrough passes too.

**Current position:** Full-score walkthrough, Section Z — Quest 28, Inscription Chamber Rubbing. Sections A–Y pass. First failure:

```
SECTION [Z) Quest 28 — Complete: Inscription Chamber Rubbing]
  cmd     : 'SOUTH'
  missing : 'Inscription Chamber'
  got     : "You can't go that way."
```

The Inscription Chamber (Mine Passage south) isn't built yet. 307 full-score steps still fail.

Y bridge plan (2026-10-04, built): the minimum load is 13 (key, shovel, rope, lockpicks, thin paper, ring + 3 worn), so Y crosses twice — `DROP ALL BUT RING, KEY, SHOVEL AND ROPE` (11), cross, unlock (the key stays in the lock), come back north, take the lockpicks and `THIN PAPER` (plain `PAPER` also matches the folded note), cross again. The shovel is dropped once the hole is dug; the rope stays tied.

Plan for Z: explore folding Section UU (Trophy Case deposits) into the run around Z — deposit treasures as they're collected instead of in one trip at the end. That removes UU's separate run and sheds weight for the bridge (EE's return trip north carries ~17–18 otherwise). Needs the Trophy Case built. Also fold AA's text (silver dust collected) into Z and drop the empty AA section.

Full-score order after C (2026-10-04): D Pond, E Bog rune stone, F Music Box, G Shamus's Recipe, H Mugger, I Beekeeper, J Viking trials, K Lynds, L Litlock, M Archer; unchanged from N.
- Mugger moved late: a level-1 Warrior can't spot him or win the fight, and the walkthrough will be player-facing.
- Lynds after the Viking trials: always-max can't win at level 3 (21 vs his 23); level 4 comes during J. Litlock follows Lynds (needs the invitation).
- Routes between all of C–M connect.

The full-score walkthrough fails at 342 steps in total; much of it predates the ring-walkthrough design decisions (cellar route, Collapsed Aqueduct split, ZENNI offering, dial direction, etc.), so expect walkthrough corrections as well as engine work.

**XP note:** in the ring walkthrough the player is level 6 by the end of K (Quest 32 reward) and finishes at level 6 with 307 XP. Not a problem for the ring path; worth checking against the level curve when TODO #4 is reconciled.

**Completed:**
- Steps 1–4 from original plan done (walkthroughs written, test files created, old tests deleted)
- Sections A–F passing (opening, tower bedroom, Kevry's island, ring retrieval + Will's second briefing, Viking trust trials, Pale Blade forging)
- Engine additions: V-WEAR, V-REMOVE, V-TALK, V-GIVE, V-PUT-ON, V-ACTIVATE, V-DRINK, V-BUY, V-BOARD-SHIP, V-SAIL, V-DOCK, V-LIGHT, V-DROP, nautical walk preaction, cave-in trigger, raw-input hook (riddle answers); NPCs Shamus, Kevry, Pyronicus, Will, Raznak, Ivanaar, Haalvar, child, Aylora; rooms through the Viking Encampment
- Parser: FIND flags are preferences (try each structurally matching rule in order, fall back to the first with FIND ignored); particle retry; preposition-before-object rules (`LOOK AT X`)
- Opening rewritten to match npcs.md
- Viking trial order: 1 and 2 in either order, Aylora (3) gated until both done
- INVENTORY verb
- Unbind Undead scroll picked up in C (Lighthouse), taught by Will in D (3 Zenni)
- Glasses instant-fail in Will's presence; GAME OVER ends input
- Hidden Zenni rooms (36, seeded at init; tests pin seed 7)
- Old Oak area (Quest 41 kite, Beekeeper's Cottage, Swarm Tree), forest + bog bowl pieces, Pond and 4 bog rooms
- SAVE / RESTORE
- Town Square statue: USE CROWBAR ON STATUE, silver stake, folded note (clue only)
- Dungeon upper tier I1/I2: ink trap (Trap 45, inked flag), Supply Room items, Storage Area/hand cart, Combat Room + Warden + plate-operated Den door (Trap 29), Creature Den, Prayer Alcove niche, Portcullis (Trap 19, LIFT + bar), Shrine Room piece, Rickety Bridge weight limit, Key Door (locked); death is GAME OVER
- Lighting: dark rooms hard-block without light; torch lit on purchase, 100-turn timer from first dark room, warnings, burnout fatal only when stranded in the dark
- Crypt (visit-based descriptions), Secret Tunnels, Toll Bridge (seal, Boggart, 200 toll, charter, strongbox — Quest 27), Dungeon Entrance; Mausoleum now dark
- Town Hall (one room: exterior + foyer), Records Room worker and charter (Quest 17 completes), Council Chamber / Upper Hall / Tower rooms
- Church Nave, Graveyard (pre/post bonk), Mausoleum, Chuckle House (mirrors, Trap 16, ghost, 50% exits), WEAR/REMOVE RING with corruption, CAST UNBIND UNDEAD; full corruption is GAME OVER
- Kevry per design (enchant on arrival if worn; WEAR in front of him if carried; quest-hint line without glasses)
- Dankhaus path (Medium perception), wards, 7 Dankhaus rooms, Litlock's tree as a numbered menu (Quest 52)
- Lynds (Quest 59): CHALLENGE / TALK TO, contested roll with tie reroll, 20-turn loss cooldown, Heart Necklace +1 heart while worn
- INVENTORY marks wearable items (not worn); TAKE prefers objects not already held
- The Alley, Back Alley, mugger (Medium perception, one combat round per KILL, losing isn't death), May's first visit and Quest 51 free drink
- Walkthrough cleanup: Q and R removed (bowl pieces in C1/E, fire clay in M), rope taken at end of C2
- Section K: Rowan (start / in progress / reward / after), Bog-SE gravestone (Easy perception), LOAD STONE ONTO CART, loaded cart blocks UP/DOWN, UNLOAD STONE (+ synonyms, SET STONE input hook) — at the Graveyard leaves the cart, Middle Tier Key (TAKE KEY). Quest 25: May's cellar key (needs crowbar), cellar door (key stays in lock), USE CROWBAR ON DRAIN / PRY COVER / REMOVE COVER WITH CROWBAR, CLEAR DRAIN, drowning GAME OVER (stairs, Bone Passage door), lit Cellar with cashbox (10 Zenni), tunnel door to the Bone Passage, Bartender's Boots. Torch exchange via BUY TORCH (swap tiers). Quest 32 reward fixed to 5 Zenni.
- Section L: cellar route, DROP ALL BUT with comma lists (DROP ALL keeps worn items), bridge weight checked both ways, Mid-Tier Key Door unlock (key stays in lock), Key Door Landing, Mine Passage, Stored Room / Hole to Below (DIG, TIE ROPE TO BEAM, JUMP death), Pile of Rubble, Will's DIG note. N and P climb back up to the Hole to Below.
- Section M: Lower Crypt (key ring; skeleton, emerald seal, pendulum blade as scenery), Thermal Vent Room (LOOK UP / LOOK AT CEILING reveals fire clay; LOOK UP elsewhere = LOOK), The Encampment. `LOOK UP` fragment → [reddish clay] in both walkthroughs.
- Section N: TAKE STAKE at the Rickety Bridge, climb out through the Crypt; Nave west door (UNLOCK DOOR WITH KEYS, keys stay in the lock), lit Keeper's Chamber (vial / no-vial descriptions, readable Keeper's note), POUR HOLY WATER ON STAKE (consecrated silver stake); torch swap in the Kitchen after the holy water. O rerouted down through the cellar.
- Section O: Antechamber (Trap 36 — CLEAR BONES, 3 XP / Rogue +5; EAST or SOUTH before clearing is death, WEST safe), Skeleton Room death, The Lower Crossing, The Narrow Pass, The Still Den (werewolf rises after the entry turn, one 3d10 round per later turn, melee and plain-stake failure lines, consecrated stake kills — stake stays in the body, amulet drops, 15 XP / Warrior +10).
- Parser (with O): `drive` is its own verb (was mapped to exorcise); DRIVE … INTO matches ("into" is a synonym of "in").
- Section P: Collapsed Gallery split — new Collapsed Aqueduct (Quest 22) south of the Storage Area, Gallery south of it, Gallery EAST ↔ Rickety Bridge WEST gated on Quests 38 and 22; PLACE BLOCKS ×3 (Medium strength check each), SEAL JOINTS WITH MORTAR / USE MORTAR ON …, fountain runs; flooded Gallery.
- Section P (cont.): TAKE ALL at the bridge collects the L drop. Parser: second PUT rule for things on the floor (PLACE), SEAL verb.
- Section S: Town Square fountain object; MIX CLAY WITH WATER (clay adhesive); ASSEMBLE BOWL (input hook — every piece answers to "bowl"); forest pedestal states; PUT BOWL ON PEDESTAL; PUT ZENNI ON PEDESTAL (OFFER / DROP ZENNI, COIN accepted; 1 Zenni, gone) → Crystal Bowl, Quest 49 complete; TAKE BOWL.
- Section T: T route (Main East → SOUTH); The Altar east of the Nave; dial (RIGHT forward, LEFT back, wraps); artifact placing, glow (persists; lost when taken off), altar listing, ring-too-early, binding ceremony (artifacts consumed, ring bound, 5 XP); a worn ring comes off through the normal removal check. Parser: a trailing particle (`TURN DIAL LEFT`) is understood.
- Section U: SCORE (treasure points, level, XP, treasures on display — meta, no turn); GIVE RING TO WILL with the bound ring plays Will's final scene, the end-of-game SCORE (denominators + tier title), the closing line, then GAME OVER. Test harness: a fragment may list several required pieces separated by `|`.

- Full-score Section C: Lighthouse scroll added; fishing rod (Shamus, 8 Zenni) bought in D after the chest pays; treasure map (Hard perception each turn aboard, straight to inventory).
- Section C (cont.): ship position on boarding fixed (from Kevry's island 69 GO WEST reach the Eastern Roundabout Sea — ring fragment updated); SET SAIL needed before sea moves from a moored deck; SAIL <dir> casts off and moves in one turn.
- Section C (cont.): Desert Island DIG / buried chest / OPEN CHEST pockets 30 Zenni (TODO #2); ship return scene and Pie Rat Coin (boarding afterwards needs the coin carried); DIG elsewhere refusal; LOOK AROUND = LOOK. Section D route fixed (Docks → town via the Kitchen for the rod → Pond).
- Section D: Roundabout Pond bottle — Medium sighting check each visit until seen, FISH (Hard fishing roll; rod required), bottle lands on the bank, TAKE BOTTLE. Full-score test harness now accepts "|" fragments, like the ring test.
- Going ashore: DOCK / LAND / MOOR / MAKE LAND are one action, working only beside land; the ring walkthrough's return now sails to the Western Roundabout Sea before DOCK.
- Section E: bog rune stone (Bog-NE), hollow log and music box key (Bog-NW), bog thyme (Bog-SW) — Medium perception every visit until found, listed in the room description. The E rune stone fragment is now [You take the rune stone] (it used to pass on the Old Oak stone already held).
- Examine text: objects have a separate `examine` field (54 objects converted); EXAMINE no longer touches an object, so room listings stay put. DROP says "You drop the [item]."; multi-object results are labelled only when the line doesn't name the item. F: Unbind Undead scroll given to Will before the music box.
- Pie Rat heist: flint and steel moved to the Assay Room; the 40-turn burnout removed from the design.
- Heist (cont.): Mine Tunnels weak point (Easy perception), DROP GUNPOWDER wedges it there, LIGHT needs the flint and the gunpowder placed, 5-turn fuse, death if still in the mine, cave-in seals DOWN from the Mine Entrance (post-cave-in description). Both walkthroughs take the flint in the Assay Room and check the explosion.
- Section F: music box (Will's three hints, locked / opened with the key, key stays in the lock), Light scroll; Quest 12 completes when the scroll is found. Light spell per mechanics.md (continuous; quests/items/npcs updated): CAST LIGHT, step into the dark from a lit room, goes out in lit rooms. Final F fragment now [The knowing, I mean].
- Torch burnout with the Light spell: not fatal while Light is lit; known but not lit — two commands to CAST LIGHT, else death. P's CAST LIGHT moved to the Mausoleum (first dark room), fragment [darkness pulls back] — check when P is reached.
- Section G: TALK TO SHAMUS adds the Quest 40 recipe line until the quest is complete (discovers Quest 40). Section J: Ivanaar fragment now [circle is south] (matches his designed line).
- Section M: Raznak states 2A (Rogue), 2B (offer), 3 (training + bow, later greeting); PAY RAZNAK / bare PAY / GIVE RAZNAK THREE ZENNI; Bow object; Quest 55 completes on training (Zenni reward dropped). Walkthrough: [learn the bow], PAY RAZNAK [This one's yours], TAKE BOW removed.
- Section O: Lighthouse scroll trip removed (scroll picked up in C, taught in F); Upper Hall display cabinet and wax seal (Quest 4). P passes as is.
- Section Q: Trap 17 (first entry, Medium/Medium, smoke jar and small clay pot), Trap 33 (SWAP IDOL WITH SALT; unswapped TAKE seals the north doorway, PRY DOOR with the crowbar, Medium strength). Q rerouted to match the ring's I1/I2/K. Parser: LOAD and UNLOAD prefer what isn't in the pack, like TAKE. Idol Room description drops the figurine once the idol is gone.
- Section R: note fragment now [folded note] (taking it uses the standard line). Section S: Light cast in the Mausoleum (the torch burns out harmlessly on the way); aqueduct repair as in the ring's P (Storage Area → Collapsed Aqueduct, PLACE BLOCKS ×3, SEAL JOINTS WITH MORTAR).
- Section T: Quest 38 — three Hard strength checks with the pickaxe (retries), support beam props the passage (only then does the way east open); HIT / CHOP / BREAK TIMBER, PROP PASSAGE WITH BEAM, PUT BEAM. "timber" is now an adjective for the support beam. Quest 38 reward fixed to 5 Zenni. T rerouted from the Collapsed Aqueduct and tries the shortcut.
- Section L: walks every Dankhaus room after Litlock's bonk (TODO #4). Lynds's Room is empty — Lynds is always in the Tale and Ale (locations.md corrected).
- Section U: rewritten on the ring's K cellar sequence (TALK TO MAY, UNLOCK DOOR WITH KEY, OPEN DOOR, USE CROWBAR ON DRAIN, CLEAR DRAIN — no going down into the water), plus the cashbox and May's boots. Parser: UNLOCK / OPEN … WITH KEY uses the one carried key that fits.
- Section V: Quest 40 delivery — thyme and pot to Shamus in either order; the second completes the quest (hearty stew flag, 3 Zenni). Between deliveries Shamus says which item he still needs. V also buys the thin paper (Shamus, 2 Zenni).
- Section W: Whispering Jar in the Pipe Room (EXAMINE JAR discovers Quest 4); Ty's Casino Corner and the Upstairs Hall built and visited. Parser: EXAMINE prefers what isn't in the pack.
- Section X: Library — Main Hall and The Stacks, the Librarian (three states), the Archivist (four states; first talk discovers Quest 28).
- Section Y: two-crossing bridge plan; Mine Passage charcoal, silver dust (Medium perception), iron chest (lockpicks, 20 Zenni pocketed); The Crevice and gold pocket watch (own object); Stored Room EAST refused after the dig; shovel dropped after the dig. Quest 28 uses up the paper and charcoal.

**Known issues still open:**
- Ty's Cargo dice game (mechanics.md, reference-cargo-game) isn't built — Ty is part of his room description; TALK TO TY gets the generic no-response line.
- The Archivist's book-research mechanic (TALK TO ARCHIVIST about a subject, READ BOOK) isn't built.
- Thin paper "destroyed if player gets wet": no wetting events are defined yet.
- Full-score plan: the torch is allowed to burn out in the full run; no repurchase once Light is learned (F). Check P onward against that.
- `TAKE ALL` also tries items already in inventory ("You already have the …" for each). Predates this session.
- Parser quirk: a full sentence naming a missing object gets the parser's "You can't see any X here!" instead of the designed refusal — `SEAL JOINTS WITH MORTAR` without the mortar, `MIX CLAY WITH WATER` away from the fountain. The designed lines appear for the short forms (`SEAL JOINTS`, `MIX CLAY`).
- Trophy Case (Town Hall Tower) not built — design in mechanics.md (Trophy Case, Score). Score and treasures read 0 until it is. The full-score walkthrough needs it.
- Deferred from P: Quest 22's food & drink price cut is a flag only — buying food and drink isn't built.
- Deferred from O: Lower Crossing north (Tool Alcove) and south (Dark Room), the 50/50 pull-back text, the Ivory Torch (Quest 34); bow and fireball attacks on the werewolf (failure lines are in mechanics.md, but neither attack exists yet).
- Deferred from L: Mine Passage south exit (Inscription Chamber and beyond).
- Floor listings: the burnt-out torch shows as "A torch." and plural items read "There is a lockpicks here."
- Deferred from I1: Flooding Room (north of the Creature Den; Trap 41 — exit blocked until built).
- Inked state (Trap 45): flag built and cancels ring invisibility; NPC refusals and the inn bath still to build.
- Ring invisibility vs. the Dankhaus wards (npcs.md: invisible-entry lines) not built yet — comes with WEAR RING in H3.
- Class XP bonuses (experience.md — Class XP Adjustments): Warrior +10 per kill is built (Aylora excluded — not a kill). Mage +1 per new dungeon room and Rogue +5 per trap disarmed are not built yet — add when the dungeon and traps are.
- Quest 51 bounty notice (May posts it after 100 turns if the mugger lives) isn't built or written. The full-score run is well past 100 turns by the mugger in F, so the notice will be due there.
- The God-Forsaken Ring has no room/inventory description in items.md (code uses placeholder "A plain dark ring.").

**Policy:** When a new walkthrough test fails, fix the engine. Never adjust the narrative or add state injection to make a test pass. Only fix the walkthrough when the design doc confirms the walkthrough is wrong.

---
## TODO #2 - Fix chest in section D — RESOLVED 2026-10-04

**Resolution:** items.md now has a Buried Chest entry. Decision: `OPEN CHEST` pockets the 30 Zenni directly, like the Cellar cashbox (no `TAKE ZENNI`). Full-score walkthrough (now Section C) uses DIG → OPEN CHEST.

When the user digs to find the chest in section D, it would be closed.  It's a container, and would need to be OPENed for the user to then take the zenni inside.  Is this not clear in the design document?

The buried chest doesn't have its own item entry in items.md — it's only referenced as a destination for the treasure map and shovel. There's no explicit definition of its flags (CONTBIT, OPENBIT, etc.) or whether DIG exposes a closed container that then requires OPEN.

The gap is in items.md — the buried chest needs its own entry that specifies it as a container with CONTBIT/OPENBIT, requiring OPEN before TAKE ZENNI. Add that entry to items.md, then fix the fullscore walkthrough to include OPEN CHEST between DIG and TAKE ZENNI.

---
## TODO #3 — Reconcile game-state key names — RESOLVED 2026-10-03

**Resolution:** Player stats use lowercase keys everywhere; story/world flags keep UPPERCASE-HYPHEN keys (no conflicts there).
- `char_create.py` writes `player_name`, `player_class`, `hearts`, `max_hearts`, `zenni`, and `skill_<starting skill> = True` (skills stay True/False flags so a player can hold several).
- `init.py` `_init_player_state` sets defaults before character creation.
- `verbs.py`: V-BUY uses `zenni`; glasses worn state comes from the object's WEARBIT, and `_set_glasses_state` sets `enchanted_glasses_worn` / `actually_enchanted_glasses_worn`. The `<OBJ>-WORN` globals are gone.
- First room visit now awards the room's value as XP (`award_xp`) as well as Zork score. Room values match locations.md XP for every room built so far.

Remaining unit-test failures (14) are unrelated: test_world expects rooms/objects not yet rebuilt, and test_combat imports weapon functions removed in the content wipe.

---
## TODO #4 — Full-score walkthrough must visit every room

`walkthrough_fullscore.txt` was scoped to quests, treasures and NPC arcs, not exploration. These rooms (all with XP in locations.md) are never entered:

- **Tale and Ale:** Pipe Room, Ty's Casino Corner, Upstairs Hall — visited in Section W (2026-10-04)
- **Dankhaus:** Hearth Room, Garden, Litlock's Room, Litlock's Study, Lynds's Room, Aurix's Room — visited in Section L (2026-10-04)
- **Tunnels / dungeon:** Hidden Secondary Entrance (mine — Assay Room gap), The Undercroft, The Forgotten Shaft, Skeleton Room (Room 6), The Flooded Passage (Room 11)

Also confirm Key Side / Trap Side sub-rooms are all entered — the walkthrough labels these areas loosely.

For each room: check access requirements in locations.md, then add the visit where the route already passes nearby. Once TODO #3 connects XP, assert total exploration XP at the end of the run.

**Total is unresolved:** experience.md says 130 (was 133 before guest rooms went to 0), but the `**XP:**` values in locations.md sum to 173 across 131 entries (2026-10-03). Reconcile before using either number as the test target.

Guest Rooms 1–3 are excluded: set to 0 XP (rest-only, random assignment) on 2026-10-03 — see locations.md and experience.md.

---
## TODO #5 — Build TIP MAY (hint system)

`TIP MAY [#]` parses to `V-TIP`, but no handler exists, so `may_hint()` in `content/actions.py` is never called. The `_HINT_LINES` table there predates the design and contradicts it for every quest it covers (51, 25, 30, 53, 41, 50, 34, 22 — e.g. a "Tally" for Quest 25, Pie Rat hints under Quest 22, hints for Quest 53 which has none by design). Replace it, don't patch it.

Build from the design: blind tipping and tier ranges (mechanics.md — Hint System), May's response lines, per-quest hints from quests.md (including one-tier and conditional hints: Quest 4 after first lower-tier descent, Quests 19&30 statue hint only if not examined, Chuckle House pre/post-visit, Quest 34 late hint), and hints unlocking on discovery.

No ring-path step needs a hint (nothing checks for one), so the ring walkthrough doesn't wait on this. Quest 32 leans on May's hints to point players at Rowan and the bog — nothing else in-game does (decided 2026-10-03: leave it that way).

Open question: quests.md Path A for Quests 19&30 reads "May's tier 1 hint → TALK TO LIBRARIAN reveals…". Confirm the Librarian's scholar dialogue does not depend on the hint having been bought.

---
## TODO #6 — Build and test the Quest Board and May's tips

Neither walkthrough needs them (no step checks the board or a hint), so the walkthrough tests won't exercise them. They need their own code and their own tests.

- **Quest Board** (Bar — `LOOK AT BOARD` / `READ BOARD`): postings from the design — quests posted at game start, on first visits (e.g. Quest 40 on meeting Shamus) and by cascade (quests.md, mechanics.md — Quest Board), removals (e.g. Quest 50 when Trap 41 is disarmed), the Quest 51 bounty after 100 turns, and how completed quests show.
- **May's tips:** build per TODO #5 (TIP MAY tiers, blind tipping, conditional hints, hints unlocking on discovery).
- **Tests:** a dedicated test file (not a walkthrough) that drives game state through do_turn where it can — discover, progress and complete quests — and checks the board text and each tier of May's hints, including conditional and one-tier hints.

