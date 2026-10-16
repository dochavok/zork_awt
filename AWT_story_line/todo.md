# Roundabout: The God-Forsaken Ring — Open Design Questions

Consolidated from all source files. Update this file when items are resolved; record the resolution and the source file where it was written.
Resolved items are removed; their history is in git (last full lists: commit 7eec353 for TODO #1–#6, b9e5feb for #7–#8, fecb0f2 for #9, cfd1724 for #13, 4a4e63c for #12, 337bf02 for #11, 6bbb3e5 for #16, 8084dfa for #14, 6cb6920 for #15, 9130035 for #20, 26df3b1 for #23, 536aab4 for #21, cb0b094 for #22, 213bcd6 for #17, c1c8b5e for #24, 89de697 for #18, eb9fbc5 for #19, 76430e1 for #26–#28).

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

### TODO #29 — The ink (found 2026-10-15)

From the v2.7 playtest. After the Ink Corridor, the ink isn't mentioned again until the councilman refuses the player.
- No `wash` verb (also tried: `clean ink`, `bathe`, `rinse`, `wash in fountain`).
- `x me` doesn't show the ink, and says "You see nothing special about the Sable."
- May's "Rooms are upstairs" sends the player to the door, which sends them back to the bartender; it works, but goes round in a circle.

### TODO #30 — Early traps and fight feedback (found 2026-10-15)

From the v2.7 playtest.
- At level 4 the Shatter Trap, Ink Corridor and Supply Room each took a heart with no roll shown and no chance to react (7 → 4 hearts). The tester wanted a visible attempt that can fail, or a warning.
- The portcullis disarm line is garbled: "You spot an arcane charge running through the portcullis, the discharge mechanism set into the wall beside it and are able to disarm it, neutralizing it."
- Swarm Tree hits are silent ("You retreat"); only the last-heart warning speaks.
- No progress feedback: the Warden ("…comes on anyway" every hit), Lynds ("Not bad").
- Unbind Undead on the Warden: "Nothing here answers the spell."

### TODO #31 — The ring, round 2 (found 2026-10-15)

From the v2.7 playtest ("Does the ring now feel fair? Mostly, yes").
- A clean removal at 41–49 still prints "Whatever it wants, it didn't get it this time" (mechanics.md — Clean success), which reassures; the near-miss line at 47 was the honest one.
- The tick-10 warning ("You hadn't noticed until just now") read as too soft to be a budget, without the next wearing's "remembers" line.
- The Ghost's Room exit fails half the time with or without the ring (by design, mechanics.md), and the tester spent 4 ticks on it. Its room text ("Your reflections are wrong by a fraction") contradicts `x mirrors` after the ghost is freed ("keeping time properly").

### TODO #32 — Small text fixes (found 2026-10-15)

From the v2.7 playtest.
- Flooding Room: "In a few heartbeats it's above your knees", then knee-deep "still pouring" forever.
- The two middle bog rooms (log room, grey-stone room) name no exits; the one above the apprentice's tunnel doesn't mention the tunnel after climbing out. The Upstairs Hall names only the stairs.
- The Bone Passage still describes the black oak door as shut after it's opened from the cellar side.
- The gravestone says "You tip up one edge far enough to read it" after it stands in the graveyard.
- The Bar description says "She works the bar…" before May is introduced.
- The heart necklace gives no message about the extra heart.
- ~~`x man` in the Council Chamber: "You see nothing special about the Councilman Rowan Finch."~~ Fixed 2026-10-15 (mechanics.md — Object descriptions). Still open: the name also matches a common player name.
- The mugger ambushes on entry and isn't seen again; nothing says where he went.
- The Volcano still says "There is no way in that you can see" next to the staircase line once it's found (from TODO #26).
- Rowan's "It's been empty for years" ignores treasures already in the Trophy Case (from TODO #26).
- Em-dashes print as "�" in the console (the VERSION line too).
