# import random


# print(random.randint(1, 10))

# name = 'John'
# print('Hello ' + name)
#
# print('#####', '#####' + '#####' + '#####', sep='\n')
# '####################'
# print('#\n#####\n' * 5)

# text = 'asjkdausfioquwrioquwroiqwrtuioqwr  '
#
# print(len(text))
#
# reports = [1, 2, 3, 4, 5, 6]
# done_reports = [1, 2, 3]

#       01234567891011
# text = 'Hello world!'
# card = '1111 1111 1111 1234'

# print(len(text))
# print( text[0] )
# print( text[14] )
# print( text[-2] )
# print( text[len(text) - 4]
#        + text[len(text) - 3]
#        + text[len(text) - 2]
#        + text[len(text) - 1] )

# range(від, до, крок) # 0, 1, 2, 3 ,4 ,5, 6, 7, 8, 9
# print(text[0:len(text):2])
# print(text[len(text):0:-1])
# print(text[5:])
# print(text[:5])
# print(text[::-1])

# text = 'Hello world world'
# print( len(text) )  # Функція
# print( text.find('w', 7, 12) )  # Метод
# print( text.rfind('w', 7, 12) )  # Метод
# print( text[6] )
# print(text.find('123'))
# print(text.index('123'))

# url = 'https://google.com'
#
# find_is_valid_url = url.find('https') != -1 and url.find('.com') != -1
# is_valid_url = url.startswith('https') and url.endswith('.com')
#
# print(f'Find: {find_is_valid_url}')
# print(f'swith: {is_valid_url}')


# string = '-12345'

# if string[0] == '-' and string[1:].isdigit():
#     number = int(string)
# elif string.isdigit():
#     number = int(string)
# else:
#     print('Error')

# print('Hello world'.isalpha())
# print('h1'.islower())
# print('H1'.isupper())


"""
replace
split
strip
join
count
"""

text = 'Hello world'
# print( text.replace('l', '1').replace('o', '0') )

# for i in range(0, len(text)):
#     print(i,'-',text[i])

"""
1) Len - 10
2) Upper
3) Lower
4) Number
5) Spec symbols (+, -, =, ., _, ,)
"""

password = '123456789011G'  # 'simplepassword'

if len(password) < 11:
    print('Error!')
    exit()

has_upper = False

for char in password:  #
    if char.isupper():
        has_upper = True

if not has_upper:
    print('Error.')
    exit()

print('Ok!')
