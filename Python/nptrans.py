import numpy as np


'''
Numpy features:
* Transpose array:
  my_array = numpy.array([[1,2,3],
                          [4,5,6]])
  numpy.transpose(my_array)
  [[1 4]
   [2 5]
   [3 6]]
* Flatten array:
  my_array = numpy.array([[1,2,3],
                          [4,5,6]])
  my_array.flatten()
  [1 2 3 4 5 6]
'''
def main():
    # Input N rows x M cols array
    rows, cols = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(rows)]
    nparr = np.array(matrix)

    # print(f'\nOriginal:\n{nparr}')
    # print(f'\nTransposed:\n{np.transpose(nparr)}')
    # print(f'\nFlattened:\n{nparr.flatten()}')

    # Per challenge specs:
    print(f'{np.transpose(nparr)}')
    print(f'{nparr.flatten()}')


if __name__ == '__main__':
    main()
