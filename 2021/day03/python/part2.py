from typing import List


def get_rating(lines: List[str], value: int) -> str:
    for index in range(len(lines[0])):
        n = len(lines)
        ones = 0
        for line in lines:
            ones += int(line[index])
        if ones * 2 >= n:
            char = str(value)
        else:
            char = str(1 - value)
        lines = [line for line in lines if line[index] == char]
        if len(lines) == 1:
            break

    assert len(lines) == 1
    return lines[0]


def compute_answer(lines: List[str]) -> int:
    oxygen_generator_rating = int(get_rating(lines, 1), 2)
    co2_scrubber_rating = int(get_rating(lines, 0), 2)
    return oxygen_generator_rating * co2_scrubber_rating
