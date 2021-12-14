from typing import List, Set, Tuple


def parse(lines: List[str]) -> Tuple[Set[Tuple[int, int]], List[Tuple[str, int]]]:
    dots, folds = set(), []
    index = 0
    while lines[index] != "":
        x, y = lines[index].split(",")
        dots.add((int(x), int(y)))
        index += 1
    index += 1
    while index < len(lines):
        axis, length = lines[index].replace("fold along ", "").split("=")
        folds.append((axis, int(length)))
        index += 1
    return dots, folds


def step(dots: Set[Tuple[int, int]], fold: Tuple[str, int]) -> Set[Tuple[int, int]]:
    result = set()
    axis, length = fold
    for dot in dots:
        x, y = dot
        if axis == "x":
            if x < length:
                result.add(dot)
            if x > length:
                result.add((2 * length - x, y))
        if axis == "y":
            if y < length:
                result.add(dot)
            if y > length:
                result.add((x, 2 * length - y))

    return result


def compute_answer(lines: List[str]) -> List[str]:
    dots, folds = parse(lines)
    for fold in folds:
        dots = step(dots, fold)
    range_x = max(dots, key=lambda dot: dot[0])[0] + 1
    range_y = max(dots, key=lambda dot: dot[1])[1] + 1
    paper = [[" "] * range_x for _ in range(range_y)]
    for dot in dots:
        x, y = dot
        paper[y][x] = "#"
    return ["".join(line) for line in paper]
