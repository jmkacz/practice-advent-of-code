from typing import List


def compute_answer(lines: List[str]) -> int:
    result = 0
    for line in lines:
        index = 0
        while index < len(line):
            # print(index, line[index])
            if line[index] == '"':
                if index == 0:
                    result += 2
                elif index == len(line) - 1:
                    result += 2
            elif line[index] == "\\":
                if line[index + 1] == "\\":
                    result += 2
                    index += 1
                elif line[index + 1] == '"':
                    result += 2
                    index += 1
                elif line[index + 1] == "x":
                    result += 1
                    index += 3
            index += 1
    return result
