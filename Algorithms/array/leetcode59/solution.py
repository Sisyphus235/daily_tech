from typing import List


def solution(n: int) -> List[List[int]]:
    nums = [[0] * n for _ in range(n)]
    start_x, start_y, count = 0, 0, 1  # 起始 x, y 坐标和填充起始值
    loop, mid = n // 2, n // 2  # 按圈填入数字，中心点位置
    for offset in range(1, loop + 1):
        for i in range(start_y, n - offset):  # 从左到右，不包括右上顶点
            nums[start_x][i] = count
            count += 1
        for i in range(start_x, n - offset):  # 从上到下，不包括右下顶点
            nums[i][n - offset] = count
            count += 1
        for i in range(n - offset, start_y, -1):  # 从右至左，不包括左下顶点
            nums[n - offset][i] = count
            count += 1
        for i in range(n - offset, start_x, -1):  # 从下至上，不包括左上顶点
            nums[i][start_y] = count
            count += 1
        start_x += 1
        start_y += 1
    if n % 2 != 0:  # 奇数时填充中心点
        nums[mid][mid] = count
    return nums


def solution1(n: int) -> List[List[int]]:
    matrix = [[0] * n for _ in range(n)]
    num = 0
    left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
    while left <= right and top <= bottom:
        for j in range(left, right + 1):
            num += 1
            matrix[top][j] = num
        for i in range(top + 1, bottom):
            num += 1
            matrix[i][right] = num
        for j in range(right, left - 1, -1):
            if top >= bottom:
                break
            num += 1
            matrix[bottom][j] = num
        for i in range(bottom - 1, top, -1):
            if left >= right:
                break
            num += 1
            matrix[i][left] = num
        left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
    return matrix


def test_cases():
    test_cases = [(3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]), (1, [[1]])]
    for case in test_cases:
        print(f'assert {case[0]} == {case[1]}')
        assert solution(case[0]) == case[1]
        assert solution1(case[0]) == case[1]


if __name__ == '__main__':
    test_cases()
