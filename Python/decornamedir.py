from collections import namedtuple
from functools import wraps
from operator import itemgetter


def dirfmt(func):
    @wraps(func)
    def inner(directory):
        new_directory = []

        for person in directory:
            title = 'Mr.' if person.sex == 'M' else 'Ms.'
            new_directory.append((title, person))

        return func(new_directory)
    return inner


@dirfmt
def printer(directory):
    for title, person in directory:
        print(f'{title} {person.first} {person.last}')


def main():
    lines = int(input())
    # Person = namedtuple('Person', ['first', 'last', 'age', 'sex', 'title'])
    # Just because problem asks to use a decorator - use that for title
    Person = namedtuple('Person', ['first', 'last', 'age', 'sex'])
    directory = []

    for _ in range(lines):
        data = input().split()
        data[2] = int(data[2])
        directory.append(Person(*data))

    directory.sort(key=itemgetter(2))
    printer(directory)


if __name__ == '__main__':
    main()
