#! /usr/bin/env python3


from locatableheap import LocatableHeap as lheap
import sys
import time


def process_queries1(heap, locators):
    match list(map(int, input().split())):
        case [1, value]:
            # Add value to heap
            locators[value] = heap.add(value)
        case [2, value]:
            # Delete arbitrary value from heap
            if value == heap.min():
                heap.remove_min()
                locators.pop(value)
            else:
                locator = locators.pop(value)
                heap.remove(locator)
        case [3]:
            print(f'{heap.min().value}')
        case _:
            raise ValueError(f'Unexpected value')


def process_queries2(heap, locators):
    command, *value = map(int, input().split())
    if command == 1:
        # Add value to heap
        locators[value[0]] = heap.add(value[0])
    elif command == 2:
        # Delete arbitrary value from heap
        if value[0] == heap.min():
            heap.remove_min()
            locators.pop(value[0])
        else:
            locator = locators.pop(value[0])
            heap.remove(locator)
    elif command == 3:
        # Per source code can use heap[0] to see smallest item on heap:
        print(f'{heap.min().value}')
    else:
        raise ValueError(f'Unexpected value "{command}"')


def main():
    stdin = None
    if len(sys.argv) == 2:
        stdin = sys.stdin
        sys.stdin = open(sys.argv[1])

    start_time = time.time()
    count = 0
    heap = lheap()
    locators = {}
    skip = True

    queries = int(input())
    for _ in range(queries):
        # Choose one:
        if sys.version_info.minor >= 10 and not skip:
            process_queries1(heap, locators)
        else:
            process_queries2(heap, locators)

        '''
        count += 1
        if count == 50_000:
            print(f'\nRun time:  {(time.time() - start_time):.3f} seconds', file=sys.stderr, flush=True)
        '''

    print(f'\nRun time:  {(time.time() - start_time):.3f} seconds', file=sys.stderr, flush=True)


if __name__ == '__main__':
    main()
