"""TODO"""
from typing import List


def parse(lines: List[str]) -> List[List[int]]:
    """TODO"""
    elves = []
    elf: List[int] = []
    for line in lines:
        if line.strip() == "":
            elves.append(elf)
            elf = []
        else:
            elf.append(int(line))

    elves.append(elf)
    return elves


def compute_answer(lines: List[str]) -> int:
    """TODO"""
    result = 0
    elves = parse(lines)
    top3 = (0, 0, 0)
    for elf in elves:
        calories = sum(elf)
        if calories > top3[0]:
            top3 = calories, top3[0], top3[1]
        elif calories > top3[1]:
            top3 = top3[0], calories, top3[1]
        elif calories > top3[2]:
            top3 = top3[0], top3[1], calories

    result = sum(top3)
    return result
