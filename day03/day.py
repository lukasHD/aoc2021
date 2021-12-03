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


def msb_bit(data):
    count_one = 0
    count_zero = 0
    for ch in data: 
        if ch == '0':
            count_zero += 1
        if ch == '1':
            count_one += 1
    if count_zero > count_one:
        msb = 0
    elif count_zero <= count_one:
        msb = 1
    return msb

def printArr(data):
    [print(l) for l in data]
    print()


def alg2(data, printDebug):
    N_BITS = len(data[0])

    if printDebug: printArr(data)

    oxy_rate = "0"
    co2_rate = "0"
    data_copy = deepcopy(data)
    for i in range(N_BITS):
        oxy_bit = msb_bit([item[i] for item in data])
        data = [item for item in data if item[i] == str(oxy_bit)]
        if printDebug: printArr(data)
        if len(data) == 1:
            oxy_rate = data[0]
            break
    if printDebug: print("=======================================================")
    if printDebug: printArr(data_copy)
    for i in range(N_BITS):
        co2_bit = 1 - msb_bit([item[i] for item in data_copy])
        data_copy = [item for item in data_copy if item[i] == str(co2_bit)]
        if printDebug: printArr(data_copy)
        if len(data_copy) == 1:
            co2_rate = data_copy[0]
            break
    oxygen_rate = int(oxy_rate, base=2)
    scrubber_rate = int(co2_rate, base=2)
    print("oxygen rate   {} --> {}".format(oxy_rate, oxygen_rate))
    print("scrubber rate {} --> {}".format(co2_rate, scrubber_rate))
    livesupport = oxygen_rate * scrubber_rate
    return livesupport
    # array = list(map(list, lines))
    # transposed = [list(x) for x in array]
    # oxygen_rate_s   = deepcopy(transposed)
    # scrubber_rate_s = deepcopy(transposed)
    # [print(l) for l in oxygen_rate_s]
    # print()
    
    # for i in range(N_BITS):
    #     line = oxygen_rate_s[i]
    #     if printDebug: print(line, end='')
    #     count_one = 0
    #     count_zero = 0
    #     for ch in line: 
    #         if ch == '0':
    #             count_zero += 1
    #         if ch == '1':
    #             count_one += 1
    #     if count_zero > count_one:
    #         msb = 0
    #     elif count_zero <= count_one:
    #         msb = 1
    #     print("  msb = {}".format(msb))


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
    print("--- Day 3: Binary Diagnostic ---\n")
    part1("day03/test.txt", True)
    part1("day03/input.txt")
    part2("day03/test.txt", True)
    part2("day03/input.txt")
