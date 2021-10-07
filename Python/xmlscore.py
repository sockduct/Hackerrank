import sys
import xml.etree.ElementTree as etree


def main():
    # lines = int(input())
    lines = int(sys.stdin.readline())
    # But with this must explicitly do EOF (e.g., Ctrl-Z):
    # xmldoc = sys.stdin.read()
    xmldoc = ''.join(input() for _ in range(lines))
    root = etree.fromstring(xmldoc)
    score = sum(len(e.attrib) for e in root.iter())
    print(f'{score}')


if __name__ == '__main__':
    main()
