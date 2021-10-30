def rotate_left(arr, count):
    '''
    In place left rotation:
    temp = arr[:count]
    arr = arr[count:]
    arr.extend(temp)
    '''

    return arr[count:] + arr[:count]


def main():
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))

    print(f'Input array:  {arr}')
    print(f'Rotated array:  {rotate_left(arr, d)}')


if __name__ == '__main__':
    main()
