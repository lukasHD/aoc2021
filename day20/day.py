# -*- coding: utf-8 -*-
"""Example Google style docstrings.
"""

import os

import helper

from collections import defaultdict
from dataclasses import dataclass

@dataclass
class Point():
    x: int
    y: int

    def as_tuple(self):
        return (self.x, self.y)

class TrenchMap():

    translate = {'#': 1, '.': 0, 1: '#', 0: '.'}

    def __init__(self, algo_array, map_array) -> None:
        self.algo = algo_array
        self.map = defaultdict(int)
        self.min_x = 0
        self.min_y = 0
        self.max_x = 0
        self.max_y = 0
        for x, line in enumerate(map_array):
            for y, char in enumerate(line):
                self.min_x = min(self.min_x, x)
                self.min_y = min(self.min_y, y)
                self.max_x = max(self.max_x, x)
                self.max_y = max(self.max_y, y)
                self.map[(x,y)] = self.translate[char]

    def pretty(self) -> None:
        for x in range(self.min_x - 2, self.max_x + 3):
            for y in range(self.min_y - 2, self.max_y + 3):
                print(self.translate[self.map[(x,y)]], end="")
            print()
        print()

    def step(self) -> None:
        new_array = defaultdict(int)
        for x in range(self.min_x - 1, self.max_x + 2):
            for y in range(self.min_y - 1, self.max_y + 2):
                # all neighbours
                # build bit string
                bitstring = ""
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        bitstring += str(self.map[(x+dx, y+dy)])
                new_array[(x, y)] = self.translate[self.algo[int(bitstring, 2)]]
                print(bitstring)
                print(new_array)
                




def alg1(data, print_debug):
    trench_map = TrenchMap(data[0], data[2:])
    trench_map.pretty()
    trench_map.step()
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

    print("--- Day 20: Trench Map ---\n")
    part1(test_fname, True)
    # part1(input_fname)
    # part2(test_fname, True)
    # part2(input_fname)
