import re
from typing import List, Set, Tuple


def parse(lines: List[str]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    pattern = re.compile(
        r"target area: x=(?P<x1>.*)\.\.(?P<x2>.*), y=(?P<y1>.*)\.\.(?P<y2>.*)"
    )
    match = pattern.match(lines[0])
    if match is None:
        raise Exception("Bad line: %s", lines[0])
    (x1, x2, y1, y2) = match.groups()
    xrange = sorted((int(x1), int(x2)))
    yrange = sorted((int(y1), int(y2)))
    return ((xrange[0], xrange[1]), (yrange[0], yrange[1]))


def play(
    velocity: Tuple[int, int], target: Tuple[Tuple[int, int], Tuple[int, int]]
) -> Tuple[bool, int]:
    tx, ty = target
    (x, y) = (0, 0)
    (dx, dy) = velocity
    max_y = y
    # print(f"(x, y) = ({x}, {y}) ; (dx, dy) = ({dx}, {dy}) ; target = {target}")  # XXX
    while x <= tx[1] and y >= ty[0]:
        (x, y) = (x + dx, y + dy)
        (dx, dy) = (max(0, dx - 1), dy - 1)
        max_y = max(max_y, y)
        # print(
        #     f"(x, y) = ({x}, {y}) ; (dx, dy) = ({dx}, {dy}) ; target = {target}"
        # )  # XXX
        if tx[0] <= x <= tx[1] and ty[0] <= y <= ty[1]:
            return True, max_y

    return False, 0


def foo(target: Tuple[Tuple[int, int], Tuple[int, int]]) -> int:
    result = 0
    tx, ty = target
    for dx in range(ty[0], tx[1] + 1):
        for dy in range(ty[0], -ty[0]):
            success, max_y = play((dx, dy), target)
            # print(f"play(({dx}, {dy}), {target}) => ({success}, {max_y})")  # XXX
            if success:
                result = max(result, max_y)
    return result


def compute_answer(lines: List[str]) -> int:
    target = parse(lines)
    return foo(target)
