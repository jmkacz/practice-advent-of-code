from typing import List


def compute_answer(lines: List[str]) -> int:
    result = 0
    line = lines[0]
    for char in line:
        if char == "(":
            result += 1
        if char == ")":
            result -= 1
    return result
