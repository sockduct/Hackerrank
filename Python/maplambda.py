def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1

    prevprev = 0
    prev = 1
    current = -1
    for i in range(3, n + 1):
        current = prevprev + prev
        prevprev = prev
        prev = current

    return current


def fibonacci(n):
    fiblist = []
    for i in range(1, n + 1):
        fiblist.append(fib(i))

    return fiblist


def main():
    n = int(input())
    cube = lambda n: n**3
    print(list(map(cube, fibonacci(n))))


if __name__ == '__main__':
    main()

