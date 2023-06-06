"""
Замикання (closure) представляє функцію, яка запам'ятовує своє
лексичне оточення навіть у тому випадку, коли вона виконується поза
своєї області видимості.
"""


def outer_func(name):
    print('outer_func')

    def greetings(lang: str = 'ua'):
        print(lang)
        print(f'Hello {name}')

    return greetings


hello_john = outer_func('John')
hello_bob = outer_func('Bob')
print('-------')
hello_john('en')
hello_john('de')
hello_john('ua')
hello_john()
hello_bob()
hello_bob()
hello_bob()
hello_bob()
hello_bob()
