"""TODO"""
import math
from typing import List


def parse(lines: List[str]) -> List[List[int]]:
    """TODO"""
    result = []
    for line in lines:
        result.append([int(_) for _ in line.strip()])

    return result


def compute_scenic_score(forest: List[List[int]], house_row: int, house_col: int) -> int:
    """TODO"""
    rows, cols = len(forest), len(forest[0])
    house_height = forest[house_row][house_col]
    counts = {"up": 0, "lt": 0, "rt": 0, "dn": 0}

    # up
    for row in range(house_row - 1, -1, -1):
        counts["up"] += 1
        if forest[row][house_col] >= house_height:
            break

    # left
    for col in range(house_col - 1, -1, -1):
        counts["lt"] += 1
        if forest[house_row][col] >= house_height:
            break

    # right
    for col in range(house_col + 1, cols):
        counts["rt"] += 1
        if forest[house_row][col] >= house_height:
            break

    # down
    for row in range(house_row + 1, rows):
        counts["dn"] += 1
        if forest[row][house_col] >= house_height:
            break

    return math.prod(counts.values())


def compute_answer(lines: List[str]) -> int:
    """TODO"""
    result = 0
    forest = parse(lines)
    rows, cols = len(forest), len(forest[0])
    for row in range(rows):
        for col in range(cols):
            result = max(result, compute_scenic_score(forest, row, col))

    return result
