from part1 import compute_answer


def test_compute_answer_sample_1():
    lines = ["D2FE28"]
    expected = 6
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_2():
    lines = ["38006F45291200"]
    expected = 9
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_3():
    lines = ["EE00D40C823060"]
    expected = 14
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_5():
    lines = ["8A004A801A8002F478"]
    expected = 16
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_6():
    lines = ["620080001611562C8802118E34"]
    expected = 12
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_6():
    lines = ["C0015000016115A2E0802F182340"]
    expected = 23
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_sample_7():
    lines = ["A0016C880162017C3686B18A3D4780"]
    expected = 31
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 940
    actual = compute_answer(lines)
    assert actual == expected
