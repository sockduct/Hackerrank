import re

def main():
    lines = int(input())
    for _ in range(lines):
        string = input()
        if re.match(r'^[789]\d{9}$', string):
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    main()

