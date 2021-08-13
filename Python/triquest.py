from itertools import repeat

def main():
    for i in range(1, int(input())):
        # Can't use another for...
        # print(sum((i * 10**j) for j in range(i)))
        print(sum(map(lambda t: t[1] * 10**t[0], (enumerate(repeat(i, i))))))

if __name__ == '__main__':
    main()

