

# password = 'Admin@123'
#
# if password.isupper():
#     print('має велику літеру')
# else:
#     print('не має велику літеру')
#
#
# print( 1 / 0 )


# import requests
#
# requests.get('a:asdasdasd')

print('start')

# a = input('Enter number: ')
# b = input('Enter number: ')
# if a.isdigit():
#     a = int(a)
# else:
#     print('er...')
#
#
#
# try:
#     number = int(input('Enter your number: '))
#     print(1 / 1)
#     lists = []
#     print(lists[123])
# except Exception as e:
#     print(f'Трапилась помилка Exception. Default text: {e}')
#     number = 0

# print(number)


# number = '123'
#
# if not number.isdigit():
#     raise ValueError(f'{number} is not a number')
#
# print('end')

# if ...:
#     pass
#
#
# '' if True else ...


# numbers = []
# for i in range(5):
#     number = int(input(f'Enter number #{i}: '))
#     numbers.append(number)
# print(numbers)


# numbers = [int(input(f'Enter number #{i}: ')) for i in range(5)]
# print(numbers)


# numbers = []
# for i in range(100):
#     if i % 2 == 0:
#         numbers.append(i)
# print(numbers)
#
#
# numbers = [i for i in range(100) if i % 2 == 0]
# print(numbers)


password = 'asd123'

has_lower = [x for x in password if x.islower()]
if has_lower:
    print('+')
else:
    print('-')

