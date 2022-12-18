"""TODO"""
import math
from collections import defaultdict
from typing import Any, Dict, List, Tuple


def parse(lines: List[str]) -> Tuple[Dict[int, Dict[str, Any]], int]:
    """TODO"""
    monkeys: Dict[int, Dict[str, Any]] = {0: {"target": {}}}
    monkey_index = 0
    modulus = 1
    for line in lines:
        if line.strip() == "":
            monkey_index += 1
            monkeys[monkey_index] = {"target": {}}
            continue

        if line.startswith("Monkey"):
            parts = line.replace(":", "").split()
            assert parts[1].strip() == str(monkey_index), f"{parts[1].strip()} == {monkey_index}"
        elif line.startswith("  Starting items: "):
            parts = line.split(":")
            monkeys[monkey_index]["items"] = [int(_) for _ in parts[1].split(",")]
        elif line.startswith("  Operation: "):
            parts = line.split(":")
            assert parts[1].startswith(" new = ")
            rhs = parts[1].split("=")[1]
            monkeys[monkey_index]["operation"] = eval(f"lambda old: {rhs}")  # pylint: disable=eval-used
        elif line.startswith("  Test: "):
            parts = line.split(":")
            assert parts[1].startswith(" divisible by ")
            monkeys[monkey_index]["test"] = eval(  # pylint: disable=eval-used
                f"lambda x: x % {parts[1].split()[-1]} == 0"
            )
            modulus *= int(parts[1].split()[-1])
        elif line.startswith("    If true: "):
            parts = line.split(":")
            assert parts[1].startswith(" throw to monkey ")
            monkeys[monkey_index]["target"][True] = int(parts[1].split()[-1])
        elif line.startswith("    If false: "):
            parts = line.split(":")
            assert parts[1].startswith(" throw to monkey ")
            monkeys[monkey_index]["target"][False] = int(parts[1].split()[-1])
        else:
            raise Exception(f'Unexpected line: "{line}"')

    return monkeys, modulus


def compute_answer(lines: List[str]) -> int:
    """TODO"""
    inspections: Dict[int, int] = defaultdict(int)
    monkeys, modulus = parse(lines)
    for _ in range(10_000):
        # print(f"ROUND {round_}")
        # print()
        for monkey_index in sorted(monkeys):
            # print(f"Monkey {monkey_index}:")
            inspections[monkey_index] += len(monkeys[monkey_index]["items"])
            for _ in range(len(monkeys[monkey_index]["items"])):
                item = monkeys[monkey_index]["items"][0]
                monkeys[monkey_index]["items"] = monkeys[monkey_index]["items"][1:]
                # print(f"  Monkey inspects an item with a worry level of {item}.")
                item = monkeys[monkey_index]["operation"](item)
                # print(f"    Worry level is now {item}.")
                item = item % modulus
                # print(f"    Monkey gets bored with item. Worry level is divided by 3 to {item}.")
                # if monkeys[monkey_index]["test"](item):
                #     print(f"    Current worry level is divisible by ?.")
                # else:
                #     print(f"    Current worry level is not divisible by ?.")
                target = monkeys[monkey_index]["target"][monkeys[monkey_index]["test"](item)]
                # print(f"    Item with worry level {item} is thrown to monkey {target}.")
                monkeys[target]["items"] += [item]

    result = math.prod(sorted(inspections.values(), reverse=True)[0:2])
    return result
