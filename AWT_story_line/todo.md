# Roundabout: The God-Forsaken Ring — Open Design Questions

Consolidated from all source files. Update this file when items are resolved; record the resolution and the source file where it was written.

---

## TODO #1 — Narrative-Driven Test Rewrite

**Status:** In progress — Sections A–H3 passing (C split into C1/C2) in `test_walkthrough_ring_v2.py`

**Goal:** Full ring quest walkthrough passing with zero state injection.

**Current position:** Section H4 — Town Charter (Records Room Worker). First failure:

```
SECTION [H4) Town Charter — Records Room Worker]
  cmd     : 'NORTH'
  missing : 'Town Hall Exterior'
  got     : "You can't go that way."
```

Needs Town Hall Exterior, Records Room, the Records Room Worker and the watch → charter exchange (Quest 17 completes: 17 XP, 8 Zenni).

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
- Church Nave, Graveyard (pre/post bonk), Mausoleum, Chuckle House (mirrors, Trap 16, ghost, 50% exits), WEAR/REMOVE RING with corruption, CAST UNBIND UNDEAD; full corruption is GAME OVER
- Kevry per design (enchant on arrival if worn; WEAR in front of him if carried; quest-hint line without glasses)
- Dankhaus path (Medium perception), wards, 7 Dankhaus rooms, Litlock's tree as a numbered menu (Quest 52)
- Lynds (Quest 59): CHALLENGE / TALK TO, contested roll with tie reroll, 20-turn loss cooldown, Heart Necklace +1 heart while worn
- INVENTORY marks wearable items (not worn); TAKE prefers objects not already held
- The Alley, Back Alley, mugger (Medium perception, one combat round per KILL, losing isn't death), May's first visit and Quest 51 free drink
- Walkthrough cleanup: Q and R removed (bowl pieces in C1/E, fire clay in M), rope taken at end of C2

**Known issues still open:**
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

