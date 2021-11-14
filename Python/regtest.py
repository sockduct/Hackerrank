import re


def main():
    # regex_pattern = r"\d{2}\D\d{2}\D\d{4}"
    # regex_pattern = r"(?:\d{2}\D){2}\d{4}"
    # regex_pattern = r'^[a-zA-Z02468]{40}[\s13579]{5}$'
    regex_pattern = r'^\b[aeiouAEIOU][a-zA-Z]*\b'
    test_string = input()

    # Info
    print(f'\ntest_string length:  {len(test_string)}')

    # Evaluate:
    print(f'{str(bool(re.search(regex_pattern, test_string))).lower()}')

    # Alternative evaluations:
    # print(f'Number of matches:  {len(re.findall(regex_pattern, test_string))}')
    # print(f'{str(re.match(regex_pattern, test_string) is not None).lower()}')


if __name__ == '__main__':
    main()
