def decor_exception(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        if type(result) is not int:
            raise Exception('Output is not integer')
        else:
            return result
    return wrapper


@decor_exception
def func_1(n):
    return n ** 2


@decor_exception
def func_2(s):
    return s + " hahaha"


print(func_1(4))
print(func_2('Hello'))