import os
from collections import Counter, deque

import helper

REPRODUCTION = 6
BIRTH = 8

def alg1(data, days, printDebug):
    start = data
    if printDebug: print(start)
    if printDebug: print(Counter(start))
    histogram = deque(maxlen=BIRTH+1)
    for _ in range(max(REPRODUCTION+1, BIRTH+1)):
        histogram.append(0)
    if printDebug: print(histogram)
    # initial Filling
    for k, v in Counter(start).items():
        histogram[k] = v
    if printDebug: print("Init{:>3} ".format(0), end='')
    if printDebug: print(histogram)
    for day in range(days):
        if printDebug: print("Day {:>3} ".format(day + 1), end='')
        # pop and shift left
        zeroes = histogram.popleft()
        # birth some new fishes at last pos (should be 8)
        histogram.append(zeroes)
        histogram[REPRODUCTION] += zeroes
        if printDebug: print(histogram)
    if printDebug: print(sum(histogram))
    return sum(histogram)


def alg2(data, days, printDebug):
    return alg1(data, days, printDebug)


def part1(fname: str, days, printDebug = False):
    print("=== PART 1 ===")
    print("-- {} --".format(fname))
    result = 0
    result = alg1(helper.single_line_as_ints(fname), days, printDebug)
    print("Result = {}".format(result))
    print()

def part2(fname: str, days, printDebug = False):
    print("=== PART 2 ===")
    print("-- {} --".format(fname))
    result = 0
    result = alg2(helper.single_line_as_ints(fname), days, printDebug)
    print("Result = {}".format(result))
    print()
    

if __name__ == '__main__':
    test_fname = os.path.join(os.path.dirname(__file__), 'test.txt')
    input_fname = os.path.join(os.path.dirname(__file__), 'input.txt')
    print(test_fname)
    print("--- Day 6: Lanternfish ---\n")
    part1(test_fname, 18, True)
    part1(test_fname, 80, False)
    part1(input_fname, 80)
    part2(test_fname, 256, False)
    part2(input_fname, 256)
