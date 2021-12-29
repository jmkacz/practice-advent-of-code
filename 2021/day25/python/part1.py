import copy
from typing import List, Tuple


def step(lines: List[str]) -> Tuple[List[str], bool]:
    result = lines.copy()
    dirty = False
    rows = len(lines)
    cols = len(lines[0])
    for r in range(rows):
        for c in range(cols):
            if lines[r][c] == ">":
                if lines[r][(c + 1) % cols] == ".":
                    # result[r][c] = "."
                    result[r] = result[r][:c] + "." + result[r][c + 1 :]
                    # result[r][(c+1)%cols] = ">"
                    result[r] = (
                        result[r][: (c + 1) % cols]
                        + ">"
                        + result[r][(c + 1) % cols + 1 :]
                    )
                    dirty = True
    lines = result.copy()
    for r in range(rows):
        for c in range(cols):
            if lines[r][c] == "v":
                if lines[(r + 1) % rows][c] == ".":
                    # result[r][c] = "."
                    result[r] = result[r][:c] + "." + result[r][c + 1 :]
                    # result[r][(c+1)%cols] = ">"
                    result[(r + 1) % rows] = (
                        result[(r + 1) % rows][:c]
                        + "v"
                        + result[(r + 1) % rows][c + 1 :]
                    )
                    dirty = True
    return result, dirty


def compute_answer(lines: List[str]) -> int:
    count = 0
    dirty = True
    while dirty and count < 1000:
        lines, dirty = step(lines)
        count += 1
    return count
