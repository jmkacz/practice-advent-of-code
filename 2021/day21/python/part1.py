import re
from typing import Dict, Generator, List


def parse(lines: List[str]) -> Dict[int, int]:
    result = {}
    pattern = re.compile(r"Player (\d+) starting position: (\d+)")
    for line in lines:
        match = pattern.match(line)
        if match is None:
            raise Exception("Invalid line")
        result[int(match.group(1)) - 1] = int(match.group(2))
    return result


def generate_roll() -> Generator[int, None, None]:
    roll = 0
    while True:
        yield roll + 1
        roll = (roll + 1) % 100


def compute_answer(lines: List[str]) -> int:
    die = generate_roll()
    spaces = parse(lines)
    scores = {k: 0 for k in spaces}
    player = 0
    rolls = 0
    while all([score < 1000 for score in scores.values()]):
        roll1 = next(die)
        roll2 = next(die)
        roll3 = next(die)
        rolls += 3
        spaces[player] = (spaces[player] + roll1 + roll2 + roll3 - 1) % 10 + 1
        scores[player] += spaces[player]
        # print(player, roll1, roll2, roll3, spaces[player], scores[player])
        player = (player + 1) % len(spaces)
    return scores[player] * rolls
