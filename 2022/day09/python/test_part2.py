"""TODO"""
from part2 import compute_answer, parse

SAMPLE_DATA = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
""".splitlines()


def test_parse():
    """TODO"""
    expected = [
        ("R", 5),
        ("U", 8),
        ("L", 8),
        ("D", 3),
        ("R", 17),
        ("D", 10),
        ("L", 25),
        ("U", 20),
    ]
    actual = parse(SAMPLE_DATA)
    assert actual == expected


def test_compute_answer_sample():
    """TODO"""
    expected = 36
    actual = compute_answer(SAMPLE_DATA)
    assert actual == expected


def test_compute_answer_full():
    """TODO"""
    with open("../data/input.dat", "r", encoding="utf-8") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 2658
    actual = compute_answer(lines)
    assert actual == expected
