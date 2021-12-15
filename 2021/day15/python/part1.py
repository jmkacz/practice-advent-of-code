from typing import List


def parse(lines: List[str]) -> List[List[int]]:
    result = []
    for line in lines:
        result.append([int(_) for _ in line])
    return result


def compute_answer(lines: List[str]) -> int:
    risk = parse(lines)
    rc = len(risk)
    cc = len(risk[0])
    for r in range(rc):
        for c in range(cc):
            if r == 0 and c > 0:
                risk[r][c] += risk[r][c - 1]
            if r > 0 and c == 0:
                risk[r][c] += risk[r - 1][c]
            if r > 0 and c > 0:
                risk[r][c] += min(risk[r][c - 1], risk[r - 1][c])
    return risk[rc - 1][cc - 1] - risk[0][0]
