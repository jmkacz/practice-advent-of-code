from typing import List


def compute_answer(lines: List[str]) -> int:
    result = 0
    for line in lines:
        dims = [int(_) for _ in line.split("x")]
        sides = [dims[0] * dims[1], dims[1] * dims[2], dims[2] * dims[0]]
        result += 2 * sum(sides) + min(sides)
    return result
