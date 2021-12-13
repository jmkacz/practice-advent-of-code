from part1 import compute_answer


def test_compute_answer_sample_1():
    lines = ['""']
    expected = 2 - 0
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_2():
    lines = ['"abc"']
    expected = 5 - 3
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_3():
    lines = ['"aaa\\"aaa"']
    expected = 10 - 7
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_4():
    lines = ['"\\x27"']
    expected = 6 - 1
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 1333
    actual = compute_answer(lines)
    assert actual == expected
