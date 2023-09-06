def filter_str_args(*args) -> tuple:
    """Returns tuple of args with str type"""
    ans = []
    for item in args:
        if isinstance(item, str):
            ans.append(item)
    return tuple(ans)


total = ['abc', 1, 2, 3, 'def', 'ghi', [1], 0]
print(filter_str_args(*total))  # ('abc', 'def', 'ghi')
