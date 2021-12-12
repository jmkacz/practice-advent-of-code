from dataclasses import dataclass
from typing import Dict, List


WORKING = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


@dataclass
class Entry:
    patterns: List[str]
    outputs: List[str]


def parse(lines: List[str]) -> List[Entry]:
    result = []
    for line in lines:
        left, _, right = line.partition(" | ")
        patterns = left.split(" ")
        outputs = right.split(" ")
        result.append(Entry(patterns, outputs))
    return result


def deduce(patterns: List[str]) -> Dict[str, int]:
    result = {}
    segments = {}

    sizes: Dict[int, List[str]] = {}
    for pattern in patterns:
        sizes[len(pattern)] = sizes.get(len(pattern), []) + [pattern]

    # ex. {7: ['acedgfb'], 5: ['cdfbe', 'gcdfa', 'fbcad'], 3: ['dab'], 6: ['cefabd', 'cdfgeb', 'cagedb'], 4: ['eafb'], 2: ['ab']}
    # print(sizes)

    # What are cf? (ex. ab)
    cf = sizes[2][0]

    # What is a? (ex. dab - ab => d)
    segments["a"] = (set(sizes[3][0]) - set(sizes[2][0])).pop()

    # What are bd? (ex. eafb - ab => ef)
    bd = "".join(set(sizes[4][0]) - set(sizes[2][0]))

    # What are eg? (ex. acedgfb - eafb - dab => cg)
    eg = "".join(set(sizes[7][0]) - set(sizes[4][0]) - set(sizes[3][0]))

    # What are cde? (ex. ~cefabd + ~cdfgeb + ~cagedb => gaf
    cde = (
        "".join(set(sizes[7][0]) - set(sizes[6][0]))
        + "".join(set(sizes[7][0]) - set(sizes[6][1]))
        + "".join(set(sizes[7][0]) - set(sizes[6][2]))
    )

    # What is b? (ex. ef - gaf => e)
    segments["b"] = "".join(set(bd) - set(cde))

    # What is c? (ex. gaf - ef - cg => a)
    segments["c"] = "".join(set(cde) - set(bd) - set(eg))

    # What is d? (ex. gaf - ab - cg => f)
    segments["d"] = "".join(set(cde) - set(cf) - set(eg))

    # What is e? (ex. gaf - ab - ef => g)
    segments["e"] = "".join(set(cde) - set(cf) - set(bd))

    # What is f? (ex. ab - gaf => b)
    segments["f"] = "".join(set(cf) - set(cde))

    # What is g? (ex. cg - gaf => c)
    segments["g"] = "".join(set(eg) - set(cde))

    # {'a': 'd', 'b': 'e', 'c': 'a', 'd': 'f', 'e': 'g', 'f': 'b', 'g': 'c'}
    # print(segments)
    segments = {v: k for k, v in segments.items()}
    # {'d': 'a', 'e': 'b', 'a': 'c', 'f': 'd', 'g': 'e', 'b': 'f', 'c': 'g'}
    # print(segments)

    for pattern in patterns:
        corrected = "".join(map(lambda x: segments[x], pattern))
        broken_key = "".join(sorted(pattern))
        working_key = "".join(sorted(corrected))
        result[broken_key] = WORKING[working_key]

    # {'abcdefg': 8, 'bcdef': 5, 'acdfg': 2, 'abcdf': 3, 'abd': 7, 'abcdef': 9, 'bcdefg': 6, 'abef': 4, 'abcdeg': 0, 'ab': 1}
    # print(result)
    return result


def compute_answer(lines: List[str]) -> int:
    result = 0
    entries = parse(lines)
    for entry in entries:
        mapping = deduce(entry.patterns)
        value = 0
        for output in entry.outputs:
            value *= 10
            value += mapping["".join(sorted(output))]
        result += value
    return result
