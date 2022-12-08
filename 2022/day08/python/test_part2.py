"""TODO"""
import pytest

from part2 import compute_answer, compute_scenic_score, parse

SAMPLE_DATA = """30373
25512
65332
33549
35390
""".splitlines()


def test_parse():
    """TODO"""
    expected = [
        [
            3,
            0,
            3,
            7,
            3,
        ],
        [
            2,
            5,
            5,
            1,
            2,
        ],
        [
            6,
            5,
            3,
            3,
            2,
        ],
        [
            3,
            3,
            5,
            4,
            9,
        ],
        [
            3,
            5,
            3,
            9,
            0,
        ],
    ]
    actual = parse(SAMPLE_DATA)
    assert actual == expected


@pytest.mark.parametrize(
    "row,col,expected",
    [
        (1, 2, 4),
        (3, 2, 8),
    ],
)
def test_compute_scenic_score(row, col, expected):
    """TODO"""
    forest = parse(SAMPLE_DATA)
    actual = compute_scenic_score(forest, row, col)
    assert actual == expected


def test_compute_answer_sample():
    """TODO"""
    expected = 8
    actual = compute_answer(SAMPLE_DATA)
    assert actual == expected


def test_compute_answer_full():
    """TODO"""
    with open("../data/input.dat", "r", encoding="utf-8") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 672280
    actual = compute_answer(lines)
    assert actual == expected
