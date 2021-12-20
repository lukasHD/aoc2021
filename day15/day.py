# -*- coding: utf-8 -*-
"""Example Google style docstrings.
"""

import os
from queue import PriorityQueue

import helper


def manhattan_distance(a, b) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def parse_grid(data):
    return [[int(x) for x in line] for line in data]


# inspiration from here ? https://github.com/Farbfetzen/Advent_of_Code/blob/main/python/2021/day15.py
def find_lowest_risk(cave_map):
    """Pathfinding using A*"""
    start = (0, 0)
    destination = (len(cave_map[0]) - 1, len(cave_map) - 1)
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {start: None}
    risk_so_far = {start: 0}
    offsets = ((1, 0), (0, 1), (-1, 0), (0, -1))
    pos = None
    while not frontier.empty():
        pos = frontier.get()[1]
        if pos == destination:
            break
        for offset in offsets:
            new_pos = (pos[0] + offset[0], pos[0] + offset[0])
            # check if in bounds
            if 0 <= new_pos[0] < len(cave_map[0]) and 0 <= new_pos[1] < len(cave_map):
                new_risk = risk_so_far[pos] + cave_map[new_pos[1]][new_pos[0]]
                # skip the way back and also skip worse risk steps ????????
                if new_pos not in came_from or new_risk < risk_so_far[new_pos]:
                    risk_so_far[new_pos] = new_risk
                    priority = new_risk + manhattan_distance(new_pos, destination)
                    frontier.put((priority, new_pos))
                    came_from[new_pos] = pos
    return risk_so_far[pos]

def pretty(array):
    for line in array:
        for char in line:
            print(char, end="")
        print()
    print()

def alg1(data, print_debug):
    array = parse_grid(data)
    pretty(array)
    return 0


def alg2(data, print_debug):
    return 0


def part1(fname: str, print_debug = False):
    print("=== PART 1 ===")
    print(f"-- {fname} --")
    result = 0
    result = alg1(helper.input_as_lines(fname), print_debug)
    print(f"Result = {result}")
    print()

def part2(fname: str, print_debug = False):
    print("=== PART 2 ===")
    print(f"-- {fname} --")
    result = 0
    result = alg2(helper.input_as_lines(fname), print_debug)
    print(f"Result = {result}")
    print()


if __name__ == '__main__':
    test_fname = os.path.join(os.path.dirname(__file__), 'test.txt')
    input_fname = os.path.join(os.path.dirname(__file__), 'input.txt')

    print("--- Day 15: Chiton ---\n")
    part1(test_fname, True)
    # part1(input_fname)
    # part2(test_fname, True)
    # part2(input_fname)
