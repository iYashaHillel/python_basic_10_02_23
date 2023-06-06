

def get_numbers(n: int):
    return list(range(1, n + 1))


def new_range(n: int):
    number = 1
    while n > number:
        yield number
        number += 1
    # yield 1
    # yield 2
    # yield 3
    # yield 4
    # yield 5
    # yield 6


for i in new_range(5):
    print(i)
# print(gen)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


# f = open('example.txt')
# # print(f.readlines())
# print(f.readline())
