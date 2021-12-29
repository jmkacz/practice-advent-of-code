from part1 import compute_answer, step


def test_step_sample1_step1():
    lines = [
        "...>...",
        ".......",
        "......>",
        "v.....>",
        "......>",
        ".......",
        "..vvv..",
    ]
    expected = [
        "..vv>..",
        ".......",
        ">......",
        "v.....>",
        ">......",
        ".......",
        "....v..",
    ], True
    actual = step(lines)
    assert actual == expected


def test_step_sample1_step2():
    lines = [
        "..vv>..",
        ".......",
        ">......",
        "v.....>",
        ">......",
        ".......",
        "....v..",
    ]
    expected = [
        "....v>.",
        "..vv...",
        ".>.....",
        "......>",
        "v>.....",
        ".......",
        ".......",
    ], True
    actual = step(lines)
    assert actual == expected


def test_step_sample1_step3():
    lines = [
        "....v>.",
        "..vv...",
        ".>.....",
        "......>",
        "v>.....",
        ".......",
        ".......",
    ]
    expected = [
        "......>",
        "..v.v..",
        "..>v...",
        ">......",
        "..>....",
        "v......",
        ".......",
    ], True
    actual = step(lines)
    assert actual == expected


def test_step_sample1_step4():
    lines = [
        "......>",
        "..v.v..",
        "..>v...",
        ">......",
        "..>....",
        "v......",
        ".......",
    ]
    expected = [
        ">......",
        "..v....",
        "..>.v..",
        ".>.v...",
        "...>...",
        ".......",
        "v......",
    ], True
    actual = step(lines)
    assert actual == expected


def test_step_sample2_step1():
    lines = [
        "v...>>.vv>",
        ".vv>>.vv..",
        ">>.>v>...v",
        ">>v>>.>.v.",
        "v>v.vv.v..",
        ">.>>..v...",
        ".vv..>.>v.",
        "v.v..>>v.v",
        "....v..v.>",
    ]
    expected = [
        "....>.>v.>",
        "v.v>.>v.v.",
        ">v>>..>v..",
        ">>v>v>.>.v",
        ".>v.v...v.",
        "v>>.>vvv..",
        "..v...>>..",
        "vv...>>vv.",
        ">.v.v..v.v",
    ], True
    actual = step(lines)
    assert actual == expected


def test_step_sample2_step2():
    lines = [
        "....>.>v.>",
        "v.v>.>v.v.",
        ">v>>..>v..",
        ">>v>v>.>.v",
        ".>v.v...v.",
        "v>>.>vvv..",
        "..v...>>..",
        "vv...>>vv.",
        ">.v.v..v.v",
    ]
    expected = [
        ">.v.v>>..v",
        "v.v.>>vv..",
        ">v>.>.>.v.",
        ">>v>v.>v>.",
        ".>..v....v",
        ".>v>>.v.v.",
        "v....v>v>.",
        ".vv..>>v..",
        "v>.....vv.",
    ], True
    actual = step(lines)
    assert actual == expected


def test_step_sample2_step3():
    lines = [
        ">.v.v>>..v",
        "v.v.>>vv..",
        ">v>.>.>.v.",
        ">>v>v.>v>.",
        ".>..v....v",
        ".>v>>.v.v.",
        "v....v>v>.",
        ".vv..>>v..",
        "v>.....vv.",
    ]
    expected = [
        "v>v.v>.>v.",
        "v...>>.v.v",
        ">vv>.>v>..",
        ">>v>v.>.v>",
        "..>....v..",
        ".>.>v>v..v",
        "..v..v>vv>",
        "v.v..>>v..",
        ".v>....v..",
    ], True
    actual = step(lines)
    assert actual == expected


