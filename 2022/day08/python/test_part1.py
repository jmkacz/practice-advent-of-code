"""TODO"""
from part1 import compute_answer, parse

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


def test_compute_answer_sample():
    """TODO"""
    expected = 21
    actual = compute_answer(SAMPLE_DATA)
    assert actual == expected


def test_compute_answer_full():
    """TODO"""
    with open("../data/input.dat", "r", encoding="utf-8") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 1698
    actual = compute_answer(lines)
    assert actual == expected
