from typing import List


def compute_answer(lines: List[str]) -> int:
    result = 0
    rows = len(lines)
    cols = len(lines[0])
    for r in range(rows):
        for c in range(cols):
            # up
            if r > 0 and lines[r - 1][c] <= lines[r][c]:
                continue

            # down
            if r < rows - 1 and lines[r + 1][c] <= lines[r][c]:
                continue

            # left
            if c > 0 and lines[r][c - 1] <= lines[r][c]:
                continue

            # right
            if c < cols - 1 and lines[r][c + 1] <= lines[r][c]:
                continue

            # print(r, c, lines[r][c])
            result += int(lines[r][c]) + 1

    return result
