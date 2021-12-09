import os
from dataclasses import dataclass

import helper


@dataclass
class Point:
    """"Class for a simple 2D position-State"""
    x: int = 0
    y: int = 0

    def __str__(self) -> str:
        return "[{},\t{}]".format(self.x, self.y)

def parse_line(data):
    formated = []
    for line in data:
        formated.append(list(map(int,list(line))))
    print(type(formated[0][0]))
    return formated

def get_straight_neighbours(data, point: Point):
    neighbours = []
    for delta in [Point(1,0), Point(-1,0), Point(0,1), Point(0,-1)]:
        try:
            px = point.x + delta.x
            py = point.y + delta.y
            if px < 0 or py < 0:
                continue
            neighbours.append(data[px][py])
        except IndexError:
            continue
    return neighbours

def pretty(data):
    for line in data:
        for element in line:
            print(element, end="")
        print()

def alg1(data, printDebug):
    result = 0
    floormap = parse_line(data=data)
    pretty(floormap)
    for x, line in enumerate(floormap):
        for y, el in enumerate(line):
            neighbours = get_straight_neighbours(floormap, Point(x,y))
            print(neighbours)
            is_minimum = all([el < x for x in neighbours])
            if is_minimum:
                result += (el + 1)
    return result


def alg2(data, printDebug):
    return 0


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

    print("--- Day 9: Smoke Basin ---\n")
    part1(test_fname, True)
    part1(input_fname)
    # part2(test_fname, True)
    # part2(input_fname)
