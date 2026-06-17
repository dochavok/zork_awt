# Roundabout: The God-Forsaken Ring — Open Design Questions

Consolidated from all source files. Update this file when items are resolved; record the resolution and the source file where it was written.

---

## TODO #1 — Narrative-Driven Test Rewrite

**Status:** In progress — Sections A, B, C passing in `test_walkthrough_ring_v2.py`

**Goal:** Full ring quest walkthrough passing with zero state injection.

**Current position:** Section D — Ring Retrieval / Pyronicus's Forge. First failure:

```
SECTION [D) Ring Retrieval — Pyronicus's Forge]
  cmd     : 'WEST'
  missing : 'Beach Road'
  got     : "You can't go that way.\n"
```

Player lands at Roundabout Beach after DOCK. Needs: Roundabout Wasteland → Beach Road westward exit (already exists), then SOUTH to Volcano, DOWN to Pyronicus's Forge. Rooms and NPC not yet implemented.

**Completed:**
- Steps 1–4 from original plan done (walkthroughs written, test files created, old tests deleted)
- Sections A, B, C passing (White House opening, tower bedroom, full Kevry's island sailing arc)
- Engine additions: V-WEAR, V-TALK, V-BUY, V-BOARD-SHIP, V-SAIL, V-DOCK, V-LIGHT, V-DROP, nautical GO EAST/WEST/LAND preaction, cave-in trigger, Shamus/Kevry NPCs, all overworld/mine/sea rooms

**Next session — implement Section D rooms and verbs:**
- Rooms needed: Volcano (perception-gated DOWN exit), Pyronicus's Forge
- NPC: Pyronicus (TALK TO → ring handover dialogue, Pale Blade forging)
- Verb: possibly V-GIVE (ring to Pyronicus) or handle via V-TALK

**Policy:** When a new walkthrough test fails, fix the engine. Never adjust the narrative or add state injection to make a test pass. Only fix the walkthrough when the design doc confirms the walkthrough is wrong.

---
