"""TODO"""
from typing import List, Tuple


def parse(lines: List[str]) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """TODO"""
    pairs = []
    for line in lines:
        elves = line.split(",")
        range1 = [int(_) for _ in elves[0].split("-")]
        range2 = [int(_) for _ in elves[1].split("-")]
        pair = ((range1[0], range1[1]), (range2[0], range2[1]))
        pairs.append(pair)

    return pairs


def is_fully_contained(sections1: Tuple[int, int], sections2: Tuple[int, int]) -> bool:
    """TODO"""
    if sections1[0] <= sections2[0] and sections2[1] <= sections1[1]:
        return True
    if sections2[0] <= sections1[0] and sections1[1] <= sections2[1]:
        return True
    return False


def compute_answer(lines: List[str]) -> int:
    """TODO"""
    result = 0
    pairs = parse(lines)
    for pair in pairs:
        if is_fully_contained(pair[0], pair[1]):
            result += 1

    return result
