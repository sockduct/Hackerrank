#! /usr/bin/env python3


'''
Note:  This relies on understanding and using segment trees.  It also relies
       on understanding how to compute the number of palindromes by making sure
       the string has 0 or 1 odd charactes and an even number of all other
       characters.  Based on this, the number of possible palindromes for a
       valid subset of characters is computable by an exponential.

       For me to complete this problem, first I'd have to get comfortable with
       segment trees, and then return to try again.  My current solution is
       completely wrong...

       See problem editorial:
       https://www.hackerrank.com/challenges/palindromic-subsets/editorial
'''

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


def palindrome_subsets(s, start, stop, minimum=1):
    letters = s[start:stop + 1]
    number = len(letters)

    if number < 1:
        return 0
    elif number == 1:
        return 1 if minimum == 1 else 0

    # Start from 0 and add 1 for each individual letter:
    total = number
    for i in range(2, number + 1):
        total += sum(is_palindrome(c) for c in combinations(letters, i))

    return total + palindrome_subsets(letters[1:], 0, number - 1, 2)


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

'''
Example test case:

Input (stdin):
15 15
bbbaccaccbacbaa
1 4 13 31
2 2 3
2 0 10
1 0 14 71
1 1 7 26
1 6 14 43
1 0 1 5
2 2 9
1 8 10 34
1 7 13 40
2 1 10
2 8 12
1 0 3 54
1 7 14 60
2 1 2

Expected Output:
2
383
27
19
5
2
'''
