import os

import helper


def alg1(data, printDebug):
    counter = {}
    illegal = []
    for line in data:
        counter["["] = 0
        counter["{"] = 0
        counter["("] = 0
        counter["<"] = 0
        for el in line:
            # print(f"{el} ", end="")
            if el == "[":
                counter["["] += 1
            elif el == "]":
                counter["["] -= 1
            elif el == "{":
                counter["{"] += 1
            elif el == "]":
                counter["{"] -= 1
            elif el == "(":
                counter["("] += 1
            elif el == ")":
                counter["("] -= 1
            elif el == "<":
                counter["<"] += 1
            elif el == ">":
                counter["<"] -= 1
            print(counter.values())
            if any(x < 0 for x in counter.values()):
                print(f"illegal character {el} found. Adding to List")
                illegal.append(el)
                continue
        print()
    print(illegal)
    return 0


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

    print("\n")
    part1(test_fname, True)
    # part1(input_fname)
    # part2(test_fname, True)
    # part2(input_fname)
