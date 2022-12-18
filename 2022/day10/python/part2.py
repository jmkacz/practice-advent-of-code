"""TODO"""
from typing import List, Tuple


def parse(lines: List[str]) -> List[Tuple[str, int]]:
    """TODO"""
    result = []
    for line in lines:
        parts = line.split(" ")
        if parts[0] == "addx":
            result.append((parts[0], int(parts[1])))
        elif parts[0] == "noop":
            result.append((parts[0], 0))
        else:
            raise Exception

    return result


def compute_answer(lines: List[str]) -> List[str]:
    """TODO"""
    result = [
        "........................................",
        "........................................",
        "........................................",
        "........................................",
        "........................................",
        "........................................",
    ]
    instructions = parse(lines)
    register = 1
    cycle = 0
    index = 0
    remaining = 0
    while index < len(instructions):
        cycle += 1
        row, col = (cycle - 1) // 40, (cycle - 1) % 40

        instruction, value = instructions[index]
        if remaining == 0:
            if instruction == "noop":
                remaining = 1
            elif instruction == "addx":
                remaining = 2

        if (register - 1) <= col <= (register + 1):
            result[row] = result[row][:col] + "#" + result[row][col + 1 :]

        remaining = max(0, remaining - 1)
        if remaining == 0:
            if instruction == "noop":
                pass
            elif instruction == "addx":
                register += value

            index += 1

    return result
