# aoc.py
from typing import List
from itertools import tee, islice
from collections import deque

def input_as_string(filename:str) -> str:
    """returns the content of the input file as a string"""
    with open(filename, encoding="utf-8") as file:
        return file.read().rstrip("\n")

def input_as_lines(filename:str) -> List[str]:
    """Return a list where each line in the input file is an element of the list"""
    return input_as_string(filename).split("\n")

def input_as_ints(filename:str) -> List[int]:
    """Return a list where each line in the input file is an element of the list,
    converted into an integer
    """
    lines = input_as_lines(filename)
    line_as_int = lambda l: int(l.rstrip('\n'))
    return list(map(line_as_int, lines))


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    first, second = tee(iterable)
    next(second, None)
    return zip(first, second)


def sliding_window_iter(iterable, size):
    """..."""
    iterable = iter(iterable)
    window = deque(islice(iterable, size), maxlen=size)
    for item in iterable:
        yield tuple(window)
        window.append(item)
    if window:
        # needed because if iterable was already empty before the `for`,
        # then the window would be yielded twice.
        yield tuple(window)

def pretty_dict(my_dict: dict[(int, int),int]):
    x_values = [el[0] for el in my_dict.keys()]
    y_values = [el[1] for el in my_dict.keys()]
    x_min = min(x_values)
    x_max = max(x_values)
    y_min = min(y_values)
    y_max = max(y_values)

    for y in range(y_min-1, y_max+2):
        for x in range(x_min-1, x_max+2):
            if my_dict[x,y] > 0: 
                char = '@'
            else:
                char = ' '
            print(char, end='')
        print()
    print()
