"""TODO"""
import pytest

from part2 import compute_answer, parse

SAMPLE_DATA = """mjqjpqmgbljsphdztnvjfqwrcgsmlb
""".splitlines()


def test_parse():
    """TODO"""
    expected = [
        "m",
        "j",
        "q",
        "j",
        "p",
        "q",
        "m",
        "g",
        "b",
        "l",
        "j",
        "s",
        "p",
        "h",
        "d",
        "z",
        "t",
        "n",
        "v",
        "j",
        "f",
        "q",
        "w",
        "r",
        "c",
        "g",
        "s",
        "m",
        "l",
        "b",
    ]
    actual = parse(SAMPLE_DATA)
    assert actual == expected


@pytest.mark.parametrize(
    "buffer,expected",
    [
        (["mjqjpqmgbljsphdztnvjfqwrcgsmlb"], 19),
        (["bvwbjplbgvbhsrlpgdmjqwftvncz"], 23),
        (["nppdvjthqldpwncqszvftbrmjlhg"], 23),
        (["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"], 29),
        (["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"], 26),
    ],
)
def test_compute_answer_sample(buffer, expected):
    """TODO"""
    actual = compute_answer(buffer)
    assert actual == expected


def test_compute_answer_full():
    """TODO"""
    with open("../data/input.dat", "r", encoding="utf-8") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 3495
    actual = compute_answer(lines)
    assert actual == expected
