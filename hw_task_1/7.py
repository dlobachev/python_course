def count_days(years: int, months: int) -> int:
    """Returns number of days in years and months"""
    return (years * 12 + months) * 29


assert count_days(0, 0) == 0
assert count_days(1, 0) == 348
assert count_days(1, 10) == 638
