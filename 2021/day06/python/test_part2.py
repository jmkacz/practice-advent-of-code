from part2 import compute_answer


def test_compute_answer_sample():
    lines = ["3,4,3,1,2"]
    days = 256
    expected = 26984457539
    actual = compute_answer(lines, days)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    days = 256
    expected = 1695929023803
    actual = compute_answer(lines, days)
    assert actual == expected
