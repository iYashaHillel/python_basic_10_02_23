
"""
N - int

1 - N + 1

i % 5 == 0 - Fizz
i % 7 == 0 - Bizz
i % 5 == 0 and i % 7 == FizzBizz
i

N = 10

1
2
3
...
8
9
10
"""

# N = int(input('N: '))
#
# for i in range(1, N + 1):
#     if i % 5 == 0 and i % 7 == 0:
#         print('FizzBizz')
#     elif i % 5 == 0:
#         print('Fizz')
#     elif i % 7 == 0:
#         print('Bizz')
#     else:
#         print(i)

# print( (not(4 % 5)) * 'Fizz' + (not(4 % 7)) * 'Bizz' or 4 )  # 5 % 5 == 0
# print( '' or 4 )  # None, '', False

# for i in range(1, N + 1):
#     print( (not(i % 5)) * 'Fizz' + (not(i % 7)) * 'Bizz' or i )


# text = 'hello world, hello John!'

# text.replace('o', '0')
# print(text)

# numbers = '123, 2, -4, 5, 10'
#
#
# for i in numbers.split(','):
#     print(int(i))


# print('hello1'.upper())
# print('HeLLo world ß'.lower())
# print('HeLlO world'.capitalize())
# print('HeLlO world'.title())
# print('HeLlO world ß'.casefold())
# print('HeLlO world'.swapcase())


# message = '____Hello world________'
# print(message)
# print(message.strip('_'))
# print(message.lstrip())
# print(message.rstrip())

# print('4'.ljust(4, '_'))
# 0004

# numbers = '123, 2, 4, 5, 10'
#
#
# for i in numbers.split(', '):
#     print(i.rjust(5, '0'))


# count

# text = 'hello worldooooooo'
#
# index = text.find('o')
# while index != -1:
#     index = text.find('o', index + 1)
#     print(index)
# print(text.find('lo'))
# print(text.count('o', 5, 12))

# number = '123'
# output - 321

# anna

# print(number[::-1])
# print(number % 10)
# print(int((number / 10) % 10))
# print(number // 100)


# number = 5

# print('Yes' if number % 2 == 0 else 'No')

# text = 'Hello world'
# print(text[::-1])

# numbers = [1, False, 2.5, -1, 4, 5, 19, 'test']
# print(numbers)
# numbers.append(10)
# numbers.append(15)
# numbers.insert(1, 'Hello')
# print(numbers[2.5])
# import math
# print(int(5 / 2))
# print(round(5 / 2))  # 2.6
# print(math.floor(5 / 2))
# print(math.ceil(5 / 2))
# print(5 // 2)
# numbers.insert(len(numbers) // 2, 'Middle')
# print(numbers)

# numbers[0], numbers[1] = 123, 124

# print(numbers[:4])
# numbers = numbers[::-1]
# print(numbers)
# numbers[0] = 123
# numbers[-1] = 123
# print(numbers)

# print(len(numbers))

# for i in numbers:
#     print(i)

# CRUD
# Create
# Read
# Update
# Delete

# numbers = []
#
# for i in range(10):
#     tmp = input(f'Enter #{i + 1} number: ')
#     while not tmp.isdigit():
#         tmp = input(f'Enter #{i + 1} number: ')
#     numbers.append(int(tmp))
#
# print(numbers)


# print([1, 2] + [3, 4, 5])
# print([1, 2] * 5)

# numbers = [1, 2, 3, 4, 5, 4, 4, 4, 4]

# print(4 in numbers)
# print(10 not in numbers)
# print(numbers.count(True))
# print(numbers.count(False))
# print(numbers.index(4))

# Enter #1 number:
# Enter #2 number:
# Enter #3 number:
# Enter #4 number:
# Enter #5 number:
# Enter #6 number:
# Enter #... number:
# Enter #10 number:


# i = 0
# while i < 10:
#     i += 1
#     print(i)


# print([1, 1, 3] > [2, 1, 10])
# print([1, 1, 3] < [2, 1, 10])
# print([15, 1, 3] > [2, 1, 10, 1000, 40000])
# print([2, 1] >= [1, 20])
# print([2, 100] >= [2, 20])
# print([2, 20, 200, 70] >= [2, 20, 200, 60])

