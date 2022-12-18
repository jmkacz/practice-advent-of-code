"""TODO"""
from part1 import compute_answer, parse

SAMPLE_DATA = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
""".splitlines()


def test_parse():
    """TODO"""
    expected = [
        ("R", 4),
        ("U", 4),
        ("L", 3),
        ("D", 1),
        ("R", 4),
        ("D", 1),
        ("L", 5),
        ("R", 2),
    ]
    actual = parse(SAMPLE_DATA)
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

    expected = 6470
    actual = compute_answer(lines)
    assert actual == expected
