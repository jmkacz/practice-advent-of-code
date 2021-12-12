from part2 import compute_answer


def test_compute_answer_sample():
    lines = [
        "2199943210",
        "3987894921",
        "9856789892",
        "8767896789",
        "9899965678",
    ]
    expected = 1134
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 1600104
    actual = compute_answer(lines)
    assert actual == expected
