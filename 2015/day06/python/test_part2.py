from part2 import compute_answer


def test_compute_answer_sample_1():
    lines = ["turn on 0,0 through 999,999"]
    expected = 1_000_000
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_2():
    lines = [
        "toggle 0,0 through 999,0",
    ]
    expected = 2_000
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 15343601
    actual = compute_answer(lines)
    assert actual == expected
