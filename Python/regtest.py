import re


def main():
    # regex_pattern = r"\d{2}\D\d{2}\D\d{4}"
    # regex_pattern = r"(?:\d{2}\D){2}\d{4}"
    # regex_pattern = r'^[a-zA-Z02468]{40}[\s13579]{5}$'
    # regex_pattern = r'^\b[aeiouAEIOU][a-zA-Z]*\b'
    # regex_pattern = r'^([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([a-zA-Z])([aeiouAEIOU])(\W)\1\2\3\4\5\6\7\8\9\10$'
    regex_pattern = r'(?<![aeiouAEIOU]).'
    # test_string = input()
    # test_string = 'ab #1?AZa ab #1?AZa '
    test_string = "1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik9ool./;p01QAZ2WSX3EDC4RFV5TGB6YHN7UJM8IK,9OL.0P;/-[\'"

    # Info
    print(f'\ntest_string length:  {len(test_string)}')

    # Evaluation #1:
    # print(f'{str(bool(re.search(regex_pattern, test_string))).lower()}')

    # Evaluation #2:
    print(f'Number of matches:  {len(re.findall(regex_pattern, test_string))}')

    # Alternative evaluations:
    # print(f'Number of matches:  {len(re.findall(regex_pattern, test_string))}')
    # print(f'{str(re.match(regex_pattern, test_string) is not None).lower()}')


if __name__ == '__main__':
    main()
