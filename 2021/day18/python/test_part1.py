from part1 import (
    add,
    compute_answer,
    compute_magnitude,
    parse,
    play,
    reduce,
    reduce_step,
)


def test_explode_1():
    number = parse(["[[[[[9,8],1],2],3],4]"])[0]
    expected = "[[[[0,9],2],3],4]"
    action, new_number = reduce_step(number)
    assert action == "explode"
    actual = "".join(new_number)
    assert actual == expected


def test_explode_2():
    number = parse(["[7,[6,[5,[4,[3,2]]]]]"])[0]
    expected = "[7,[6,[5,[7,0]]]]"
    action, new_number = reduce_step(number)
    assert action == "explode"
    actual = "".join(new_number)
    assert actual == expected


def test_explode_3():
    number = parse(["[[6,[5,[4,[3,2]]]],1]"])[0]
    expected = "[[6,[5,[7,0]]],3]"
    action, new_number = reduce_step(number)
    assert action == "explode"
    actual = "".join(new_number)
    assert actual == expected


def test_explode_4():
    number = parse(["[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"])[0]
    expected = "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"
    action, new_number = reduce_step(number)
    assert action == "explode"
    actual = "".join(new_number)
    assert actual == expected


def test_explode_5():
    number = parse(["[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"])[0]
    expected = "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"
    action, new_number = reduce_step(number)
    assert action == "explode"
    actual = "".join(new_number)
    assert actual == expected


def test_split_1():
    number = ["[", "10", ",", "1", "]"]
    expected = "[[5,5],1]"
    action, new_number = reduce_step(number)
    assert action == "split"
    actual = "".join(new_number)
    assert actual == expected


def test_split_2():
    number = ["[", "2", ",", "11", "]"]
    expected = "[2,[5,6]]"
    action, new_number = reduce_step(number)
    assert action == "split"
    actual = "".join(new_number)
    assert actual == expected


def test_add():
    lines = ["[[[[4,3],4],4],[7,[[8,4],9]]]", "[1,1]"]
    numbers = parse(lines)
    actual = "".join(add(numbers[0], numbers[1]))
    expected = "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
    assert actual == expected


def test_reduce():
    numbers = parse(["[[[[4,3],4],4],[7,[[8,4],9]]]", "[1,1]"])
    expected = "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"
    actual = "".join(reduce(add(*numbers)))
    assert actual == expected


def test_play_1():
    lines = [
        "[1,1]",
        "[2,2]",
        "[3,3]",
        "[4,4]",
    ]
    expected = "[[[[1,1],[2,2]],[3,3]],[4,4]]"
    actual = "".join(play(lines))
    assert actual == expected


def test_play_2():
    lines = [
        "[1,1]",
        "[2,2]",
        "[3,3]",
        "[4,4]",
        "[5,5]",
    ]
    expected = "[[[[3,0],[5,3]],[4,4]],[5,5]]"
    actual = "".join(play(lines))
    assert actual == expected


def test_play_3():
    lines = [
        "[1,1]",
        "[2,2]",
        "[3,3]",
        "[4,4]",
        "[5,5]",
        "[6,6]",
    ]
    expected = "[[[[5,0],[7,4]],[5,5]],[6,6]]"
    actual = "".join(play(lines))
    assert actual == expected


def test_play_4():
    lines = [
        "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]",
        "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]",
        "[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]",
        "[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]",
        "[7,[5,[[3,8],[1,4]]]]",
        "[[2,[2,2]],[8,[8,1]]]",
        "[2,9]",
        "[1,[[[9,3],9],[[9,0],[0,7]]]]",
        "[[[5,[7,4]],7],1]",
        "[[[[4,2],2],6],[8,7]]",
    ]
    expected = "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"
    actual = "".join(play(lines))
    assert actual == expected


def test_compute_magnitude_1():
    number = "[9,1]"
    expected = 29
    actual = compute_magnitude(number)
    assert actual == expected


def test_compute_magnitude_2():
    number = "[1,9]"
    expected = 21
    actual = compute_magnitude(number)
    assert actual == expected


def test_compute_magnitude_3():
    number = "[[9,1],[1,9]]"
    expected = 129
    actual = compute_magnitude(number)
    assert actual == expected


def test_compute_magnitude_4():
    number = "[[1,2],[[3,4],5]]"
    expected = 143
    actual = compute_magnitude(number)
    assert actual == expected


def test_compute_magnitude_5():
    number = "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"
    expected = 1384
    actual = compute_magnitude(number)
    assert actual == expected


def test_compute_magnitude_6():
    number = "[[[[1,1],[2,2]],[3,3]],[4,4]]"
    expected = 445
    actual = compute_magnitude(number)
    assert actual == expected


def test_compute_magnitude_7():
    number = "[[[[3,0],[5,3]],[4,4]],[5,5]]"
    expected = 791
    actual = compute_magnitude(number)
    assert actual == expected


def test_compute_magnitude_8():
    number = "[[[[5,0],[7,4]],[5,5]],[6,6]]"
    expected = 1137
    actual = compute_magnitude(number)
    assert actual == expected


def test_compute_magnitude_9():
    number = "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"
    expected = 3488
    actual = compute_magnitude(number)
    assert actual == expected


def test_compute_answer_full():
    with open("../data/input.dat", "r") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 4365
    actual = compute_answer(lines)
    assert actual == expected
