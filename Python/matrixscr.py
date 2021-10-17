import re


def printer(matrix):
    for row in matrix:
        print(row)


def main():
    '''
    * Process N x M grid of strings
    * Consists of alphanumeric charaters (A-Z, a-z, 0-9), spaces, and symbols
      (!, @, #, $, %, &)
    * Read from top to bottom, left to right
    * If there are symbols or multiple spaces between two alphanumeric charaters
      then replace them with a single space
    * No using if's
    '''
    # Read in N (rows) x (columns)
    rows, cols = map(int, input().split())
    matrix = [input() for _ in range(rows)]

    # print(f'\nDebug:\nn={rows}\nm={cols}\nmatrix:\n{matrix}\n')

    tmatrix = zip(*matrix)

    '''
    print('\nOriginal:')
    printer(matrix)
    print('\nTransposed:')
    printer(tmatrix)
    '''

    string = ''.join(''.join(row) for row in tmatrix)
    fixed = re.sub(r'([A-Za-z0-9])[ !@#\$%&]+([A-Za-z0-9])', r'\1 \2', string)
    # Alternate (untested) pattern:  r'(?<=[A-Za-z0-9])([^A-Za-z0-9]+)(?=[A-Za-z0-9])'

    print(f'{fixed}')


if __name__ == '__main__':
    main()
