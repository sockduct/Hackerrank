from functools import wraps
import re


def stdfmt(func):
    '''
    * Standard number format:  +91 ##### #####
    * Numbers may start with +91, 91, 0, or no prefix but will all be converted
      to use the above format
    '''
    @wraps(func)
    def inner(nums):
        fmtnums = []

        for num in nums:
            res = re.search(r'^(?:\+?91|0)?(\d{10})', num).group(1)
            fmtnums.append(f'+91 {res[:5]} {res[5:]}')
            # Alternatively - just grab last 10 digits:
            # "+91" + " " + number[-10:-5] + " " + number[-5:]

        return func(fmtnums)
    return inner


# Update numbers to standard format
@stdfmt
def numsort(nums):
    # Sort the numbers in ascending order
    return sorted(nums)


def main():
    nums = int(input())
    num_list = [input() for _ in range(nums)]

    for num in numsort(num_list):
        print(num)


if __name__ == '__main__':
    main()
