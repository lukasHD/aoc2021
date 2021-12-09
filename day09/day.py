import os
from collections import defaultdict
from dataclasses import dataclass

import helper


@dataclass
class Point:
    """"Class for a simple 2D position-State"""
    x: int = 0
    y: int = 0

    def __str__(self) -> str:
        return "[{:>3},{:>3}]".format(self.x, self.y)

    def __hash__(self) -> int:
        return hash((self.x, self.y))

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

def get_min_lower_neighbor_point(data, point :Point):
    minNeighbor = Point()
    minValue = 10
    pointValue = data[point.x][point.y]
    for delta in [Point(1,0), Point(-1,0), Point(0,1), Point(0,-1)]:
        try:
            px = point.x + delta.x
            py = point.y + delta.y
            if px < 0 or py < 0:
                continue
            if data[px][py] < minValue:
                minNeighbor = Point(px,py)
                minValue = data[px][py]
        except IndexError:
            continue
    # print("minValue={}, pointValue={}".format(minValue, pointValue))
    if minValue < pointValue:
        return minNeighbor
    return None

def flow_down(data, point: Point):
    print(point, end=" ")
    next_point = get_min_lower_neighbor_point(data, point)
    if next_point == None:
        return point
    return flow_down(data, next_point)

def pretty(data):
    for line in data:
        for element in line:
            print(element, end="")
        print()

def alg1(data, printDebug):
    result = 0
    floormap = parse_line(data=data)
    if printDebug: pretty(floormap)
    for x, line in enumerate(floormap):
        for y, el in enumerate(line):
            neighbours = get_straight_neighbours(floormap, Point(x,y))
            print(neighbours)
            is_minimum = all([el < x for x in neighbours])
            if is_minimum:
                result += (el + 1)
    return result


def alg2(data, printDebug):
    """FLow down until we are in a minimum and then add point to size of bassin
    Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.
    """
    basins = defaultdict(int)
    floormap = parse_line(data=data)
    if printDebug: pretty(floormap)
    for x, line in enumerate(floormap):
        for y, el in enumerate(line):
            if el == 9:
                continue
            basin_point = flow_down(floormap, Point(x,y))
            print("{} --> {}".format(Point(x,y), basin_point))
            basins[basin_point] += 1

    result = 1
    basin_sizes = basins.values()
    print(basin_sizes)
    for n in list(sorted(basin_sizes))[-3:]:
        print(n)
        result *= n
    return result


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
    # part1(test_fname, True)
    # part1(input_fname)
    part2(test_fname, True)
    part2(input_fname)
