from typing import List


def compute_answer(lines: List[str]) -> int:
    floor = 0
    line = lines[0]
    for pos, char in enumerate(line):
        if char == "(":
            floor += 1
        if char == ")":
            floor -= 1
        if floor == -1:
            return pos + 1
    return -1
