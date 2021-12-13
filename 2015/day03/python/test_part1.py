from part1 import compute_answer


def test_compute_answer_sample_1():
    lines = [">"]
    expected = 2
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_2():
    lines = ["^>v<"]
    expected = 4
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_3():
    lines = ["^v^v^v^v^v"]
    expected = 2
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 2592
    actual = compute_answer(lines)
    assert actual == expected
