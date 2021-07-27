from collections import deque

def main():
    deck = deque()
    num_ops = int(input())

    for _ in range(num_ops):
        line = input().split()
        if len(line) == 1:
            method = line[0]
            getattr(deck, method)()
        else:
            method, value = line
            getattr(deck, method)(value)

    print(' '.join(deck))

if __name__ == '__main__':
    main()
