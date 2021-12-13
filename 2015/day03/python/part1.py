from collections import defaultdict
from typing import Dict, List, Tuple


def compute_answer(lines: List[str]) -> int:
    houses: Dict[Tuple[int, int], int] = defaultdict(int)
    position = (0, 0)
    houses[position] += 1
    line = lines[0]
    for char in line:
        if char == "<":
            position = (position[0] - 1, position[1])
        if char == ">":
            position = (position[0] + 1, position[1])
        if char == "v":
            position = (position[0], position[1] - 1)
        if char == "^":
            position = (position[0], position[1] + 1)
        houses[position] += 1
    return len(houses)
