from part1 import compute_answer, parse, step


def test_step_1():
    lines = parse(
        [
            "11111",
            "19991",
            "19191",
            "19991",
            "11111",
        ]
    )
    expected = parse(
        [
            "34543",
            "40004",
            "50005",
            "40004",
            "34543",
        ]
    )
    actual = step(lines)
    assert actual == expected


def test_step_2():
    lines = parse(
        [
            "34543",
            "40004",
            "50005",
            "40004",
            "34543",
        ]
    )
    expected = parse(
        [
            "45654",
            "51115",
            "61116",
            "51115",
            "45654",
        ]
    )
    actual = step(lines)
    assert actual == expected


def test_compute_answer_sample():
    lines = [
        "5483143223",
        "2745854711",
        "5264556173",
        "6141336146",
        "6357385478",
        "4167524645",
        "2176841721",
        "6882881134",
        "4846848554",
        "5283751526",
    ]
    expected = 1656
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 1640
    actual = compute_answer(lines)
    assert actual == expected
