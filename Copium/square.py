import numpy as np


def SquareArray(row, col):
    listf = [i for i in range(1, row * col + 1)]
    square = np.array(listf).reshape(row, col)
    total = 1
    total2 = 1
    print(square)
    for i in range(row):
        total *= square[i][i]
        total2 *= square[i][row - i - 1]
        # for j in i:
        #     if (j - 1) % (row + 1) == 0:
        #         total *= j
        #     if (j - 1) % (row - 1) == 0 and j - 1 != 0 and j != row * col:
        #         total1 *= j
    return total, total2


def main():
    row = int(input("row: "))
    col = int(input("col: "))
    if row != col:
        main()
    else:
        total_left, total_right = SquareArray(row, col)
        print(total_left, total_right)


if __name__ == "__main__":
    main()
