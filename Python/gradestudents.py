#! /usr/bin/env python3

'''
Problem Description:
* Every student gets grade:  [0, 100]
    * Grade < 40 = fail
* Grading rules:
    * If grade < 38, no rounding occurs
    * If difference between grade and next multiple of 5 is < 3, round grade up to next multiple of 5

Sample Data:
* Input:
    4
    73
    67
    38
    33
* Output:
    75
    67
    40
    33

Approach:
* x

To Do:
* x
'''


import pathlib
import sys
import time


def grade(data):
    final_grades = []

    for grade in data:
        adjust = 0
        match (ones:= grade % 10):
            case 8 | 9 if grade >= 38:
                adjust = 10 - ones
            case 3 | 4 if grade >= 38:
                adjust = 5 - ones
            case digit if digit in range(10):
                pass
            case _:
                raise ValueError(f'Unexpected value:  {ones} from {grade}')
        final_grades.append(grade + adjust)

    return final_grades


def get_input(file=None):
    def process_input():
        '''
        Input format:
        * n students
        * Each subsequent line contains a single grade - an integer
        '''
        n = int(input())
        return [int(input().strip()) for _ in range(n)]

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
    res = grade(data)
    for grade in res:
        print(grade)

    end_time = time.time()
    if verbose:
        print(f'\nRun time:  {(end_time - start_time):,.4f} seconds\n')
