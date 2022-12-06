"""TODO"""
from collections import deque

from part2 import compute_answer, parse

SAMPLE_DATA = """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""".splitlines()


def test_parse():
    """TODO"""
    stacks = [
        deque(["N", "Z"]),
        deque(["D", "C", "M"]),
        deque(["P"]),
    ]
    labels = ["1", "2", "3"]
    moves = [
        (1, "2", "1"),
        (3, "1", "3"),
        (2, "2", "1"),
        (1, "1", "2"),
    ]
    expected = (stacks, labels, moves)
    actual = parse(SAMPLE_DATA)
    assert actual == expected


def test_compute_answer_sample():
    """TODO"""
    expected = "MCD"
    actual = compute_answer(SAMPLE_DATA)
    assert actual == expected


def test_compute_answer_full():
    """TODO"""
    with open("../data/input.dat", "r", encoding="utf-8") as infile:
        # lines = [line.strip() for line in infile.readlines()]
        lines = list(infile.readlines())

    expected = "RNLFDJMCT"
    actual = compute_answer(lines)
    assert actual == expected
