# -*- coding: utf-8 -*-
import os
from copy import deepcopy

import helper


class Octo():

    def __init__(self, array) -> None:
        self.array = deepcopy(array)
        self.max_x = len(self.array)
        self.max_y = len(self.array[0])
        self.flash_count = 0
        print(f"loadad an array with max_y = {self.max_y} and max_x = {self.max_x}")

    def pretty(self) -> None:
        print()
        for line in self.array:
            for char in line: 
                print(f" {char}", end="")
            print()
        print()

    def get_neighbour_coords(self, x, y):
        neighbours = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dy == 0 and dx == 0:
                    continue
                new_x = x + dx
                new_y = y + dy
                if new_x >= 0 and new_x < self.max_x and new_y >= 0 and new_y < self.max_y:
                    neighbours.append([new_x, new_y])
        return neighbours

    def increase_safe(self, x, y):
        if self.array[x][y] != 0:
            self.array[x][y] += 1
    
    def increase_value(self, x, y):
        self.array[x][y] += 1

    def step(self):
        flashes_this_round = 0
        # increase all values by one
        for x in range(self.max_x):
            for y in range(self.max_y):
                self.increase_value(x, y)
        # as long as there are any 9-Values keep flashing the octopusses
        while any(map(any, [[char > 9 for char in line] for line in self.array] )):
            for x in range(self.max_x):
                for y in range(self.max_y):
                    current = self.array[x][y]
                    if current > 9:
                        # flash neighbours
                        for neighbour in self.get_neighbour_coords(x, y):
                            self.increase_safe(*neighbour)
                        self.array[x][y] = 0
                        self.flash_count += 1
                        flashes_this_round += 1
        return flashes_this_round


        


def alg1(data, print_debug):
    array = []
    for line in data:
        array.append(list(map(int, list(line))))
    octo = Octo(array)
    for i in range(100):
        octo.step()
        if (i+1) % 10 == 0:
            print(f"After Step {i+1:>3} total flashes = {octo.flash_count}")
    return octo.flash_count


def alg2(data, print_debug):
    array = []
    for line in data:
        array.append(list(map(int, list(line))))
    octo = Octo(array)
    counter = 0
    n_all = octo.max_y * octo.max_y
    while True:
        counter += 1
        flashes = octo.step()
        if flashes >= n_all:
            break
    return counter


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

    print("--- Day 11: Dumbo Octopus ---\n")
    part1(test_fname, True)
    part1(input_fname)
    part2(test_fname, True)
    part2(input_fname)
