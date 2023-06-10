#! /usr/bin/env python3

import copy
import pathlib
import sys
import time


def equal_heights(heights):
    return heights[0] == heights[1] == heights[2]


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
            heights[0] -= stacks[0].pop()
        elif heights[0] <= heights[1] >= heights[2]:
            heights[1] -= stacks[1].pop()
        else:
            heights[2] -= stacks[2].pop()

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
    start_time = time.time()
    file = None

    if len(sys.argv) == 2:
        file = sys.argv[1]
    elif len(sys.argv) > 2:
        print(f'Usage:  {pathlib.Path(__file__).name} [<input_file>]')
        sys.exit(1)

    stacks = get_input(file)
    input_time = time.time()

    # Top of stack is left of list, so reverse lists:
    for stack in stacks.values():
        stack.reverse()
    reversal_time = time.time()

    res = max_equal_height(stacks)
    print(res)

    end_time = time.time()
    print(f'\nRun times:\n* Input time:  {(input_time - start_time):,.4f} seconds\n'
          f'* Reversal time:  {(reversal_time - input_time):,.4f} seconds\n'
          f'* Algorithm time:  {(end_time - reversal_time):,.4f} seconds\n')
