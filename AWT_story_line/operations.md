# Operations — Building and Releasing the .exe

How `Roundabout.exe` is built, checked and published. Not game design. This file holds the procedure, so it doesn't live only in someone's memory.

## What you need

- Python, run as `py` (not `python`).
- PyInstaller: `py -m pip install pyinstaller` (6.22 was used for v2.2 onward).
- A git checkout of this repo. The build reads the version from git.
- For publishing: the GitHub CLI (`gh`), signed in to the `dochavok/zork_awt` repo.

## Building

1. **Commit first.** The .exe's version comes from git. A build with uncommitted changes is marked `-dirty`, and the build script warns about it.
2. **Tag, if this is a release.** Tags are `vX.Y-roundabout` (e.g. `v2.2-roundabout`). An untagged build is fine for testing; its version shows how far past the last tag it is (below).
3. **Run the build script** from the repo root, pointing it at an output folder in the Claude scratch area:

   ```
   py roundabout/build_exe.py C:\Users\docha\AppData\Local\Temp\claude\c--zork-awt\<session>\scratchpad\release-X.Y
   ```

   The finished file is `<output folder>\dist\Roundabout.exe`. PyInstaller's working files go in `build\` and `work\` beside it.

What the script does (`roundabout/build_exe.py`):
- Reads the version with `git describe --tags --dirty --always`.
- Writes it into `roundabout/content/_version.py`. That file is in `.gitignore` and is never committed.
- Runs PyInstaller: one file, console window, named `Roundabout`, built from `roundabout/main.py`.
- Deletes `_version.py` again, so the source tree is left as it was.

## Checking the build

Copy the .exe into its own empty folder (e.g. `<output folder>\play\`) and run it there. Saved games are written next to the .exe, so don't run it from `dist\`.

- Type `VERSION`. It works even at West of House, before the mailbox. It should print:
  *Roundabout: The God-Forsaken Ring — v2.2-roundabout*
- Play a few commands, then `SAVE`, `QUIT`, relaunch, make the same character and `RESTORE`.

**Reading the version:**

| Shows | Means |
|---|---|
| `v2.2-roundabout` | Built exactly on the tag |
| `v2.2-roundabout-2-g516dfc1` | 2 commits past the tag, at commit `516dfc1` |
| `…-dirty` | Built with uncommitted changes. Don't release it. |
| `unknown version` | Run from source without git. Never seen in a built .exe. |

Run from source (`py roundabout/main.py`), VERSION asks git directly, so it always matches the checkout.

## Publishing a release

1. Push the commits and the tag: `git push` then `git push origin vX.Y-roundabout`.
2. Create the release with the .exe attached:

   ```
   gh release create vX.Y-roundabout "<output folder>\dist\Roundabout.exe" --title "Roundabout: The God-Forsaken Ring — vX.Y" --notes-file notes.md
   ```

3. Release notes. The player-facing part used since v2.2:

   > **Roundabout: The God-Forsaken Ring — vX.Y**
   >
   > A text adventure. Download `Roundabout.exe` and double-click it; nothing else to install.
   >
   > Windows may say "Windows protected your PC" because the file isn't signed. Click **More info → Run anyway**.
   >
   > Put the .exe in its own folder: your saved games are written next to it. `SAVE` saves your game. To continue another time, start the game, create a character with the same name, then type `RESTORE`.

To replace the .exe on an existing release (same tag), use `gh release upload vX.Y-roundabout "<path>\Roundabout.exe" --clobber`. Only do this if the tag hasn't moved. Otherwise VERSION in the new .exe won't match the release name.
