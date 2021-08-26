import re

def main():
    string = input()
    '''
    SO Solution:
        consonants = 'qwrtypsdfghjklzxcvbnm'
        vowels = 'aeiou'
        match = re.findall(r'(?<=['+consonants+'])(['+vowels+']{2,})(?=['+consonants+'])',
                           raw_input(), flags = re.I)
    '''
    pattern = r'(?i)[bcdfghjklmnpqrstvwxyz]([aeoiu]{2,})(?=[bcdfghjklmnpqrstvwxyz])'
    res = re.findall(pattern, string)
    if res:
        for match in res:
            print(match)
    else:
        print(-1)

if __name__ == '__main__':
    main()

