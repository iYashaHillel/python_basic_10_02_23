import time

print('hello')

def hello_decorator(func):

    def inner():
        print("Hello, this is before function execution")
        func()
        print("This is after function execution")

    return inner


def timeit(func):

    def inner(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print(time.time() - start)
        return res

    return inner


def logit(func):

    def inner(*args, **kwargs):
        print('Function name:', func.__name__)
        print('Args:', args)
        print('Kwargs:', kwargs)
        try:
            res = func(*args, **kwargs)
            print('Result:', res)
            return res
        except Exception as e:
            print('Error:', e)

    return inner


@logit
def some_func(a, b):
    if not isinstance(a, int):
        raise ValueError('Type `a` must be int')
    if not isinstance(b, int):
        raise ValueError('Type `b` must be int')
    return a + b


@timeit
def greetings():
    print('Hello world')


@timeit
def some_math_func(n: int):
    start_time = time.time()
    res = 1
    for i in range(n):
        res **= i
    print(time.time() - start_time)
    return res

some_func('1', 2)
# some_math_func(n=10000000)
#
# greetings()
#
# some_math_func(10000000)
#
# some_math_func(10000000)
#
#
