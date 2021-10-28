def hglist(arr):
    size = 6
    hgres = []

    for row in range(size - 2):
        for col in range(size - 2):
            hgres.append(sum(arr[row][col:col + 3]) + arr[row + 1][col + 1] +
                         sum(arr[row + 2][col:col + 3]))

    return hgres


def arrstr(arr, colwidth=3):
    size = 6
    res = ''

    for row in arr:
        for col in row:
            res += f'{col:>{colwidth}}'
        res += '\n'

    return res


def main():
    matrix = [list(map(int, input().split())) for _ in range(6)]

    '''
    print(f'\n{arrstr(matrix)}')
    res = hglist(matrix)
    hgmatrix = [res[step:step + 4] for step in range(0, 13, 4)]
    print(f'{arrstr(hgmatrix, 4)}')
    '''
    print(f'{max(hglist(matrix))}')


if __name__ == '__main__':
    main()
