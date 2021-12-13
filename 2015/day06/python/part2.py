from typing import List


def compute_answer(lines: List[str]) -> int:
    result = 0
    grid = [[0] * 1000 for _ in range(1000)]
    for line in lines:
        if line.startswith("turn on "):
            line = line[8:]
            fn = lambda x: x + 1
        elif line.startswith("turn off "):
            line = line[9:]
            fn = lambda x: max(x - 1, 0)
        elif line.startswith("toggle "):
            line = line[7:]
            fn = lambda x: x + 2
        a, b = line.split(" through ")
        ar, ac = [int(_) for _ in a.split(",")]
        br, bc = [int(_) for _ in b.split(",")]
        for r in range(ar, br + 1):
            for c in range(ac, bc + 1):
                grid[r][c] = fn(grid[r][c])
    for r in range(len(grid)):
        result += sum(grid[r])
    return result
