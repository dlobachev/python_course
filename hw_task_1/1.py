def string_length(s="") -> int:
    """Return the length of input string -> int"""
    return len(s)


assert string_length() == 0
assert string_length("") == 0
assert string_length("1") == 1
assert string_length("kkk") == 3
assert string_length("''") == 2
assert string_length("/?'|<>{}][") == 10
