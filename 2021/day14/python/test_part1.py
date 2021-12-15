from part1 import compute_answer, step

SAMPLE_RULE = {
    "CH": "B",
    "HH": "N",
    "CB": "H",
    "NH": "C",
    "HB": "C",
    "HC": "B",
    "HN": "C",
    "NN": "C",
    "BH": "H",
    "NC": "B",
    "NB": "B",
    "BN": "B",
    "BB": "N",
    "BC": "B",
    "CC": "N",
    "CN": "C",
}


def test_step_1():
    polymer = "NNCB"
    expected = "NCNBCHB"
    actual = step(polymer, SAMPLE_RULE)
    assert actual == expected


def test_step_2():
    polymer = "NCNBCHB"
    expected = "NBCCNBBBCBHCB"
    actual = step(polymer, SAMPLE_RULE)
    assert actual == expected


def test_step_3():
    polymer = "NBCCNBBBCBHCB"
    expected = "NBBBCNCCNBBNBNBBCHBHHBCHB"
    actual = step(polymer, SAMPLE_RULE)
    assert actual == expected


def test_step_4():
    polymer = "NBBBCNCCNBBNBNBBCHBHHBCHB"
    expected = "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"
    actual = step(polymer, SAMPLE_RULE)
    assert actual == expected


def test_compute_answer_sample():
    lines = [
        "NNCB",
        "",
        "CH -> B",
        "HH -> N",
        "CB -> H",
        "NH -> C",
        "HB -> C",
        "HC -> B",
        "HN -> C",
        "NN -> C",
        "BH -> H",
        "NC -> B",
        "NB -> B",
        "BN -> B",
        "BB -> N",
        "BC -> B",
        "CC -> N",
        "CN -> C",
    ]
    expected = 1588
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 2937
    actual = compute_answer(lines)
    assert actual == expected
