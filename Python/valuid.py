import re


def valid(uid):
    '''Rules:
    * Must contain at least 2 upper case letters
    * Must contain at least 3 digits
    * Must only contain alphanumberics
    * No repeating characters
    * Must be exactly 10 characters
    '''

    if len(re.findall(r'[A-Z]', uid)) < 2:
        return False

    if len(re.findall(r'\d', uid)) < 3:
        return False

    if len(re.findall(r'[^a-zA-Z\d]', uid)) > 0:
        return False

    if len(re.findall(r'([a-zA-Z\d]).*\1', uid)) > 0:
        return False

    if len(uid) != 10:
        return False

    return True


def main():
    lines = int(input())
    for _ in range(lines):
        uid = input()
        if valid(uid):
            print('Valid')
        else:
            print('Invalid')


if __name__ == '__main__':
    main()