def test_step_sample2_step4():
    lines = [
        "v>v.v>.>v.",
        "v...>>.v.v",
        ">vv>.>v>..",
        ">>v>v.>.v>",
        "..>....v..",
        ".>.>v>v..v",
        "..v..v>vv>",
        "v.v..>>v..",
        ".v>....v..",
    ]
    expected = [
        "v>..v.>>..",
        "v.v.>.>.v.",
        ">vv.>>.v>v",
        ">>.>..v>.>",
        "..v>v...v.",
        "..>>.>vv..",
        ">.v.vv>v.v",
        ".....>>vv.",
        "vvv>...v..",
    ], True
    actual = step(lines)
    assert actual == expected


def test_step_sample2_step5():
    lines = [
        "v>..v.>>..",
        "v.v.>.>.v.",
        ">vv.>>.v>v",
        ">>.>..v>.>",
        "..v>v...v.",
        "..>>.>vv..",
        ">.v.vv>v.v",
        ".....>>vv.",
        "vvv>...v..",
    ]
    expected = [
        "vv>...>v>.",
        "v.v.v>.>v.",
        ">.v.>.>.>v",
        ">v>.>..v>>",
        "..v>v.v...",
        "..>.>>vvv.",
        ".>...v>v..",
        "..v.v>>v.v",
        "v.v.>...v.",
    ], True
    actual = step(lines)
    assert actual == expected


def test_step_sample2_step10():
    lines = [
        "v...>>.vv>",
        ".vv>>.vv..",
        ">>.>v>...v",
        ">>v>>.>.v.",
        "v>v.vv.v..",
        ">.>>..v...",
        ".vv..>.>v.",
        "v.v..>>v.v",
        "....v..v.>",
    ]
    expected = [
        "..>..>>vv.",
        "v.....>>.v",
        "..v.v>>>v>",
        "v>.>v.>>>.",
        "..v>v.vv.v",
        ".v.>>>.v..",
        "v.v..>v>..",
        "..v...>v.>",
        ".vv..v>vv.",
    ], True
    actual = lines, None
    for _ in range(10):
        actual = step(actual[0])
    assert actual == expected


def test_step_sample2_step20():
    lines = [
        "v...>>.vv>",
        ".vv>>.vv..",
        ">>.>v>...v",
        ">>v>>.>.v.",
        "v>v.vv.v..",
        ">.>>..v...",
        ".vv..>.>v.",
        "v.v..>>v.v",
        "....v..v.>",
    ]
    expected = [
        "v>.....>>.",
        ">vv>.....v",
        ".>v>v.vv>>",
        "v>>>v.>v.>",
        "....vv>v..",
        ".v.>>>vvv.",
        "..v..>>vv.",
        "v.v...>>.v",
        "..v.....v>",
    ], True
    actual = lines, None
    for _ in range(20):
        actual = step(actual[0])
    assert actual == expected


def test_step_sample2_step30():
    lines = [
        "v...>>.vv>",
        ".vv>>.vv..",
        ">>.>v>...v",
        ">>v>>.>.v.",
        "v>v.vv.v..",
        ">.>>..v...",
        ".vv..>.>v.",
        "v.v..>>v.v",
        "....v..v.>",
    ]
    expected = [
        ".vv.v..>>>",
        "v>...v...>",
        ">.v>.>vv.>",
        ">v>.>.>v.>",
        ".>..v.vv..",
        "..v>..>>v.",
        "....v>..>v",
        "v.v...>vv>",
        "v.v...>vvv",
    ], True
    actual = lines, None
    for _ in range(30):
        actual = step(actual[0])
    assert actual == expected


def test_step_sample2_step40():
    lines = [
        "v...>>.vv>",
        ".vv>>.vv..",
        ">>.>v>...v",
        ">>v>>.>.v.",
        "v>v.vv.v..",
        ">.>>..v...",
        ".vv..>.>v.",
        "v.v..>>v.v",
        "....v..v.>",
    ]
    expected = [
        ">>v>v..v..",
        "..>>v..vv.",
        "..>>>v.>.v",
        "..>>>>vvv>",
        "v.....>...",
        "v.v...>v>>",
        ">vv.....v>",
        ".>v...v.>v",
        "vvv.v..v.>",
    ], True
    actual = lines, None
    for _ in range(40):
        actual = step(actual[0])
    assert actual == expected


