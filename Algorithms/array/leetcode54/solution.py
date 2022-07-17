from typing import List


def solution(matrix: List[List[int]]) -> List[int]:
    result = []
    if not matrix:
        return result
    left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
    while left <= right and top <= bottom:
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        for i in range(top + 1, bottom):
            result.append(matrix[i][right])
        for j in range(right, left - 1, -1):
            if top >= bottom:
                break
            result.append(matrix[bottom][j])
        for i in range(bottom - 1, top, -1):
            if left >= right:
                break
            result.append(matrix[i][left])
        left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
    print(result)
    return result


def test_cases():
    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
        ([[7], [9], [6]], [7, 9, 6]),
        ([[1, 2, 3]], [1, 2, 3]),
        ([[1]], [1]),
    ]
    for case in test_cases:
        print(f'assert {case[0]} == {case[1]}')
        assert solution(case[0]) == case[1]


if __name__ == '__main__':
    test_cases()
