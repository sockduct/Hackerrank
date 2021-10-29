def main():
    lastAnswer = 0
    ns, qs = map(int, input().split())
    arr = [[] for _ in range(ns)]

    for _ in range(qs):
        q, x, y = map(int, input().split())

        idx = (x ^ lastAnswer) % ns
        if q == 1:
            arr[idx].append(y)
        else:
            lastAnswer = arr[idx][y % len(arr[idx])]
            print(f'{lastAnswer}')


if __name__ == '__main__':
    main()
