def tsk_10_v1(lst: list) -> list:
    lst = [x * y for x, y in zip(lst, range(len(lst)))]
    print(lst)
    return lst


def tsk_10_v2(lst: list) -> list:
    lst = list(map(lambda x, y: x * y, lst, range(len(lst))))
    print(lst)
    return lst


my_lst = [2, 4, 5, 8, 9, 13]
assert tsk_10_v1(my_lst) == [0, 4, 10, 24, 36, 65]
assert tsk_10_v2(my_lst) == [0, 4, 10, 24, 36, 65]
