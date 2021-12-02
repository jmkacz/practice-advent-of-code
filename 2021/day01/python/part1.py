from typing import List


def parse(lines: List[str]) -> List[int]:
    return [int(_) for _ in lines]


def compute_answer(lines: List[str]) -> int:
    result = 0
    depths = parse(lines)
    for index in range(1, len(depths)):
        if depths[index] > depths[index - 1]:
            result += 1
    return result
