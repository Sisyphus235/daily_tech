from typing import List


def solution(matrix: List[List[int]]) -> List[int]:
    result = []
    len_y, len_x = len(matrix), len(matrix[0])
    start_x, start_y = 0, 0
    loop = len_y // 2
    offset = 1
    while offset <= loop:
        for i in range(start_y, len_x - offset):
            result.append(matrix[start_x][i])
        for i in range(start_x, len_y - offset):
            result.append(matrix[i][len_x - offset])
        for i in range(len_x - offset, start_y, -1):
            result.append(matrix[len_y - offset][i])
        for i in range(len_y - offset, start_x, -1):
            result.append(matrix[i][start_y])
        start_x += 1
        start_y += 1
        offset += 1
    if len_y % 2 != 0:
        for i in range(start_y, len_x - offset + 1):
            result.append(matrix[start_x][i])
    print(result)
    return result


def test_cases():
    test_cases = [([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
                  ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])]
    for case in test_cases:
        print(f'assert {case[0]} == {case[1]}')
        assert solution(case[0]) == case[1]


if __name__ == '__main__':
    test_cases()
