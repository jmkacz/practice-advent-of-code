from part2 import compute_answer


def test_compute_answer_sample_1():
    lines = ["qjhvhtzxzqqjkmpb"]
    expected = 1
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_2():
    lines = ["xxyxx"]
    expected = 1
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_3():
    lines = ["uurcxstgmygtbstg"]
    expected = 0
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_4():
    lines = ["ieodomkazucvgmuy"]
    expected = 0
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 53
    actual = compute_answer(lines)
    assert actual == expected
