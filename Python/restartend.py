import re

def main():
    string = input()
    substring = input()
    pattern = fr'(?=({substring}))'
    res = re.finditer(pattern, string)

    count = 0
    for e in res:
        count += 1
        print(f'({e.start(1)}, {e.end(1) - 1})')

    if count == 0:
        print('(-1, -1)')


if __name__ == '__main__':
    main()
