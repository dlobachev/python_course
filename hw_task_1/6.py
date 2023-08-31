def count_positive(lst: list) -> int:
    """Returns number of positive numbers in list"""
    ans = 0
    for elem in lst:
        if elem > 0:
            ans += 1
    return ans


assert count_positive([]) == 0
assert count_positive([0]) == 0
assert count_positive([1]) == 1
assert count_positive([1, 2, 3, 4, 5]) == 5
assert count_positive([-1, -2, -3, -4, -10000]) == 0
assert count_positive([1, -1, 2, -2, 0]) == 2
