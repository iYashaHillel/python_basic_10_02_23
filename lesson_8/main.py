# n = int(input("Введiть кiлькiсть зiрочок: "))
# n += 1
# print("Трикутник №3")
# for i in range(0, n):  # 1 - n
#     print(" " * i + "*" * (n - i - 1))
# print('----')


"""
Завдання максимум на 80 балів:
Вивести трикутник #1 із шириною N за допомогою циклу for
N = 5
*****  # = '*' * 5
****   # = '*' * 4
***    # = '*' * 3
**
*

Вивести трикутник #2 із шириною N за допомогою циклу for
*     # '*' * 1
**    # '*' * 2
***   # '*' * 3
****  # '*' * 4
***** # '*' * 5

Завдання із зірочкою:
Вивести трикутник #3 із шириною N за допомогою циклу for
*****  # '*' * 5  | ' ' * 0
 ****  # '*' * 4  | ' ' * 1
  ***  # '*' * 3  | ' ' * 2
   **  # '*' * 2  | ' ' * 3
    *  # '*' * 1  | ' ' * 4

Вивести трикутник #4 із шириною N за допомогою циклу for
    *  # '*' * 1  | ' ' * 4
   **  # '*' * 2  | ' ' * 3
  ***
 ****
*****
"""

# N = 5 # int(input('> '))

# print('1.')
# for i in range(N, 0, -1):
#     print('*' * i)
#
# print('2.')
# for i in range(1, N + 1):
#     print('*' * i)
#
# print('3.')
# for i in range(N, 0, -1):
#     print(' ' * (N - i) + '*' * i)
#
# print('4.')
# for i in range(1, N + 1):
#     print(' ' * (N - i) + '*' * i)


# numbers = [1, 2, 3]

# import sys
#
# a = 1
# b = 111
#
# print(sys.getrefcount(1))  # 3 ref
#
# print(hex(id(1)))
# print(hex(id(a)))

# a = [1, 2, 3]
# print(hex(id(a)), sys.getsizeof(a))

# a += [3, 4]  # 120 -> 120 * 2 -> 240 * 2 -> 240 * 4 -> 240 * 6
# a *= 10
# print(hex(id(a)), sys.getsizeof(a))
# print(a)

# a = ['aaa', 'aab', 'aqq']
# print(ord('B'))
# print(chr(65))
# print(bin(101))
# utf-8
# cp1256
# utf-16
# asci
# numbers = [-10, 2, 1000, 5, -6, 1001]
# print(hex(id(numbers)))
# print(max(numbers))
# print(min(numbers))
# new_sorted_list = sorted(numbers, reverse=True)
# new_reversed_list = list(reversed(numbers))
# print(numbers)
# print(numbers.sort())
# numbers.reverse()
# print(numbers)
# print(hex(id(new_sorted_list)))
# print(hex(id(new_reversed_list)))
# print(hex(id(numbers)))

# numbers = [-10, 2, 1000, 5, -6, 1001, 2, 2]
# print(numbers.count(2))  # O(N)
# print(numbers)  # O(N)
# print(numbers[1])  # O(1)
# numbers.remove(2)  # O(N)
# numbers.pop(3)  # O(1)
# numbers.extend((1, 2, 3))
# numbers = numbers + [1, 2, 3]  # numbers += [1, 2, 3]
# print(numbers)


# A = [1, 2]
# B = A.copy()
# print(hex(id(A)), hex(id(B)))
#
# B.append(3)
# print(A, B)
# print(hex(id(A)), hex(id(B)))


numbers = [
    [1, 2, 3],  # 0
    [4, 5, 6],  # 1
    [7, 8, 9],  # 2
]

for i in range(0, len(numbers)):
    print(numbers[i][i])
