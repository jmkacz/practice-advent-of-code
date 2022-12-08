"""TODO"""
from part1 import Node, NodeType, compute_answer, get_size, parse

SAMPLE_DATA = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""".splitlines()


def test_parse():
    """TODO"""
    expected = Node(
        "/",
        NodeType.DIRECTORY,
        0,
        [
            Node(
                "a",
                NodeType.DIRECTORY,
                0,
                [
                    Node(
                        "e",
                        NodeType.DIRECTORY,
                        0,
                        [
                            Node("i", NodeType.FILE, 584, []),
                        ],
                    ),
                    Node("f", NodeType.FILE, 29116, []),
                    Node("g", NodeType.FILE, 2557, []),
                    Node("h.lst", NodeType.FILE, 62596, []),
                ],
            ),
            Node("b.txt", NodeType.FILE, 14848514, []),
            Node("c.dat", NodeType.FILE, 8504156, []),
            Node(
                "d",
                NodeType.DIRECTORY,
                0,
                [
                    Node("j", NodeType.FILE, 4060174, []),
                    Node("d.log", NodeType.FILE, 8033020, []),
                    Node("d.ext", NodeType.FILE, 5626152, []),
                    Node("k", NodeType.FILE, 7214296, []),
                ],
            ),
        ],
    )
    actual = parse(SAMPLE_DATA)
    assert actual == expected


def test_get_size():
    """TODO"""
    root = parse(SAMPLE_DATA)
    expected = 48381165
    actual = get_size(root)
    assert actual == expected


def test_compute_answer_sample():
    """TODO"""
    expected = 95437
    actual = compute_answer(SAMPLE_DATA)
    assert actual == expected


def test_compute_answer_full():
    """TODO"""
    with open("../data/input.dat", "r", encoding="utf-8") as infile:
        lines = [line.strip() for line in infile.readlines()]

    expected = 1297159
    actual = compute_answer(lines)
    assert actual == expected
