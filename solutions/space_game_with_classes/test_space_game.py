import io
import pytest

from space_game import travel


# the actual solution to the game
SOLUTION = [
    "2",
    "2",  # go to sirius and win quiz
    "1",
    "42",  # hire copilot on orion
    "1",
    "yes",  # go to centauri and buy GPU drive
    "2",
    "2",
    "3",
    "yes",  # jump into black hole
]

DEATH_BY_BLACK_HOLE = [
    "2",
    "2",  # go to sirius and win quiz
    "1",
    "41",  # hire copilot on orion
    "1",
    "yes",  # go to centauri and buy GPU drive
    "1",
    "2",
    "3",
    "yes",  # jump into black hole
]

# text sniplets that should appear literally in the output
PHRASES = [
    "The stars are waiting for you",
    "Betelgeuse",
    "credits",
    "tech-savvy native",
    "copilot",
    "buy",
    "life, the universe and everything",
    "Black Hole",
    "stupid idea",
    "wonders beyond description",
    "THE END",
]


@pytest.fixture
def solution_input():
    """helper function to hijack the keyboard for testing"""
    return io.StringIO("\n".join(SOLUTION))


def test_travel(monkeypatch, solution_input):
    """game finishes"""
    monkeypatch.setattr("sys.stdin", solution_input)
    travel()


def test_output(monkeypatch, capsys, solution_input):
    """text output is not empty"""
    monkeypatch.setattr("sys.stdin", solution_input)

    travel()

    captured = capsys.readouterr()
    assert len(captured.out) > 0


def test_die(monkeypatch, capsys):
    """player dies"""
    monkeypatch.setattr("sys.stdin", io.StringIO("\n".join(DEATH_BY_BLACK_HOLE)))

    travel()

    captured = capsys.readouterr()
    assert "grain of dust" in captured.out
    assert " wonders beyond description" not in captured.out


@pytest.mark.parametrize("phrase", PHRASES)
def test_output_phrases(monkeypatch, capsys, solution_input, phrase):
    """check for some key phrases in the output"""
    monkeypatch.setattr("sys.stdin", solution_input)

    travel()

    captured = capsys.readouterr()
    assert phrase in captured.out
