from typing import List, Tuple

OPENERS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
CLOSERS = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}
SYNTAX_ERROR_SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def calculate_syntax_error_score(line: str) -> int:
    stack: List[str] = []
    for char in line:
        if char in CLOSERS:
            tmp = stack.pop()
            if tmp != CLOSERS[char]:
                return SYNTAX_ERROR_SCORES[char]
        else:
            # assert char in OPENERS
            stack.append(char)
    return 0


def remove_corrupted_lines(lines: List[str]) -> Tuple[List[str], int]:
    result = []
    total_syntax_error_score = 0
    for line in lines:
        syntax_error_score = calculate_syntax_error_score(line)
        if syntax_error_score > 0:
            total_syntax_error_score += syntax_error_score
        else:
            result.append(line)
    return result, total_syntax_error_score


def calculate_score(line: str) -> int:
    result = 0
    stack: List[str] = []
    for char in line:
        if char in CLOSERS:
            tmp = stack.pop()
            assert tmp == CLOSERS[char]
        else:
            assert char in OPENERS
            stack.append(char)
    while stack:
        result = 5 * result + SCORES[OPENERS[stack.pop()]]
    return result


def compute_answer(lines: List[str]) -> int:
    scores = []
    lines, _ = remove_corrupted_lines(lines)
    for line in lines:
        scores.append(calculate_score(line))
    return sorted(scores)[len(scores) // 2]
