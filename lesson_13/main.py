import pickle
import json


# a = ['Hello', 'world']
# b = '_Hello_world'
#
# print(b.replace('_', ''))

# contacts = {
#     'John': '+11231245125',
#     'Bob': '+3806665121225',
#     'func': print
# }
# Write contacts to file
# f = open('contacts.bin', 'wb')
# pickle.dump(contacts, f)

# contacts_in_bytes = pickle.dumps(contacts)
# print(contacts_in_bytes)

# Read contacts from file
# f = open('contacts.bin', 'rb')
# contacts = pickle.load(f)
# print(contacts['func'])
# print(type(contacts))
# print(contacts)

# contacts_from_bytes = pickle.loads(contacts_in_bytes)
# print(contacts_from_bytes)


# contacts = {
#     'John': '+11231245125',
#     'Bob': '+3806665121225',
#     'other': [True, False, None, ('Hello', 'world')],
#     'set_example': list({1, 2, 3, 4}),
#     'data': print
# }
# {"John": "+11231245125", "Bob": "+3806665121225"}

# f = open('contacts.json', 'w')
# json.dump(contacts, f)
# json_string = json.dumps(contacts)
# print(json_string)


# f = open('contacts.json', 'r')
# contacts_from_json = json.load(f)
# print(contacts)
# print(contacts_from_json)


# print_output = print('Hello', 'world', 3, 3, 132, 13, 123, 12, 31, 23)
#
# print(print_output)
# text = 'Hello world'
# new_text = text.replace('l', '-')
# print(text, new_text)

# d = input()
#
# print(d)

# def greetings(name, n=5):
#     print(f'name={name} | n={n}')
#     if n < 0:
#         print(f'N is negative')
#         return 'error'
#     for i in range(n):
#         print(i)
#     text = f'Welcome {name}!'
#     print(text)
#     return text


# def greetings_all(n, *names, end, **kwargs):
#     print('n=', n, 'names=', names, 'end=', end, 'Kwargs=', kwargs)
#     for name in names:
#         print(f'Welcome {name}!{end}' * n)
#
#
# def foo(*args, **kwargs):
#     print('Function <foo>')
#     settings_1 = kwargs.get('settings_1', '...')
#     print(args, kwargs)


# foo(1, 2, 3, 4, 5, a=2, b=5, name='John', hello='world')
# a, *b = (1, 2, 3, 4, 5, 6)
# print(1, 2, 3, 4, 5, sep='_')
# greetings_all(2, 'Bob', 'John', 'Mike', 'Max', end='__', test1=1, a=3, b=4)
# print('start')
# output_1 = greetings(n=10, name='John')
# output_2 = greetings('Bob')
# output_3 = greetings('Bob2')
# print('Output 1', output_1)
# print('Output 2', output_2)
# print('Output 3', output_3)


def get_max_number(a: int, b: int) -> str:
    if a > b:
        return 'A'
    else:
        return 'B'


output = get_max_number(1, 2)

# get_max_number('hello', 2)




