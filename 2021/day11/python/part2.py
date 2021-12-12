import copy
from typing import List


def parse(lines: List[str]) -> List[List[int]]:
    cave = []
    for line in lines:
        cave.append([int(_) for _ in line])
    return cave


def step(cave: List[List[int]]) -> List[List[int]]:
    flashes = 0
    cave = copy.deepcopy(cave)
    valid = lambda r, c: 0 <= r < len(cave) and 0 <= c < len(cave[0])
    dirty = False
    for r in range(len(cave)):
        for c in range(len(cave[0])):
            cave[r][c] += 1
    dirty = True
    while dirty:
        dirty = False
        for r in range(len(cave)):
            for c in range(len(cave[0])):
                if cave[r][c] > 9:
                    dirty = True
                    cave[r][c] = 0
                    flashes += 1
                    for dr in (-1, 0, 1):
                        for dc in (-1, 0, 1):
                            if valid(r + dr, c + dc) and cave[r + dr][c + dc] > 0:
                                cave[r + dr][c + dc] += 1
    return cave


def compute_answer(lines: List[str]) -> int:
    result = 0
    cave = parse(lines)
    while True:
        cave = step(cave)
        result += 1
        if sum([sum(_) for _ in cave]) == 0:
            break
    return result
