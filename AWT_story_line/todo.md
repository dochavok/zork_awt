# Roundabout: The God-Forsaken Ring — Open Design Questions

Consolidated from all source files. Update this file when items are resolved; record the resolution and the source file where it was written.

---

## Narrative-Driven Test Rewrite

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

## Weapons System

**Status:** Design complete — implementation in progress

Three weapons sold by Shamus: Dagger (+2, 5Z), Mace (+4, 25Z), Battle Axe (+6, 100Z). Flat roll bonus model. Auto-select best usable weapon on bare `KILL X`. Weapon Use skill required (Warriors always; Mages/Rogues after Quest 54). Knight delivers Shamus referral after Quest 54 training. Design recorded in `mechanics.md`, `items.md`, `quests.md`.

**Work required (in order):**

1. ~~**Design:** Decide how weapons work mechanically.~~ **Done.**

2. ~~**Update design docs:** Record the decisions in `mechanics.md`, `items.md`, `quests.md`.~~ **Done.**

3. **Update `objects.py`:** Add dagger, mace, battle-axe objects with TAKEBIT/WEAPONBIT flags, starting location in Shamus's kitchen, and weapon bonus metadata.

4. **Update `char_create.py`:** Warriors no longer start with a sword — remove the `world.objects.get("sword")` call. No starting weapon for any class (warriors buy from Shamus).

5. **Update `verbs.py` / `combat.py`:** Wire weapon bonuses into the combat roll. Auto-select best usable weapon on bare `KILL X`. Skill gate for Mages/Rogues without Weapon Use.

6. **Update tests:** Add weapon-specific combat tests to `test_combat.py`.

