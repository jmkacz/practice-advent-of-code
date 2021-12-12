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
SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def is_corrupted(line: str) -> Tuple[bool, str, str]:
    """Return whether or not a line is corrupted.

    Returns: is_corrupted, expected, actual

    A corrupted line is one where a chunk closes with the wrong character - that
    is, where the characters it opens and closes with do not form one of the
    four legal pairs listed above.
    """
    stack: List[str] = []
    for char in line:
        if char in CLOSERS:
            tmp = stack.pop()
            if tmp != CLOSERS[char]:
                return True, OPENERS[tmp], char
        else:
            assert char in OPENERS
            stack.append(char)

    return False, "", ""


def remove_corrupted_lines(lines: List[str]) -> Tuple[List[str], int]:
    result = []
    total_score = 0
    for line in lines:
        bad, expected, actual = is_corrupted(line)
        if not bad:
            result.append(line)
        else:
            total_score += SCORES[actual]
    return result, total_score


def compute_answer(lines: List[str]) -> Tuple[List[str], int]:
    return remove_corrupted_lines(lines)
