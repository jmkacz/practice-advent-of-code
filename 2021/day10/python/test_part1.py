from part1 import compute_answer, is_corrupted


def test_not_is_corrupted_1():
    line = "()"
    expected = False
    actual, _, _ = is_corrupted(line)
    assert actual == expected


def test_not_is_corrupted_2():
    line = "[]"
    expected = False
    actual, _, _ = is_corrupted(line)
    assert actual == expected


def test_not_is_corrupted_3():
    line = "([])"
    expected = False
    actual, _, _ = is_corrupted(line)
    assert actual == expected


def test_not_is_corrupted_4():
    line = "{()()()}"
    expected = False
    actual, _, _ = is_corrupted(line)
    assert actual == expected


def test_not_is_corrupted_5():
    line = "<([{}])>"
    expected = False
    actual, _, _ = is_corrupted(line)
    assert actual == expected


def test_not_is_corrupted_6():
    line = "[<>({}){}[([])<>]]"
    expected = False
    actual, _, _ = is_corrupted(line)
    assert actual == expected


def test_not_is_corrupted_7():
    line = "(((((((((())))))))))"
    expected = False
    actual, _, _ = is_corrupted(line)
    assert actual == expected


def test_is_corrupted_1():
    line = "(]"
    expected = True
    actual, _, _ = is_corrupted(line)
    assert actual == expected


def test_is_corrupted_2():
    line = "{()()()>"
    expected = True
    actual, _, _ = is_corrupted(line)
    assert actual == expected


def test_is_corrupted_3():
    line = "(((()))}"
    expected = True
    actual, _, _ = is_corrupted(line)
    assert actual == expected


def test_is_corrupted_4():
    line = "<([]){()}[{}])"
    expected = True
    actual, _, _ = is_corrupted(line)
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
    # {([(<{}[<>[]}>{[]{[(<()> - Expected ], but found } instead.
    # [[<[([]))<([[{}[[()]]]   - Expected ], but found ) instead.
    # [{[{({}]{}}([{[{{{}}([]  - Expected ), but found ] instead.
    # [<(<(<(<{}))><([]([]()   - Expected >, but found ) instead.
    # <{([([[(<>()){}]>(<<{{   - Expected ], but found > instead.
    expected = [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "(((({<>}<{<{<>}{[]{[]{}",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "<{([{{}}[<[[[<>{}]]]>[]]",
    ]
    expected_score = 26397
    actual, actual_score = compute_answer(lines)
    assert actual == expected
    assert actual_score == expected_score


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected_score = 266301
    _, actual_score = compute_answer(lines)
    assert actual_score == expected_score
