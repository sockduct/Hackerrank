import re

def valid_email(email):
    if re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', email):
        return True

    return False


def main():
    n = int(input())
    emails = []

    for _ in range(n):
        emails.append(input())

    print(sorted(filter(valid_email, emails)))


if __name__ == '__main__':
    main()

