
from typing import List


def solution(fruits: List[int]) -> int:
    choices = dict()
    left = right = result = picked = 0
    while right < len(fruits):
        if fruits[right] in choices.keys():
            picked += 1
            choices[fruits[right]] = right
        else:
            if len(choices) < 2:
                choices[fruits[right]] = right
                picked += 1
            else:
                result = max(result, picked)
                drop_fruit = drop_index = None
                for fruit, index in choices.items():
                    if drop_fruit is not None and drop_index is not None and index >= drop_index:
                        continue
                    drop_fruit, drop_index = fruit, index
                choices.pop(drop_fruit)
                picked -= drop_index - left + 1
                left = drop_index + 1
                choices[fruits[right]] = right
                picked += 1
        right += 1
    return max(picked, result)


def test_cases():
    cases = [
        ([1, 2, 1], 3),
        ([0, 1, 2, 2], 3),
        ([1, 2, 3, 2, 2], 4),
        ([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4], 5),
    ]
    for case in cases:
        print(f'assert {case[0]} == {case[1]}')
        assert solution(case[0]) == case[1]


if __name__ == '__main__':
    test_cases()
