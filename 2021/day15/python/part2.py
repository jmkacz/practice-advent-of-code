import heapq
import networkx as nx  # type: ignore
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


def original(lines: List[str]) -> int:
    """dijkstras single source shortest path algorithm"""
    risks = parse(lines)
    rc = len(risks)
    cc = len(risks[0])
    graph = [[sys.maxsize // 4] * cc for _ in range(rc)]
    pq: List[Tuple[int, Tuple[int, int]]] = []
    heapq.heappush(pq, (0, (0, 0)))
    graph[0][0] = 0
    while pq:
        risk, (r, c) = heapq.heappop(pq)
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if 0 <= r + dr < rc and 0 <= c + dc < cc:
                if graph[r + dr][c + dc] > graph[r][c] + risks[r + dr][c + dc]:
                    graph[r + dr][c + dc] = graph[r][c] + risks[r + dr][c + dc]
                    heapq.heappush(pq, (graph[r + dr][c + dc], (r + dr, c + dc)))
    return graph[rc - 1][cc - 1]


def build_graph(risks: List[List[int]]) -> nx.Graph:
    graph = nx.DiGraph()
    rc = len(risks)
    cc = len(risks[0])
    for r in range(rc):
        for c in range(cc):
            graph.add_node((r, c))
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                r2, c2 = r + dr, c + dc
                if 0 <= r2 < rc and 0 <= c2 < cc:
                    graph.add_edge((r, c), (r2, c2), weight=risks[r2][c2])
    # print(graph)
    # print(graph.nodes)
    # print(graph.edges(data=True))
    return graph


def alternative(lines: List[str]) -> int:
    risks = parse(lines)
    rc = len(risks)
    cc = len(risks[0])
    graph = build_graph(risks)
    path = nx.shortest_path(
        graph, source=(0, 0), target=(rc - 1, cc - 1), weight="weight"
    )
    # print(path)
    return sum(risks[r][c] for r, c in path[1:])


def compute_answer(lines: List[str]) -> int:
    return original(lines)
    # return alternative(lines)
