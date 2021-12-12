from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class Pair:
    x1: int
    y1: int
    x2: int
    y2: int


def parse(lines: List[str]) -> List[Pair]:
    result = []
    for line in lines:
        a, b = line.split(" -> ")
        x1, y1 = a.split(",")
        x2, y2 = b.split(",")
        result.append(Pair(int(x1), int(y1), int(x2), int(y2)))
    return result


def sign(n: int) -> int:
    if n < 0:
        return -1
    if n > 0:
        return 1
    return 0


def generate_line(pair: Pair) -> List[Tuple[int, int]]:
    result = []
    if pair.x1 == pair.x2:
        result = [
            (pair.x1, y)
            for y in range(min(pair.y1, pair.y2), max(pair.y1, pair.y2) + 1)
        ]
    elif pair.y1 == pair.y2:
        result = [
            (x, pair.y1)
            for x in range(min(pair.x1, pair.x2), max(pair.x1, pair.x2) + 1)
        ]
    return result


def compute_answer(lines: List[str]) -> int:
    pairs = parse(lines)
    counts: Dict[Tuple[int, int], int] = defaultdict(int)
    for pair in pairs:
        # print(pair, generate_line(pair))
        for point in generate_line(pair):
            counts[point] += 1
    # for point, count in counts.items():
    #    if count > 1:
    #        print(point, count)
    return len([count for count in counts.values() if count > 1])
