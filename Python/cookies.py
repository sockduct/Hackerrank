#!/usr/bin/env python3

import heapq

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

class Heap:
    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = list(data)
            heapq.heapify(self.data)

    def __repr__(self):
        return f'Heap({self.data})'

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
    jar = Heap(A)
    ops = 0

    while jar.first <= k and jar.count >= 2:
        first = jar.pop()
        second = jar.pop()
        sweeter = first + (2 * second)
        jar.push(sweeter)
        ops += 1

    return ops

if __name__ == '__main__':
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    result = cookies(k, A)

    print(result)
