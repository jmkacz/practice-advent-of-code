import re
from functools import cache
from typing import List, Tuple


def parse(lines: List[str]) -> Tuple[int, int]:
    result = {}
    pattern = re.compile(r"Player (\d+) starting position: (\d+)")
    for line in lines:
        match = pattern.match(line)
        if match is None:
            raise Exception("Invalid line")
        result[int(match.group(1)) - 1] = int(match.group(2))
    return result[0], result[1]


@cache
def play(
    player: int, space0: int, space1: int, score0: int, score1: int
) -> Tuple[int, int]:
    if score0 >= 21:
        return (1, 0)
    if score1 >= 21:
        return (0, 1)
    net_wins0 = 0
    net_wins1 = 0
    for roll1 in (1, 2, 3):
        for roll2 in (1, 2, 3):
            for roll3 in (1, 2, 3):
                roll = roll1 + roll2 + roll3
                if player == 0:
                    new_space0 = (space0 + roll - 1) % 10 + 1
                    new_score0 = score0 + new_space0
                    wins0, wins1 = play(
                        1 - player, new_space0, space1, new_score0, score1
                    )
                else:
                    new_space1 = (space1 + roll - 1) % 10 + 1
                    new_score1 = score1 + new_space1
                    wins0, wins1 = play(
                        1 - player, space0, new_space1, score0, new_score1
                    )
                net_wins0 += wins0
                net_wins1 += wins1
    return net_wins0, net_wins1


def compute_answer(lines: List[str]) -> int:
    player = 0
    spaces = parse(lines)
    scores = (0, 0)
    wins = play(player, spaces[0], spaces[1], scores[0], scores[1])
    return max(wins)
