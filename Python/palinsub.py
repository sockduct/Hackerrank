#! /usr/bin/env python3


from itertools import combinations
import sys


def shift(s, start, stop, inc):
    dec = ord('a')  # Code point number for letter 'a'
    letters = 26    # Number of lower case English letters

    charinc = lambda c: chr(((ord(c) + inc - dec) % letters) + dec)
    s_list = list(s)
    mod_list = [charinc(i) for i in s_list[start:stop + 1]]
    new_list = s_list[:start] + mod_list + s_list[stop + 1:]

    return ''.join(new_list)


def is_palindrome(letters):
    size = len(letters)

    if size == 1:
        return True

    mid = size // 2
    return all(letters[i] == letters[-(i + 1)] for i in range(mid))


def palindrome_subsets(s, start, stop):
    letters = s[start:stop + 1]
    number = len(letters)

    if number < 1:
        return 0
    elif number == 1:
        return 1

    # Start from 0 and add 1 for each individual letter:
    total = number
    for i in range(2, number + 1):
        total += sum(is_palindrome(c) for c in combinations(letters, i))

    return total + palindrome_subsets(letters[1:], 0, number - 1)


if __name__ == '__main__':
    verbose = len(sys.argv) == 2 and sys.argv[1] == 'verbose'
    n, q = map(int, input().split())
    s = input()

    for _ in range(q):
        query_type, *query_params = map(int, input().split())

        if query_type == 1:
            s = shift(s, *query_params)
            if verbose:
                print(f's is now "{s}"')
        else:
            res = palindrome_subsets(s, *query_params)
            print(f'{res % (10**9 + 7)}')
