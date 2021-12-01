import helper


def count_increasing_steps(depths, debug_print = False):
    count = 0
    if debug_print: 
        for d in depths:
            print(d)
        print("---")

    for previous_depth, current_depth in helper.pairwise(depths):
        name = "undefined"
        if current_depth > previous_depth:
            name = "increased"
            count = count + 1
        elif current_depth == previous_depth:
            name = "unchanged"
        elif current_depth < previous_depth:
            name = "decreased"
        else:
            raise UnboundLocalError

        if debug_print: print("{} --> {}    Threfore {}".format(previous_depth, current_depth, name))
    
    print("Result = {}".format(count))
    return count



if __name__ == '__main__':
    count_increasing_steps(helper.input_as_ints("day01/test.txt"), True)
    count_increasing_steps(helper.input_as_ints("day01/input.txt"))