#
# number = 10
# # text = ''
# #
# if number % 2 == 0:
#     text = 'even'
# else:
#     text = 'odd'
#
# text = 'even' if number % 2 == 0 else 'odd'
#
# print(text, type(text))
# print(f'{number} is {text}')
#
#
# number = 10
# if number == 1:
#     text = 'One'
# elif number == 2:
#     text = 'Two'
# elif number == 3:
#     text = 'Three'
# elif number == 4:
#     text = 'Four'
# elif number == 5:
#     text = 'Five'
# else:
#     text = 'Unknown'
#
# text = 'One' if number == 1 else 'Two' if number == 2 else 'Three' if number == 3 else 'Four' if number == 4 else 'Five' if number == 5 else 'Unknown'
# print(text)

# iter_count = 1

# while True:
#     print(f'Iter #{iter_count}')
#     month = int(input('Enter month: '))
#     if not 1 <= month <= 12:
#         print('Incorrect month value')
#     else:
#         break
#     print(f'End of iter #{iter_count}')
#     iter_count += 1

# month = int(input('Enter month: '))
# while not 1 <= month <= 12:
#     print('Incorrect month value')
#     month = int(input('Enter month: '))
#     if month == 404:
#         break
# else:
#     print('End!')
#
#
# print(f'Month - {month} is correct!')


# from_number = int(input('Enter from number: '))
# to_number = int(input('Enter to number: '))
# summ_type = input('Choose: even, odd, all: ')
#
# while summ_type != 'even' and summ_type != 'odd' and summ_type != 'all':
#     print('Incorrect type!')
#     summ_type = input('Choose: even, odd, all: ')
#
# current_number = from_number
# summ = 0
#
# while current_number <= to_number:
#     if summ_type == 'even' and current_number % 2 == 0:
#         summ += current_number
#     elif summ_type == 'odd' and current_number % 2 != 0:
#         summ += current_number
#     else:
#         summ += current_number
#     current_number += 1
#
# print(f'Sum even numbers from 1 to {to_number}: {summ}')

# name = ''

# if True:
#     name = 'John'
# else:
#     name = 'Unknown'
#
# print(f'Your name is {name}')

# current_number = 0
# while current_number < 10:
#     print(current_number)
#     current_number += 1

# from datetime import date


# for main_date in date(2023, 2, 1), date(2023, 3, 1):
#     print(main_date)


for name in 'Petro', 'John', 'Bob', 'Bill':
    print(f'Hello {name}!')

summ = 0
# range(5) - range(0, 5, 1) = 0, 1, 2, 3, 4
# range(0, 5) - range(0, 5, 1) = 0, 1, 2, 3, 4
# range(0, 5, 1) - range(0, 5, 1) = 0, 1, 2, 3, 4

# range(0, 10, 2) = 0, 2, 4, 6, 8

# for number in list(range(0, 20)) + list(range(60, 100)):  # range(від, до, крок)
#     print(number)
    # summ += number

# min_number = None
# 2, 3, 4, 5, 6, 7, 8, 9, 10
# for number in range(0, 10):
#     user_number = int(input(f'Enter #{number} number: '))
#     if min_number is None or min_number > user_number:
#         min_number = user_number
#
# print(f'Min number: {min_number}')
# print('end')


"""
N = 5

1.
*
**
***
****
*****
2.
*****
****
***
**
*
3. 
*****
 ****
  ***
   **
    * 
4.
    *
   **
  ***
 ****
*****
"""











