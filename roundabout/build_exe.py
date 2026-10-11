"""
Build Roundabout.exe (AWT_story_line/operations.md — Building the .exe).

    py roundabout/build_exe.py <output folder>

Stamps the git version into content/_version.py (so VERSION in the .exe names
the tag it was built from), runs PyInstaller (one file, console), then removes
the stamp so the source tree is left as it was. The .exe lands in
<output folder>/dist/Roundabout.exe.
"""

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
STAMP = os.path.join(HERE, "content", "_version.py")


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    out = os.path.abspath(sys.argv[1])
    sys.path.insert(0, HERE)
    from content.version import git_version
    version = git_version()
    if version is None:
        print("git describe failed — build from a git checkout.")
        return 1

    with open(STAMP, "w", encoding="utf-8") as fh:
        fh.write(f'"""Written by build_exe.py — not committed."""\nVERSION = {version!r}\n')
    try:
        result = subprocess.run([
            sys.executable, "-m", "PyInstaller", "--noconfirm", "--onefile", "--console",
            "--name", "Roundabout",
            "--distpath", os.path.join(out, "dist"),
            "--workpath", os.path.join(out, "build"),
            "--specpath", os.path.join(out, "work"),
            "--paths", HERE,
            "--hidden-import", "content._version",
            os.path.join(HERE, "main.py"),
        ])
    finally:
        os.remove(STAMP)
    if result.returncode != 0:
        return result.returncode
    print(f"\nBuilt {os.path.join(out, 'dist', 'Roundabout.exe')} — {version}")
    if version.endswith("-dirty"):
        print("Warning: built with uncommitted changes (the version says -dirty).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
