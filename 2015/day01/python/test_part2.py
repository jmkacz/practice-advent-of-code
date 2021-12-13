from part2 import compute_answer


def test_compute_answer_sample_1():
    lines = [")"]
    expected = 1
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_2():
    lines = ["()())"]
    expected = 5
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 1771
    actual = compute_answer(lines)
    assert actual == expected
