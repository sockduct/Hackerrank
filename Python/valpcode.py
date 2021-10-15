import re
import sys


def valpcode(code):
    '''
    * must be a number in the range from 100,000 to 999,999 inclusive
      * Create regex_integer_in_range to match this
    * must not contain more than one alternating repetitive digit pair
      * Create regex_alternating_repetitive_digit_pair to match this
      * Note:  Alternating repetitive digits are digits which repeat immediately
        after the next digit. i.e., an alternating repetitive digit pair is
        formed by two equal digits that have just a single digit between them.
        e.g.,
        * 121426 - Here, 1 is an alternating repetitive digit.
        * 523563 - Here, NO digit is an alternating repetitive digit.
        * 552523 - Here, both 2 and 5 are alternating repetitive digits.
    '''
    in_range = r'^[1-9]\d{5}$'
    digit_pair = r'(\d)(?=\d\1)'

    return bool(re.match(in_range, code) and len(re.findall(digit_pair, code)) <= 1)


if __name__ == '__main__':
    code = sys.argv[1] if len(sys.argv) > 1 else input('Postal Code:  ')
    res = valpcode(code)
    print(f'{code} valid postal code?  {res}')
