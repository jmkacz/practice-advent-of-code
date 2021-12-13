from part2 import compute_answer


def test_compute_answer_sample_1():
    lines = ["2x3x4"]
    expected = 34
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_2():
    lines = ["1x1x10"]
    expected = 14
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 3737498
    actual = compute_answer(lines)
    assert actual == expected
