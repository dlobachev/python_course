def max_length(list_1, list_2) -> int:
    """Return length of the longest list -> int"""
    return max(len(list_1), len(list_2))


assert max_length([], []) == 0
assert max_length([], [0]) == 1
assert max_length([], [0, 1]) == 2
assert max_length([1, 0], [0, 1]) == 2
assert max_length(['wwdawdas'], [0, 1]) == 2
