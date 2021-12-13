from pprint import pprint
from typing import Dict, List, Union


class Circuit:
    def __init__(self, wires):
        self.wires: Dict[str, List[str]] = wires

    def debug(self):
        pprint(self.wires)

    def get_value(self, instruction: List[str]) -> int:
        compute_value = lambda x: int(x) if x.isdigit() else self.process(x)

        if "AND" in instruction:
            return compute_value(instruction[0]) & compute_value(instruction[2])
        elif "OR" in instruction:
            return compute_value(instruction[0]) | compute_value(instruction[2])
        elif "LSHIFT" in instruction:
            return compute_value(instruction[0]) << compute_value(instruction[2])
        elif "RSHIFT" in instruction:
            return compute_value(instruction[0]) >> compute_value(instruction[2])
        elif "NOT" in instruction:
            return ((2 << 15) - 1) ^ compute_value(instruction[1])
        else:
            return compute_value(instruction[0])

    def process(self, wire: str) -> int:
        result = self.get_value(self.wires[wire])
        self.wires[wire] = [str(result)]
        # self.debug()
        return result


def parse(lines: List[str]) -> Dict[str, List[str]]:
    result = {}
    for line in lines:
        instruction, wire = line.split(" -> ")
        result[wire] = instruction.split(" ")
    return result


def compute_answer(lines: List[str], wire: str) -> int:
    circuit = Circuit(parse(lines))
    return circuit.process(wire)
