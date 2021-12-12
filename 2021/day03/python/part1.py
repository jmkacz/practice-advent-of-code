from typing import List


def compute_answer(lines: List[str]) -> int:
    gamma_rate = 0
    epsilon_rate = 0

    n = len(lines)
    ones = [0] * len(lines[0])
    for line in lines:
        for index, bit in enumerate(line):
            ones[index] += int(bit)

    for index in range(len(ones)):
        gamma_rate = gamma_rate * 2
        epsilon_rate = epsilon_rate * 2
        if ones[index] * 2 >= n:
            gamma_rate += 1
        else:
            epsilon_rate += 1

    return gamma_rate * epsilon_rate
