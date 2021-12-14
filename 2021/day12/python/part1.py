from collections import defaultdict
from pprint import pprint
from typing import Dict, List


def parse(lines: List[str]) -> Dict[str, List[str]]:
    """Convert the undirected graph into a directed graph."""
    map = defaultdict(list)
    for line in lines:
        cave1, cave2 = line.split("-")
        # You cannot enter the "start" node.
        # You cannot leave the "end" node.
        if cave2 != "start" and cave1 != "end":
            map[cave1].append(cave2)
        if cave1 != "start" and cave2 != "end":
            map[cave2].append(cave1)
    return map


def compute_answer(lines: List[str]) -> int:
    map = parse(lines)
    paths = []
    queue = [["start"]]
    while queue:
        # pprint(queue)
        path = queue.pop()
        last = path[-1]
        if last == "end":
            paths.append(path + ["end"])
            continue
        for cave in map[last]:
            if cave.isupper() or cave not in path:
                queue.append(path + [cave])
    # pprint(paths)
    return len(paths)
