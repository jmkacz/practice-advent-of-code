"""TODO"""
import operator
from typing import List, Tuple

DELTA = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0),
}


def parse(lines: List[str]) -> List[Tuple[str, int]]:
    """TODO"""
    result = []
    for line in lines:
        parts = line.split()
        result.append((parts[0], int(parts[1])))

    return result


def sign(num: int) -> int:
    """Return the sign of the given number."""
    if num > 0:
        return 1
    if num < 0:
        return -1
    return 0


def compute_answer(lines: List[str]) -> int:
    """TODO"""
    result = 0
    head = (0, 0)
    tail = (0, 0)
    seen = set([tail])
    moves = parse(lines)
    for direction, steps in moves:
        for _ in range(steps):
            head = tuple(map(operator.add, head, DELTA[direction]))
            (dx, dy) = tuple(map(operator.sub, head, tail))
            if dx < -1 or dx > 1 or dy < -1 or dy > 1:
                tail = tuple(map(operator.add, tail, (sign(dx), sign(dy))))
                seen.add(tail)

        result = len(seen)

    return result
