from typing import List


def parse(lines: List[str]) -> List[int]:
    return [int(_) for _ in lines[0].split(",")]


def median(pos: List[int]) -> int:
    pos = sorted(pos)
    if len(pos) % 2 == 1:
        return pos[len(pos) // 2]
    else:
        m1 = pos[len(pos) // 2 - 1]
        m2 = pos[len(pos) // 2]
        assert m1 == m2
        return m1


def compute_answer(lines: List[str]) -> int:
    result = 0
    pos = parse(lines)
    m = median(pos)
    for p in pos:
        result += abs(p - m)
    return result
