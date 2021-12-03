from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Position:
    hpos: int
    depth: int
    aim: int


def parse_line(line: str) -> Tuple[str, int]:
    parts = line.partition(" ")
    dir = parts[0]
    amt = int(parts[2])
    return dir, amt


def compute_answer(lines: List[str]) -> int:
    pos = Position(0, 0, 0)
    for line in lines:
        dir, amt = parse_line(line)

        if dir == "forward":
            pos.hpos += amt
            pos.depth += pos.aim * amt
        elif dir == "down":
            pos.aim += amt
        elif dir == "up":
            pos.aim -= amt
        else:
            raise Exception(f"Unknown direction: {dir}")

        assert pos.depth >= 0

    return pos.hpos * pos.depth
