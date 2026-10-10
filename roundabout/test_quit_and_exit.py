"""
QUIT and the end of the game (mechanics.md — Save and Restore: Quitting, and
The end of the game).

QUIT asks first; yes ends the game at once, anything else plays on. When the
game ends on its own (death, the ending, declining the adventure), the last
text stays up until the player presses ENTER, so a double-clicked console
window doesn't close over it.

The game loop (Game.run) is driven here with a scripted input(): each answer
the game asks for is taken in order, and an empty script means stdin closed.
What matters is what the player sees and when the game stops reading input.
Run with: pytest roundabout/test_quit_and_exit.py  (from c:\\zork_awt)
"""

import sys
import os
import io
import subprocess
from unittest.mock import patch
sys.path.insert(0, os.path.dirname(__file__))

from test_knight import _make_world
from test_cellar_gravestone import _door_open
from test_corruption import _ringed, GAME_OVER as CORRUPTION_GAME_OVER

QUIT_PROMPT = 'Quit now? (type "no" to save first) [yes/no] '
EXIT_PROMPT = "[Press ENTER to exit] "
_HERE = os.path.dirname(os.path.abspath(__file__))


class _Script:
    """Scripted input(): answers in order; records each prompt with the output
    printed before it was asked."""

    def __init__(self, lines, out):
        self.lines = list(lines)
        self.out = out
        self.asked = []                 # (prompt, output so far)

    def __call__(self, prompt=""):
        self.asked.append((prompt, self.out.getvalue()))
        self.out.write(prompt)
        if not self.lines:
            raise EOFError
        return self.lines.pop(0)

    @property
    def prompts(self):
        return [p for p, _ in self.asked]


def _run(g, lines, entry=None):
    """Play `lines` through the real game loop (or `entry`, e.g. main.main)."""
    out = io.StringIO()
    script = _Script(lines, out)
    with patch("builtins.input", script), patch("sys.stdout", out):
        (entry or g.run)()
    return script, out.getvalue()


def _town():
    return _make_world(cls="warrior")


# --- QUIT ----------------------------------------------------------------------

def test_quit_asks_and_yes_stops_reading_commands():
    w, g = _town()
    script, out = _run(g, ["quit", "yes", "inventory", "look"])
    assert QUIT_PROMPT in script.prompts
    assert script.lines == ["inventory", "look"]          # nothing after yes is played
    assert "empty-handed" not in out
    assert EXIT_PROMPT not in script.prompts               # quitting isn't a game end to read


def test_quit_answers_y_and_any_case():
    for answer in ("y", "YES", " Yes "):
        w, g = _town()
        script, _ = _run(g, ["quit", answer, "inventory"])
        assert script.lines == ["inventory"], answer


def test_q_is_quit():
    w, g = _town()
    script, _ = _run(g, ["q", "yes", "inventory"])
    assert QUIT_PROMPT in script.prompts
    assert script.lines == ["inventory"]


def test_quit_no_plays_on_so_the_player_can_save():
    w, g = _town()
    script, out = _run(g, ["quit", "no", "inventory"])
    assert script.lines == []
    after = out.split(QUIT_PROMPT, 1)[1]
    assert "empty-handed" in after                         # the next command was played
    assert not w.get_global("GAME-OVER")


def test_quit_no_then_save_writes_the_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    w, g = _town()
    script, out = _run(g, ["quit", "no", "save", "quit", "yes"])
    assert script.lines == []
    assert "Saved." in out
    assert (tmp_path / "Tess.sav").exists()
    assert script.prompts.count(QUIT_PROMPT) == 2


def test_any_other_answer_plays_on():
    for answer in ("n", "maybe", ""):
        w, g = _town()
        script, out = _run(g, ["quit", answer, "inventory"])
        assert script.lines == [], answer
        assert "empty-handed" in out.split(QUIT_PROMPT, 1)[1], answer


def test_quit_uses_no_turn():
    w, g = _town()
    moves = w.moves
    _run(g, ["quit", "no"])
    assert w.moves == moves


def test_stdin_closed_at_the_question_quits_quietly():
    w, g = _town()
    script, out = _run(g, ["quit"])                        # no answer: stdin closed
    assert script.prompts[-1] == QUIT_PROMPT
    assert "Traceback" not in out


