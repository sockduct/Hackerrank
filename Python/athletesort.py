from operator import itemgetter

def main():
    athletes, attributes = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(athletes)]
    key = int(input())

    matrix.sort(key=itemgetter(key))

    for line in matrix:
        # print(' '.join(str(i) for i in line))
        print(' '.join(map(str, line)))

if __name__ == '__main__':
    main()
