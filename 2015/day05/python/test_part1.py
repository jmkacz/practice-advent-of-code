from part1 import compute_answer


def test_compute_answer_sample_1():
    lines = ["ugknbfddgicrmopn"]
    expected = 1
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_2():
    lines = ["aaa"]
    expected = 1
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_3():
    lines = ["jchzalrnumimnmhp"]
    expected = 0
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_4():
    lines = ["haegwjzuvuyypxyu"]
    expected = 0
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_5():
    lines = ["dvszwmarrgswjxmb"]
    expected = 0
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 258
    actual = compute_answer(lines)
    assert actual == expected
