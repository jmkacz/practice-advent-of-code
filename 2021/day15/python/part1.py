import networkx as nx  # type: ignore
from typing import List


def parse(lines: List[str]) -> List[List[int]]:
    result = []
    for line in lines:
        result.append([int(_) for _ in line])
    return result


def original(lines: List[str]) -> int:
    """NOTE: This only works because the solution is strictly down and right!"""
    risks = parse(lines)
    rc = len(risks)
    cc = len(risks[0])
    for r in range(rc):
        for c in range(cc):
            if r == 0 and c > 0:
                risks[r][c] += risks[r][c - 1]
            if r > 0 and c == 0:
                risks[r][c] += risks[r - 1][c]
            if r > 0 and c > 0:
                risks[r][c] += min(risks[r][c - 1], risks[r - 1][c])
    return risks[rc - 1][cc - 1] - risks[0][0]


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
