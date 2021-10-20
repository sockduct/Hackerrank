import numpy as np


def main():
    narray = np.array(input().split(), float)
    # print(f'Forward:  {narray}')
    # print(f'Reverse:  {narray[::-1]}')
    # Alternatively:  np.flipud(narray)
    print(f'{narray[::-1]}')


if __name__ == '__main__':
    main()
