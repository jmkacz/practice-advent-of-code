from typing import List


def is_nice(line: str) -> bool:
    vowel_count = len([c for c in line if c in "aeiou"])
    if vowel_count < 3:
        return False

    double_count = len(
        [line[idx] for idx in range(len(line) - 1) if line[idx] == line[idx + 1]]
    )
    if double_count == 0:
        return False

    if "ab" in line:
        return False

    if "cd" in line:
        return False

    if "pq" in line:
        return False

    if "xy" in line:
        return False

    return True


def compute_answer(lines: List[str]) -> int:
    result = 0
    for line in lines:
        if is_nice(line.lower()):
            result += 1
    return result
