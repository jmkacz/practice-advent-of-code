"""TODO"""
import pytest

from part1 import compare, compute_answer, parse

SAMPLE_DATA = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
""".splitlines()


def test_parse():
    """TODO"""
    expected = [
        (
            [1, 1, 3, 1, 1],
            [1, 1, 5, 1, 1],
        ),
        (
            [[1], [2, 3, 4]],
            [[1], 4],
        ),
        (
            [9],
            [[8, 7, 6]],
        ),
        (
            [[4, 4], 4, 4],
            [[4, 4], 4, 4, 4],
        ),
        (
            [7, 7, 7, 7],
            [7, 7, 7],
        ),
        (
            [],
            [3],
        ),
        (
            [[[]]],
            [[]],
        ),
        (
            [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
            [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
        ),
    ]
    actual = parse(SAMPLE_DATA)
    assert actual == expected


@pytest.mark.parametrize(
    "left,right,expected",
    [
        ([1, 1, 3, 1, 1], [1, 1, 5, 1, 1], -1),
        ([[1], [2, 3, 4]], [[1], 4], -1),
        ([9], [[8, 7, 6]], 1),
        ([[4, 4], 4, 4], [[4, 4], 4, 4, 4], -1),
        ([7, 7, 7, 7], [7, 7, 7], 1),
        ([], [3], -1),
        ([[[]]], [[]], 1),
        ([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9], 1),
        (10, 22, -1),
        (10, 10, 0),
        (22, 10, 1),
        ([[[1]], 1], [[1], 2], -1),
        ([[[1]], 2], [[1], 1], 1),
        ([[1], 1], [[[1]], 2], -1),
        ([[1], 2], [[[1]], 1], 1),
        ([[8, [[7]]]], [[[[8]]]], 1),
        ([[8, [[7]]]], [[[[8], 2]]], -1),
    ],
)
def test_compare(left, right, expected):
    """TODO"""
    actual = compare(left, right)
    assert actual == expected


def test_compute_answer_sample():
    """TODO"""
    expected = 13
    actual = compute_answer(SAMPLE_DATA)
    assert actual == expected


def test_compute_answer_full():
    """TODO"""
    with open("../data/input.dat", "r", encoding="utf-8") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 5720
    actual = compute_answer(lines)
    assert actual == expected
