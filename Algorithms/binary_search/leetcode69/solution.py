

def solution(x: int) -> int:
    left = 0
    right = x
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        target = mid * mid
        if target > x:
            right = mid - 1
        elif target <= x:
            result = mid
            left = mid + 1
    return result


def test_cases():
    cases = [
        (1, 1),
        (2, 1),
        (4, 2),
        (6, 2),
        (8, 2),
    ]
    for case in cases:
        print(
            f'assert {case[0]} == {case[1]}, actual value {solution(case[0])}')
        assert solution(case[0]) == case[1]


if __name__ == '__main__':
    test_cases()
