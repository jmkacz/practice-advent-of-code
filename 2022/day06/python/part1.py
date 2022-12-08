"""TODO"""
from typing import List


def parse(lines: List[str]) -> List[str]:
    """TODO"""
    return list(lines[0].strip())


def compute_answer(lines: List[str]) -> int:
    """TODO"""
    buffer = parse(lines)
    segment: List[str] = []
    count = 0
    for char in buffer:
        count += 1
        if char in segment:
            segment = segment[segment.index(char) + 1 :]

        segment.append(char)
        if len(segment) >= 4:
            break

    assert len(segment) == 4

    return count
