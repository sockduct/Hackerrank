#! /usr/bin/env python3


import heapq
import sys


def process_queries1(data):
    match list(map(int, input().split())):
        case [1, value]:
            # Add value to heap
            heapq.heappush(data, value)
        case [2, value]:
            # Delete value from heap
            # Can't use this because may not be smallest element (not exactly
            # matching a heap data structure)
            # heapq.heappop(data, value)
            data.pop(data.index(value))
            heapq.heapify(data)
        case [3]:
            # Print minimum value on heap
            print(f'{heapq.nsmallest(1, data)[0]}')
        case _:
            raise ValueError(f'Unexpected value')


def process_queries2(data):
    command, *value = map(int, input().split())
    if command == 1:
        # Add value to heap
        heapq.heappush(data, value[0])
    elif command == 2:
        # Delete value from heap
        data.pop(data.index(value[0]))
        heapq.heapify(data)
    elif command == 3:
        print(f'{heapq.nsmallest(1, data)[0]}')
    else:
        raise ValueError(f'Unexpected value "{command}"')


def main():
    data = []
    skip = True

    queries = int(input())
    for _ in range(queries):
        # Choose one:
        if sys.version_info.minor >= 10 and not skip:
            process_queries1(data)
        else:
            process_queries2(data)


if __name__ == '__main__':
    main()
