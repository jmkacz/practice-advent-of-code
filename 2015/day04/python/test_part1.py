from part1 import compute_answer


def test_compute_answer_sample_1():
    lines = ["abcdef"]
    expected = 609043
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_2():
    lines = ["pqrstuv"]
    expected = 1048970
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 346386
    actual = compute_answer(lines)
    assert actual == expected
