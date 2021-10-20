import numpy as np


def shape_demo():
    arr1d = np.array([1, 2, 3, 4, 5])
    print(f'1D Array:  {arr1d}')

    arr2d = np.array([[1, 2], [3, 4], [5, 6]])
    print(f'2D Array:\n{arr2d}')

    arr3 = np.array([1, 2, 3, 4, 5, 6])
    print(f'1D Array:  {arr3}')

    arr3.shape = (3, 2)
    # Or:  np.resahpe(arr3(3, 2))
    print(f'Reshaped:\n{arr3}')


def main():
    # shape_demo()
    arr = np.array(input().split(), int)
    arr.shape = (3, 3)
    print(f'{arr}')


if __name__ == '__main__':
    main()
