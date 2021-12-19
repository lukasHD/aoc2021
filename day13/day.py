# -*- coding: utf-8 -*-
"""Example Google style docstrings.
"""

import os
from collections import defaultdict
from dataclasses import dataclass
from copy import deepcopy

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


def fold_paper(in_dict: dict[(int, int),int], dir: str, pos: int):
    print(f"Try to fold along {dir}={pos}")
    new_coordinates = defaultdict(int)
    for coord in in_dict.keys():
        if dir == 'y':
            # fold up along the line
            new_coord = coord[1]
            if coord[1] > pos:
                new_coord = pos - (coord[1] - pos)
            new_coordinates[(coord[0], new_coord)] += in_dict[coord]
        elif dir == 'x':
            # fold left on the line 
            new_coord = coord[0]
            if coord[0] > pos:
                new_coord = pos - (coord[0] - pos)
            new_coordinates[(new_coord, coord[1])] += in_dict[coord]
        else:
            raise ValueError
    return new_coordinates



def alg1(data, print_debug):
    paper_coordinates, instuctions = parse_data(data, print_debug)
    inst = instuctions[0]
    if print_debug: helper.pretty_dict(paper_coordinates)
    new_paper_coordinates = fold_paper(paper_coordinates, inst[0], inst[1])
    if print_debug: helper.pretty_dict(new_paper_coordinates)
    result = (sum([x>0 for x in new_paper_coordinates.values()]))
    return result

def alg2(data, print_debug):
    paper_coordinates, instuctions = parse_data(data, print_debug)
    if print_debug: helper.pretty_dict(paper_coordinates)
    for inst in instuctions:
        old_coords = deepcopy(paper_coordinates)
        paper_coordinates = defaultdict(int)
        paper_coordinates = fold_paper(old_coords, inst[0], inst[1])
        if print_debug: helper.pretty_dict(paper_coordinates)
    helper.pretty_dict(paper_coordinates)
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

    print("--- Day 13: Transparent Origami ---\n")
    part1(test_fname, True)
    part1(input_fname)
    part2(test_fname, True)
    part2(input_fname)
