from functools import reduce
from typing import Optional


def foo(a: int, b: int, c: int) -> Optional[str]:
    if a == b == c:
        return
    if a > b and a > c:
        return '1'
    elif b > a and b > c:
        return '2'


def get_files_from_user(files_count: int):
    files = {}

    for i in range(files_count):
        file, *available_operations = input(f'File #{i}: ').lower().strip().split(' ')
        files[file] = available_operations
    return files


def check_files_permission(operations_count: int, files, operations) -> str:
    output = ''

    for i in range(operations_count):
        operation_type, file_name = input(f'Operation #{i}: ').lower().strip().split(' ')
        if operations[operation_type] in files[file_name]:
            output += 'OK\n'
        else:
            output += 'Access Denied\n'
    return output


def main():
    operations = {
        'read': 'r',
        'write': 'w',
        'execute': 'x',
    }
    files_count = int(input('File count: '))
    files = get_files_from_user(files_count)
    operations_count = int(input('Operation count: '))

    print(check_files_permission(operations_count, files, operations))


# main()

"""
global
local
nonlocal
"""


def boo():
    def bar():
        global x
        x = 3
        print('In bar func X =', x)

    x = 5
    print('Before bar execution X =', x)
    bar()
    print('After bar execution X =', x)


# x = 10
# print('Before boo execution X =', x)
# boo()
# print('After boo execution X =', x)


def sum_two_numbers(a, b):
    return a + b


def minus_two_numbers(a, b):
    return a - b


def calculator(a: int, b: int, operation) -> int:
    if not isinstance(a, int):
        raise ValueError('Type `a` must be int')
    if not isinstance(b, int):
        raise ValueError('Type `b` must be int')
    print(operation(a, b))


# calculator(2, 4, lambda a, b: a + b)
# calculator(2, 4, lambda a, b: a - b)
# calculator(2, 4, lambda a, b: a ** b)

# print(sum_two_numbers(2, 4))

# my_list = [37, 55, 65, 7, 87, 23, 19, 78, 42, 68]
# print(my_list)

students = {
    'John': {
        'total_mark': 80,
        'avg_mark': 66,
    },
    'Mark': {
        'total_mark': 30,
        'avg_mark': 10,
    },
    'Bob': {
        'total_mark': 70,
        'avg_mark': 55,
    },
}

# print(sorted(students, key=lambda x: students[x]['avg_mark'], reverse=True))

# filtered_list = list(filter(lambda x: x % 2 == 0, my_list))
# filtered_dict = list(filter(lambda x: students[x] > 50, students))
# print(filtered_dict)


my_list = [37, 55, 65, 7, 87, 23, 19, 78, 42, 68]

# new_list = []
# for number in my_list:
#     new_list.append(str(number))

# new_list = [str(number) for number in my_list]

# new_list = list(map(str, my_list))
# print(new_list)
# print('\n'.join(new_list))


# def debug_reduce(x, y):
#     print(x, y)
#     return x + y
#
#
# print(reduce(debug_reduce, [1, 2, 3, 4, 5]))





