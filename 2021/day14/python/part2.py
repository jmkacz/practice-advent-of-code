from collections import Counter, defaultdict
from typing import Dict, List, Tuple


def parse(lines: List[str]) -> Tuple[str, Dict[str, Tuple[str, str]]]:
    template = lines[0]
    rules = {}
    for index in range(2, len(lines)):
        # ex. "CH -> B" => {"CH": ["CB", "BH"]}
        key, value = lines[index].split(" -> ")
        rules[key] = (key[0] + value, value + key[1])
    return template, rules


def compute_answer(lines: List[str]) -> int:
    template, rules = parse(lines)
    counts = Counter(template)
    # ex. "NNCB" => {"NN": 1, "NC": 1, "CB": 1}
    pairs = Counter(["".join(_) for _ in zip(template[:-1], template[1:])])
    # print(sum(counts.values()), counts, pairs)
    for _ in range(40):
        tmp: Counter[str] = Counter()
        # ex. "CC", 823172187
        for pair, freq in pairs.items():
            # ex. ["CN", "NC"][0][1] => ["CN"][1] => "N"
            value = rules[pair][0][1]  # second character of first element
            # The new character, "N", occurs `freq` times.
            counts[value] += freq
            # Inserting the new character in the middle of an existing pair
            # generates `freq` instances of each new pair.
            tmp[rules[pair][0]] += freq
            tmp[rules[pair][1]] += freq
        pairs = tmp
        # print(sum(counts.values()), counts, pairs)
    max_count = counts[max(counts, key=lambda x: counts[x])]
    min_count = counts[min(counts, key=lambda x: counts[x])]
    return max_count - min_count
