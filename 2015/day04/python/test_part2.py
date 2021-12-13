from part2 import compute_answer


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 9958218
    actual = compute_answer(lines)
    assert actual == expected
