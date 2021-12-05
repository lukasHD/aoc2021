import os
from collections import defaultdict
from dataclasses import dataclass
from typing import DefaultDict
from collections import Counter

import helper

def sign(x):
    s = 0
    if x > 0:
        s = 1
    elif x < 0:
        s = -1
    return s

@dataclass
class Point:
    x: int
    y: int

    def __init__(self, in_list) -> None:
        if len(in_list) == 2:
            self.x = in_list[0]
            self.y = in_list[1]

    def __hash__(self):
        return hash(tuple((self.x, self.y)))
    
    def as_tuple(self):
        return tuple((self.x, self.y))

def parse_line(data):
    for line in data:
        start, stop = line.split(" -> ")[0:2]
        # print("{}     {}".format(start, stop))
        start_p = Point([int(x) for x in start.split(",")])
        stop_p  = Point([int(x) for x in stop.split(",")])
        # print("{}     {}".format(start_p, stop_p))
        yield start_p, stop_p
        

def get_straight(start, stop, no_diagonals = False, printDebug = False):
    current_pos = start
    # normalize directions to one
    delta_x = sign(stop.x - start.x)
    delta_y = sign(stop.y - start.y)
    # print("{}     {}".format(start, stop))
    # print("delta_x = {}, delta_y  = {}".format(delta_x, delta_y))
    if no_diagonals and delta_x != 0 and delta_y != 0:
        # print("NO DIAGONALS I SAID!")
        return None
    if printDebug: print("Vent: {} --> {}".format(start, stop))
    yield current_pos
    while current_pos != stop:
        current_pos.x += delta_x
        current_pos.y += delta_y
        # print(current_pos)
        yield current_pos

def alg1(data, printDebug):
    coordinates = defaultdict(int)
    for start, stop in parse_line(data):
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for current in get_straight(start, stop, no_diagonals=True, printDebug = printDebug):
            # print(current)
            coordinates[current.as_tuple()] += 1
    if printDebug: print(coordinates.values())
    counted = list(filter(lambda c: c > 1, coordinates.values()))
    if printDebug: print(counted)
    return len(counted)


def alg2(data, printDebug):
    coordinates = defaultdict(int)
    for start, stop in parse_line(data):
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for current in get_straight(start, stop, no_diagonals=False, printDebug = printDebug):
            # print(current)
            coordinates[current.as_tuple()] += 1
    if printDebug: print(coordinates.values())
    counted = list(filter(lambda c: c > 1, coordinates.values()))
    if printDebug: print(counted)
    return len(counted)


def part1(fname: str, printDebug = False):
    print("=== PART 1 ===")
    print("-- {} --".format(fname))
    result = 0
    result = alg1(helper.input_as_lines(fname), printDebug)
    print("Result = {}".format(result))
    print()

def part2(fname: str, printDebug = False):
    print("=== PART 2 ===")
    print("-- {} --".format(fname))
    result = 0
    result = alg2(helper.input_as_lines(fname), printDebug)
    print("Result = {}".format(result))
    print()
    

if __name__ == '__main__':
    test_fname = os.path.join(os.path.dirname(__file__), 'test.txt')
    input_fname = os.path.join(os.path.dirname(__file__), 'input.txt')
    print("--- Day 5: Hydrothermal Venture ---\n")
    part1(test_fname, True)
    part1(input_fname)
    part2(test_fname, True)
    part2(input_fname)
