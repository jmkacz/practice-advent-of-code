from part2 import compute_answer


def test_compute_answer_sample_1():
    lines = ["C200B40A82"]
    expected = 3  # 1 + 2
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_2():
    lines = ["04005AC33890"]
    expected = 54  # 6 * 9
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_3():
    lines = ["880086C3E88112"]
    expected = 7  # min(8, 9)
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_5():
    lines = ["CE00C43D881120"]
    expected = 9  # max(7, 8, 9)
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_6():
    lines = ["D8005AC2A8F0"]
    expected = 1  # 5 < 15
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_6():
    lines = ["F600BC2D8F"]
    expected = 0  # not(5 > 15)
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_7():
    lines = ["9C005AC2F8F0"]
    expected = 0  # not(5 != 15)
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_8():
    lines = ["9C0141080250320F1802104A08"]
    expected = 1  # (1 + 3) == (2 * 2)
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 13476220616073
    actual = compute_answer(lines)
    assert actual == expected
