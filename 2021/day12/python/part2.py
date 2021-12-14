from collections import defaultdict
from pprint import pprint
from typing import Dict, List, Tuple


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
    queue: List[Tuple[List[str], bool]] = [(["start"], False)]
    while queue:
        # pprint(queue)
        path, repeat = queue.pop()
        last = path[-1]
        if last == "end":
            paths.append(path + ["end"])
            continue
        for cave in map[last]:
            if cave.isupper() or cave not in path or not repeat:
                queue.append(
                    (path + [cave], (repeat or (cave.islower() and cave in path)))
                )
    # pprint(paths)
    return len(paths)
