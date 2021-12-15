from part1 import compute_answer, play


def test_play_1():
    nums = [1]
    expected = [1, 1]
    actual = play(nums)
    assert actual == expected


def test_play_2():
    nums = [1, 1]
    expected = [2, 1]
    actual = play(nums)
    assert actual == expected


def test_play_3():
    nums = [2, 1]
    expected = [1, 2, 1, 1]
    actual = play(nums)
    assert actual == expected


def test_play_4():
    nums = [1, 2, 1, 1]
    expected = [1, 1, 1, 2, 2, 1]
    actual = play(nums)
    assert actual == expected


def test_play_5():
    nums = [1, 1, 1, 2, 2, 1]
    expected = [3, 1, 2, 2, 1, 1]
    actual = play(nums)
    assert actual == expected


def test_compute_answer_sample():
    lines = ["1"]
    expected = 82350
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 252594
    actual = compute_answer(lines)
    assert actual == expected
