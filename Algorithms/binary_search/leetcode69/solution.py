

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


def newton_solution(x: int) -> int:
    c, x0 = float(x), float(x)
    while True:
        xi = 0.5 * (x0 + c/x0)
        if abs(x0 - xi) < 1e-7:
            break
        x0 = xi
    return int(x0)


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
        assert newton_solution(case[0]) == case[1]


if __name__ == '__main__':
    test_cases()
