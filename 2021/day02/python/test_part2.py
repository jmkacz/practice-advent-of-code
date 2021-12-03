from part2 import compute_answer


def test_compute_answer_sample():
    lines = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]
    expected = 900
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 1282809906
    actual = compute_answer(lines)
    assert actual == expected
