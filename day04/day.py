import helper
from copy import deepcopy
from dataclasses import dataclass


# @dataclass
class BingoCard:
    array_rep = []
    size = 0
    numbers = dict()
    called = dict()
    id = 0

    def __init__(self, in_array, id_):
        # print("__init__ {}  {}".format(in_array, id_))
        self.numbers = dict()
        self.called = dict()
        # print(self.numbers)
        # print(self.called)
        self.size = len(in_array)
        self.id = id_
        self.array_rep = in_array
        for i, line in enumerate(in_array):
            for j, number in enumerate(line):
                # print(number, end=', ')
                self.numbers[number] = (i, j)
        # print()
        for pos in self.numbers.values():
            self.called[pos] = False
        # print(self.numbers.keys())
        # print("_____________________________________________________")
        
    def pretty(self):
        print("I am Bingo-Card {}".format(self.id))
        for line in range(self.size):
            for pos in range(self.size):
                a = " "
                if self.called[(line, pos)]: 
                    a = "-"
                print("{}".format(a), end='')
                print("{:>2}".format(self.array_rep[line][pos]), end='')
                print("{} ".format(a), end='')
            print()
        

    def call_number_return_bingo(self, number: int) -> bool:
        # if number in card mark as called
        # print("Calling Number {}".format(number))
        try:
            pos = self.numbers[number]
        except KeyError:
            # print ("Not in my Board")
            return False
        self.called[pos] = True
        # check for bingo in lines 
        for line in range(self.size):
            a = 0
            for pos in range(self.size):
                a += self.called[(line, pos)]
            if a == self.size : 
                return True
        # check for bingo in columns 
        for pos in range(self.size):
            a = 0
            for line in range(self.size):
                a += self.called[(line, pos)]
            if a == self.size : 
                return True
        return False

    def calc_result(self, number):
        non_called = 0
        for line in range(self.size):
            for pos in range(self.size):
                if not self.called[(line, pos)]:
                    print(self.array_rep[line][pos], end=' + ')
                    non_called += self.array_rep[line][pos]
        result = non_called*number
        print(" --> {} * {} = {}".format(non_called, number, result))
        return result


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
            bingo_card = []
            continue
        bingo_card.append(bingo_line)
    return bingo_cards, numbers

def alg1(lines, printDebug):
    result = None
    bingo_cards_array, numbers = parse_input(lines)
    bingo_cards = []
    for id, card_array in enumerate(bingo_cards_array):
        bingo_cards.append(BingoCard(deepcopy(card_array), id+1))
    for a in bingo_cards:
        a.pretty() 
    # numbers = [99, 22, 13, 17, 11, 0]
    # numbers = [99, 0, 24, 7, 5, 19]
    for call in numbers:
        print("Calling Number {}".format(call))
        for card in bingo_cards:
            bingo = card.call_number_return_bingo(call)
            # card.pretty()
            if bingo:
                print("B I N G O")
                card.pretty()
                result = card.calc_result(call)
                return result
    return result


def alg2(data, printDebug):
    result = None
    bingo_cards_array, numbers = parse_input(data)
    bingo_cards = []
    for id, card_array in enumerate(bingo_cards_array):
        bingo_cards.append(BingoCard(deepcopy(card_array), id+1))
    for a in bingo_cards:
        a.pretty() 
    # numbers = [99, 22, 13, 17, 11, 0]
    # numbers = [99, 0, 24, 7, 5, 19]
    winners = []
    for call in numbers:
        print("Calling Number {}".format(call))
        
        for card in bingo_cards:
            if card in winners:
                if printDebug: print("Skip Card {}".format(card.id))
                continue
            bingo = card.call_number_return_bingo(call)
            # card.pretty()
            if bingo:
                print("B I N G O !  on card {}".format(card.id))
                #card.pretty()
                result = card.calc_result(call)
                winners.append(card)
                # return result
        if printDebug: print([card.id for card in winners], sep = ', ')
        if printDebug: print([card.id for card in bingo_cards], sep = ', ')
        if printDebug: print(bingo_cards)
        bingo_cards = list(filter(lambda c: c.id not in [x.id for x in winners], bingo_cards))
        if printDebug: print([card.id for card in bingo_cards], sep = ', ')
        if printDebug: print(bingo_cards)
        if len(bingo_cards) == 0:
            print("No Bingo-cards left")
            break

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
    print("--- Day 4: Giant Squid ---\n")
    # parse_input(helper.input_as_lines("day04/test.txt"))
    # part1("day04/test.txt", True)
    # part1("day04/input.txt")
    part2("day04/test.txt", True)
    part2("day04/input.txt")
