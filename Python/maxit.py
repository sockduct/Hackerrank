from itertools import product

def main():
    k, m = map(int, input().split())
    rows = []

    for _ in range(k):
        _, *line = map(int, input().split())
        rows.append(line)

    combos = product(*rows)
    res = max(sum(map(lambda x: x**2, combo)) % m for combo in combos)
    print(res)


if __name__ == '__main__':
    main()
