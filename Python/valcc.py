import re


''' Test Data:
8
4253625879615786
4424424424442444
5122-2368-7954-3214
42536258796157867
4424444424442444
5122-2368-7954 - 3214
44244x4424442444
0525362587961578
'''

def valid(cc):
    '''Valid Credit Card:
    1) Must start with 4-6
    2) Must contain exactly 16 digits
    3) Must only contain digits (0-9)
    4) May have digits in groups of 4 seperated by a hyphen
    5) No other separators allowed
    6) Must not have 4 or more consecutive repeated digits
    '''
    # 1:
    if not re.match(r'^[4-6]', cc):
        return False
    # 2:
    if len(re.findall(r'\d', cc)) != 16:
        return False
    # 3, 5:
    if re.search(r'[^-\d]', cc):
        return False
    # 6:
    if re.search(r'(\d)-?\1-?\1-?\1', cc):
        return False
    # 4:
    if re.match(r'(\d{4}-?){3}\d{4}', cc):
        return True
    # Alternatively validate 1-5 with:
    # r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$'
    # Alternatively validate 6 by first removing hyphens and then using
    # simple regex

    return False


def main():
    count = int(input())
    for _ in range(count):
        cc = input()
        if valid(cc):
            print('Valid')
        else:
            print('Invalid')


if __name__ == '__main__':
    main()
