import pytest
from part1 import compute_answer

SAMPLE = [
    ("d", 72),
    ("e", 507),
    ("f", 492),
    ("g", 114),
    ("h", 65412),
    ("i", 65079),
    ("x", 123),
    ("y", 456),
]


@pytest.mark.parametrize("wire,signal", SAMPLE)
def test_compute_answer_sample(wire, signal):
    lines = [
        "123 -> x",
        "456 -> y",
        "x AND y -> d",
        "x OR y -> e",
        "x LSHIFT 2 -> f",
        "y RSHIFT 2 -> g",
        "NOT x -> h",
        "NOT y -> i",
    ]
    expected = signal
    actual = compute_answer(lines, wire)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    wire = "a"
    expected = 16076
    actual = compute_answer(lines, wire)
    assert actual == expected
