from typing import List


def parse(lines: List[str]) -> List[int]:
    result = [0] * 9
    for x in lines[0].split(","):
        result[int(x)] += 1
    return result


def compute_answer(lines: List[str], days: int) -> int:
    timers = parse(lines)
    for day in range(days):
        # print(day, timers)
        tmp = timers[0]
        for i in range(1, len(timers)):
            timers[i - 1] = timers[i]
        timers[6] += tmp
        timers[8] = tmp
    # print(day + 1, timers)
    return sum(timers)
