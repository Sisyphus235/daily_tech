# -*- coding: utf8 -*-


def reverse_words(s: str) -> str:
    def remove_space(s: str) -> list:
        res = []
        i = 0
        while i < len(s):
            if s[i] != ' ':
                break
            i += 1
        while i < len(s):
            if s[i] != ' ':
                res.append(s[i])
            elif res[-1] != ' ':
                res.append(s[i])
            i += 1
        if res[-1] == ' ':
            res.pop(-1)
        return res

    def reverse_string(s: list, left: int, right: int):
        while left < right:
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
            left += 1
            right -= 1

    def reverse_word(s: list):
        start, end = 0, 0
        while start < len(s):
            while end < len(s) and s[end] != ' ':
                end += 1
            reverse_string(s, start, end - 1)
            start = end + 1
            end += 1

    s_list = remove_space(s)
    reverse_string(s_list, 0, len(s_list) - 1)
    reverse_word(s_list)
    return ''.join(s_list)


if __name__ == '__main__':
    assert reverse_words('the sky is blue') == 'blue is sky the'
    assert reverse_words('  hello world  ') == 'world hello'
    assert reverse_words('a good   example') == 'example good a'
