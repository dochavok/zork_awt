# Roundabout: The God-Forsaken Ring — Open Design Questions

Consolidated from all source files. Update this file when items are resolved; record the resolution and the source file where it was written.

---

## TODO #1 — Narrative-Driven Test Rewrite

**Status:** In progress — Sections A–M passing (C split into C1/C2; I split into I1/I2) in `test_walkthrough_ring_v2.py`

**Goal:** Full ring quest walkthrough passing with zero state injection.

**Current position:** Section N — Holy Water & Consecration. First failure:

```
SECTION [N) Werewolf's Amulet — Holy Water & Consecration]
  cmd     : 'SOUTH'
  missing : 'Church of All'
  got     : "Tale and Ale — Main Room …"
```

**Section N route:** N climbs out through the Crypt and the Graveyard (Charnel Walk → UP → UP → NORTH → NORTH), arriving in the Church of All — the three lines after that (NORTH Main East, WEST Town Square, SOUTH) are deleted. The Keeper's Chamber is WEST of the Nave (locations.md), not east. TAKE STAKE at the Rickety Bridge on the way north. The Keeper's Chamber isn't built yet.

**Torch budget:** the torch lights at the Mausoleum (H5) and ticks every turn, in town too. K swaps it at Shamus (`BUY TORCH` at 38 left, "Getting there"); the fresh torch lights at the Bone Passage in L, is at 79 at the Pile of Rubble and about 73 leaving the Lower Crypt.

N reaches the Church at about 50 and finishes the holy water at about 46. Swap after the holy water: Nave → Main East → Town Square → Tale and Ale → Bar → Kitchen, `BUY TORCH` at about 40 ("Getting there"), then O goes down through the cellar. The fresh torch covers O–S (~55 turns).

**XP note:** the player is level 6 by the end of K (Quest 32 reward). Not a problem for the ring path; worth checking against the level curve when TODO #4 is reconciled.

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

**Known issues still open:**
- Deferred from L: The Crevice and gold pocket watch (no room description yet — Stored Room east exit closed until built); Mine Passage south exit (Inscription Chamber and beyond); charcoal, silver dust, and the iron chest's lock (Mine Passage keeps its default description; the chest is scenery).
- Deferred from I1: Flooding Room (north of the Creature Den; Trap 41 — exit blocked until built); Trap 17 (Supply Room smoke-pot shelf — smoke jar, small clay pot; the room uses its default description until then), Trap 33 (idol — fixed in place until then).
- Inked state (Trap 45): flag built and cancels ring invisibility; NPC refusals and the inn bath still to build.
- Ring invisibility vs. the Dankhaus wards (npcs.md: invisible-entry lines) not built yet — comes with WEAR RING in H3.
- Class XP bonuses (experience.md — Class XP Adjustments): Warrior +10 per kill is built (Aylora excluded — not a kill). Mage +1 per new dungeon room and Rogue +5 per trap disarmed are not built yet — add when the dungeon and traps are.
- Full-score walkthrough does the mugger (its section C) before Kevry: a level-1 Warrior with regular glasses maxes at 8 perception < Medium 9, so the mugger is never spotted. Move it after the glasses enchantment or after level 2.
- Section P (aqueduct) needs cleanup: ends with NORTH [Dungeon Entrance] while already there; aqueduct repair rooms aren't defined in locations.md.
- Raznak only has State 1 (trust not earned). States 2A/2B/3 and PAY are Quest 55 (full-score walkthrough).
- Section T has `REMOVE RING [ring won't go on]`. items.md says that message belongs to `WEAR RING` on the bound ring. Check before implementing.
- The God-Forsaken Ring has no room/inventory description in items.md (code uses placeholder "A plain dark ring.").

**Policy:** When a new walkthrough test fails, fix the engine. Never adjust the narrative or add state injection to make a test pass. Only fix the walkthrough when the design doc confirms the walkthrough is wrong.

---
## TODO #2 - Fix chest in section D

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

- **Tale and Ale:** Pipe Room, Ty's Casino Corner, Upstairs Hall
- **Dankhaus:** Hearth Room, Garden, Litlock's Room, Litlock's Study, Lynds's Room, Aurix's Room, Hidden Secondary Entrance
- **Tunnels / dungeon:** The Undercroft, The Forgotten Shaft, Skeleton Room (Room 6), The Flooded Passage (Room 11)

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

