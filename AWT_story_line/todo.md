# Roundabout: The God-Forsaken Ring — Open Design Questions

Consolidated from all source files. Update this file when items are resolved; record the resolution and the source file where it was written.

---

## TODO #1 — Walkthrough / Design Doc Alignment

**Status:** In progress

**Goal:** Ensure both walkthrough files (`walkthrough_ring.txt`, `walkthrough_fullscore.txt`) match the design docs exactly before any test code is written.

**Process:**
1. Go through each walkthrough section by section.
2. For each section, confirm every direction and command matches the design docs.
3. If something doesn't match, ask ONE specific clarifying question before changing anything.
4. Update the design doc first, then update both walkthroughs.
5. No code changes except where descriptions in code directly contradict established cardinals (as an explicit exception).

**Current position:** Section H of `walkthrough_ring.txt` — tunnel navigation fixed, Town Hall / Records Room navigation next.

**Remaining sections:** H (Town Hall), I through U of `walkthrough_ring.txt`, all sections of `walkthrough_fullscore.txt` (unreviewed as a standalone pass).

---

## TODO #2 — Narrative-Driven Test Rewrite

**Status:** Not started — see implementation plan at `C:\Users\docha\.claude\plans\we-ve-completed-requirements-for-effervescent-rainbow.md`

**Problem:** The current walkthroughs (`test_walkthrough_ring.py`, `test_walkthrough_fullscore.py`) are not real integration tests. They bypass the engine with direct state injection (`set_room()`, `give_item()`, `w.globals[...] = ...`) and contain `or True` guards that make assertions impossible to fail. The tests prove nothing about whether the game actually works.

**Work required (in order):**

1. **Generate two narrative walkthroughs** derived solely from the design documents (`locations.md`, `quests.md`, `npcs.md`, `items.md`, `ring-rituals.md`). Each narrative must be written before any test code is touched.

   **Format:** Lettered sections matching the Zork walkthrough_text_narrative.txt style. Each section corresponds to one quest, one NPC arc, or one design-doc requirement (not a gameplay convenience grouping). Within each section, executable lines are marked explicitly so the test runner can extract them without parsing prose:

   ```
   A) Opening — Will's Briefing
   ----------------------------
   The game starts west of the white house. Open the mailbox to trigger
   character creation. Select Warrior and enter your name.

   > OPEN MAILBOX           [mailbox opens]
   > (select: warrior)      [You have chosen: Warrior]
   > (enter name: Tester)   [Welcome, Tester]
   > EXAMINE PAINTING       [Tale and Ale]
   ```

   The `>` prefix marks a command. The bracketed text is the required output fragment (case-insensitive substring match). Prose between commands is annotation only — ignored by the test runner. Sections map one-to-one with design requirements so a failing section identifies exactly which requirement is broken.

   Walkthroughs to generate:
   - **Minimal ring quest** — fewest commands to reach the binding ritual and Will's "Well done"
   - **Full score** — all major quests, covering every quest group

2. **Create new test files** that execute the narratives literally. Rules:
   - `do_turn(command)` only — no `set_room()`, no `give_item()`, no direct `w.globals` writes
   - Each `do_turn` checks that the expected output fragment appears in stdout
   - No `or True` fallbacks anywhere
   - If a command produces wrong output, the engine is wrong — fix the engine, not the test

3. **Fix engine/verb gaps** that are exposed by running the narrative. Known gaps likely to surface:
   - `"talk to <npc>"` parser routing (obj2 vs obj1 issue)
   - Opening sequence must fire via `OPEN MAILBOX`, not direct `run_opening()` call
   - `EXAMINE PAINTING` must trigger the tavern transition
   - Verb handlers for quest-critical commands (DRIVE STAKE, MAKE RUBBING, CLEAR DRAIN, etc.)

4. **Delete the old walkthrough tests** once the new ones pass.

**Policy:** When a new walkthrough test fails, fix the engine. Never adjust the narrative or add state injection to make a test pass.

---

