# -*- coding: utf-8 -*-
"""Example Google style docstrings.
"""

import os
import operator
from copy import copy
from functools import reduce

import helper


def parse_bits(data, version_sum = 0, calculated_value = 0):
    # Every packet begins with a standard header:
    # the first three bits encode the packet version,
    # and the next three bits encode the packet type ID. 
    # These two values are numbers;
    # all numbers encoded in any packet are represented as binary with the most significant bit first.
    # For example, a version encoded as the binary sequence 100 represents the number 4.
    version = data[0:3]
    id = data[3:6]
    # print(f"version={version} id={id}")
    version = int(version, 2)
    id = int(id, 2)
    print(f"version={version} id={id}")
    version_sum += version
    rest = data[6:]
    # Packets with type ID 4 represent a literal value. 
    # Literal value packets encode a single binary number. 
    # To do this, the binary number is padded with leading zeroes until its length is a multiple of four bits, 
    # and then it is broken into groups of four bits. 
    # Each group is prefixed by a 1 bit except the last group, which is prefixed by a 0 bit. 
    # These groups of five bits immediately follow the packet header.
    if id == 4:
        # literal value
        full_value = ""
        while True:
            seq = rest[0] 
            value = rest[1:5]
            rest = rest[5:]
            # print(f"seq={seq} value={value} rest={rest}")
            full_value = full_value + value
            # print(f"full_value={full_value}")
            if seq == "0":
                break
        full_value = int(full_value, 2)
        print(f"full_value={full_value}, rest={rest}")
        return int(full_value), rest, version_sum, calculated_value
    # Every other type of packet (any packet with a type ID other than 4) represent an operator 
    # that performs some calculation on one or more sub-packets contained within. 
    length_type = rest[0]
    rest = rest[1:]
    print(f"length_type={length_type}")
    # If the length type ID is 0, then the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
    # If the length type ID is 1, then the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.
    subs = []
    if length_type == "0":
        length = rest[0:15]
        # print(f"length={length}")
        length = int(length, 2)
        rest = rest[15:]
        print(f"length={length} rest={rest}")
        sub_packages = rest[:length]
        rest = rest[length:]
        print(f"sub_packages={sub_packages}")
        # parse all subpackages 
        sub_value, other_subpackages, version_sum, calculated_value = parse_bits(sub_packages, version_sum, calculated_value)
        subs.append(sub_value)
        while len(other_subpackages) != 0 and int(other_subpackages, 2) != 0:
            sub_packages = copy(other_subpackages)
            sub_value, other_subpackages, version_sum, calculated_value = parse_bits(sub_packages, version_sum, calculated_value)
            subs.append(sub_value)
    elif length_type == "1":
        number = rest[0:11]
        # print(f"number={number}")
        number = int(number, 2)
        rest = rest[11:]
        print(f"number={number} rest={rest}")
        # parse all those packages
        for _ in range(number):
            sub_value, rest, version_sum, calculated_value = parse_bits(rest, version_sum, calculated_value)
            subs.append(sub_value)
    print(f"subs={subs}, rest={rest}")
    if id == 0:
        calculated_value = sum(subs)
        print(f"add {subs} to {calculated_value}")
    elif id == 1:
        calculated_value = reduce(operator.mul, subs, 1)
        print(f"multiply {subs} to {calculated_value}")
    elif id == 2:
        calculated_value = min(subs)
        print(f"min of {subs} is {calculated_value}")
    elif id == 3:
        calculated_value = max(subs)
        print(f"max of {subs} is {calculated_value}")
    elif id == 5:
        if subs[0] > subs[1]:
            calculated_value = 1
        else:
            calculated_value = 0
        print(f"greater than of {subs} is {calculated_value}")
    elif id == 6:
        if subs[0] < subs[1]:
            calculated_value = 1
        else:
            calculated_value = 0
        print(f"less than of {subs} is {calculated_value}")
    elif id == 7:
        if subs[0] == subs[1]:
            calculated_value = 1
        else:
            calculated_value = 0
        print(f"equal of {subs} is {calculated_value}")
    else:
        raise ValueError
    
    return calculated_value, rest, version_sum, calculated_value





def alg1(data, print_debug):
    for line in data:
        bits = (bin(int(line, 16))[2:]).zfill(len(line) * 4)
        print(f"\n\n{bits}")
        _, _ , result, _ = parse_bits(bits)
    return result


def alg2(data, print_debug):
    for line in data:
        bits = (bin(int(line, 16))[2:]).zfill(len(line) * 4)
        print(f"\n\n{bits}")
        _, _ , _, result = parse_bits(bits)
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

    print("--- Day 16: Packet Decoder ---\n")
    part1(test_fname, True)
    part1(input_fname)
    part2(test_fname, True)
    part2(input_fname)
