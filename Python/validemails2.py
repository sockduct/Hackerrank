from email.utils import parseaddr, formataddr
import re

def main():
    lines = int(input())
    for _ in range(lines):
        string = input()
        # Using regular expressions:
        username = r'[A-Za-z][A-Za-z0-9_.-]*'
        email = r'<[A-Za-z][A-Za-z0-9_.-]*@[A-Za-z]+\.[A-Za-z]{1,3}>'
        if res := re.match(fr'^({username})\s+({email})', string):
            # print(f'Username:  {res.group(1)}, E-mail address:  {res.group(2)}')
            print(f'{string}')

        # Using email library utility functions:
        # Doesn't appear to work so well in 3.x:
        '''
        res = parseaddr(string)
        if res != ('', ''):
            print(f'Parsed e-mail address:  {res}')
            res = formataddr(res)
            print(f'Formatted e-mail address:  {res}')
        '''

if __name__ == '__main__':
    main()

