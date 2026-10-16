# Roundabout: The God-Forsaken Ring — Open Design Questions

Consolidated from all source files. Update this file when items are resolved; record the resolution and the source file where it was written.
Resolved items are removed; their history is in git (last full lists: commit 7eec353 for TODO #1–#6, b9e5feb for #7–#8, fecb0f2 for #9, cfd1724 for #13, 4a4e63c for #12, 337bf02 for #11, 6bbb3e5 for #16, 8084dfa for #14, 6cb6920 for #15, 9130035 for #20, 26df3b1 for #23, 536aab4 for #21, cb0b094 for #22, 213bcd6 for #17, c1c8b5e for #24, 89de697 for #18, eb9fbc5 for #19, 76430e1 for #26–#28, 66bfb6e for #29–#30, 02970a7 for #25, #31–#32).

**Policy:** When a new walkthrough test fails, fix the engine. Never adjust the narrative or add state injection to make a test pass. Only fix the walkthrough when the design doc confirms the walkthrough is wrong.

---

### TODO #10 — Pre-release antivirus steps in operations.md (found 2026-10-12)

A player using ESET couldn't open the v2.5 .exe (permission error, most likely quarantine).
The .exe was uploaded to VirusTotal afterwards; waiting to hear whether their next download gets through.
Once known, add to operations.md (Antivirus false positives) whichever steps actually helped: e.g. uploading each new build to VirusTotal before announcing it, and submitting false positives to the engines that flag it (ESET: in-product Tools → Submit sample for analysis, or samples@eset.com).
