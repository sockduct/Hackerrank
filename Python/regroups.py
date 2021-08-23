import re

def main():
    string = input()
    # Name the capture group:
    # res = re.match(r'(?P<target>[0-9a-zA-Z])\1', string)
    res = re.search(r'([0-9a-zA-Z])\1', string)

    # Leverage capture group name - but only works if capture group matched
    # something:
    # if 'target' in res.groupdict():
    if res:
        print(res.group(1))
    else:
        print('-1')

if __name__ == '__main__':
    main()

