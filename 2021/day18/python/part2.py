import itertools
from typing import List, Tuple, Union


def parse(lines: List[str]) -> List[List[str]]:
    return [list(line) for line in lines]


def add(a: List[str], b: List[str]) -> List[str]:
    return ["["] + a + [","] + b + ["]"]


def reduce_step(number: List[str]) -> Tuple[str, List[str]]:
    index = 0
    level = 0
    while index < len(number):
        if number[index] == "[":
            level += 1
        elif number[index] == "]":
            level -= 1
        elif level > 4:
            if (
                number[index].isdigit()
                and number[index + 1] == ","
                and number[index + 2].isdigit()
            ):
                for lindex in range(index - 1, -1, -1):
                    if number[lindex].isdigit():
                        number[lindex] = str(int(number[lindex]) + int(number[index]))
                        break
                for rindex in range(index + 3, len(number)):
                    if number[rindex].isdigit():
                        number[rindex] = str(
                            int(number[rindex]) + int(number[index + 2])
                        )
                        break
                return "explode", number[: index - 1] + ["0"] + number[index + 4 :]
        index += 1

    index = 0
    while index < len(number):
        if number[index].isdigit() and int(number[index]) >= 10:
            a = str(int(number[index]) // 2)
            b = str(int(number[index]) - int(a))
            return "split", number[:index] + ["[", a, ",", b, "]"] + number[index + 1 :]
        index += 1

    return "noop", number


def reduce(number: List[str]) -> List[str]:
    action = ""
    # print("".join(number))
    while action != "noop":
        action, number = reduce_step(number)
        # print(action, "".join(number))
    return number


def play(lines: List[str]) -> List[str]:
    numbers = parse(lines)
    result = numbers[0]
    for index in range(1, len(numbers)):
        result = reduce(add(result, numbers[index]))
    return result


def compute_magnitude(number: str) -> int:
    def inner(x) -> int:
        if isinstance(x, int):
            return x
        return 3 * inner(x[0]) + 2 * inner(x[1])

    tree = eval(number)
    return inner(tree)


def compute_answer(lines: List[str]) -> int:
    result = 0
    for a, b in itertools.permutations(range(len(lines)), 2):
        result = max(result, compute_magnitude("".join(play([lines[a], lines[b]]))))
    return result
