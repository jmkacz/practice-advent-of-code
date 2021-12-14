from itertools import permutations
from typing import Dict, Iterable, List, Set, Tuple


def parse(lines: List[str]) -> Tuple[Dict[Tuple[str, str], int], Set[str]]:
    distances = {}
    cities = set()
    for line in lines:
        route, value = line.split(" = ")
        start, end = route.split(" to ")
        cities.add(start)
        cities.add(end)
        distances[(start, end)] = int(value)
        distances[(end, start)] = int(value)
    return distances, cities


def score(distances: Dict[Tuple[str, str], int], route: Tuple[str, ...]) -> int:
    result = 0
    for index in range(len(route) - 1):
        key = (route[index], route[index + 1])
        if key not in distances:
            return 0
        result += distances[key]
    return result


def compute_answer(lines: List[str]) -> int:
    result = 0
    distances, cities = parse(lines)
    for route in permutations(cities):
        route_length = score(distances, route)
        # print(route, route_length)
        if route_length > result:
            result = route_length
    return result
