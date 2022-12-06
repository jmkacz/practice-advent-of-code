"""TODO"""
import pytest

from part1 import compute_answer, find_common_item, get_priority, parse

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
        ("vJrwpWtwJgWr", "hcsFMMfFFhFp"),
        ("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"),
        ("PmmdzqPrV", "vPwwTWBwg"),
        ("wMqvLMZHhHMvwLH", "jbvcjnnSBnvTQFn"),
        ("ttgJtRGJ", "QctTZtZT"),
        ("CrZsJsPPZsGz", "wwsLwLmpwMDw"),
    ]
    actual = parse(SAMPLE_DATA)
    assert actual == expected


@pytest.mark.parametrize(
    "compartment1,compartment2,expected",
    [
        ("vJrwpWtwJgWr", "hcsFMMfFFhFp", "p"),
        ("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL", "L"),
        ("PmmdzqPrV", "vPwwTWBwg", "P"),
        ("wMqvLMZHhHMvwLH", "jbvcjnnSBnvTQFn", "v"),
        ("ttgJtRGJ", "QctTZtZT", "t"),
        ("CrZsJsPPZsGz", "wwsLwLmpwMDw", "s"),
    ],
)
def test_find_common_item(compartment1, compartment2, expected):
    """TODO"""
    actual = find_common_item(compartment1, compartment2)
    assert actual == expected


@pytest.mark.parametrize(
    "item,expected",
    [
        ("p", 16),
        ("L", 38),
        ("P", 42),
        ("v", 22),
        ("t", 20),
        ("s", 19),
    ],
)
def test_get_priority(item, expected):
    """TODO"""
    actual = get_priority(item)
    assert actual == expected


def test_compute_answer_sample():
    """TODO"""
    expected = 157
    actual = compute_answer(SAMPLE_DATA)
    assert actual == expected


def test_compute_answer_full():
    """TODO"""
    with open("../data/input.dat", "r", encoding="utf-8") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 7795
    actual = compute_answer(lines)
    assert actual == expected
