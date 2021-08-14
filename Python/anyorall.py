def is_palindrome(n):
    if n > 0 and n < 10:
        return True
    elif n < 100 and (n % 11 == 0):
        return True
    elif n > 100:
        # HR solution - slick, just flip string:
        # return str(n) == str(x)[::-1]
        num = str(n)
        halfway = len(num)//2

        return all((num[i] == num[-(i + 1)]) for i in range(halfway))

    return False


def main():
    quantity = int(input())
    numbers = list(map(int, input().split()))
    condition = False

    '''HackerRank Solution:
       print([False,any(map(lambda x: str(x) == str(x)[::-1], s))][all(map(lambda x: x > 0, s))]))

       I don't care for the clever solution of using False coerces to 0 and True
       coerces to 1, but I do like the string flipping.
    '''
    if all((n > 0) for n in numbers):
        condition = any(is_palindrome(n) for n in numbers)

    print(condition)


if __name__ == '__main__':
    main()
