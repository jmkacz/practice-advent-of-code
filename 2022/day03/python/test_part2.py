"""TODO"""
import pytest

from part2 import compute_answer, find_badge, get_priority, parse

SAMPLE_DATA = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".splitlines()


def test_parse():
    """TODO"""
    expected = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]
    actual = parse(SAMPLE_DATA)
    assert actual == expected


@pytest.mark.parametrize(
    "rucksack1,rucksack2,rucksack3,expected",
    [
        ("vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", "r"),
        ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw", "Z"),
    ],
)
def test_find_badge(rucksack1, rucksack2, rucksack3, expected):
    """TODO"""
    actual = find_badge(rucksack1, rucksack2, rucksack3)
    assert actual == expected


@pytest.mark.parametrize(
    "item,expected",
    [
        ("r", 18),
        ("Z", 52),
    ],
)
def test_get_priority(item, expected):
    """TODO"""
    actual = get_priority(item)
    assert actual == expected


def test_compute_answer_sample():
    """TODO"""
    expected = 70
    actual = compute_answer(SAMPLE_DATA)
    assert actual == expected


def test_compute_answer_full():
    """TODO"""
    with open("../data/input.dat", "r", encoding="utf-8") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 2703
    actual = compute_answer(lines)
    assert actual == expected
