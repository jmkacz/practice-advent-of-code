from part1 import compute_answer


def test_compute_answer_sample():
    lines = [
        "London to Dublin = 464",
        "London to Belfast = 518",
        "Dublin to Belfast = 141",
    ]
    expected = 605
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 141
    actual = compute_answer(lines)
    assert actual == expected
