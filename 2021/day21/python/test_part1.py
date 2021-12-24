from part1 import compute_answer


def test_compute_answer_sample():
    lines = [
        "Player 1 starting position: 4",
        "Player 2 starting position: 8",
    ]
    expected = 739785
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 918081
    actual = compute_answer(lines)
    assert actual == expected
