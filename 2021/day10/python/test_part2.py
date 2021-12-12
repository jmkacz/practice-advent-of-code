from part2 import calculate_score, compute_answer


def test_calculate_score_1():
    # Complete by adding }}]])})]
    line = "[({(<(())[]>[[{[]{<()<>>"
    expected = 288957
    actual = calculate_score(line)
    assert actual == expected


def test_calculate_score_2():
    # Complete by adding )}>]})
    line = "[(()[<>])]({[<{<<[]>>("
    expected = 5566
    actual = calculate_score(line)
    assert actual == expected


def test_calculate_score_3():
    # Complete by adding }}>}>))))
    line = "(((({<>}<{<{<>}{[]{[]{}"
    expected = 1480781
    actual = calculate_score(line)
    assert actual == expected


def test_calculate_score_4():
    # Complete by adding ]]}}]}]}>
    line = "{<[[]]>}<{[{[{[]{()[[[]"
    expected = 995444
    actual = calculate_score(line)
    assert actual == expected


def test_calculate_score_5():
    # Complete by adding ])}>
    line = "<{([{{}}[<[[[<>{}]]]>[]]"
    expected = 294
    actual = calculate_score(line)
    assert actual == expected


def test_compute_answer_sample():
    lines = [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]",
    ]
    expected = 288957
    actual = compute_answer(lines)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 3404870164
    actual = compute_answer(lines)
    assert actual == expected
