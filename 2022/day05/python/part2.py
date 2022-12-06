"""TODO"""
from collections import deque
from typing import List, Tuple


def parse(lines: List[str]) -> Tuple[List[deque], List[str], List[Tuple[int, str, str]]]:
    """TODO"""
    stacks: List[deque] = []
    labels: List[str] = []
    moves: List[Tuple[int, str, str]] = []

    # parse stacks
    index = 0
    while lines[index].strip() != "":
        line = lines[index]

        while len(stacks) < ((len(line) + 1) // 4):
            stacks.append(deque())

        stack_index = 0
        while True:
            offset = 4 * stack_index + 1
            if offset >= len(line):
                break
            if line[offset] != " ":
                stacks[stack_index].append(line[offset])
            stack_index += 1

        index += 1

    # remove labels
    for stack in stacks:
        value = stack.pop()
        assert value.isdigit()

    # parse labels
    labels = lines[index - 1].split()
    index += 1

    # parse moves
    while index < len(lines):
        parts = lines[index].split()
        moves.append((int(parts[1]), parts[3], parts[5]))
        index += 1

    return stacks, labels, moves


def compute_answer(lines: List[str]) -> str:
    """TODO"""
    result = ""
    stacks, labels, moves = parse(lines)
    for move in moves:
        count = move[0]
        source = labels.index(move[1])
        sink = labels.index(move[2])
        tmp: deque = deque()
        for _ in range(count):
            tmp.append(stacks[source].popleft())
        for _ in range(count):
            stacks[sink].appendleft(tmp.pop())

    result = "".join([stack.popleft() for stack in stacks])
    return result
