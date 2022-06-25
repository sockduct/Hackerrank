#! /usr/bin/env python3


def shift(s, start, stop, inc):
    dec = ord('a')  # Code point number for letter 'a'
    letters = 26    # Number of lower case English letters

    charinc = lambda c: chr(((ord(c) + inc - dec) % letters) + dec)
    s_list = list(s)
    mod_list = [charinc(i) for i in s_list[start:stop + 1]]
    new_list = s_list[:start] + mod_list + s_list[stop + 1:]

    return ''.join(new_list)


def palindrome_subsets(s, start, stop):
    ...


if __name__ == '__main__':
    n, q = map(int, input().split())
    s = input()

    for _ in range(q):
        query_type, query_params = map(int, input().split())

        if query_type == 1:
            start, stop, inc = query_params
            shift(s, start, stop, inc)
        else:
            start, stop = query_params
            res = palindrome_subsets(s, start, stop)
            print(f'{res % (10**9 + 7)}')
