# -*- coding: utf8 -*-

from typing import List


def find_number_in_2D_array(matrix: List[List[int]], target: int) -> bool:
    if not matrix:
        return False
    row_len = len(matrix)
    col_len = len(matrix[0])
    i, j = 0, col_len - 1
    while i < row_len and j > -1:
        if matrix[i][j] == target:
            return True
        if matrix[i][j] < target:
            i += 1
        else:
            j -= 1
    return False


if __name__ == '__main__':
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    assert find_number_in_2D_array(matrix, 5) is True
