import math
from typing import List, Tuple


def find_low_points(lines: List[str]) -> List[Tuple[int, int]]:
    result = []
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

            result.append((r, c))

    return result


def compute_answer(lines: List[str]) -> int:
    result = 0
    basins: List[int] = []
    rows = len(lines)
    cols = len(lines[0])
    visited = [[False] * cols for _ in range(rows)]
    low_points = find_low_points(lines)
    for low_point in low_points:
        q = [low_point]
        basin = 0
        while q:
            (r, c) = q.pop()
            if r < 0 or r >= rows or c < 0 or c >= cols:
                continue
            if visited[r][c]:
                continue
            if lines[r][c] == "9":
                continue
            visited[r][c] = True
            basin += 1
            q.extend([(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)])
        basins = sorted(basins + [basin], reverse=True)[0:3]
    result = math.prod(basins)
    return result
