def mul_k(lst: list, k: int) -> list:
    """Returns elements of input list which are multiple of input parameter"""
    if k > 0:
        return list(filter(lambda x: x % k == 0, lst))
    else:
        raise Exception("k should be greater then zero")


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(mul_k(my_list, 3))  # [3, 6, 9]
