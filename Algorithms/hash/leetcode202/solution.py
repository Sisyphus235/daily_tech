# -*- coding: utf8 -*-


def is_happy(n: int) -> bool:
    def get_sum(n: int) -> int:
        total = 0
        while n > 0:
            total += n % 10
            n = n // 10
        return total
    record = []
    while n != 1:
        n = get_sum(n)
        if n in record:
            return False
        else:
            record.append(n)
    return True