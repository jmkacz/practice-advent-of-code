from part1 import compute_answer


def test_compute_answer_sample():
    lines = ["target area: x=20..30, y=-10..-5"]
    expected = 45
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 4278
    actual = compute_answer(lines)
    assert actual == expected
