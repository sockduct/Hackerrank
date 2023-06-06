#! /usr/bin/env python3

import copy
import pathlib
import sys


def equal_heights(heights):
    return all(val == heights[0] for val in heights)


def max_equal_height(stacks):
    '''
    Get height of each stack
    Start with tallest stack and pop top, update height
    Check if heights equal or repeat
    '''
    # Don't mutate parameter:
    stacks = copy.deepcopy(stacks)
    heights = [sum(vals) for vals in stacks.values()]

    while min(heights) > 0:
        if equal_heights(heights):
            return heights[0]

        if heights[2] <= heights[0] >= heights[1]:
            stacks[0].pop()
            heights[0] = sum(stacks[0])
        elif heights[0] <= heights[1] >= heights[2]:
            stacks[1].pop()
            heights[1] = sum(stacks[1])
        else:
            stacks[2].pop()
            heights[2] = sum(stacks[2])

    return 0


def get_input(file=None):
    def process_input(file=None):
        # Number of elements for each stack (stack element #):
        # Don't need these in Python but since they're part of the spec, reading
        # them in:
        se1, se2, se3 = map(int, input().split())
        return {stack: [int(n) for n in input().split()] for stack in range(3)}

    if file:
        with open(file) as infile:
            save_stdin = sys.stdin
            sys.stdin = infile
            res = process_input(infile)
            sys.stdin = save_stdin
            return res

    return process_input()


if __name__ == '__main__':
    file = None

    if len(sys.argv) == 2:
        file = sys.argv[1]
    elif len(sys.argv) > 2:
        print(f'Usage:  {pathlib.Path(__file__).name} [<input_file>]')
        sys.exit(1)

    stacks = get_input(file)

    # Top of stack is left of list, so reverse lists:
    for stack in stacks.values():
        stack.reverse()

    res = max_equal_height(stacks)
    print(res)
