#! /usr/bin/env python3

from bisect import bisect_left, bisect, insort
import pathlib
import sys
import time


def get_max(data):
    stack = []
    sorted_list = []
    res = []

    for line in data:
        match line.split():
            case ['1', n]:
                n = int(n)
                stack.append(n)
                insort(sorted_list, n)
            case ['2']:
                val = stack.pop()
                index = bisect_left(sorted_list, val)
                sorted_list.pop(index)
            case ['3']:
                res.append(sorted_list[-1])
            case _:
                raise ValueError(f'Unexpected query:  {line}')

    return res


def get_input(file=None):
    def process_input():
        # Input format:
        # n queries
        # Queries:
        # 1 x  -Push the element x into the stack
        # 2    -Delete the element present at the top of the stack.
        # 3    -Print the maximum element in the stack.
        n = int(input())
        return [input() for _ in range(n)]

    if file:
        with open(file) as infile:
            save_stdin = sys.stdin
            sys.stdin = infile
            res = process_input()
            sys.stdin = save_stdin
            return res

    return process_input()


if __name__ == '__main__':
    start_time = time.time()
    file = None

    if len(sys.argv) == 2 and pathlib.Path(sys.argv[1]).is_file():
        file = sys.argv[1]
    elif len(sys.argv) >= 2:
        print(f'Usage:  {pathlib.Path(__file__).name} [<input_file>]')
        sys.exit(1)

    # Get input...
    data = get_input(file)

    # Process...
    res = get_max(data)
    for item in res:
        print(item)

    end_time = time.time()
    print(f'\nRun time:  {(end_time - start_time):,.4f} seconds\n')
