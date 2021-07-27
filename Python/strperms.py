# Input:  str int

from itertools import permutations

def main():
    S: str
    r: int
    line: List[str] = input().split()
    S, r = line[0], int(line[1])

    res = permutations(S, r)
    res = [''.join(e) for e in res]
    res.sort()

    for e in res:
        print(e)

if __name__ == '__main__':
    main()

