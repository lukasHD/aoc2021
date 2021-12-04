import helper
from copy import deepcopy
from dataclasses import dataclass


@dataclass
class BingoCard:
    array_rep = []
    size = 0
    numbers = dict()
    called = dict()

    def __init__(self, in_array):
        self.size = len(in_array)
        self.array_rep = in_array
        for i, line in enumerate(in_array):
            for j, number in enumerate(line):
                self.numbers[number] = (i, j)
        for pos in self.numbers.values():
            self.called[pos] = False
        
    def pretty(self):
        print("I am a Bingo-Card")
        for line in range(self.size):
            for pos in range(self.size):
                print("{:>2} ".format(self.array_rep[line][pos]), end='')
            print()
        

    def call_number_return_bingo(self, number: int) -> bool:
        # if number in card mark as called
        # check for bingo
        return False


def parse_input(lines):
    numbers = list(map(int, lines[0].split(',')))
    print("Bingo Caller Numbers: {}".format(numbers))
    bingo_card = []
    bingo_cards = []
    for line in lines[2:]:
        bingo_line = list(map(int, filter(lambda a: a != '' ,line.strip().split(' '))))
        # print(bingo_line)
        if bingo_line == []:
            # save this bingo_card
            print("Have a full bingo card: {}".format(bingo_card))
            bingo_cards.append(deepcopy(bingo_card))
            b1 = BingoCard(bingo_card)
            b1.pretty()
            bingo_card = []
            continue
        bingo_card.append(bingo_line)
    return bingo_cards

def alg1(lines, printDebug):
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
    print("--- Day 4: Giant Squid ---\n")
    parse_input(helper.input_as_lines("day04/test.txt"))
    # part1("day04/test.txt", True)
    # part1("day04/input.txt")
    # part2("day04/test.txt", True)
    # part2("day04/input.txt")
