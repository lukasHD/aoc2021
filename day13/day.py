# -*- coding: utf-8 -*-
"""Example Google style docstrings.
"""

import os
from collections import defaultdict
from dataclasses import dataclass

import helper


def parse_data(data, print_debug):
    # count the number of holes lining up
    paper_coordinates = defaultdict(int)
    instuctions = []
    for line in data:
        if "," in line:
            x,y = line.split(",")
            x = int(x)
            y = int(y)
            paper_coordinates[(x,y)] += 1
        if "fold along" in line:
            axis, pos = line.strip("fold along ").split("=")
            instuctions.append([axis, int(pos)])
    if print_debug: print(f"paper_coordinates={paper_coordinates}\n\ninstuctions={instuctions}\n")
    return paper_coordinates, instuctions


def fold_paper(dir: str, pos: int):
    print(f"Try to fold along {dir}={pos}")


def alg1(data, print_debug):
    paper_coordinates, instuctions = parse_data(data, print_debug)
    inst = instuctions[0]
    fold_paper(inst[0], inst[1])
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

    print("\n")
    part1(test_fname, True)
    # part1(input_fname)
    # part2(test_fname, True)
    # part2(input_fname)
