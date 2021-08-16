import numpy as np

def main():
    lines, cols = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(lines)]
    matrix = np.array(data)
    res = np.max(np.min(matrix, axis=1))
    print(res)

if __name__ == '__main__':
    main()

