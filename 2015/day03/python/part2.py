from collections import defaultdict
from typing import Dict, List, Tuple


def compute_answer(lines: List[str]) -> int:
    houses: Dict[Tuple[int, int], int] = defaultdict(int)
    positions = [(0, 0), (0, 0)]  # Santa, Robo-Santa
    houses[positions[0]] += 1
    houses[positions[1]] += 1
    index = 0
    line = lines[0]
    for char in line:
        if char == "<":
            positions[index] = (positions[index][0] - 1, positions[index][1])
        if char == ">":
            positions[index] = (positions[index][0] + 1, positions[index][1])
        if char == "v":
            positions[index] = (positions[index][0], positions[index][1] - 1)
        if char == "^":
            positions[index] = (positions[index][0], positions[index][1] + 1)
        houses[positions[index]] += 1
        index = 1 - index
    return len(houses)
