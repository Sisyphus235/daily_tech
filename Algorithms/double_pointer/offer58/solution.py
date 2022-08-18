# -*- coding: utf8 -*-


def reverse_left_words(s: str, n: int) -> str:
    """
    左侧反转 + 右侧反转 + 整体反转 得到左旋字符串
    :param s:
    :param n:
    :return:
    """

    def reverse_words(s_list: list) -> list:
        if len(s_list) < 2:
            return s_list
        left, right = 0 ,len(s_list) - 1
        while left < right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        return s_list

    s_list = list(s)
    left_reverse = reverse_words(s_list[:n])
    right_reverse = reverse_words(s_list[n:])
    all_reverse = reverse_words(left_reverse + right_reverse)
    return ''.join(all_reverse)


if __name__ == '__main__':
    assert reverse_left_words('asdfdasf', 1) == 'sdfdasfa'
