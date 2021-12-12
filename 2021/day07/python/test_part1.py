from part1 import compute_answer


def test_compute_answer_sample():
    lines = ["16,1,2,0,4,2,7,1,2,14"]
    expected = 37
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 364898
    actual = compute_answer(lines)
    assert actual == expected
