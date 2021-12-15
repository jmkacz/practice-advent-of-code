from typing import Dict, List, Tuple


def parse(lines: List[str]) -> Tuple[str, Dict[str, str]]:
    template = lines[0]
    rules = {}
    for index in range(2, len(lines)):
        key, value = lines[index].split(" -> ")
        rules[key] = value
    return template, rules


def step(polymer: str, rules: Dict[str, str]) -> str:
    result = polymer[0]
    for index in range(len(polymer) - 1):
        key = polymer[index : index + 2]
        result += rules[key] + key[1]
    return result


def compute_answer(lines: List[str]) -> int:
    polymer, rules = parse(lines)
    for _ in range(10):
        polymer = step(polymer, rules)
    counts: Dict[str, int] = {}
    for ch in polymer:
        counts[ch] = counts.get(ch, 0) + 1
    # max_count = counts[max(counts, key=counts.get)]
    max_count = counts[max(counts, key=lambda x: counts[x])]
    # min_count = counts[min(counts, key=counts.get)]
    min_count = counts[min(counts, key=lambda x: counts[x])]
    return max_count - min_count
