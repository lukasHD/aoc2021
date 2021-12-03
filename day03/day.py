import helper
from copy import deepcopy

def alg1(lines, printDebug):
    array = list(map(list, lines))
    transposed = [list(x) for x in zip(*array)]
    # print(list(zip(*array)))
    # most significant
    gamma_rate_s = ""
    # least significant
    epsilon_rate_s = ""
    for line in transposed:
        if printDebug: print(line)
        count_one = 0
        count_zero = 0
        for ch in line: 
            if ch == '0':
                count_zero += 1
            if ch == '1':
                count_one += 1
        if count_zero > count_one:
            gamma_rate_s += "0"
            epsilon_rate_s += "1"
        elif count_zero < count_one:
            gamma_rate_s += "1"
            epsilon_rate_s += "0"
        else:
            print("Panic !!!")
    gamma_rate = int(gamma_rate_s, base=2)
    epsilon_rate = int(epsilon_rate_s, base=2)
    print("gamma rate   {} --> {}".format(gamma_rate_s, gamma_rate))
    print("epsilon rate {} --> {}".format(epsilon_rate_s, epsilon_rate))
    powerconsumption = epsilon_rate * gamma_rate
    return powerconsumption

def alg2(lines, printDebug):
    array = list(map(list, lines))
    transposed = [list(x) for x in zip(*array)]
    oxygen_rate_s = ""
    scrubber_rate_s = ""
    for line in transposed:
        if printDebug: print(line)
        count_one = 0
        count_zero = 0
        for ch in line: 
            if ch == '0':
                count_zero += 1
            if ch == '1':
                count_one += 1
        if count_zero > count_one:
            gamma_rate_s += "0"
            epsilon_rate_s += "1"
        elif count_zero < count_one:
            gamma_rate_s += "1"
            epsilon_rate_s += "0"
        else:
            print("Panic !!!")
    oxygen_rate = int(oxygen_rate_s, base=2)
    scrubber_rate = int(scrubber_rate_s, base=2)
    print("oxygen rate   {} --> {}".format(oxygen_rate_s, oxygen_rate))
    print("scrubber rate {} --> {}".format(scrubber_rate_s, scrubber_rate))
    livesupport = oxygen_rate * scrubber_rate
    return livesupport


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
    print("\n")
    part1("day03/test.txt", True)
    part1("day03/input.txt")
    part2("day03/test.txt", True)
    # part2("day03/input.txt")
