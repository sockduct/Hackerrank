'''
Input:
* n: int, m: int
* n=# of words group A (not necessarily unique)
* m=# of words group B

Goal:
* For each word in m, check if it's in A or not
  * Yes:  print index (1-based) of each occurrence space separated, -1 if none
'''

from collections import defaultdict
import sys

def main():
    groupa_count = defaultdict(int)
    groupa: List[str] = []
    groupb: List[str] = []
    key: str
    n: int
    m: int
    n, m = [int(e) for e in input().split()]

    for _ in range(n):
        key = input()
        groupa_count[key] += 1
        groupa.append(key)

    for _ in range(m):
        groupb.append(input())

    for item in groupb:
        if item in groupa_count:
            count = groupa_count[item]
            offset = 0
            indexes = []
            while count:
                index = groupa.index(item, offset)
                offset = index + 1
                # Add 1 to do 1-based indexing:
                indexes.append(index + 1)
                count -= 1
        else:
            indexes = [-1]
        print(f'{" ".join(str(e) for e in indexes)}')


if __name__ == '__main__':
    fd_open = False

    if len(sys.argv) == 2:
        fd = open(sys.argv[1])
        sys.stdin = fd
        fd_open = True

    main()

    if fd_open:
        fd.close()

