"""TODO"""
import pytest

from part2 import compute_answer, is_overlap, parse

SAMPLE_DATA = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".splitlines()


def test_parse():
    """TODO"""
    expected = [
        ((2, 4), (6, 8)),
        ((2, 3), (4, 5)),
        ((5, 7), (7, 9)),
        ((2, 8), (3, 7)),
        ((6, 6), (4, 6)),
        ((2, 6), (4, 8)),
    ]
    actual = parse(SAMPLE_DATA)
    assert actual == expected


@pytest.mark.parametrize(
    "section1,section2,expected",
    [
        ([2, 4], [6, 8], False),
        ([2, 3], [4, 5], False),
        ([5, 7], [7, 9], True),
        ([2, 8], [3, 7], True),
        ([6, 6], [4, 6], True),
        ([2, 6], [4, 8], True),
    ],
)
def test_is_overlap(section1, section2, expected):
    """TODO"""
    actual = is_overlap(section1, section2)
    assert actual == expected


def test_compute_answer_sample():
    """TODO"""
    expected = 4
    actual = compute_answer(SAMPLE_DATA)
    assert actual == expected


def test_compute_answer_full():
    """TODO"""
    with open("../data/input.dat", "r", encoding="utf-8") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 924
    actual = compute_answer(lines)
    assert actual == expected
