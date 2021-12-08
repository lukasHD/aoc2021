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
        if printDebug: print(input, output)
        yield input, output

def alg1(data, printDebug):
    """In the output values, how many times do digits 1, 4, 7, or 8 appear?"""
    count_easy = 0
    for _, output in parse_input(data, printDebug):
        for el in output:
            if len(el) in [2, 4, 3, 7]:
                count_easy += 1
    return count_easy


def translate(el, onepattern, fourpattern): 
    """With a little bit of help from my reddit friends:
    https://www.reddit.com/r/adventofcode/comments/rbj87a/comment/hnp38wn/?utm_source=share&utm_medium=web2x&context=3
    """
    el = set(el)
    if len(el) == 2:
        return 1
    elif len(el) == 4:
        return 4
    elif len(el) == 3:
        return 7
    elif len(el) == 7:
        return 8
    elif len(el) == 6:
        if len(el & onepattern) == 1:
            return 6
        elif len(el & fourpattern) == 4:
            return 9
        else:
            return 0
    elif len(el) == 5:
        if len(el & onepattern) == 2:
            return 3
        elif len(el & fourpattern) == 2:
            return 2
        else:
            return 5
    else:
        print("unreachable Error")
        raise(ValueError)

def alg2(data, printDebug):
    result = 0
    for input, output in parse_input(data, printDebug):
        if printDebug: print("======================================================================================================================================")
        input = [set(x) for x in  input]
        fourpattern = list(filter(lambda x: len(x) == 4, input))[0]
        onepattern = list(filter(lambda x: len(x) == 2, input))[0]
        # for number in input:
        #     print(number, end="")
        number = ""
        for el in output:
            num = translate(el, onepattern, fourpattern)
            number = number + str(num)
        if printDebug: print("{} => {}".format(output, number))
        result += int(number)
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

    print("--- Day 8: Seven Segment Search ---\n")
    part1(test_fname, True)
    part1(input_fname)
    part2(test_fname, True)
    part2(input_fname)
