import helper
from dataclasses import dataclass

@dataclass
class SimplePosition:
    """"Class for a simple 2D position-State"""
    horizontal: int = 0
    depth: int = 0

    def result(self) -> int:
        return self.horizontal * self.depth

    def __str__(self) -> str:
        return "[{},\t{}]".format(self.horizontal, self.depth)


@dataclass
class StateVector(SimplePosition):
    aim: int = 0

    def __str__(self) -> str:
        return "[{},\t{},\t{}]".format(self.horizontal, self.depth, self.aim)


def final_position(instructions, printDebug):
    position = SimplePosition(0,0)
    if printDebug: print(position)
    for line in instructions:
        inst_array = line.split(" ")
        direction = inst_array[0]
        amplitude = int(inst_array[1])
        if printDebug: print(direction, amplitude)
        if direction == "forward":
            position.horizontal += amplitude
        if direction == "up": 
            position.depth -= amplitude
        if direction == "down":
            position.depth += amplitude
        if printDebug: print(position)
    return position.result()

def final_position_2(instructions, printDebug):
    state = StateVector()
    if printDebug: print(state)
    for line in instructions:
        inst_array = line.split(" ")
        direction = inst_array[0]
        amplitude = int(inst_array[1])
        if printDebug: print(direction, amplitude)
        if direction == "forward":
            state.horizontal += amplitude
            state.depth += amplitude * state.aim
        if direction == "up": 
            state.aim -= amplitude
        if direction == "down":
            state.aim += amplitude
        if printDebug: print(state)
    return state.result()

def part1(fname: str, printDebug = False):
    print("=== PART 1 ===")
    print("-- {} --".format(fname))
    result = 0
    result = final_position(helper.input_as_lines(fname), printDebug)
    print("Result = {}".format(result))
    print()

def part2(fname: str, printDebug = False):
    print("=== PART 2 ===")
    print("-- {} --".format(fname))
    result = 0
    result = final_position_2(helper.input_as_lines(fname), printDebug)
    print("Result = {}".format(result))
    print()
    

if __name__ == '__main__':
    print("--- Day 2: Dive! ---\n")
    part1("day02/test.txt", True)
    part1("day02/input.txt")
    part2("day02/test.txt", True)
    part2("day02/input.txt")
