def second_chance(fn):
    def wrapper(*args, **kwargs):
        count = 2
        while count:
            try:
                return fn(*args, **kwargs)
            except Exception as e:
                print('Error', e)
                count -= 1
    return wrapper


@second_chance
def exception_func():
    """ 1/2 chance to print 'OK' """
    import random
    if random.randint(0, 1):
        raise Exception('Ahaha!!!')
    else:
        print("Ok")


exception_func()
