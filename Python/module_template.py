#! /usr/bin/env python3

import pathlib
import sys
import time


def task_to_do(data):
    ...

    return res


def get_input(file=None):
    def process_input():
        '''
        Input format:
        * n queries
        * Queries:
            1 x - Push the element x into the stack
            2   - Delete the element present at the top of the stack.
            3   - Print the maximum element in the stack.
        '''
        n = int(input())
        return [input() for _ in range(n)]

    if file:
        with open(file) as in_file:
            save_stdin = sys.stdin
            sys.stdin = in_file
            res = process_input()
            sys.stdin = save_stdin
            return res

    return process_input()


if __name__ == '__main__':
    start_time = time.time()
    verbose = True
    file = None

    if len(sys.argv) == 2 and pathlib.Path(sys.argv[1]).is_file():
        file = sys.argv[1]
    elif len(sys.argv) >= 2:
        print(f'Usage:  {pathlib.Path(__file__).name} [<input_file>]')
        sys.exit(1)

    # Get input...
    data = get_input(file)

    # Process...
    res = task_to_do(data)
    print(res)

    end_time = time.time()
    if verbose:
        print(f'\nRun time:  {(end_time - start_time):,.4f} seconds\n')
