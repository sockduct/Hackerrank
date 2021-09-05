'''
Validate Roman Numberals

* Valid Roman Numerals:
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000

* General Rules
  * Can have up to 3 "additive" digits
  * Can have one "subtractive" digit

* Pattern (ignore case), 1-3999 (standard form):
  * Digit 1:  M{0,3}|CM|DC{0,3}|CD|C{0,3}|XC|LX{0,3}|XL|X{0,3}|IX|VI{0,3}|IV|I{0,3}
  * Digit 2:  CM|DC{0,3}|CD|C{0,3}|XC|LX{0,3}|XL|X{0,3}|IX|VI{0,3}|IV|I{0,3}
  * Digit 3:  XC|LX{0,3}|XL|X{0,3}|IX|VI{0,3}|IV|I{0,3}
  * Digit 4:  IX|VI{0,3}|IV|I{0,3}
'''

import re

def main():
    valid_digits = 'IVXLCDM'
    digit4 = r'IX|VI{0,3}|IV|I{1,3}'
    digit3 = r'XC|LX{0,3}|XL|X{1,3}|' + digit4
    digit2 = r'CM|DC{0,3}|CD|C{1,3}|' + digit3
    digit1 = r'M{1,3}|' + digit2
    pattern = (fr'({digit1})({digit2})({digit3})({digit4})|'
               fr'({digit1})({digit2})({digit3})|({digit1})({digit2})|({digit1})')
    #pattern2 = r'^M{0,3} CM|DC{0,3}|CD|C{1,3} XC|LX{0,3}|XL|X{1,3} IX|VI{0,3}|IV|I{1,3}$'
    pattern2 = r'^M{0,3}(CM|DC{0,3}|CD|C{0,3})(XC|LX{0,3}|XL|X{0,3})(IX|VI{0,3}|IV|I{0,3})$'
    hrpattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

    string = input()

    # Challenge forces use of match
    # if re.fullmatch(pattern, string, flags=re.I):
    print(f'Match 1:  {fr"({digit1})"}:\n\t{re.match(fr"({digit1})", string, flags=re.I).groups()}')
    print(f'Match 2:  {fr"({digit1})({digit2})"}:\n\t{re.match(fr"({digit1})({digit2})", string, flags=re.I).groups()}')
    print(f'Match 3:  {fr"({digit1})({digit2})({digit3})"}:\n\t{re.match(fr"({digit1})({digit2})({digit3})", string, flags=re.I).groups()}')
    print(f'Match 4:  {fr"({digit1})({digit2})({digit3})({digit4})"}:\n\t{re.match(fr"({digit1})({digit2})({digit3})({digit4})", string, flags=re.I).groups()}')
    print(f'Match 5:  {pattern}:\n\t{re.match(pattern, string, flags=re.I).groups()}')
    print(f'Match 6:  {pattern2}:\n\t{re.match(pattern2, string, flags=re.I)}')

    if re.match(pattern, string, flags=re.I):
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    main()

