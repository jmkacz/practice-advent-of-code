"""TODO"""
from collections import deque, namedtuple
from typing import List, Tuple

DELTAS = [
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
]

Cell = namedtuple("Cell", ["row", "col"])


def parse(lines: List[str]) -> Tuple[List[List[int]], Cell, Cell]:
    """TODO"""
    grid, start, end = [], Cell(0, 0), Cell(0, 0)
    for row, heights in enumerate(lines):
        gridrow = []
        for col, height in enumerate(heights):
            if height == "S":
                start = Cell(row, col)
                height = "a"
            elif height == "E":
                end = Cell(row, col)
                height = "z"
            gridrow.append(ord(height) - ord("a"))
        grid.append(gridrow)

    return grid, start, end


def find_neighbors(current: Cell, row_max: int, col_max: int) -> List[Cell]:
    """TODO"""
    result = []
    for delta in DELTAS:
        neighbor = Cell(current.row + delta[0], current.col + delta[1])
        if neighbor.row < 0 or neighbor.row >= row_max:
            continue
        if neighbor.col < 0 or neighbor.col >= col_max:
            continue
        result.append(neighbor)

    return result


def init_queue(heightmap):
    """TODO"""
    queue = deque()
    for row, heights in enumerate(heightmap):
        for col, height in enumerate(heights):
            if height == 0:
                queue.append((0, Cell(row, col)))

    return queue


def compute_answer(lines: List[str]) -> int:
    """TODO"""
    result = 0
    heightmap, _, end = parse(lines)
    row_max, col_max = len(heightmap), len(heightmap[0])

    visited = [[False for _ in range(col_max)] for _ in range(row_max)]
    queue = init_queue(heightmap)

    while queue and result < row_max * col_max:
        moves, current = queue.popleft()
        if current == end:
            result = moves
            break

        if visited[current.row][current.col]:
            continue

        visited[current.row][current.col] = True
        for neighbor in find_neighbors(current, row_max, col_max):
            distance = heightmap[neighbor.row][neighbor.col] - heightmap[current.row][current.col]
            if distance > 1:
                continue
            queue.append((moves + 1, neighbor))

        result += 1

    return result
