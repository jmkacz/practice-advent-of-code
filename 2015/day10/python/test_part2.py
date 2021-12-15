from part2 import compute_answer


def test_compute_answer_sample():
    lines = ["1"]
    expected = 1166642
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 3579328
    actual = compute_answer(lines)
    assert actual == expected
