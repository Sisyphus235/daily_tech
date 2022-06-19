

def isPerfectSquare(self, num: int) -> bool:
    left = 0
    right = num
    while left <= right:
        mid = left + (right - left) // 2
        target = mid * mid
        if target == num:
            return True
        elif target > num:
            right = mid - 1
        else:
            left = mid + 1
    return False
