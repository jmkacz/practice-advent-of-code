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
}

OUTCOME_LOOKUP = {
    "X": Outcome.LOSE,
    "Y": Outcome.DRAW,
    "Z": Outcome.WIN,
}

PLAY = {
    Play.ROCK: {
        Outcome.LOSE: Play.SCISSORS,
        Outcome.DRAW: Play.ROCK,
        Outcome.WIN: Play.PAPER,
    },
    Play.PAPER: {
        Outcome.LOSE: Play.ROCK,
        Outcome.DRAW: Play.PAPER,
        Outcome.WIN: Play.SCISSORS,
    },
    Play.SCISSORS: {
        Outcome.LOSE: Play.PAPER,
        Outcome.DRAW: Play.SCISSORS,
        Outcome.WIN: Play.ROCK,
    },
}


def parse(lines: List[str]) -> List[Tuple[Play, Outcome]]:
    """TODO"""
    rounds = []
    for line in lines:
        parts = line.split()
        rounds.append((PLAY_LOOKUP[parts[0]], OUTCOME_LOOKUP[parts[1]]))

    return rounds


def compute_answer(lines: List[str]) -> int:
    """TODO"""
    result = 0
    rounds = parse(lines)
    for round_ in rounds:
        play_score = PLAY[round_[0]][round_[1]].value
        outcome_score = round_[1].value
        result += play_score + outcome_score

    return result
