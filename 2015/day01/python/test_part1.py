from part1 import compute_answer


def test_compute_answer_sample_1():
    lines = ["(())"]
    expected = 0
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_2():
    lines = ["()()"]
    expected = 0
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_3():
    lines = ["((("]
    expected = 3
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_4():
    lines = ["(()(()("]
    expected = 3
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_5():
    lines = ["))((((("]
    expected = 3
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_6():
    lines = ["())"]
    expected = -1
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_7():
    lines = ["))("]
    expected = -1
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_8():
    lines = [")))"]
    expected = -3
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_9():
    lines = [")())())"]
    expected = -3
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 138
    actual = compute_answer(lines)
    assert actual == expected
