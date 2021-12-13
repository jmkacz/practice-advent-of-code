from part2 import compute_answer


def test_compute_answer_sample_1():
    lines = ['""']
    expected = 6 - 2
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_2():
    lines = ['"abc"']
    expected = 9 - 5
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_3():
    lines = ['"aaa\\"aaa"']
    expected = 16 - 10
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_4():
    lines = ['"\\x27"']
    expected = 11 - 6
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 2046
    actual = compute_answer(lines)
    assert actual == expected
