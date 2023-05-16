"""
Завдання 5:
Запросити користувача 5 чисел і записати їх до списку A
Записати всі числа зі списку A які більше 5 до списку C
"""

# # 1
# A = []
# C = []
# for i in range(5):
#     number = int(input(f'Enter number #{i}: '))
#     A.append(number)
#     if number > 5:
#         C.append(number)
#
# # 2
# A = [int(input(f'Enter number #{i}: ')) for i in range(5)]
# C = [x for x in A if x > 5]


contacts = {
    'John': ['+3806696653426', '+38099555235223'],
    'Bob': ['+1123121251432'],
    'Max': ['+3809585235523']
}

# if 'Max2' in contacts:
#     print(contacts['Max2'])
# else:
#     print('Контакт не знайдено!')
# print(contacts.get('Max1', 'Контакт не знайдено!'))

# new_dict = contacts.fromkeys(['Max2', 'Bob2', 'Max3'], None)
# print(new_dict)
#
# new_dict_2 = {}
# for key in new_dict:
#     new_dict_2[key] = None
# print(new_dict_2)

# print(contacts)

my_list = ['Bob', 'John', 123, 2.4, False, 2123]

# point = (1.2, -1.5, 3)
# x, y, z = point
# print(x, y, z)
# print(point[0], point[1], point[2])
#
# a = 5
# b = 10

# print(a, b)
# a, b = b, a
# tmp = a
# a = b
# b = tmp
# print(a, b)


# for idx, value in enumerate(my_list):
#     print(idx, value)

# print(contacts.items())
#
# for name, phone_numbers in contacts.items():
#     print(f'Name: {name}')
#     for number in phone_numbers:
#         print(number)


# points = [
#     (-1, 0, 1),
#     (-2, 1, 2),
#     (0, -1, -1)
# ]
# for x, y, z in points:
#     print(x, y)


# print(contacts.items())
# print(contacts.keys())
# print(contacts.values())

# new_contacts = {
#     'Ivan': '+3806681251251',
#     'Sasha': '+3809952352352',
# }
#
# print(contacts, new_contacts)
# contacts.update(new_contacts)
# contacts.update({'Max': '+38099558989999'})
# print(contacts)

# new_dict = { [1, 2, 3]: 'test' }
# new_dict = { (1, 2, 3): 'test' }
# print(new_dict[(1, 2, 3)])


numbers = {2, 100, (1, 2, 3), 1, 1, 3, 4, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6}
numbers_2 = {1, 2, 3, 101}

# print(2 in numbers_2)
# print(len(numbers_2))
# print(numbers)
# print(numbers_2)
# print(numbers_2 - numbers)
# for number in numbers:
#     print(number)

# A = {1, 2, 3}
# B = {3, 4, 5}

# print(A | B)  # A.union(B)  # A.update(B)
# print(A & B)  # A.intersection(B)  # A.intersection_update(B)
# print(A - B)  # A.difference(B)  # A.difference_update(B)
# print(A ^ B)  # A.symmetric_difference(B)  # A.symmetric_difference_update(B)

# print(A)
# A.add(10)
# A.add(4)
# A.add(1)
# A.remove(3)
# A.remove(100)
# A.discard(100)
# print(A)

# while A:
#     item = A.pop()
#     print(item)
# print(A)

# List, Dict, Set

# frozen_set = frozenset({1, 2, 3})
# A = {1, 2, 3}
# B = {3, 4, frozenset(A)}
# print(A, B)

"""
List comprehension
Dict comprehension
Set comprehension
"""
import random

# -10 to 10
# new_list = list({random.randint(-10, 10) for x in range(10)})
# print(len(new_list))
# print(new_list)

# students = {
#     'John': {
#         'mark': 100,
#         'phone_number': '+38099912124'
#     },
#     'Bob': {
#         'mark': 50,
#         'phone_number': '+38099912124'
#     }
# }

# names = ['Bob', 'John', 'Mark', 'Max', 'Sasha']

# print(random.choices(names, k=20))
# print(random.sample(names, k=20))
# import string
#
# prefix = '+38099'
# print(prefix + ''.join(random.choices(string.digits, k=7)))
# students = {
#     name: {'mark': random.randint(40, 100), 'phone_numbers': '+38099' + ''.join(random.choices(string.digits, k=7))}
#     for name in names
# }
# students = {
#     'Bob': {'mark': 97, 'phone_numbers': '+380990109146'},
#     'John': {'mark': 87, 'phone_numbers': '+380998270544'},
#     'Mark': {'mark': 94, 'phone_numbers': '+380997745214'},
#     'Max': {'mark': 82, 'phone_numbers': '+380997131403'},
#     'Sasha': {'mark': 85, 'phone_numbers': '+380995044009'}
# }
#
# new_students = {
#     x: students[x] for x in students if students[x]['mark'] >= 90
# }
# new_students = {
#     name: student_info for name, student_info in students.values() if student_info['mark'] >= 90
# }
# print(new_students)


numbers = [1, 2, 3, 4, 5, 6, 'last']

first, second, *other, last = numbers

print(first, second, other, last)

# x = numbers[0]
# y = numbers[1]
# other = numbers[2:]
# x, y, *other = numbers
# John, Kiev, 100, 90, 80, 100
# data = 'John,Kyiv,100,90,80,100,90'
# name, city, *marks = data.split(',')
# print(name, city, marks)
# print(x, y, other)

