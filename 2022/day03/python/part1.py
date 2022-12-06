"""TODO"""
from typing import List, Tuple


def parse(lines: List[str]) -> List[Tuple[str, str]]:
    """TODO"""
    rucksacks = []
    for line in lines:
        items_per_compartment = len(line) // 2
        compartments = (line[0:items_per_compartment], line[items_per_compartment:])
        rucksacks.append(compartments)

    return rucksacks


def find_common_item(compartment1: str, compartment2: str) -> str:
    """TODO"""
    common = set(compartment1) & set(compartment2)
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
    for rucksack in rucksacks:
        result += get_priority(find_common_item(*rucksack))

    return result
