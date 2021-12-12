import statistics
from typing import List


def parse(lines: List[str]) -> List[int]:
    return [int(_) for _ in lines[0].split(",")]


def calc_cost(crabs: List[int], target: int) -> int:
    result = 0
    for crab in crabs:
        dist = abs(crab - target)
        result += dist * (dist + 1) // 2
    return result


def compute_answer(lines: List[str]) -> int:
    result = 0
    crabs = parse(lines)

    target = round(statistics.mean(crabs))
    result = calc_cost(crabs, target)
    for delta in range(1, 10):
        dirty = False

        cost = calc_cost(crabs, target - delta)
        if cost < result:
            dirty = True
            result = cost

        cost = calc_cost(crabs, target + delta)
        if cost < result:
            dirty = True
            result = cost

        if not dirty:
            break

    return result
