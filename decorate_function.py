from time import time


def decorate(fn):
    def inner(*args, **kwargs):
        print("************")
        print(fn(*args, **kwargs))
        print("************")
    return inner


@decorate
def show_name(name):
    return name


show_name(name="omi ewa")


def time_taken(function):
    def wrap(*args, **kwargs):
        t1 = time()
        result = function(*args, **kwargs)
        t2 = time()
        print(f'it took {t2 - t1:.3f}ms to execute')
        return result

    return wrap


@time_taken
def get_list(numbers):
    result = []
    for i in range(numbers):
        result.append(i)
    return result


get_list(10000000)
