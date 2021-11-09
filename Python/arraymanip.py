# from array import array
from time import perf_counter

# import numpy as np

# ctypes - appears to be for interfacing with C
# Convert to C++


def arrmanip(n, queries):
    # beginfunc = perf_counter()
    # Could also use itertools.repeat(0, n)
    # This is too slow:
    arr = list([0] * n)
    # This is even slower!
    # arr = array('L', [0] * n)
    # Quite a bit slower!!!
    # arr = np.zeros(n, dtype=np.int32)
    maxval = 0

    for start, stop, inc in queries:
        # Subtract 1 from start because arrays in Python are 0-indexed, and the
        # queries are designed for 1-indexed arrays:
        '''
        # Too slow, O(n**2)
        for i in range(start - 1, stop):
            arr[i] += inc
            # Better to take hit here or do max(arr)?
            # if arr[i] > maxval:
            #    maxval = arr[i]
        print('.', end='', flush=True)
        '''
        arr[start - 1] += inc
        arr[stop] -= inc

    # res = max(arr)
    total = 0
    for i in arr:
        total += i
        if total > maxval:
            maxval = total
    # endfunc = perf_counter()
    # print(f'\nCompleted array manipulation in {endfunc - beginfunc:,.6f} seconds')

    return maxval


def main():
    beginfunc = perf_counter()
    n, m = map(int, input().split())
    queries = [list(map(int, input().split())) for _ in range(m)]
    endfunc = perf_counter()

    print(f'Read in queries in {endfunc - beginfunc:,.6f} seconds:')
    res = arrmanip(n, queries)
    print(f'{res:,}')


if __name__ == '__main__':
    main()
