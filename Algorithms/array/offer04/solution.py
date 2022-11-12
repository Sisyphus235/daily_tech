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
