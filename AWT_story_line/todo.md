# Roundabout: The God-Forsaken Ring — Open Design Questions

Consolidated from all source files. Update this file when items are resolved; record the resolution and the source file where it was written.
Resolved items are removed; their history is in git (last full lists: commit 7eec353 for TODO #1–#6, b9e5feb for #7–#8, fecb0f2 for #9, cfd1724 for #13, 4a4e63c for #12).

**Policy:** When a new walkthrough test fails, fix the engine. Never adjust the narrative or add state injection to make a test pass. Only fix the walkthrough when the design doc confirms the walkthrough is wrong.

---

### TODO #11 — Pathing issues (found 2026-10-12) — RESOLVED 2026-10-12

1. Up through the mine after the explosion.
2. Aqueduct corridor clearing through the Portcullis room.

**Resolution:**
1. After the cave-in, `UP` from the Main Shaft was still open, so a player who came in by the Hidden Secondary Entrance could walk out through the collapse. It is now blocked: *The way up is buried under the collapse.* The way out is back through the Hidden Secondary Entrance (content/mine.py; locations.md — Mine Entrance, Main Shaft).
2. Only the portcullis's south exit checked it, so coming up from the Shrine Room by the Quest 38 shortcut walked straight north through it. You are now on the side you came in from, and until it's propped only the way back is open. Propped from the south: *…The way north is open.* The side is saved; a save from before this has none and counts as north (content/shrine_path.py; locations.md — Portcullis Corridor, Either side; traps.md — Trap 19).
Tests: test_pathing.py.

---

### TODO #10 — Pre-release antivirus steps in operations.md (found 2026-10-12)

A player using ESET couldn't open the v2.5 .exe (permission error, most likely quarantine). The .exe was uploaded to VirusTotal afterwards; waiting to hear whether their next download gets through. Once known, add to operations.md (Antivirus false positives) whichever steps actually helped: e.g. uploading each new build to VirusTotal before announcing it, and submitting false positives to the engines that flag it (ESET: in-product Tools → Submit sample for analysis, or samples@eset.com).
