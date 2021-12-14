# -*- coding: utf-8 -*-
"""Example Google style docstrings.
"""

from collections import Counter, defaultdict
import os

import helper

from copy import copy


def parse_data(data, print_debug):
    molecule = data[0]
    rules = dict()
    for line in data[2:]:
        pattern, insert = line.split(" -> ")
        rules[pattern] = insert
    if print_debug: print(f"molecule={molecule} \nrules={rules}")
    return molecule, rules

def alg1(data, print_debug):
    molecule, rules = parse_data(data, print_debug)
    if print_debug: print(f"Template:      {molecule}")
    for i in range(1,11):
        new_string = ""
        for pair in helper.sliding_window_iter(molecule, 2):
            # print("".join(pair))
            new_string += pair[0]
            new_string += rules["".join(pair)]

        new_string += molecule[-1]
        molecule = copy(new_string)
        if print_debug: print(f"After Step {i:>2}: {molecule} \n{Counter(molecule)}")
    frequencies = Counter(list(molecule))
    if print_debug: print(frequencies)
    min_freq = min(frequencies.values())
    max_freq = max(frequencies.values())
    result = max_freq - min_freq
    return result


def alg2(data, print_debug):
    """With a little bit of help from here https://www.reddit.com/r/adventofcode/comments/rfzq6f/comment/hohc8vc/?utm_source=share&utm_medium=web2x&context=3

    Counting Pairs is a good idea, implementing I first only added 1 not the counter value
    """
    molecule, rules = parse_data(data, print_debug)
    pair_counter = defaultdict(int)
    frequencies = Counter(list(molecule))
    for pair in helper.sliding_window_iter(molecule, 2):
        pair_counter["".join(pair)] += 1
    if print_debug: print(f"Template:      {pair_counter}\n                {frequencies}")

    for i in range(1,41):
        for pair, count in pair_counter.copy().items():
            insert = rules["".join(pair)]
            p1 = pair[0] + insert
            p2 = insert + pair[1]
            pair_counter[pair] -= count
            pair_counter[p1] += count
            pair_counter[p2] += count
            frequencies[insert] += count
        if print_debug: print(f"After Step {i:>2}: {pair_counter}\n                {frequencies}")
    min_freq = min(frequencies.values())
    max_freq = max(frequencies.values())
    result = max_freq - min_freq
    return result


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

    print("--- Day 14: Extended Polymerization ---\n")
    part1(test_fname, True)
    part1(input_fname)
    part2(test_fname, True)
    part2(input_fname)
