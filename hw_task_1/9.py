def factorial(num: int) -> int:
    """Returns the factorial of input number"""
    if num < 0:
        print("Error")
    else:
        fact = 1
        while num > 0:
            fact *= num
            num -= 1
        return fact


assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(2) == 2
assert factorial(3) == 6
assert factorial(4) == 24
assert factorial(5) == 120
assert factorial(-1) is None
