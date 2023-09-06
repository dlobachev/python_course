def lists_intersection(a: list, b: list) -> list:
    """Returns list of common elements in a and b"""
    return list(set(a).intersection(b))


a = [1, 2, 3, 4, 5, 6, 7]
b = [2, 6, 6, 9, 112, 5]
print(lists_intersection(a, b))  # [2, 5, 6]
