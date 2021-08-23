import re

def main():
    lines = int(input())
    for _ in range(lines):
        works = True
        value = input()
        try:
            float(value)
            if re.search(r'\.[0-9]', value) is None:
                works = False
        except ValueError:
            works = False
        print(works)


if __name__ == '__main__':
    main()

