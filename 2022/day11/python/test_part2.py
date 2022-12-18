"""TODO"""
from part2 import compute_answer, parse

SAMPLE_DATA = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
""".splitlines()


def test_parse():
    """TODO"""
    expected_monkeys = {
        0: {
            "items": [79, 98],
            "operation": lambda old: old * 19,
            "test": lambda x: x % 23 == 0,
            "result": {
                True: 2,
                False: 3,
            },
        },
        1: {
            "items": [54, 65, 75, 74],
            "operation": lambda old: old + 6,
            "test": lambda x: x % 19 == 0,
            "result": {
                True: 2,
                False: 0,
            },
        },
        2: {
            "items": [79, 60, 97],
            "operation": lambda old: old * old,
            "test": lambda x: x % 13 == 0,
            "result": {
                True: 1,
                False: 3,
            },
        },
        3: {
            "items": [74],
            "operation": lambda old: old + 3,
            "test": lambda x: x % 17 == 0,
            "result": {
                True: 0,
                False: 1,
            },
        },
    }
    expected_modulus = 23 * 19 * 13 * 17
    actual_monkeys, actual_modulus = parse(SAMPLE_DATA)
    assert actual_modulus == expected_modulus
    assert actual_monkeys.keys() == expected_monkeys.keys()
    for i in expected_monkeys:  # pylint: disable=consider-using-dict-items
        assert actual_monkeys[i]["items"] == expected_monkeys[i]["items"]
        assert (
            actual_monkeys[i]["operation"].__code__.co_argcount == expected_monkeys[i]["operation"].__code__.co_argcount
        )
        assert actual_monkeys[i]["operation"].__code__.co_code == expected_monkeys[i]["operation"].__code__.co_code
        assert actual_monkeys[i]["test"].__code__.co_argcount == expected_monkeys[i]["test"].__code__.co_argcount
        assert actual_monkeys[i]["test"].__code__.co_code == expected_monkeys[i]["test"].__code__.co_code


def test_compute_answer_sample():
    """TODO"""
    expected = 2713310158
    actual = compute_answer(SAMPLE_DATA)
    assert actual == expected


def test_compute_answer_full():
    """TODO"""
    with open("../data/input.dat", "r", encoding="utf-8") as infile:
        # lines = [line.strip() for line in infile.readlines()]
        lines = list(infile.readlines())

    expected = 30893109657
    actual = compute_answer(lines)
    assert actual == expected
