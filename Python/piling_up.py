from collections import deque
import sys


def stackable(cube_deque):
    stack = []
    iterations = len(cube_deque)

    for _ in range(iterations):
        if stack:
            if cube_deque[0] >= cube_deque[-1] and cube_deque[0] <= stack[-1]:
                stack.append(cube_deque.popleft())
            elif cube_deque[-1] >= cube_deque[0] and cube_deque[-1] <= stack[-1]:
                stack.append(cube_deque.pop())
            else:
                break
        # Pick largest to start
        else:
            if cube_deque[0] > cube_deque[-1]:
                stack.append(cube_deque.popleft())
            else:
                stack.append(cube_deque.pop())

    if len(cube_deque) > 0:
        print('No')
    else:
        print('Yes')


def main():
    if len(sys.argv) == 2:
        infile = sys.argv[1]

        infd = open(infile)
        sys.stdin = infd

    test_cases = int(input())

    for _ in range(test_cases):
        num_cubes = int(input())
        cube_lengths = map(int, input().split())
        cube_deque = deque(cube_lengths)

        stackable(cube_deque)


if __name__ == '__main__':
    main()
