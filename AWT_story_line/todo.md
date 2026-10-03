# Roundabout: The God-Forsaken Ring — Open Design Questions

Consolidated from all source files. Update this file when items are resolved; record the resolution and the source file where it was written.

---

## TODO #1 — Narrative-Driven Test Rewrite

**Status:** In progress — Sections A–F passing in `test_walkthrough_ring_v2.py`

**Goal:** Full ring quest walkthrough passing with zero state injection.

**Current position:** Section G — Werewolf's Amulet / Silver Stake from Town Square Statue. First failure:

```
SECTION [G) Werewolf's Amulet — Silver Stake from Town Square Statue]
  cmd     : 'LOOK AT STATUE'
  missing : 'seam'
  got     : "You can't see any statue here!"
```

**Completed:**
- Steps 1–4 from original plan done (walkthroughs written, test files created, old tests deleted)
- Sections A–F passing (opening, tower bedroom, Kevry's island, ring retrieval + Will's second briefing, Viking trust trials, Pale Blade forging)
- Engine additions: V-WEAR, V-REMOVE, V-TALK, V-GIVE, V-PUT-ON, V-ACTIVATE, V-DRINK, V-BUY, V-BOARD-SHIP, V-SAIL, V-DOCK, V-LIGHT, V-DROP, nautical walk preaction, cave-in trigger, raw-input hook (riddle answers); NPCs Shamus, Kevry, Pyronicus, Will, Raznak, Ivanaar, Haalvar, child, Aylora; rooms through the Viking Encampment
- Parser: FIND flags are preferences (try each structurally matching rule in order, fall back to the first with FIND ignored); particle retry; preposition-before-object rules (`LOOK AT X`)
- Opening rewritten to match npcs.md

**Known issues still open:**
- Viking trials are not enforced in order (design says Riddle → Circle → Fire Pit). Needs refusal text for out-of-order attempts.
- Raznak only has State 1 (trust not earned). States 2A/2B/3 and PAY are Quest 55 (full-score walkthrough).
- No INVENTORY verb yet.
- Section T has `REMOVE RING [ring won't go on]`. items.md says that message belongs to `WEAR RING` on the bound ring. Check before implementing.
- Glasses instant-fail in Will's presence is not implemented. Walkthroughs remove glasses before talking to Will and put them back on after leaving through the painting.
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

