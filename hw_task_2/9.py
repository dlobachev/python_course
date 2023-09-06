import datetime as dt


def time_of_function(fn):
    def wrapped(*args, **kwargs):
        start_time = dt.datetime.now()
        res = fn(*args, **kwargs)
        print(f'Time of function: {dt.datetime.now() - start_time}')
        return res
    return wrapped


@time_of_function
def func(n):
    ans = 0
    for i in range(n+1):
        ans += i
    return ans


print(func(100000000))
