import re

def replace(match):
    string = match.group(0)
    string = 'and' if string == '&&' else 'or'
    return string


def main():
    lines = int(input())
    pattern = r'(?<= )(&&|\|\|)(?= )'

    for line in range(lines):
        string = input()
        res = re.sub(pattern, replace, string)
        # print(f'{(line + 1):>2}:  {res}')
        print(res)


if __name__ == '__main__':
    main()
