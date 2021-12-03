from advent.part1 import compute_answer


def test_compute_answer_sample():
    lines = ["1721", "979", "366", "299", "675", "1456"]
    target = 2020
    actual = compute_answer(lines, target)
    expected = 514579
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    target = 2020
    actual = compute_answer(lines, target)
    expected = 542619
    assert actual == expected
