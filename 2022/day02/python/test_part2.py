"""TODO"""
from part2 import Outcome, Play, compute_answer, parse

SAMPLE_DATA = """A Y
B X
C Z
""".splitlines()


def test_parse():
    """TODO"""
    expected = [(Play.ROCK, Outcome.DRAW), (Play.PAPER, Outcome.LOSE), (Play.SCISSORS, Outcome.WIN)]
    actual = parse(SAMPLE_DATA)
    assert actual == expected


def test_compute_answer_sample():
    """TODO"""
    expected = 12
    actual = compute_answer(SAMPLE_DATA)
    assert actual == expected


def test_compute_answer_full():
    """TODO"""
    with open("../data/input.dat", "r", encoding="utf-8") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 13193
    actual = compute_answer(lines)
    assert actual == expected
