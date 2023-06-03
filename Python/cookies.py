#!/usr/bin/env python3

import heapq
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

class Heap:
    class HeapIterator:
        def __init__(self, wrapped):
            self.wrapped = list(wrapped)
            self.offset = 0

        def __next__(self):
            if self.offset >= len(self.wrapped):
                raise StopIteration

            item = self.wrapped[self.offset]
            self.offset += 1
            return item

    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = list(data)
            heapq.heapify(self.data)
            # Single pass iteration:
            # self.iterator = 0

    def __repr__(self):
        return f'Heap({self.data})'

    # Multi-pass Iteration:
    def __iter__(self):
        return Heap.HeapIterator(self.data)

    '''
    # Single Pass Iteration:
    def __iter__(self):
        return self

    def __next__(self):
        if self.iterator >= len(self.data):
            raise StopIteration

        item = self.data[self.iterator]
        self.iterator += 1
        return item
    '''

    @property
    def count(self):
        return len(self.data)

    @property
    def first(self):
        return self.data[0] if self.data else None

    def pop(self):
        return heapq.heappop(self.data)

    def push(self, value):
        heapq.heappush(self.data, value)


def cookies(k, A):
    # Write your code here
    # Objective:
    # * Use algorithm on jar "A"
    # * All remaining cookies must have sweetness >= k
    # * If yes, return iterations to achieve objective
    # * If no, return -1
    jar = Heap(A)
    ops = 0

    while jar.first < k and jar.count >= 2:
        first = jar.pop()
        second = jar.pop()
        sweeter = first + (2 * second)
        jar.push(sweeter)
        ops += 1

    # Check if objective met:
    return ops if all(cookie >= k for cookie in jar) else -1


if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as infile:
            for lnum, line in enumerate(infile):
                if lnum == 0:
                    n, k = map(int, line.split())
                else:
                    A = list(map(int, line.split()))
    else:
        n, k = map(int, input().split())
        A = list(map(int, input().split()))

    result = cookies(k, A)

    print(result)
