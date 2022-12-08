"""TODO"""
from collections import deque
from dataclasses import dataclass
from enum import Enum
from typing import Deque, List


class NodeType(Enum):
    """TODO"""

    DIRECTORY = 1
    FILE = 2


@dataclass
class Node:
    """TODO"""

    name: str
    type: NodeType
    size: int
    children: List["Node"]


def parse(lines: List[str]) -> Node:
    """TODO"""
    assert lines[0] == "$ cd /"
    root = Node("/", NodeType.DIRECTORY, 0, [])
    current = root
    directory_stack: Deque[Node] = deque()
    last_command = lines[0].split()[1:]
    for line in lines[1:]:
        parts = line.split()
        if parts[0] == "$":
            if parts[1] == "ls":
                pass
            elif parts[1] == "cd":
                if parts[2] == "..":
                    current = directory_stack.popleft()
                else:
                    directory_stack.appendleft(current)
                    current = [_ for _ in current.children if _.name == parts[2]][0]
                    assert current.type == NodeType.DIRECTORY
            else:
                raise Exception()

            last_command = parts[1:]
        else:
            if last_command[0] == "ls":
                if parts[0] == "dir":
                    current.children.append(Node(parts[1], NodeType.DIRECTORY, 0, []))
                else:
                    current.children.append(Node(parts[1], NodeType.FILE, int(parts[0]), []))
            else:
                raise Exception()

    return root


def get_size(node: Node) -> int:
    """TODO"""
    if node.type == NodeType.FILE:
        return node.size

    total = 0
    for child in node.children:
        total += get_size(child)
    node.size = total

    return node.size


def compute_answer(lines: List[str]) -> int:
    """TODO"""
    root = parse(lines)
    total_available_space = 70_000_000
    target_unused_space = 30_000_000
    actual_unused_space = total_available_space - get_size(root)
    assert actual_unused_space < target_unused_space
    target_cleanup_space = target_unused_space - actual_unused_space

    result = root.size
    queue = deque([root])
    while queue:
        current = queue.popleft()
        if current.type == NodeType.DIRECTORY:
            if current.size >= target_cleanup_space and current.size < result:
                result = current.size
            for child in current.children:
                queue.append(child)
    return result
