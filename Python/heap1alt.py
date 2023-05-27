#! /usr/bin/env python3


import heapq
import sys
import time


def process_queries1(heap):
    match list(map(int, input().split())):
        case [1, value]:
            # Add value to heap
            heapq.heappush(heap, value)
        case [2, value]:
            # Delete arbitrary value from heap
            if value[0] == heap[0]:
                heapq.heappop(heap)
            else:
                # Better way?
                heap.pop(heap.index(value[0]))
                heapq.heapify(heap)
        case [3]:
            # Print minimum value on heap - slow:
            # print(f'{heapq.nsmallest(1, heap)[0]}')
            # Per source code can use heap[0] to see smallest item on heap:
            print(f'{heap[0]}')
        case _:
            raise ValueError(f'Unexpected value')


def process_queries2(heap):
    command, *value = map(int, input().split())
    if command == 1:
        # Add value to heap
        heapq.heappush(heap, value[0])
    elif command == 2:
        # Delete arbitrary value from heap
        if value[0] == heap[0]:
            heapq.heappop(heap)
        else:
            # Better way?
            heap.pop(heap.index(value[0]))
            heapq.heapify(heap)
    elif command == 3:
        # Per source code can use heap[0] to see smallest item on heap:
        print(f'{heap[0]}')
    else:
        raise ValueError(f'Unexpected value "{command}"')


def main():
    stdin = None
    if len(sys.argv) == 2:
        stdin = sys.stdin
        sys.stdin = open(sys.argv[1])

    start_time = time.time()
    count = 0
    heap = []
    skip = True

    queries = int(input())
    for _ in range(queries):
        # Choose one:
        if sys.version_info.minor >= 10 and not skip:
            process_queries1(heap)
        else:
            process_queries2(heap)

        count += 1
        if count == 50_000:
            print(f'\nRun time:  {(time.time() - start_time):.3f} seconds', file=sys.stderr, flush=True)

    print(f'\nRun time:  {(time.time() - start_time):.3f} seconds', file=sys.stderr, flush=True)


if __name__ == '__main__':
    main()
