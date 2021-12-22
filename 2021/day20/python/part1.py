import sys
from typing import List, Set, Tuple

MAPPING = {
    ".": 0,
    "#": 1,
}


def parse(lines: List[str]) -> Tuple[List[int], Set[Tuple[int, int]]]:
    algorithm, image = [], set()

    index = 0
    while lines[index] != "":
        algorithm.extend([MAPPING[pixel] for pixel in lines[index]])
        index += 1

    index += 1
    for r in range(len(lines) - index):
        for c in range(len(lines[index])):
            if MAPPING[lines[r + index][c]] == 1:
                image.add((r, c))

    return algorithm, image


def find_bounds(image: Set[Tuple[int, int]]) -> Tuple[int, int, int, int]:
    r1 = min(image, key=lambda x: x[0])[0]
    r2 = max(image, key=lambda x: x[0])[0]
    c1 = min(image, key=lambda x: x[1])[1]
    c2 = max(image, key=lambda x: x[1])[1]
    return r1, r2, c1, c2


def step(
    algorithm: List[int], image: Set[Tuple[int, int]], inf: int
) -> Set[Tuple[int, int]]:
    next_image = set()
    r1, r2, c1, c2 = find_bounds(image)
    for r in range(r1 - 1, (r2 + 1) + 1):
        for c in range(c1 - 1, (c2 + 1) + 1):
            index = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    index = index << 1
                    # inside frontier
                    if r1 <= (r + dr) <= r2 and c1 <= (c + dc) <= c2:
                        if (r + dr, c + dc) in image:
                            index += 1
                    # outside frontier
                    else:
                        index += inf
            if algorithm[index]:
                next_image.add((r, c))
    return next_image


def dump(image: Set[Tuple[int, int]]):
    r1, r2, c1, c2 = find_bounds(image)
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            sys.stdout.write("#" if (r, c) in image else ".")
        sys.stdout.write("\n")


def compute_answer(lines: List[str]) -> int:
    algorithm, image = parse(lines)

    # dump(image)

    iteration = 0
    inf = iteration & algorithm[0]  # ex. 0 & 0 = 0, 0 & 1 = 0
    image = step(algorithm, image, inf)

    # dump(image)

    iteration = 1
    inf = iteration & algorithm[0]  # ex. 1 & 0 = 0, 1 & 1 = 1
    image = step(algorithm, image, inf)

    # dump(image)

    return len(image)
