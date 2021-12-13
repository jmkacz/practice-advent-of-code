from typing import List


def check1(line: str) -> bool:
    for index in range(len(line) - 3):
        # print(line, len(line), index, index+2, line[index:index+2])
        for index2 in range(index + 2, len(line) - 1):
            # print(line, len(line), index, index+2, index2, index2+2, line[index:index+2], line[index2:index2+2])
            if line[index : index + 2] == line[index2 : index2 + 2]:
                return True
    return False


def check2(line: str) -> bool:
    for index in range(len(line) - 2):
        if line[index] == line[index + 2]:
            return True
    return False


def is_nice(line: str) -> bool:
    return check1(line) and check2(line)


def compute_answer(lines: List[str]) -> int:
    result = 0
    for line in lines:
        if is_nice(line.lower()):
            result += 1
    return result
