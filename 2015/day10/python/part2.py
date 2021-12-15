import re

# from itertools import groupby
from typing import List

PATTERN = re.compile(r"(\d)\1*")


# def compute_answer(lines: List[str]) -> int:
#     nums = lines[0]
#     for _ in range(50):
#         nums = "".join([str(len(list(g))) + str(k) for k, g in groupby(nums)])
#     return len(nums)


def replace(match):
    run = match.group(0)
    return str(len(run)) + run[0]


def compute_answer(lines: List[str]) -> int:
    nums = lines[0]
    for _ in range(50):
        nums = PATTERN.sub(replace, nums)
    return len(nums)
