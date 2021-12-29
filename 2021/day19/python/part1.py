import re
from itertools import permutations
from pprint import pprint
from typing import Dict, Generator, List, Sequence, Tuple, Union


def determinant(A: List[List[int]]) -> int:
    [[a, b, c], [d, e, f], [g, h, i]] = A
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def generate_orientations() -> Generator[List[List[int]], None, None]:
    for (x, y, z) in permutations([0, 1, 2]):
        for sx in (-1, 1):
            for sy in (-1, 1):
                for sz in (-1, 1):
                    o = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                    o[0][x], o[1][y], o[2][z] = sx, sy, sz
                    if determinant(o) == 1:
                        yield o


ORIENTATIONS = list(generate_orientations())


def parse(lines: List[str]) -> Dict[int, List[Tuple[int, int, int]]]:
    result: Dict[int, List[Tuple[int, int, int]]] = {}
    pattern = re.compile(r"--- scanner (\d+) ---")
    scanner = -1
    for line in lines:
        match = pattern.match(line)
        if match:
            scanner = int(match.group(1))
            result[scanner] = []
        elif line.strip() != "":
            x, y, z = line.split(",")
            result[scanner].append((int(x), int(y), int(z)))
    return result


def multiply3(
    A: Sequence[Sequence[int]], B: Sequence[Sequence[int]]
) -> List[Tuple[int, int, int]]:
    c = [(0, 0, 0) for _ in range(len(B))]
    for index, b in enumerate(B):
        c[index] = (
            b[0] * A[0][0] + b[1] * A[1][0] + b[2] * A[2][0],
            b[0] * A[0][1] + b[1] * A[1][1] + b[2] * A[2][1],
            b[0] * A[0][2] + b[1] * A[1][2] + b[2] * A[2][2],
        )
    return c


def subtract3(a: Tuple[int, int, int], b: Tuple[int, int, int]) -> Tuple[int, int, int]:
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def add3(a: Tuple[int, int, int], b: Tuple[int, int, int]) -> Tuple[int, int, int]:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def calculate_orientation_and_delta(
    a: List[Tuple[int, int, int]], b: List[Tuple[int, int, int]]
) -> Union[None, Tuple[List[List[int]], Tuple[int, int, int]]]:
    for orientation in ORIENTATIONS:
        rot = multiply3(orientation, a)
        for ai in range(len(a)):
            for bi in range(len(b)):
                delta = subtract3(b[bi], rot[ai])
                tmp = [add3(x, delta) for x in rot]
                if len(set(tmp) & set(b)) >= 12:
                    return orientation, delta
    return None


def build_mapping(
    scanners: Dict[int, List[Tuple[int, int, int]]]
) -> Dict[int, Dict[int, Tuple[List[List[int]], Tuple[int, int, int]]]]:
    mapping: Dict[int, Dict[int, Tuple[List[List[int]], Tuple[int, int, int]]]] = {}
    for i in range(len(scanners)):
        for j in range(len(scanners)):
            if i == j:
                continue
            result = calculate_orientation_and_delta(scanners[i], scanners[j])
            if result is not None:
                if i not in mapping:
                    mapping[i] = {}
                mapping[i][j] = result
    return mapping


def find_path(
    source: int,
    sink: int,
    mapping: Dict[int, Dict[int, Tuple[List[List[int]], Tuple[int, int, int]]]],
) -> List[int]:
    q = [[source]]
    index = 0
    while q[index][-1] != sink:
        tmp = q[index][-1]
        for scanner in mapping[tmp]:
            q.append(q[index] + [scanner])
        index += 1
    return q[index]


def merge(
    source: int,
    sink: int,
    mapping: Dict[int, Dict[int, Tuple[List[List[int]], Tuple[int, int, int]]]],
    scanners: Dict[int, List[Tuple[int, int, int]]],
) -> Dict[int, List[Tuple[int, int, int]]]:
    path = find_path(source, sink, mapping)
    tmp = scanners[path[0]]
    for index in range(len(path) - 1):
        source, sink = path[index], path[index + 1]
        orientation, delta = mapping[source][sink][0], mapping[source][sink][1]
        tmp = [add3(x, delta) for x in multiply3(orientation, tmp)]
    scanners[sink] = list(set(scanners[sink]) | set(tmp))
    return scanners


def play(lines: List[str]) -> List[Tuple[int, int, int]]:
    scanners = parse(lines)
    mapping = build_mapping(scanners)
    sink = 0
    for source in range(1, len(scanners)):
        scanners = merge(source, sink, mapping, scanners)
    return scanners[sink]


def compute_answer(lines: List[str]) -> int:
    result = play(lines)
    return len(result)
