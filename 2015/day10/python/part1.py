from typing import List


def play(nums: List[int]) -> List[int]:
    result = []
    run = 1
    index = 1
    while index < len(nums):
        if nums[index] == nums[index - 1]:
            run += 1
        else:
            result += [run, nums[index - 1]]
            run = 1
        index += 1
    result += [run, nums[index - 1]]
    return result


def compute_answer(lines: List[str]) -> int:
    nums = [int(_) for _ in lines[0]]
    for _ in range(40):
        nums = play(nums)
    return len(nums)