def test_step_sample2_step50():
    lines = [
        "v...>>.vv>",
        ".vv>>.vv..",
        ">>.>v>...v",
        ">>v>>.>.v.",
        "v>v.vv.v..",
        ">.>>..v...",
        ".vv..>.>v.",
        "v.v..>>v.v",
        "....v..v.>",
    ]
    expected = [
        "..>>v>vv.v",
        "..v.>>vv..",
        "v.>>v>>v..",
        "..>>>>>vv.",
        "vvv....>vv",
        "..v....>>>",
        "v>.......>",
        ".vv>....v>",
        ".>v.vv.v..",
    ], True
    actual = lines, None
    for _ in range(50):
        actual = step(actual[0])
    assert actual == expected


def test_step_sample2_step55():
    lines = [
        "v...>>.vv>",
        ".vv>>.vv..",
        ">>.>v>...v",
        ">>v>>.>.v.",
        "v>v.vv.v..",
        ">.>>..v...",
        ".vv..>.>v.",
        "v.v..>>v.v",
        "....v..v.>",
    ]
    expected = [
        "..>>v>vv..",
        "..v.>>vv..",
        "..>>v>>vv.",
        "..>>>>>vv.",
        "v......>vv",
        "v>v....>>v",
        "vvv...>..>",
        ">vv.....>.",
        ".>v.vv.v..",
    ], True
    actual = lines, None
    for _ in range(55):
        actual = step(actual[0])
    assert actual == expected


def test_step_sample2_step56():
    lines = [
        "v...>>.vv>",
        ".vv>>.vv..",
        ">>.>v>...v",
        ">>v>>.>.v.",
        "v>v.vv.v..",
        ">.>>..v...",
        ".vv..>.>v.",
        "v.v..>>v.v",
        "....v..v.>",
    ]
    expected = [
        "..>>v>vv..",
        "..v.>>vv..",
        "..>>v>>vv.",
        "..>>>>>vv.",
        "v......>vv",
        "v>v....>>v",
        "vvv....>.>",
        ">vv......>",
        ".>v.vv.v..",
    ], True
    actual = lines, None
    for _ in range(56):
        actual = step(actual[0])
    assert actual == expected


def test_step_sample2_step57():
    lines = [
        "v...>>.vv>",
        ".vv>>.vv..",
        ">>.>v>...v",
        ">>v>>.>.v.",
        "v>v.vv.v..",
        ">.>>..v...",
        ".vv..>.>v.",
        "v.v..>>v.v",
        "....v..v.>",
    ]
    expected = [
        "..>>v>vv..",
        "..v.>>vv..",
        "..>>v>>vv.",
        "..>>>>>vv.",
        "v......>vv",
        "v>v....>>v",
        "vvv.....>>",
        ">vv......>",
        ".>v.vv.v..",
    ], True
    actual = lines, None
    for _ in range(57):
        actual = step(actual[0])
    assert actual == expected


def test_step_sample2_step58():
    lines = [
        "v...>>.vv>",
        ".vv>>.vv..",
        ">>.>v>...v",
        ">>v>>.>.v.",
        "v>v.vv.v..",
        ">.>>..v...",
        ".vv..>.>v.",
        "v.v..>>v.v",
        "....v..v.>",
    ]
    expected = [
        "..>>v>vv..",
        "..v.>>vv..",
        "..>>v>>vv.",
        "..>>>>>vv.",
        "v......>vv",
        "v>v....>>v",
        "vvv.....>>",
        ">vv......>",
        ".>v.vv.v..",
    ], False
    actual = lines, None
    for _ in range(58):
        actual = step(actual[0])
    assert actual == expected


def test_compute_answer_sample():
    lines = [
        "v...>>.vv>",
        ".vv>>.vv..",
        ">>.>v>...v",
        ">>v>>.>.v.",
        "v>v.vv.v..",
        ">.>>..v...",
        ".vv..>.>v.",
        "v.v..>>v.v",
        "....v..v.>",
    ]
    expected = 58
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 380
    actual = compute_answer(lines)
    assert actual == expected
