
def solution(s: str, t: str) -> bool:
    """
    构建退格后的字符串，空间复杂度 O(M+N)
    """
    def _backspace(s: str) -> str:
        result = ''
        for i in range(len(s)):
            if s[i] != '#':
                result += s[i]
            else:
                result = result[:-1]
        return result
    return _backspace(s) == _backspace(t)


def solution_inplace(s: str, t: str) -> bool:
    s_flag = len(s) - 1
    t_flag = len(t) - 1
    s_skip = t_skip = 0
    while s_flag > -1 or t_flag > -1:
        while s_flag > -1:
            if s[s_flag] == '#':
                s_skip += 1
                s_flag -= 1
            elif s_skip > 0:
                s_skip -= 1
                s_flag -= 1
            else:
                break
        while t_flag > -1:
            if t[t_flag] == '#':
                t_skip += 1
                t_flag -= 1
            elif t_skip > 0:
                t_skip -= 1
                t_flag -= 1
            else:
                break
        if s_flag > -1 and t_flag > -1:
            if s[s_flag] != t[t_flag]:
                return False
        elif s_flag > -1 or t_flag > -1:
            return False
        s_flag -= 1
        t_flag -= 1
    return True


def test_cases():
    cases = [
        ('ab#c', 'ad#c', True),
        ('ab##', 'c#d#', True),
        ('a#c', 'b', False),
    ]
    for case in cases:
        print(f'assert {case[0]} == {case[1]}')
        assert solution(case[0], case[1]) is case[2]
        assert solution_inplace(case[0], case[1]) is case[2]


if __name__ == '__main__':
    test_cases()
