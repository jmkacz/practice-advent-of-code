from typing import List


def parse(lines: List[str]) -> List[int]:
    return [int(_) for _ in lines]


def compute_answer(lines: List[str]) -> int:
    result = 0
    depths = parse(lines)
    for index in range(3, len(depths)):
        if depths[index] > depths[index - 3]:
            result += 1
    return result
