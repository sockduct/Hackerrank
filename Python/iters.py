from itertools import combinations

def main():
    target_letter = 'a'
    count = 0
    total = 0

    list_len = int(input())
    letter_list = ''.join(input().split())
    rlen = int(input())

    res = combinations(letter_list, rlen)

    for e in res:
        total += 1
        if target_letter in e:
            count += 1

    print(f'{count/total}')


if __name__ == '__main__':
    main()
