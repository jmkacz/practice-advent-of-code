"""TODO"""
from typing import List


def parse(lines: List[str]) -> List[List[int]]:
    """TODO"""
    result = []
    for line in lines:
        result.append([int(_) for _ in line.strip()])

    return result


def init_visible_matrix(rows: int, cols: int) -> List[List[int]]:
    """Initialize the "visible" matrix, where every cell is set to False (not visible),
    except for the first and last row and column, which are set to True (visible).
    We start with each of the outermost trees in the forest being marked as visible.
    """
    result = []

    result.append([1] * cols)

    for _ in range(rows - 2):
        result.append([1] + [0] * (cols - 2) + [1])

    result.append([1] * cols)

    return result


def mark_visible_left_to_right(forest: List[List[int]], visible: List[List[int]], rows: int, cols: int) -> None:
    """TODO"""
    for row in range(1, rows - 1):
        tallest = forest[row][0]
        for col in range(1, cols - 1):
            if forest[row][col] > tallest:
                tallest = forest[row][col]
                visible[row][col] = 1


def mark_visible_right_to_left(forest: List[List[int]], visible: List[List[int]], rows: int, cols: int) -> None:
    """TODO"""
    for row in range(1, rows - 1):
        tallest = forest[row][cols - 1]
        for col in range(cols - 2, 0, -1):
            if forest[row][col] > tallest:
                tallest = forest[row][col]
                visible[row][col] = 1


def mark_visible_top_to_bottom(forest: List[List[int]], visible: List[List[int]], rows: int, cols: int) -> None:
    """TODO"""
    for col in range(1, cols - 1):
        tallest = forest[0][col]
        for row in range(1, rows - 1):
            if forest[row][col] > tallest:
                tallest = forest[row][col]
                visible[row][col] = 1


def mark_visible_bottom_to_top(forest: List[List[int]], visible: List[List[int]], rows: int, cols: int) -> None:
    """TODO"""
    for col in range(1, cols - 1):
        tallest = forest[rows - 1][col]
        for row in range(rows - 2, 0, -1):
            if forest[row][col] > tallest:
                tallest = forest[row][col]
                visible[row][col] = 1


def compute_answer(lines: List[str]) -> int:
    """TODO"""
    result = 0
    forest = parse(lines)
    rows, cols = len(forest), len(forest[0])
    visible = init_visible_matrix(rows, cols)

    for row in range(1, rows - 1):
        tallest = forest[row][0]
        for col in range(1, cols - 1):
            if forest[row][col] > tallest:
                tallest = forest[row][col]
                visible[row][col] = 1

    mark_visible_left_to_right(forest, visible, rows, cols)
    mark_visible_right_to_left(forest, visible, rows, cols)
    mark_visible_top_to_bottom(forest, visible, rows, cols)
    mark_visible_bottom_to_top(forest, visible, rows, cols)

    result = sum(sum(_) for _ in visible)
    return result
