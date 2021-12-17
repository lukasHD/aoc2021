# -*- coding: utf-8 -*-
"""Example Google style docstrings.
"""

import os
from dataclasses import dataclass, field
from copy import copy

import helper

@dataclass
class Cannonball():
    position_x :int
    position_y :int
    velocity_x :int
    velocity_y :int
    trajectory: list[tuple[int, int]] = field(default_factory=list)

    def step(self):
        self.position_x += self.velocity_x # The probe's x position increases by its x velocity.
        self.position_y += self.velocity_y # The probe's y position increases by its y velocity.
        self.velocity_y -= 1               # Due to gravity, the probe's y velocity decreases by 1.
        if self.velocity_x > 0:            # Due to drag, the probe's x velocity changes by 1 toward the value 0;
            self.velocity_x -= 1           # that is, it decreases by 1 if it is greater than 0,
        elif self.velocity_x < 0:          # increases by 1 if it is less than 0,
            self.velocity_x += 1           # or does not change if it is already 0.
        else:
            self.velocity_x = 0
        self.trajectory.append((self.position_x, self.position_y))
        return self.position_x, self.position_y



@dataclass
class Target():
    x_min :int
    x_max :int
    y_min :int
    y_max :int

    def is_inside(self, point: tuple[int, int]):
        x, y = point
        x_inside = x >= self.x_min and x <= self.x_max
        y_inside = y >= self.y_min and y <= self.y_max
        return x_inside and y_inside

    def is_behind(self, point: tuple[int, int]):
        x, y = point
        x_behind = x > self.x_max
        y_behind = y < self.y_min
        return x_behind or y_behind

def parse_date(line) -> Target:
    x_str, y_str = line.split(": ")[1].split(", ")
    x_min, x_max = list(map(int, x_str.split("=")[1].split("..")))
    y_min, y_max = list(map(int, y_str.split("=")[1].split("..")))
    target = Target(x_min, x_max, y_min, y_max)
    # print(target)
    # print(f"x = [{x_min}, {x_max}] \t y = [{y_min}, {y_max}]")
    return target


def draw_game(target: Target, trajectory = [], BORDER = 3):
    trajet_x_max = max(list(zip(*trajectory))[0])
    trajet_x_min = min(list(zip(*trajectory))[0])
    trajet_y_max = max(list(zip(*trajectory))[1])
    trajet_y_min = min(list(zip(*trajectory))[1])
    draw_x_max = max(0, target.x_max, trajet_x_max) + BORDER + 1
    draw_x_min = min(0, target.x_min, trajet_x_min) - BORDER
    draw_y_max = max(0, target.y_max, trajet_y_max) + BORDER + 1
    draw_y_min = min(0, target.y_min, trajet_y_min) - BORDER
    print()
    for y in range(draw_y_max, draw_y_min, -1):
        for x in range(draw_x_min, draw_x_max):
            if (x, y) == (0, 0):
                print("S", end="")
            elif (x, y) in trajectory:
                print("#", end="")
            elif target.is_inside((x, y)):
                print("T", end="")
            else:
                print("·", end="")
        print()
    print()
    return 0


def shoot(target: Target, vector = (7,2), print_debug = False):
    ball = copy(Cannonball(0, 0, vector[0], vector[1]))
    hit = False
    for _ in range(3000):
        current = ball.step()
        if target.is_inside(current):
            if print_debug: print("Hit the Target")
            hit = True
            break
        if target.is_behind(current):
            if print_debug: print("Missed the Target")
            break
    else:
        print("!!!!!!!!!!!!!!  RUN OUT OF STEPS  !!!!!!!!!!!!!!")

    if print_debug: print(ball.trajectory)
    if print_debug: draw_game(target, ball.trajectory)
    return hit, ball.trajectory

def alg1(data, print_debug):
    target = parse_date(data[0])
    # draw_game(target)
    # shoot(target, (7,2))
    # shoot(target, (6,9), True)
    # shoot(target, (17,135), False)
    # return 0
    max_height = 0
    best_v_y = None
    best_v_x = None
    # hit_counter = 0
    for v_x in range(1, 300):
        for v_y in range(-150, 300):
            # print(f"Shoot with vector ({v_x}, {v_y})")
            hit, trajet = shoot(target, (v_x, v_y), print_debug)
            if hit:
                this_max_height = max(list(zip(*trajet))[1])
                # hit_counter += 1
                if this_max_height > max_height:
                    max_height = this_max_height
                    best_v_y = v_y
                    best_v_x = v_x
                if print_debug: print(f"Shoot with vector ({v_x:>3}, {v_y:>3})", end="")
                if print_debug: print(f" \t--- HIT MAX HEIGHT {this_max_height}")
    print(f"max height: {max_height} reached for velocity=({best_v_x}, {best_v_y})")
    # print(f"a total of {hit_counter} shots can hit")
    return max_height


def alg2(data, print_debug):
    target = parse_date(data[0])
    hit_counter = 0
    for v_x in range(1, 300):
        for v_y in range(-150, 300):
            hit, _ = shoot(target, (v_x, v_y), print_debug)
            if hit:
                hit_counter += 1
    print(f"a total of {hit_counter} shots can hit")
    return hit_counter


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

    print("--- Day 17: Trick Shot ---\n")
    part1(test_fname, False)
    part1(input_fname)
    part2(test_fname, False)
    part2(input_fname)
