"""
Ex. version = 6, type_id = 4 (literal value)
D2FE28
  6   4     7    14     5
110 100 10111 11110 00101 000
VVV TTT AAAAA BBBBB CCCCC
(7*16*16 + 14*16 + 5*1 = 2021)


Ex. version = 1, type_id = 6 (operator), length_type_id = 0, length = 27
38006F45291200
  1   6 0              27
001 110 0 000000000011011 1101000101001010010001001000000000
VVV TTT I LLLLLLLLLLLLLLL
  6   4    10
110 100 01010 01010010001001000000000
VVV TTT AAAAA
(10*1 = 10)
  2   4     1     4
010 100 10001 00100 0000000
VVV TTT AAAAA BBBBB
(1*16 + 4*1 = 20)


Ex. version = 7, type_id = 3 (operator), length_type_id = 1, subpackets = 3
EE00D40C823060
  7   3 1           3
111 011 1 00000000011 01010000001100100000100011000001100000
VVV TTT I LLLLLLLLLLL 
  2   4     1
010 100 00001 100100000100011000001100000
VVV TTT AAAAA
(1*1 = 1)
  4   4     2
100 100 00010 0011000001100000
VVV TTT BBBBB
(2*1 = 2)
  1   4     3
001 100 00011 00000
VVV TTT BBBBB
(3*1 = 3)
"""
from typing import List

HEX2BIN = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def parse(lines: List[str]) -> str:
    return "".join([HEX2BIN[_] for _ in lines[0]])


def btoi(bitstring: str) -> int:
    result = 0
    for char in bitstring:
        result *= 2
        if char == "1":
            result += 1
    return result


def process(transmission: str, offset: int, data: List[int]) -> int:
    version = btoi(transmission[offset : offset + 3])
    print("version", version)  # XXX
    data.append(version)
    offset += 3

    type_id = btoi(transmission[offset : offset + 3])
    print("type_id", type_id)  # XXX
    offset += 3

    if type_id == 4:
        # literal value
        value = 0
        while True:
            terminal = transmission[offset] == "0"
            value = (value << 4) + btoi(transmission[offset + 1 : offset + 5])
            offset += 5
            if terminal:
                break
        print("value", value)  # XXX

    else:
        length_type_id = btoi(transmission[offset : offset + 1])
        print("length_type_id", length_type_id)  # XXX
        offset += 1

        if length_type_id == 0:
            # total length in bits of the sub-packets contained by this packet.
            length = btoi(transmission[offset : offset + 15])
            offset += 15
            print("length", length)  # XXX
            target = offset + length
            while offset < target:
                offset = process(transmission, offset, data)

        if length_type_id == 1:
            # number of sub-packets immediately contained by this packet.
            subpackets = btoi(transmission[offset : offset + 11])
            offset += 11
            print("subpackets", subpackets)  # XXX
            for _ in range(subpackets):
                offset = process(transmission, offset, data)

    return offset


def compute_answer(lines: List[str]) -> int:
    transmission = parse(lines)
    print("transmission", transmission)  # XXX
    data: List[int] = []
    offset = process(transmission, 0, data)
    print("remaining", transmission[offset:])  # XXX
    assert "1" not in transmission[offset:]
    return sum(data)
