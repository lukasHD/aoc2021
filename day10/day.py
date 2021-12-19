import os

import helper

def transform(element :str):
    if element == ")":
        return 3
    if element == "]":
        return 57
    if element == "}":
        return 1197
    if element == ">":
        return 25137
    raise ValueError


def is_corrupted(line, print_debug):
    stack = []
    opening = "<[{("
    closing = ">]})"
    for element in line:
        if element in opening:
            stack.append(element)
        elif element in closing:
            last = stack.pop()
            expected = closing[opening.index(last)]
            if element == expected:
                # this pair is closed
                continue
            else:
                if print_debug: print(f"{line} -- Expected {expected}, but found {element} instead")
                return True, element
    # print(stack)
    stack.reverse()
    # print(stack)
    closing_elements = [closing[opening.index(element)] for element in stack]
    # print(closing_elements)
    nice = "".join(closing_elements)
    if print_debug: print(f"Remaining Stack as needed to close = {nice}")
    return False, nice


def score(completed: str):
    def value(element):
        if element == ")":
            return 1
        if element == "]":
            return 2
        if element == "}":
            return 3
        if element == ">":
            return 4
        raise ValueError(element)
    score_value = 0
    for element in completed:
        score_value *= 5
        score_value += value(element)
    return score_value


def alg1(data, print_debug):
    illegal = []
    for line in data:
        corrupted, element = is_corrupted(line, print_debug)
        if corrupted:
            illegal.append(element)
    if print_debug: print(illegal)
    converted = list(map(transform, illegal))
    if print_debug: print(converted)
    result = sum(converted)
    return result


def alg2(data, print_debug):
    scores = []
    for line in data:
        corrupted, completion = is_corrupted(line, print_debug)
        if corrupted:
            # skip corrupted entires
            continue
        if print_debug: print(completion)
        scores.append(score(completion))
    if print_debug: print(f"scores = {scores}")
    scores.sort()
    if print_debug: print(f"scores = {scores}")
    middle_index = int((len(scores)-1)/2)
    result = scores[middle_index]
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

    print("--- Day 10: Syntax Scoring ---\n")
    part1(test_fname, True)
    part1(input_fname)
    part2(test_fname, True)
    part2(input_fname)
