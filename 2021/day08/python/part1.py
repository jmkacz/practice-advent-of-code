from dataclasses import dataclass
from typing import List


@dataclass
class Entry:
    patterns: List[str]
    outputs: List[str]


def parse(lines: List[str]) -> List[Entry]:
    result = []
    for line in lines:
        left, _, right = line.partition(" | ")
        patterns = left.split(" ")
        outputs = right.split(" ")
        result.append(Entry(patterns, outputs))
    return result


def compute_answer(lines: List[str]) -> int:
    result = 0
    entries = parse(lines)
    for entry in entries:
        for output in entry.outputs:
            if len(output) in (2, 4, 3, 7):  # 1, 4, 7, 8
                result += 1
    return result
