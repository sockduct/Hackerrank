import numpy as np


'''
Numpy axes:
                  Axis 1: ====>
        |  R/C  | col 1 | col 2 | ...   |
        |-------+-------+-------+-------+
Axis 0: | row 1 |       |       |       |
  ||    --------+-------+-------+-------+
  ||    | row 2 |       |       |       |
  \/    --------+-------+-------+-------+
        | ...   |       |       |       |
        --------+-------+-------+-------+

* In an array, axis 0 is the "first" axis and axis 1 is the "second" axis
  * This follows 0-based indexing, the first axis is numbered 0
* In a 2D array, axis 0 runs down along the rows (see above)
  np.concatenate([np.array([[1,2], [3,4]]), np.array([[5,6], [7,8])])], axis=0)
  [[1 2],
   [3 4],
   [5 6],
   [7 8]]
   Note:  axis=0 is the default if it's omitted
* In a 2D array, axis 1 runs across the columns (see above)
  np.concatenate([np.array([[1,2], [3,4]]), np.array([[5,6], [7,8])])], axis=1)
  [[1 2 5 6],
   [3 4 7 8]]
* In a 1D array, there is only one axis - 0, using axis 1 is an error
  * Because there is only 1 axis, axis 0 acts like axis 1 in a 2D array:
    np.concatenate([np.array([1,2]), np.array([3,4])])
    [1 2 3 4]

Numpy features:
* Concatenation:
  array_1 = np.array([1,2,3])
  array_2 = np.array([4,5,6])
  array_3 = np.array([7,8,9])

  np.concatenate((array_1, array_2, array_3))
  [1 2 3 4 5 6 7 8 9]

Reference:  https://www.sharpsightlabs.com/blog/numpy-axes-explained/
'''
def main():
    rows1, rows2, cols = map(int, input().split())
    matrix1 = np.array([list(map(int, input().split())) for _ in range(rows1)])
    matrix2 = np.array([list(map(int, input().split())) for _ in range(rows2)])

    print(f'{np.concatenate([matrix1, matrix2])}')


if __name__ == '__main__':
    main()
