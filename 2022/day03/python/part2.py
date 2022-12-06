"""TODO"""
from typing import List


def parse(lines: List[str]) -> List[str]:
    """TODO"""
    rucksacks = []
    for line in lines:
        rucksacks.append(line)

    return rucksacks


def find_badge(rucksack1: str, rucksack2: str, rucksack3: str) -> str:
    """TODO"""
    common = set(rucksack1) & set(rucksack2) & set(rucksack3)
    assert len(common) == 1
    return common.pop()


def get_priority(item):
    """TODO

    To help prioritize item rearrangement, every item type can be converted to a priority:
    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.
    """
    if "a" <= item <= "z":
        return (ord(item) - ord("a")) + 1
    if "A" <= item <= "Z":
        return (ord(item) - ord("A")) + 27
    return 0


def compute_answer(lines: List[str]) -> int:
    """TODO"""
    result = 0
    rucksacks = parse(lines)
    index = 0
    while index < len(rucksacks):
        result += get_priority(find_badge(rucksacks[index], rucksacks[index + 1], rucksacks[index + 2]))
        index += 3

    return result
