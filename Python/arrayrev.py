from array import array


def reverseArray(arr):
    # Guard:
    if len(arr) < 2:
        return arr

    if isinstance(arr, array):
        revarr = array(arr.typecode)
        revitr = False
        chgtype = False
    elif isinstance(arr, list):
        revarr = []
        revitr = True
        chgtype = False
    elif isinstance(arr, tuple):
        revarr = []
        revitr = False
        chgtype = True
    else:
        raise TypeError('Expected array.array, list, or tuple')

    if revitr:
        for i in arr.__reversed__():
            revarr.append(i)
    else:
        for i in range(len(arr) - 1, -1, -1):
            revarr.append(arr[i])

    if chgtype:
        revarr = tuple(revarr)

    return revarr


def main():
    # Either array.array, list, or tuple:
    # container_type = 'array'
    # container_type = 'list'
    container_type = 'tuple'
    arr_size = int(input())
    arr_input = map(int, input().split())

    if container_type == 'array':
        arr_type = 'i'  # signed int
        arr = array(arr_type, arr_input)
    elif container_type == 'list':
        arr = list(arr_input)
    elif container_type == 'tuple':
        arr = tuple(arr_input)
    else:
        raise TypeError('Expected container_type of array, list, or tuple')

    revarr = reverseArray(arr)

    print(' '.join(str(i) for i in revarr))


if __name__ == '__main__':
    main()
