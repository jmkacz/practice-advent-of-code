"""TODO"""
import pytest

from part2 import Cell, compute_answer, find_neighbors, parse

SAMPLE_DATA = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""".splitlines()


def test_parse():
    """TODO"""
    expected = (
        [
            [0, 0, 1, 16, 15, 14, 13, 12],
            [0, 1, 2, 17, 24, 23, 23, 11],
            [0, 2, 2, 18, 25, 25, 23, 10],
            [0, 2, 2, 19, 20, 21, 22, 9],
            [0, 1, 3, 4, 5, 6, 7, 8],
        ],
        Cell(0, 0),
        Cell(2, 5),
    )
    actual = parse(SAMPLE_DATA)
    assert actual == expected


@pytest.mark.parametrize(
    "cell,expected",
    [
        # corners
        (Cell(0, 0), [Cell(0, 1), Cell(1, 0)]),
        (Cell(4, 0), [Cell(4, 1), Cell(3, 0)]),
        (Cell(0, 7), [Cell(0, 6), Cell(1, 7)]),
        (Cell(4, 7), [Cell(4, 6), Cell(3, 7)]),
        # edges
        (Cell(0, 1), [Cell(0, 0), Cell(0, 2), Cell(1, 1)]),
        (Cell(4, 1), [Cell(4, 0), Cell(4, 2), Cell(3, 1)]),
        (Cell(1, 7), [Cell(1, 6), Cell(0, 7), Cell(2, 7)]),
        (Cell(3, 7), [Cell(3, 6), Cell(2, 7), Cell(4, 7)]),
        # center
        (Cell(2, 5), [Cell(2, 4), Cell(2, 6), Cell(1, 5), Cell(3, 5)]),
    ],
)
def test_find_neighbors(cell, expected):
    """TODO"""
    heightmap, _, _ = parse(SAMPLE_DATA)
    row_max, col_max = len(heightmap), len(heightmap[0])
    actual = find_neighbors(cell, row_max, col_max)
    assert actual == expected


def test_compute_answer_sample():
    """TODO"""
    expected = 29
    actual = compute_answer(SAMPLE_DATA)
    assert actual == expected


def test_compute_answer_full():
    """TODO"""
    with open("../data/input.dat", "r", encoding="utf-8") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 354
    actual = compute_answer(lines)
    assert actual == expected
