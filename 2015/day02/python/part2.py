import math
from typing import List


def compute_answer(lines: List[str]) -> int:
    result = 0
    for line in lines:
        dims = [int(_) for _ in line.split("x")]
        result += 2 * (sum(dims) - max(dims)) + math.prod(dims)
    return result
