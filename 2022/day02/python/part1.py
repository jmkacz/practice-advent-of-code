"""TODO"""
from enum import Enum
from typing import List, Tuple


class Play(Enum):
    """TODO"""

    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcome(Enum):
    """TODO"""

    LOSE = 0
    DRAW = 3
    WIN = 6


PLAY_LOOKUP = {
    "A": Play.ROCK,
    "B": Play.PAPER,
    "C": Play.SCISSORS,
    "X": Play.ROCK,
    "Y": Play.PAPER,
    "Z": Play.SCISSORS,
}

OUTCOME = {
    Play.ROCK: {
        Play.ROCK: Outcome.DRAW,
        Play.PAPER: Outcome.WIN,
        Play.SCISSORS: Outcome.LOSE,
    },
    Play.PAPER: {
        Play.ROCK: Outcome.LOSE,
        Play.PAPER: Outcome.DRAW,
        Play.SCISSORS: Outcome.WIN,
    },
    Play.SCISSORS: {
        Play.ROCK: Outcome.WIN,
        Play.PAPER: Outcome.LOSE,
        Play.SCISSORS: Outcome.DRAW,
    },
}


def parse(lines: List[str]) -> List[Tuple[Play, Play]]:
    """TODO"""
    rounds = []
    for line in lines:
        parts = line.split()
        rounds.append((PLAY_LOOKUP[parts[0]], PLAY_LOOKUP[parts[1]]))

    return rounds


def compute_answer(lines: List[str]) -> int:
    """TODO"""
    result = 0
    rounds = parse(lines)
    for round_ in rounds:
        play_score = round_[1].value
        outcome_score = OUTCOME[round_[0]][round_[1]].value
        result += play_score + outcome_score

    return result
