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


def compute_answer(lines: List[str]) -> int:
    """TODO"""
    result = 0
    instructions = parse(lines)
    register = 1
    cycle = 0
    index = 0
    remaining = 0
    while index < len(instructions):
        cycle += 1

        instruction, value = instructions[index]
        if remaining == 0:
            print(f"At the start of cycle {cycle}. The {instruction} {value} instruction begins execution.")
            if instruction == "noop":
                remaining = 1
            elif instruction == "addx":
                remaining = 2

        if (cycle - 20) % 40 == 0:
            strength = register * cycle
            result += strength
            print(
                f"During cycle {cycle}, X is {register}. So the signal strength is"
                f" {cycle} * {register} = {strength} (total = {result})."
            )
        else:
            print(f"During cycle {cycle}, X is {register}.")

        remaining = max(0, remaining - 1)
        if remaining == 0:
            if instruction == "noop":
                print(f"After cycle {cycle}, the {instruction} {value} instruction finishes execution, doing nothing.")
            elif instruction == "addx":
                register += value
                print(
                    f"After cycle {cycle}, the {instruction} {value} instruction"
                    f" finishes execution, setting X to {register}."
                )

            index += 1

        print()

    return result
