"""TODO"""
import operator
from typing import List, Tuple

KNOT_COUNT = 10
DELTA = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0),
}


def parse(lines: List[str]) -> List[Tuple[str, int]]:
    """TODO"""
    result = []
    for line in lines:
        parts = line.split()
        result.append((parts[0], int(parts[1])))

    return result


def sign(num: int) -> int:
    """Return the sign of the given number."""
    if num > 0:
        return 1
    if num < 0:
        return -1
    return 0


def dump_board(direction: str, steps: int, knots: List[Tuple[int, int]]) -> None:
    """TODO"""
    labels = ["H", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    min_x = min(_[0] for _ in knots)
    max_x = max(_[0] for _ in knots)
    min_y = min(_[1] for _ in knots)
    max_y = max(_[1] for _ in knots)
    board = []
    for _ in range(max_y - min_y + 1):
        board.append(["."] * (max_x - min_x + 1))

    for index, knot in enumerate(knots):
        x = knot[0] - min_x
        y = knot[1] - min_y
        if board[y][x] == ".":
            board[y][x] = labels[index]

    print(f"{direction} {steps} [{min_x},{min_y}]..[{max_x},{max_y}]")
    print()
    for row in board:
        print("".join(row))
    print()


def dump_seen(seen: List[Tuple[int, int]]) -> None:
    """TODO"""
    min_x = min(_[0] for _ in seen)
    max_x = max(_[0] for _ in seen)
    min_y = min(_[1] for _ in seen)
    max_y = max(_[1] for _ in seen)
    board = []
    for _ in range(max_y - min_y + 1):
        board.append(["."] * (max_x - min_x + 1))

    for point in seen:
        x = point[0] - min_x
        y = point[1] - min_y
        board[y][x] = "#"

    print("seen")
    print()
    for row in board:
        print("".join(row))
    print()


def compute_answer(lines: List[str]) -> int:
    """TODO"""
    result = 0
    knots = [(0, 0)] * KNOT_COUNT
    seen = set([knots[-1]])
    moves = parse(lines)
    for direction, steps in moves:
        for _ in range(steps):
            knots[0] = tuple(map(operator.add, knots[0], DELTA[direction]))
            for index in range(1, KNOT_COUNT):
                (dx, dy) = tuple(map(operator.sub, knots[index - 1], knots[index]))
                if dx < -1 or dx > 1 or dy < -1 or dy > 1:
                    knots[index] = tuple(map(operator.add, knots[index], (sign(dx), sign(dy))))

            seen.add(knots[-1])

        # dump_board(direction, steps, knots)
        # dump_seen(seen)

        result = len(seen)

    return result
