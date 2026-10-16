# Roundabout: The God-Forsaken Ring — Open Design Questions

Consolidated from all source files. Update this file when items are resolved; record the resolution and the source file where it was written.
Resolved items are removed; their history is in git (last full lists: commit 7eec353 for TODO #1–#6, b9e5feb for #7–#8, fecb0f2 for #9, cfd1724 for #13, 4a4e63c for #12, 337bf02 for #11, 6bbb3e5 for #16, 8084dfa for #14, 6cb6920 for #15, 9130035 for #20, 26df3b1 for #23, 536aab4 for #21, cb0b094 for #22, 213bcd6 for #17, c1c8b5e for #24, 89de697 for #18, eb9fbc5 for #19, 76430e1 for #26–#28, 66bfb6e for #29–#30).

**Policy:** When a new walkthrough test fails, fix the engine. Never adjust the narrative or add state injection to make a test pass. Only fix the walkthrough when the design doc confirms the walkthrough is wrong.

---

### TODO #10 — Pre-release antivirus steps in operations.md (found 2026-10-12)

A player using ESET couldn't open the v2.5 .exe (permission error, most likely quarantine).
The .exe was uploaded to VirusTotal afterwards; waiting to hear whether their next download gets through.
Once known, add to operations.md (Antivirus false positives) whichever steps actually helped: e.g. uploading each new build to VirusTotal before announcing it, and submitting false positives to the engines that flag it (ESET: in-product Tools → Submit sample for analysis, or samples@eset.com).

### TODO #25 — A raw traceback when input ends at a prompt (found 2026-10-15)

From the 2026-10 playtest (feedback "Crash with a Python traceback when input ends at a prompt"); seen again while checking the v2.7 build.
When input runs out at a prompt, `input()` raises `EOFError` and the .exe prints a Python traceback and `[PYI-…:ERROR] Failed to execute script 'main'`. Seen at the class question (`content/char_create.py` `_prompt_class`, reached via `run_opening`). The same can likely happen at the name question, a yes/no, and `[Press ENTER to continue]` (`content.char_create._pause`).
- Only piped input reaches it (the playtester's runs; a closed console), not a player typing. It clutters playtest transcripts, and a traceback is never the right ending.
- Likely fix: treat end of input as quitting. Catch `EOFError` (and `KeyboardInterrupt`?) once, around the main loop in `main.py` / `engine/game.py`, so every prompt is covered, and exit quietly without saving.
- To decide: whether a short closing line prints (it would need writing and review), and whether Ctrl+C at the keyboard should behave the same.
- **Also (moved from TODO #32):** em-dashes print as "�" in piped output (the playtest transcripts; the VERSION line too). Piped, Python writes the Windows code page, not UTF-8; a console shows them correctly. Likely fix: always write UTF-8.
**Resolved 2026-10-15** (mechanics.md — The end of the game): main.py catches end of input and Ctrl+C around the game, so every prompt ends quietly as `>` does — a blank line, no save, no closing text. Output is always UTF-8. Untested in the .exe until the next build.

### TODO #31 — The ring, round 2 (found 2026-10-15)

From the v2.7 playtest ("Does the ring now feel fair? Mostly, yes"). Done 2026-10-15:
- A clean removal at 41–49 prints "Whatever it wants, it didn't get it this time". **Kept** — "this time" says it will try again.
- The tick-10 warning read as soft. **Kept** — the next wearing's "remembers" line makes it a budget.
- The Ghost's Room exit failing half the time: **kept** (mechanics.md); four in a row was bad luck. ~~Its room text contradicts `x mirrors`~~ — the reflections sentence follows the mirrors' state (locations.md — Ghost's Room).

### TODO #32 — Small text fixes (found 2026-10-15)

From the v2.7 playtest. Done 2026-10-15:
- ~~Flooding Room: "above your knees", then knee-deep "still pouring" forever~~ — "up to your knees"; *The level holds there, for now.* (locations.md — Flooding Room).
- ~~The Bone Passage describes the black oak door as shut once open~~ — its own line (locations.md — The Bone Passage).
- ~~The gravestone says "tip up one edge" standing in the graveyard~~ — the Graveyard's line (items.md — Gravestone).
- ~~The heart necklace gives no message~~ — wear and remove lines (items.md — Heart Necklace).
- ~~`x man`: "the Councilman Rowan Finch"~~ (mechanics.md — Object descriptions). ~~The Volcano's "no way in" once the stairs are found~~ (locations.md — The Volcano).
- **Kept, by design:** the bog interior names no exits (mechanics.md — navigation is the puzzle); no hole on the bog side of the apprentice's tunnel (locations.md); the Upstairs Hall has only the stairs; the Bar's "She" is the bartender, before May's introduction (locations.md); the mugger hides behind a repeating perception check, with the bounty after 100 turns; Rowan's name.
- Em-dashes printing as "�": moved to TODO #25 (piped output only).
