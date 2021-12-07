import os

import helper


def alg1(data, printDebug):
    MIN = min(data)
    MAX = max(data)
    if printDebug: print("min={}, max={}, data={}".format(MIN,MAX,data))
    costs = []
    min_cost = 99999999999999
    for i in range(MIN, MAX+1):
        if printDebug: print("Pos = {} ".format(i), end='')

        cost = sum(map(lambda n: abs(n-i),data))
        min_cost = min(min_cost, cost)
        if printDebug: print(cost)
        costs.append((i, cost))
    return min_cost


def alg2(data, printDebug):
    MIN = min(data)
    MAX = max(data)
    if printDebug: print("min={}, max={}, data={}".format(MIN,MAX,data))
    costs = []
    min_cost = 99999999999999
    for i in range(MIN, MAX+1):
        if printDebug: print("Pos = {} ".format(i), end='')

        cost = sum(map(lambda n: int(abs(n-i)*(abs(n-i)+1)/2),data))
        min_cost = min(min_cost, cost)
        if printDebug: print(cost)
        costs.append((i, cost))
    return min_cost


def part1(fname: str, printDebug = False):
    print("=== PART 1 ===")
    print("-- {} --".format(fname))
    result = 0
    result = alg1(helper.single_line_as_ints(fname), printDebug)
    print("Result = {}".format(result))
    print()

def part2(fname: str, printDebug = False):
    print("=== PART 2 ===")
    print("-- {} --".format(fname))
    result = 0
    result = alg2(helper.single_line_as_ints(fname), printDebug)
    print("Result = {}".format(result))
    print()
    

if __name__ == '__main__':
    test_fname = os.path.join(os.path.dirname(__file__), 'test.txt')
    input_fname = os.path.join(os.path.dirname(__file__), 'input.txt')

    print("--- Day 7: The Treachery of Whales ---\n")
    part1(test_fname, True)
    part1(input_fname)
    part2(test_fname, True)
    part2(input_fname)
