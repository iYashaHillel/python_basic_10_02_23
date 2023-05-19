

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix_2 = [
#     [1, 3, 3],
#     [4, 3, 6],
#     [7, 3, 9],
# ]
#
# result = []
# for y in range(len(matrix)):  # O(n^2)
#     result.append([])
#     for x in range(len(matrix[y])):
#         if (matrix[y][x] + matrix_2[y][x]) % 2 == 0:
#             result[y].append(matrix[y][x] + matrix_2[y][x])
#         else:
#             result[y].append(0)
#
# print(result)



# matrix = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10]
# ]
#
# target = 8
#
# left = 0
# right = len(matrix) * len(matrix[0]) - 1
#
# while left <= right:  # O(log n)
#     middle = (left + right) // 2
#     middle_value = matrix[middle // len(matrix[0])][middle % len(matrix[0])]
#     if middle_value == target:
#         print(middle // len(matrix[0]), middle % len(matrix[0]))
#         break
#     elif middle_value < target:
#         left = middle + 1
#     else:
#         right = middle - 1



# contacts = {
#     'test': 'value',
#     'test2': 'value2'
# }

# print(contacts['test'])  # O(1)

# my_list = [10, -2, 3, 4, 100]
# 0x10
# 0x10 + 2 = 0x12
# print(my_list[2])  # O(1)

# target = 100

# O(n)
# for item in my_list:  # O(n)
#     if item == target:  # O(1)
#         print('Found!')


# [1, 2, 3, 4, 5]
# 3 > 5
# [3, 4, 5]
# 4 > 5
# [5]
# 5 == 5

# import random


# my_list = [random.randint(1, 10) for x in range(15)]  # O(n)

# print(my_list)


# counter = {}

# for number in my_list:  # O(n)
#     for item in [1, 2, 3, 4, 5]:  # O(k)
#         summ = number + item
#         counter[summ] = my_list.count(summ)  # O(n)

# O(n^2 * k)

# print(my_list)
# print(counter)


import os
import time
import datetime

# print(os.getcwd())

# for i in range(10):
#     print(datetime.datetime.now())
#     time.sleep(1)
#     os.system('clear')  # Windows - cls | MacOs/Linux - clear

# folder_name = 'test1'
#
# if not os.path.exists(folder_name):
#     os.mkdir(folder_name)

# base_folder_name = 'test'
# folder_path = ''
#
# for i in range(1, 101):
#     folder_path = os.path.join(folder_path, base_folder_name + str(i))
#     os.mkdir(folder_path)

# os.removedirs('test1')

# print(os.listdir('test1'))

# for folder_name in os.listdir('test1'):

# John
# A -> 65 -> 101111110101

# utf-8
# ascii
# cp1252
# utf-16
# A -> 123 -> 111111110010111
# 101111110101 -> 32590 -> @


# f = open('test.txt', 'r')

numbers = [1, 2, 3, 4, 5]

with open('test.txt', 'w') as f:
    f.write(str(numbers))
print('...')

# lines = f.readlines()
# lines[2] = 'test'
#
# f_w.writelines(lines)
# f.write('Test')
# 'r'
# 'w'
# f.close()
# for i in range(3):
#     f.readline()
# f.write
# f.read
# 1000
# offset - 500
# limit - 100
# end - 600
# text = f.readlines()
# print(type(text))
# print(text)

# text_copy = f.readline()
# print(text_copy)
#
# text_copy = f.readline()
# print(text_copy)

