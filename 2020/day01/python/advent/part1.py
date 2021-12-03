from typing import List


def find_pair(values: List[int], target: int) -> List[int]:
    distinct_values = set(values)
    for value in distinct_values:
        if (target - value) in distinct_values:
            return sorted([value, target - value])

    return [0, 0]


def compute_answer(lines: List[str], target: int) -> int:
    values = [int(line) for line in lines]
    results = find_pair(values, target)
    return results[0] * results[1]
