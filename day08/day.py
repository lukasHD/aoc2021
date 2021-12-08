import os

import helper

def digits(): 
    """
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
    """
    return 0

def parse_input(data, printDebug = False):
    for line in data:
        input_, output_ = line.split(" | ")
        input = input_.split(" ")
        output = output_.split(" ")
        print(input, output)
        yield input, output

def alg1(data, printDebug):
    """In the output values, how many times do digits 1, 4, 7, or 8 appear?"""
    count_easy = 0
    for input, output in parse_input(data, printDebug):
        for el in output:
            if len(el) in [2, 4, 3, 7]:
                count_easy += 1
    return count_easy


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

    print("--- Day 8: Seven Segment Search ---\n")
    part1(test_fname, True)
    part1(input_fname)
    # part2(test_fname, True)
    # part2(input_fname)
