import heapq
import sys
from typing import List, Tuple

FACTOR = 5


def parse(lines: List[str]) -> List[List[int]]:
    tmp = []
    for line in lines:
        tmp.append([int(_) for _ in line])
    rc = len(tmp)
    cc = len(tmp[0])
    result = [[0] * FACTOR * cc for _ in range(FACTOR * rc)]
    for dr in range(FACTOR):
        for dc in range(FACTOR):
            for r in range(rc):
                for c in range(cc):
                    result[dr * rc + r][dc * cc + c] = (tmp[r][c] + dr + dc - 1) % 9 + 1
    return result


def compute_answer(lines: List[str]) -> int:
    """dijkstras single source shortest path algorithm"""
    weights = parse(lines)
    rc = len(weights)
    cc = len(weights[0])
    risks = [[sys.maxsize // 4] * cc for _ in range(rc)]
    pq: List[Tuple[int, Tuple[int, int]]] = []
    heapq.heappush(pq, (0, (0, 0)))
    risks[0][0] = 0
    while pq:
        weight, (r, c) = heapq.heappop(pq)
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if 0 <= r + dr < rc and 0 <= c + dc < cc:
                if risks[r + dr][c + dc] > risks[r][c] + weights[r + dr][c + dc]:
                    risks[r + dr][c + dc] = risks[r][c] + weights[r + dr][c + dc]
                    heapq.heappush(pq, (risks[r + dr][c + dc], (r + dr, c + dc)))
    return risks[rc - 1][cc - 1]
