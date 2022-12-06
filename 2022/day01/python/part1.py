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
    result = max(sum(elf) for elf in elves)
    return result
