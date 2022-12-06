"""TODO"""
from part1 import compute_answer, parse

SAMPLE_DATA = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""".splitlines()


def test_parse():
    """TODO"""
    expected = [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]
    actual = parse(SAMPLE_DATA)
    assert actual == expected


def test_compute_answer_sample():
    """TODO"""
    expected = 24000
    actual = compute_answer(SAMPLE_DATA)
    assert actual == expected


def test_compute_answer_full():
    """TODO"""
    with open("../data/input.dat", "r", encoding="utf-8") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 69310
    actual = compute_answer(lines)
    assert actual == expected
