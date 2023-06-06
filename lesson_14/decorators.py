import time


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


@hello_decorator
def greetings():
    print('Hello world')


greetings()
