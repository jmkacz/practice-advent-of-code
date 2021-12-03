from typing import List


def find_triple(values: List[int], target: int) -> List[int]:
    distinct_values = set(values)
    for first in distinct_values:
        for second in distinct_values:
            if first == second:
                continue
            third = target - first - second
            if third in distinct_values and third not in (first, second):
                return sorted([first, second, third])

    return [0, 0, 0]


def compute_answer(lines: List[str], target: int) -> int:
    values = [int(line) for line in lines]
    results = find_triple(values, target)
    return results[0] * results[1] * results[2]
