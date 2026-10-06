# Roundabout: The God-Forsaken Ring — Open Design Questions

Consolidated from all source files. Update this file when items are resolved; record the resolution and the source file where it was written.

---

## TODO #1 — Narrative-Driven Test Rewrite — RESOLVED 2026-10-05

**Status:** Resolved — both walkthroughs pass end to end with no state injection: the ring walkthrough (`walkthrough_ring.txt`, `test_walkthrough_ring_v2.py`), A–U, and the full-score walkthrough (`walkthrough_fullscore.txt`, `test_walkthrough_fullscore_v2.py`), A–SS (2026-10-04). The known issues below were all resolved by 2026-10-05.

**Goal:** Both walkthroughs — ring quest and full score — passing with zero state injection. The narrative rewrite is complete only when the full-score walkthrough passes too.

**Current position:** Both walkthroughs pass end to end with no state injection (2026-10-04). Full-score sections renumbered A–Z, AA–SS. All known issues resolved 2026-10-05.

0 full-score steps fail.

Y bridge plan (2026-10-04, built): the minimum load is 13 (key, shovel, rope, lockpicks, thin paper, ring + 3 worn), so Y crosses twice — `DROP ALL BUT RING, KEY, SHOVEL AND ROPE` (11), cross, unlock (the key stays in the lock), come back north, take the lockpicks and `THIN PAPER` (plain `PAPER` also matches the folded note), cross again. The shovel is dropped once the hole is dug; the rope stays tied.

Trophy Case: deposit treasures as they're collected (O: Ship-in-a-Bottle, Pie Rat Coin; EE: gold watch, diamond brooch, idol).

Surface-items plan (2026-10-04, built for EE, HH2, II, OO; TT pickup still to write) — II's bridge crossing was 21 against 12:
- Quest 42 moves to right after HH: all three rune stones go to Ivanaar (tunic worn, 1). NN shrinks to the bog-exit route.
- EE drops the Pale Blade in the Church of All (TT picks it up there) and the three bowl pieces and smoke jar in the Bone Passage.
- II's crossing is then 11: worn 4 + tunic 1 + stake 2 + incantation scroll 1 + vial 1 + lantern 2.
- OO went down through the Tale and Ale cellar to the Bone Passage, took the bowl pieces and smoke jar, then detoured Junction → Undercroft → Forgotten Shaft → Hidden Secondary Entrance → Assay Room and back for the room XP (from the tunnel side the gap is found automatically). Back up the cellar to the Town Square fountain, then the Forest shrine. No Trophy Case stop — treasures are deposited at the end. The mine can't be entered from the Forest — the Mine Entrance is sealed after Section C's explosion.
- Section letters renumbered 2026-10-04 (old → new): BB→AA, CC→BB, EE→CC, FF→DD, GG→EE, HH1→FF, HH2→GG, II→HH, JJ→II, KK→JJ, LL1→KK, LL2→LL, OO→MM, PP→NN, QQ→OO, RR→PP, TT→QQ, UU→RR, VV→SS. A–Z unchanged. Done entries above use the old letters.
- LL1 built: shovel taken at the Hole to Below; the bridge is crossed twice (blade and mask first, then shovel, fire clay, amulet).

Full-score order after C (2026-10-04): D Pond, E Bog rune stone, F Music Box, G Shamus's Recipe, H Mugger, I Beekeeper, J Viking trials, K Lynds, L Litlock, M Archer; unchanged from N.
- Mugger moved late: a level-1 Warrior can't spot him or win the fight, and the walkthrough will be player-facing.
- Lynds after the Viking trials: always-max can't win at level 3 (21 vs his 23); level 4 comes during J. Litlock follows Lynds (needs the invitation).
- Routes between all of C–M connect.

