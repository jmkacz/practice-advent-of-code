from part1 import compute_answer


def test_compute_answer_sample():
    lines = ["3,4,3,1,2"]
    days = 18
    expected = 26
    actual = compute_answer(lines, days)
    assert actual == expected


def test_compute_answer_sample2():
    lines = ["3,4,3,1,2"]
    days = 80
    expected = 5934
    actual = compute_answer(lines, days)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    days = 80
    expected = 377263
    actual = compute_answer(lines, days)
    assert actual == expected
