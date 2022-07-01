import re

def findlinks(html):
    entries = []
    pattern = r'<\s*a\s*href\s*=\s*"([^"]*)"\s*>(?:<[^>]*>)*([^<]*)(?:<[^>]*>)*<\s*/a\s*>'

    for line in html:
        res = re.findall(pattern, line, re.I)
        if res:
            entries.extend(res)

    return entries

def main():
    lines = int(input())
    html = [input() for _ in range(lines)]

    res = findlinks(html)
    for link, title in res:
        print(f'{link.strip()},{title.strip()}')

if __name__ == '__main__':
    main()
