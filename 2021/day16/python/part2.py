import math
from typing import List, Tuple

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


def process(transmission: str, offset: int) -> Tuple[int, List[int]]:
    version = btoi(transmission[offset : offset + 3])
    print("version", version)  # XXX
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
        data = [value]

    else:
        length_type_id = btoi(transmission[offset : offset + 1])
        print("length_type_id", length_type_id)  # XXX
        offset += 1

        match length_type_id:
            case 0:
                # total length in bits of the sub-packets contained by this packet.
                length = btoi(transmission[offset : offset + 15])
                offset += 15
                print("length", length)  # XXX
                target = offset + length
                data = []
                while offset < target:
                    offset, datum = process(transmission, offset)
                    data += datum
            case 1:
                # number of sub-packets immediately contained by this packet.
                subpackets = btoi(transmission[offset : offset + 11])
                offset += 11
                print("subpackets", subpackets)  # XXX
                data = []
                for _ in range(subpackets):
                    offset, datum = process(transmission, offset)
                    data += datum

        match type_id:
            case 0:
                data = [sum(data)]
            case 1:
                data = [math.prod(data)]
            case 2:
                data = [min(data)]
            case 3:
                data = [max(data)]
            case 5:
                data = [1 if data[0] > data[1] else 0]
            case 6:
                data = [1 if data[0] < data[1] else 0]
            case 7:
                data = [1 if data[0] == data[1] else 0]

    return offset, data


def compute_answer(lines: List[str]) -> int:
    transmission = parse(lines)
    print("transmission", transmission)  # XXX
    offset, data = process(transmission, 0)
    print("remaining", transmission[offset:])  # XXX
    assert "1" not in transmission[offset:]
    return sum(data)
