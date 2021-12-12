from typing import List, Tuple


SIZE = 5


class Card:
    def __init__(self, rows: List[List[int]]):
        self.rows = rows
        self.marks = [[0] * SIZE for _ in range(SIZE)]

    def __repr__(self) -> str:
        s = ""
        for r in range(SIZE):
            if r > 0:
                s += "\n"
            for c in range(SIZE):
                s += f"{self.rows[r][c]:>3}"
            s += "\t"
            for c in range(SIZE):
                s += f"{self.marks[r][c]:>3}"

        return s

    def mark(self, draw: int) -> int:
        for r in range(SIZE):
            for c in range(SIZE):
                if self.rows[r][c] == draw:
                    self.marks[r][c] = 1
                    if self.is_winner():
                        return self.score(draw)

        return 0

    def is_winner(self) -> bool:
        for r in range(SIZE):
            tmp = sum([self.marks[r][c] for c in range(SIZE)])
            if tmp == SIZE:
                return True

        for c in range(SIZE):
            tmp = sum([self.marks[r][c] for r in range(SIZE)])
            if tmp == SIZE:
                return True

        return False

    def score(self, draw: int) -> int:
        result = 0
        for r in range(SIZE):
            for c in range(SIZE):
                result += self.rows[r][c] * (1 - self.marks[r][c])

        result *= draw
        return result


def parse(lines: List[str]) -> Tuple[List[int], List[Card]]:
    draws = [int(_) for _ in lines[0].split(",")]
    cards = []

    index = 1
    while index < len(lines):
        assert lines[index] == ""

        tmp = []
        for offset in range(1, SIZE + 1):
            # "19  8  7 25 23" => [19, 8, 7, 25, 23]
            tmp.append([int(_) for _ in lines[index + offset].split(" ") if _ != ""])

        cards.append(Card(tmp))
        index += SIZE + 1

    return draws, cards


def compute_answer(lines: List[str]) -> int:
    remaining = len(lines)
    last_score = 0
    has_won = [False] * len(lines)
    draws, cards = parse(lines)
    for draw in draws:
        for index, card in enumerate(cards):
            if has_won[index]:
                continue
            score = card.mark(draw)
            if score > 0:
                has_won[index] = True
                last_score = score
    return last_score