**XP check (2026-10-05, Warrior):** ring walkthrough — level 2 in C1 (before the dungeon), level 6 in K, level 7 in S; finishes at level 7 with 332 XP. Full-score walkthrough — level 2 in C, level 8 in II (440 XP); finishes with 552 XP. Both fit the curve in experience.md.

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
- Section Z: Inscription Chamber (Medium rune stone and snare checks; Trap 8 — spotted = stepped around, 3 XP / Rogue +5; fired = hanging until PULL FREE / STRUGGLE or CUT CORD with a blade), RUB PAPER ON ENGRAVING (paper + charcoal used up → rubbing), Cave Creature's Lair and bone flute, Echo Alcove, Magnetic Vault (Trap 15 — DISARM LODESTONE, iron-only pulse, stuck-to-chest line, Medium strength per item), Diamond Brooch, Deep Lock Door.
- Section Z (cont.): AA folded into Z; UU's brooch detour removed. Lockpicks dropped after the Mine Passage chest. Parser: CUT prefers what isn't carried; STRUGGLE / PULL FREE verbs.
- Section CC: Tool Alcove (Medium perception, 'notices you' + question lines, also on a return visit; EXAMINE WALL / LISTEN; 50/50 pull-back line once; north waits for READ SCROLL in JJ). Ivory Torch on the Still Den wall — heat, not light (LIGHT refusal).
- Section CC (cont.): CC is the Quest 34 discovery only (no Still Den visit); DD folded into II (fire clay after the jar's hint); torch taken in II after the kill; EE's first SOUTH removed; FF prose fixed.
- Trophy Case (The Tower): OPEN / CLOSE CASE, PUT / DROP … IN CASE (treasures only, points from items.md, SCORE reads them), room and EXAMINE / LOOK IN listings, nothing comes back out (deposits are flagged against the implicit take). Section O deposits the Ship-in-a-Bottle and Pie Rat Coin (no sailing after O); UU reworded to 'remaining'. Post-dig [Stored Room] fragments → [Hole to Below] (EE, II, LL).
- Section EE: bridge pickups (stake, idol, wax seal, Pale Blade, three bowl pieces, two rune stones, smoke jar — the vial and lantern stay for II); ring's N route to the Keeper's Chamber; Tower stop deposits the gold watch, diamond brooch and idol. FF reaches the Pipe Room from the Tower.
- Bowl pieces and rune stones have distinct names (large / muddy / stone bowl piece; flat / grey / pale rune stone); fragments updated in both walkthroughs.
- Section FF: Whispering Jar restoration (PRESS SEAL → 5 Zenni in the jar, DUST JAR, READ INSCRIPTION — Medium perception, whisper repeats on re-read; LISTEN hum / quiet; seal and dust used up). Jar's READ word is INSCRIPTION (GG brings the incantation scroll). Parser: DUST / LISTEN TO prefer what isn't carried; PUT / SPRINKLE / PRESS … ON targets prefer what isn't carried. GG starts WEST from the Pipe Room.
- Section GG: GIVE RUBBING TO ARCHIVIST (or TALK TO him carrying it) → his line, [Incantation scroll added to inventory.], Quest 28 (3 Zenni silent). Incantation scroll object; READ SCROLL away from the door has its own line; the scroll is never used up (can be left behind after Quest 34). GIVE refusals say 'The' for titled / common-noun NPCs. [Main Hall] fragments in GG and HH; TAKE SCROLL dropped.
- Section HH1: GIVE FLUTE TO PYRONICUS → his line, [Fireball scroll added to inventory.], Quest 7 (3 Zenni silent); Fireball scroll joins Will's spell scrolls; GIVE prefers items meant for whoever is present. Section HH2: Quest 42 moved before II — GIVE STONES (any stone stands for the set; fewer than three handed back), tunic object + WEAR line, combat checks the tunic is worn; Quest 42 Zenni 6 → 5 per quests.md. II: CAST LIGHT in the Mausoleum, [creature drops] as in the ring walkthrough. EE drops the bowl pieces and smoke jar in the Bone Passage, the Pale Blade in the church.
- Section JJ: READ SCROLL opens the Tool Alcove wall (scroll dropped after); The Flooded Passage (swimming 1 heart, POUR VIAL freezes the pool, vial used up) and The Fountain Room (HOLD TORCH NEAR ICE / MELT ICE WITH TORCH twice → [The Forgotten Blade added to inventory.], Quest 34; ordinary torch lit/out lines; Ivory Torch dropped after). II picks up the vial and lantern at the bridge. Fireball wired into CAST (enemy loses 1 heart, no strike back; werewolf failure line; ice line; 'Nothing here' with no timer); a spell cast before it's ready doesn't use a turn (engine: HOOK_NO_TURN). test_combat's two fireball tests (passing by accident) rewritten against the Warden. KK starts with SOUTH ×3 from the Fountain Room.
- Section KK: Dark Room (magical darkness; LIGHT / TURN ON LANTERN reveal, lantern hangs for good; SOUTH and CAST LIGHT lines before it; flicker line elsewhere), Spirit Room (both exits blocked while visible, ink counts; ring-on/off lines; invisible description; spirits examine/attack), Burial Chamber (Funeral Mask, plinth line changes once taken). Prose fixed (south of the Lower Crossing); WEAR RING fragment tightened.
- Section LL1: Flooding Room (Trap 41 — plate like Trap 29, two-turn sluice, levers, middle lever re-arms, sweep to The Spillway); parser object lists (TAKE BLADE AND MASK).
- Section LL2 (+MM): Dream Corridor (numbered menus, light not torch), Lost Apprentice's Cell (fight 2d8/3 hearts, Fireball, freed not killed, USE SHOVEL, UP to Bog-NW with the gloves; Quest 50 Zenni 6→5), Supply Cache (SEARCH RUBBLE → gold nugget), Flood Sump.
- Section OO: Forgotten Shaft and Hidden Secondary Entrance (mine branch; Assay Room gap — Medium perception from the mine side, found from the tunnel side); cellar route with CAST LIGHT twice; bowl ending from the ring walkthrough (PUT ZENNI ON PEDESTAL); Assay Room description restored to the design text.
- Section PP: Swarm Tree (USE SMOKE JAR settles the bees, the jar is used up, the queen vial appears; carrying the jar holds the swarm off), GIVE VIAL TO BEEKEEPER → enchanted honey straight to inventory (Quest 24), EAT HONEY restores 2 hearts; TAKE HONEY step removed.
- Section QQ: Redcrosse Knight in Town Square (presence, examine, Warrior lines); Quest 54 trial for Mages and Rogues (2d8, 4 hearts, to 1 heart either way; Fireball refused), PAY KNIGHT / GIVE KNIGHT THREE ZENNI teaches melee; Quest 54 Zenni reward dropped (3 Zenni fee kept). test_knight.py plays the trial as Mage and Rogue. Fragment: TALK TO KNIGHT [already know what I teach].
- Section RR (SS folded in): Will's Bedroom — nightstand scenery (EXAMINE, PUT … ON), dragon-nip under it (silent Hard check on every entry and on WEAR GLASSES there; Actually Enchanted Glasses auto-pass), GIVE DRAGON-NIP TO WILL → Golden Dragon Scale straight to inventory (Quest 58: 15 XP, 5 Zenni — experience.md updated from 4).
  DROP / PUT GLASSES ON NIGHTSTAND completes Quest 53 (20/10 XP, 5 Zenni); dropping a worn item takes it off first (the ring goes through its removal roll). Bedroom nightstand sentence no longer names the glasses.
  Q and the ring walkthrough: Rowan hands the Middle Tier Key straight to inventory (TAKE KEY removed; NPC hand-over convention written into mechanics.md). Fragments: NORTH [Bedroom], LOOK [glows faintly], TAKE DRAGON-NIP [sprig], GIVE … [looking for that|golden dragon scale added].
- Sections TT–VV: TAKE BLADE in the Church of All (left there in EE); the ritual aligned with the ring walkthrough (dial LEFT each time, PUT RING ON ALTAR binds it).
  UU: OPEN CASE removed (the case is opened in O), the three repeat deposits removed (brooch, idol, watch — deposited in EE), LOOK IN CASE and SCORE check [9 treasures on display]; GIVE RING TO WILL checks "9 of 9 treasures on display".
  Trophy Case: score and count are worked out from the case contents (the running counters double-counted repeat deposits: SCORE showed 12 treasures and 405 points); a treasure already in the case is refused — "It's already in the case." (mechanics.md).
- Full-score section letters renumbered (mapping above); stale prose references fixed (clay pot: section Q; vial and lantern at the bridge since Y).
  Stale code comments fixed: full-score test seed note (35 Zenni at Will's first teaching in F), and "built with section …" notes in lower_tier, mid_tier, tunnels, upper_tier and verbs now point at where those exits and traps are wired.
- TODO #4: Z detours to Deep Lock Door, AA opens with The Encampment; still_den.py stale Dark Room note fixed.
- Shamus's stock is out of the world until bought — BUY X in the Kitchen. TAKE and TAKE ALL there used to take it for free, and the Kitchen listed it. Buying an item you already carry is refused ("You've already got one."), except the torch exchange. test_shamus_shop.py.
- Forgotten Shaft: the last sentence was a copy of the Assay Room's hidden-gap line; it now describes the west passage.
- Ship and shore connect only by LAND / DOCK and BOARD SHIP. Land, Ho! is the last sea square and the Empty Beach is the shore. Walking exits between islands and sea removed.
  Both walkthroughs: GO EAST [Land, Ho!] / LAND [Empty Beach], and one more GO WEST home. test_ship_shore.py.
- Mage class XP bonus: +1 XP the first time a Mage enters each of the 43 dungeon rooms (experience.md — Class XP Adjustments), paid lit or dark, once per room even if its visited state resets. A move refused by darkness pays nothing. Quests 19 & 30 hints stay on sale from game start (mechanics.md). test_mage_bonus.py.
- TAKE ALL / TAKE ALL BUT leave out what the player carries; nothing left: "There's nothing here you can take." (as in Zork). test_take_all.py.
- LISTEN defaults (plain, object, NPC — passive, never TALK TO); PULL / MOVE / PUSH defaults; the Redcrosse Knight takes "The". test_listen.py, test_pull_push_move.py.
- Magnetic Vault: after-the-trap room description (locations.md); the "faint ring" line no longer returns. test_magnetic_vault_desc.py.
- Floor listings: items reaching the player's hands any way are touched (no stale first-sight lines); plural / mass names ("There are lockpicks here.", "There is some charcoal here.").
  Torch: a burnt-out torch dropped leaves the game; BUY TORCH sells a fresh one (a lit one left elsewhere leaves its room); a torch away from the player burns down unseen. test_floor_listing.py.
- SEAL JOINTS WITH MORTAR / MIX CLAY WITH WATER with the tool missing give the designed lines (SyntaxRule.obj2_optional). test_optional_with.py.
- Design-doc lines over 400 chars split (experience.md Mage bonus, mechanics.md).
- GIVE / HAND / PAY Zenni to May (with her present) is a tip — same lines and tiers as TIP MAY; no amount: "How much?". test_may_hints.py (TestGiveZenniAsTip).
- Plain CAST lists known spells (Light, Unbind Undead, Fireball order) or "You don't know any spells."; no turn. test_cast_what.py.
- Ty's Cargo game (content/cargo.py): fair d6, Ty rolls first (keeps cargo dice 4–6, rerolls 1–3), player REROLL BOTH / REROLL n / STAND, ties push, Ty's bankroll grows with his winnings, cleaned out = table closed. mechanics.md and npcs.md updated (reroll one or both). test_cargo.py.
- actions.py deleted: the old play_cargo, altar_ritual, altar_pray, tick_cooldowns and the unused start_combat, with the five test_combat tests that only exercised start_combat. Suite baseline is now 11 old failures (test_combat 5, test_world 6).
- Town Charter: the Boggart hands it back after Quest 27; it stays with the player (items.md).
- Cargo: if Ty misses 6-5-4 and the player makes it, the player wins outright — no reroll choice (mechanics.md). test_cargo.py.
- Zenni total: INVENTORY ends with "You have N Zenni." (1 Zenni / no Zenni; empty-handed prints both lines); SCORE during play adds "Zenni: N" under the Level line (mechanics.md). test_zenni_display.py.
- Pie Rat Ship gangplank: EAST from the Docks is BOARD SHIP (it skipped every check before). Boarding needs the disguise and the explosion; the Pie Rat Coin always works; new "Crew's all aboard" refusal (locations.md — The gangplank; mechanics.md heist step 8). test_gangplank.py.
- OPEN MAILBOX no longer works in Will's Tower (the Tale and Ale mailbox was a Tower global too); locations.md Tower connections fixed. test_tower_mailbox.py.
- Zenni display decisions: no ZENNI / PURSE command; the end-of-game score leaves Zenni out (mechanics.md).
- Shamus's slate: Kitchen description line; READ / LOOK AT / EXAMINE SLATE and LIST / WARES / PRICES show his prices ("(sold)" once bought, torch always listed); TALK greeting points at it. Dagger, Mace, Battle Axe and Tip Journal on sale; untrained-buyer line. Buyback removed from the design (npcs.md, locations.md, mechanics.md). test_shamus_slate.py.
- Shared combat rules (content/combat.py): level dice + best usable weapon (or the one named) + gloves +3 while worn, in every fight; the tunic now covers the mugger too; werewolf bonuses only decide whether its claws land. Old resolve_round and its 8 tests removed. test_combat_rules.py.
- Finishing Move (Level 8) built: mugger, Warden, apprentice; not the knight or werewolf; 216-in-8000 draw so max test dice never fire it (mechanics.md).
- EQUIP / WIELD / UNEQUIP: one of the bow, Dagger, Mace or Battle Axe at a time; only the equipped one counts (KILL uses it, bare hands otherwise); KILL X WITH Y equips Y first; untrained / non-weapon / already-holding lines; REMOVE puts it away; parting with it unequips silently; INVENTORY shows (equipped) (mechanics.md — Equipping weapons). test_combat_rules.py.
- Bow attacks: SHOOT X (WITH BOW) and KILL X WITH BOW — SHOOT equips the bow; +5 only on a fight's opening round (reset on re-entering the room); gloves count, melee weapons don't; own hit / tie lines; werewolf arrow line (round still happens); knight's bow line, no turn; no-bow / not-a-bow / non-enemy lines (mechanics.md — Bow attacks; npcs.md). test_combat_rules.py.
- WEAR refuses anything not wearable ("You can't wear the X."); the Pie Rat disguise is now wearable.
- Ship-in-a-Bottle is a plain treasure: no quest, no May hint (locations.md — Pond; items.md; mechanics.md's stray "(Quest 12)" fixed).
- Dragon-nip check raised from Hard to Very Hard (18): a Level 3 Mage was finding it on ~56% of tries (locations.md, quests.md — Quest 58). test_sprig_check.py.
- Ring vs. the Dankhaus wards: the ring (not inked) slips an uninvited player past the ward; Litlock's unseen line replaces the Common Room description and he won't engage (TALK, menu choices);
  Taking the ring off inside (REMOVE or DROP) throws an uninvited player out to Bog-SE ("There you are" / faint line in the Common Room, ward line elsewhere); invited, the inciting moment waits for the ring to come off (npcs.md, locations.md). test_dankhaus_ring.py.
- The inn (content/tavern.py): BUY / ORDER / PURCHASE DRINK, FOOD or STEW at the Bar (1 heart; stew 2 after Quest 40; 2 Zenni, 1 after Quest 22); RENT / BUY ROOM (5 Zenni, full heal, random guest room with its wake-up text);
  full-hearts and "You're short." refusals; Guest Rooms 1–3 built (one-way out), taken out of the Zenni pool. test_inn.py.
- Inked: renting a room bathes off the ink, even at full hearts; it's the only thing May does for an inked player (food, drink, TALK, tips refused; hand-overs and the free drink wait). Will engages with disdain rather than refusing (traps.md). test_inn.py.
- Inked player (content/ink.py): Shamus, Raznak, the Knight, the Records Room Worker and the Librarian refuse with their own lines; the active quest givers (Archivist, oak child, beekeeper, Ivanaar, Haalvar, Aylora, Pyronicus, Rowan Finch, Lynds) share one;
  TALK / GIVE (item kept) / BUY / PAY / CHALLENGE / FIGHT / SHOOT / riddle answers / Aylora's DRINK refused, no Zenni taken, a turn used; reading the slate still works. Arrival greetings (Ivanaar, Haalvar's riddle, the beekeeper) wait until clean.
  Will: TALK gets his disdainful line every time; the first GIVE / teaching gets it once, then goes ahead. Litlock turns an inked player away at the door, invited or not (npcs.md, traps.md). test_ink.py.
- Opening pacing: two stops only — after "Then we begin" and after the ring briefing — each showing "[Press ENTER to continue]"; no silent waits; the rest flows into the first > prompt (npcs.md — Will Passion, Pauses). test_opening.py.
- SHOW dropped from the design: GIVE DRAGON-NIP TO WILL is the only way (quests.md — Quest 58).
- The ring's description is minimal by design — "plain dark ring" / "A plain dark ring.", no hint of what it is; only the corruption milestones reveal it (items.md).
- The ring can't be dropped (content/ring.py): DROP / THROW / PUT anywhere but the altar get "Bring it to me, or keep it close," Will said. You keep it close.; worn, no removal attempt; DROP ALL skips it (KEEPBIT); weight 0 (items.md, mechanics.md). test_ring_keep.py.
- DROP ALL with nothing to drop: "You are empty-handed." / "You'll need to remove anything you want to drop." (only worn items) / the ring's line (only the ring) (mechanics.md). test_ring_keep.py.
- Quest 50: Will is shaken on the first tower arrival afterwards — once, before the room description: "Thank you," he says, to the glass. Fires even if inked (npcs.md — Will Passion). test_will_shaken.py.
- test_world.py trimmed to 7 tests (engine object/flag basics, starting state): the stale name lookups and arbitrary count thresholds from the original baseline removed — the walkthroughs cover them. The player now starts inside the White House (it had no location until the opening). Suite baseline: 0 failures.
- Thin paper: the Flooding Room sweep (Trap 41) is the one thing that soaks the player — carried paper is destroyed ("The thin paper didn't survive the trip. …") and is back on Shamus's slate; the rubbing, scrolls and other paper survive (items.md, traps.md). test_thin_paper.py.
- DROP ALL BUT that keeps back everything droppable: "That leaves nothing to drop." (it was silent); the ring's line and the worn-items line still come first (mechanics.md — Several objects). test_ring_keep.py.
- The Archivist: Quest 28 (the rubbing) is his only role — the book-research mechanic was dropped in favor of it (locations.md — The Stacks, npcs.md).
- Quest 34's soldier doesn't return to town — weapon training belongs to the Redcrosse Knight (Quest 54); the town return and its unreachable ambient line removed (npcs.md, quests.md, locations.md).
- Tip Journal: READ / EXAMINE JOURNAL lists each discovered, unfinished quest by name in discovery order with [Board] / [May] / [Organic] and the hints bought from May (the Hollow Statue hint shows under the Undead Warden too); "You don't have a journal." / "The journal is empty."; weight 0 (mechanics.md — Tip Journal, items.md). content/journal.py, test_journal.py.
- XP vs the level curve checked (Warrior walkthroughs fit). experience.md totals corrected: quest XP by class (each class does two of Quests 54–56; Quest 56 is 4 XP × three spells), Warrior bonus 3 kills = +30, summary per class (550–560 / 559–569 / 572–582).

**Known issues still open:**
- None.

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
## TODO #4 — Full-score walkthrough must visit every room — RESOLVED 2026-10-04

The full-score walkthrough enters every room worth XP: The Encampment (lower tier) and Deep Lock Door were the last two, added to AA and Z. test_walkthrough_fullscore_v2.py now fails if a room worth XP is never entered, and if the room XP paid differs from experience.md's exploration total.

Exploration total reconciled at 167 (experience.md, locations.md and the engine agree). The old 173 counted the Kevry's Island and Sea group headings as rooms; experience.md's 131 was stale. The White House went to 0 XP: the game starts there and never returns, so it could never be paid.

Mage bonus count checked: 43 reachable dungeon rooms, not 47 (experience.md corrected; tier headers in locations.md corrected to 15 / 14 / 15). The class-bonus total range was also corrected to 568–588.

---
## TODO #5 — Build TIP MAY (hint system) — RESOLVED 2026-10-04

Built in content/may_hints.py, tested in test_may_hints.py (21 tests). Rules in mechanics.md (Hint System): the tip amount sets the tier paid for; May picks a random hint at that tier, stepping down a tier at a time; her response follows the amount tipped.

Per-quest decisions in quests.md (4, 17, 19&30, 32, 34, 49). May has no Kevry pond hint (npcs.md). The old hint table and the old quest completions in actions.py are gone.

---
## TODO #6 — Build and test the Quest Board and May's tips — RESOLVED 2026-10-04

Both built and tested: the Quest Board (below) and May's tips (TODO #5).

No ring-path step needs them, and no walkthrough step checks a hint, so they need their own code and their own tests. (The full-score walkthrough now reads the board twice — see below.)

- **Quest Board** (Bar — `LOOK AT BOARD` / `READ BOARD`): postings from the design — quests posted at game start, on first visits (e.g. Quest 40 on meeting Shamus) and by cascade (quests.md, mechanics.md — Quest Board), removals (e.g. Quest 50 when Trap 41 is disarmed), the Quest 51 bounty after 100 turns, and how completed quests show.
- **May's tips:** build per TODO #5 (TIP MAY tiers, blind tipping, conditional hints, hints unlocking on discovery).
- **Tests:** a dedicated test file (not a walkthrough) that drives game state through do_turn where it can — discover, progress and complete quests — and checks the board text and each tier of May's hints, including conditional and one-tier hints.

Organic quest discovery wired 2026-10-04 (19&30, 34, 41, 42, 51, 53, 58, 59); Quests 19&30 now complete at the werewolf. test_quest_discovery.py checks every quest is discovered before it's completed over the full-score run.

Quest Board built 2026-10-04 (content/quest_board.py, test_quest_board.py — 15 tests).
- Rules and all board text are in mechanics.md (Quest Board). Reading the board discovers what it shows; postings alone don't.
- The full-score walkthrough reads the board in O and U, so the board quests (7, 17, 22, 50) are discovered before they're completed. test_quest_discovery.py has no exemptions now.
- May's tips: built under TODO #5.

