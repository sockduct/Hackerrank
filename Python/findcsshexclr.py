import re

def main():
    lines = int(input())
    for _ in range(lines):
        string = input()
        if re.match(r'[\s+{]*[\w-]+:', string):
            for i in re.finditer(r'[([{<\s]*(#[0-9A-F]{3}|#[0-9A-F]{6})\b', string, re.I):
                print(i.group(1))
    '''
    # Solution is mostly better - matches text with {}
    # Not sure if you want to match any #<hex> string - what about abc#fff,
    # is that valid?
    css = ""
    for i in range(int(raw_input())):
        css+=raw_input()
        css+='\n'

    # re.DOTALL also matches \n:
    inside_brackets = re.findall(r'\{.*?\}', css, flags=re.DOTALL)
    for property in inside_brackets:
        # Use non-capture group - not sure if this is necessary
        map(lambda i: print(i, sep='\n', end='\n'),
            (re.findall(r'#(?:[a-fA-F0-9]{3}|[a-fA-F0-9]{6})\b', property)))
    '''


if __name__ == '__main__':
    main()