def test_quit_works_at_west_of_house():
    from content.init import initialize_world
    from engine.world import World
    from engine.parser import Parser
    from engine.clock import Clock
    from engine.game import Game
    from content.vocabulary import make_vocabulary
    from content.syntax import make_syntax_rules
    w = World()
    g = Game(w, Parser(make_vocabulary(), make_syntax_rules()), Clock())
    initialize_world(w, g)
    assert w.here.name == "WHITE-HOUSE"
    script, out = _run(g, ["quit", "yes", "open mailbox"])
    assert QUIT_PROMPT in script.prompts
    assert "Great Underground Empire" not in out
    assert script.lines == ["open mailbox"]


def test_quit_works_while_ty_waits_for_a_choice():
    # mechanics.md — Ty's Casino Corner: SAVE / RESTORE / QUIT still work
    from test_cargo import _table, _play, _TY_9
    w, g = _table()
    _play(g, "bet 3", _TY_9 + [6, 5, 4, 2, 6])             # waiting on reroll or stand
    script, out = _run(g, ["quit", "yes", "stand"])
    assert QUIT_PROMPT in script.prompts
    assert "Ty waits" not in out
    assert script.lines == ["stand"]


# --- The end of the game -----------------------------------------------------

def test_drowning_waits_for_enter_before_closing():
    w, g = _door_open()                                    # cellar still flooded
    script, out = _run(g, ["down", "", "look"])
    prompt, shown = script.asked[-1]
    assert prompt == EXIT_PROMPT
    assert "*** GAME OVER ***" in shown                    # the death is on screen first
    assert script.lines == ["look"]                        # ENTER closes; nothing more played


def test_full_corruption_waits_for_enter_before_closing():
    w, g = _ringed(tick=48)
    script, out = _run(g, ["wait", "wait", "", "look"])
    prompt, shown = script.asked[-1]
    assert prompt == EXIT_PROMPT
    assert CORRUPTION_GAME_OVER in shown
    assert script.lines == ["look"]


def test_exit_pause_comes_once_after_everything_else():
    w, g = _door_open()
    script, out = _run(g, ["down", ""])
    assert script.prompts.count(EXIT_PROMPT) == 1
    assert out.rstrip().endswith(EXIT_PROMPT.rstrip())     # nothing printed after it


def test_stdin_closed_at_the_exit_pause_ends_quietly():
    w, g = _door_open()
    script, out = _run(g, ["down"])                        # no ENTER: stdin closed
    assert script.prompts[-1] == EXIT_PROMPT
    assert "Traceback" not in out


def test_playing_on_never_shows_the_exit_pause():
    w, g = _town()
    script, _ = _run(g, ["look", "inventory"])             # then stdin closes
    assert EXIT_PROMPT not in script.prompts


def test_declining_the_adventure_waits_for_enter():
    # locations.md — West of House: No = game over, never leaves the field
    import main
    script, out = _run(None, ["open mailbox", "no", ""], entry=main.main)
    prompt, shown = script.asked[-1]
    assert prompt == EXIT_PROMPT
    assert "Are you up for an adventure?" in "".join(script.prompts)
    assert script.lines == []


# --- The real program --------------------------------------------------------
# main.py run as its own process with typed input piped in, as the .exe is.

def _launch(stdin, tmp_path):
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    return subprocess.run(
        [sys.executable, os.path.join(_HERE, "main.py")],
        input=stdin, capture_output=True, text=True, encoding="utf-8",
        cwd=tmp_path, env=env, timeout=60,
    )


def test_program_quit_yes_exits(tmp_path):
    proc = _launch("quit\nyes\nopen mailbox\n", tmp_path)
    assert proc.returncode == 0, proc.stderr
    assert QUIT_PROMPT in proc.stdout
    assert "Are you up for an adventure?" not in proc.stdout   # exited before the mailbox
    assert proc.stderr == ""


def test_program_game_over_ends_on_the_exit_pause(tmp_path):
    proc = _launch("open mailbox\nno\n\n", tmp_path)
    assert proc.returncode == 0, proc.stderr
    assert proc.stdout.rstrip().endswith(EXIT_PROMPT.rstrip())
    assert proc.stderr == ""


def test_program_save_quit_relaunch_restore(tmp_path):
    opening = "open mailbox\nyes\n\nwarrior\nTess\n\n"
    proc = _launch(opening + "save\nquit\nno\nquit\nyes\n", tmp_path)
    assert proc.returncode == 0, proc.stderr
    assert (tmp_path / "Tess.sav").exists()
    proc = _launch(opening + "restore\nquit\nyes\n", tmp_path)
    assert proc.returncode == 0, proc.stderr
    assert "Restored." in proc.stdout
