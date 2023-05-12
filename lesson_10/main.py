

# print('10 2 3 5 6 7124 23'.split(' '))
#
# if '10' > '2':
#     print('10 is greater than 2')

# A = [1, 2, 3, 4]
#
# print(A)
#
# print(' '.join([str(x) for x in A]))
# print(*A)
#
# for i in A:
#     print(i)

import random

# A = [random.randint(-10, 10) for i in range(10)]
# B = [-3, 4, 9, 2, 2, 3, 7, 6, 5, -8]
#
# D = []
# for x in B:
#     if x >= 0:
#         D.append(x)
#
# C = [x for x in B if x >= 0]  # B.copy()
#
# print(B, hex(id(B)))
# print(C, hex(id(C)))

# numbers = '10 2 3 5 6 7124 23'.split(' ')
#
# print(numbers)

# real_numbers = []
# for x in numbers:
#     real_numbers.append(int(x))


# real_numbers = [int(x) for x in numbers]

# real_numbers = [x for x in real_numbers if x % 2 == 0]
# _
# [10, 2, 6, 7124] -> '10_2_6_7124'

# print('_'.join([str(x) for x in real_numbers]))
# print(real_numbers)

import sys


# list_numbers = [random.randint(-100, 100) for x in range(10)]
# tuple_numbers = tuple(list_numbers)
#
# print(hex(id(tuple_numbers)))
# print(tuple_numbers)
# numbers = list(tuple_numbers)
# numbers.pop()
# numbers.pop()
# numbers.pop()
# numbers.pop()
# tuple_numbers = tuple(numbers)
# print(hex(id(tuple_numbers)))
# print(tuple_numbers)


# print(sys.getsizeof(tuple_numbers))
# print(sys.getsizeof(list_numbers))

# A = (1, 2, 3, 4)  # tuple
#
# print(A)
#
# print(tuple('Hello'))

# Error
# A.append(5)
# A.insert(1, 5)
# A.pop()

# print(A[::-1])
# print(tuple(reversed(A)))
# print(A.index(10))
# A.count()
# print(10 in A)


# test_tuple = ('123', False, 2.5, 2, [1, 2, 3, 4], 'Hello world')
# new_tuple = (1,)
# print(type(new_tuple))

# A = '123'
# A = '456'
#
# B = [1, 2, 3]
# B += [4, 5]
# B.append(6)

# print(test_tuple)
# try:
#     # test_tuple[4] += [4, 5]
#     test_tuple[4].extend([4, 5])
# except TypeError as e:
#     print(e)
# print(test_tuple)

# print(sys.getsizeof(test_tuple), sys.getsizeof(test_tuple[4]))
# test_tuple[4].extend([4, 5, 5, 6, 7, 8, 9, 10, 123] * 10)
# print(sys.getsizeof(test_tuple), sys.getsizeof(test_tuple[4]))

# key:value, key2:value2
contacts = {
    'John': ['+380669995554', '+380991245125'],
    'Bob': ['+123124125124'],
}

students = {
    'John': {
        'Full Name': 'John John',
        'Phone number': '+3806669555555',
        'Mark': 99
    },
    'Bob': {
        'Full Name': 'asdasd',
        'Phone number': '+112312412512',
        'Mark': 79
    },
}

while True:
    choice = input('> ')
    if choice == '1':
        name = input('Enter your name: ')
        full_name = input('Enter your full name: ')
        phone_number = input('Enter your full name: ')
        mark = int(input('Enter your mark: '))
        students[name] = {
            'Full Name': full_name,
            'Phone number': phone_number,
            'Mark': mark
        }
    elif choice == '2':
        break
    elif choice == '3':
        print(students)
    elif choice == '4':
        print('Delete student')
        name = input('Enter students name: ')
        if name in students:
            item = students.pop(name)
            print(f'{item["Full Name"]} deleted!')
        else:
            print(f'{name} not found!')

print(students['Bob']['Phone number'])

print(contacts)
# contacts['Petr'].append('+380556645645')
print('Petr' in contacts)
if 'Petr' not in contacts:
    contacts['Petr'] = ['+380556645645']
else:
    contacts['Petr'].append('+380556645645')
# contacts['Bob'] = ['+123124555555']
print(contacts)

