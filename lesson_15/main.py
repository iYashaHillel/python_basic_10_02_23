
"""
C - Create
R - Read
U - Update
D - Delete
"""

# import sys
#
# print(sys.argv)


board = """
_____________
| X | 2 | 3 |
-------------
| 4 | O | 6 |
-------------
| 7 | 8 | 9 |
-------------

Choose:
"""


class Person:
    planet: str = 'Earth'
    _greetings_text = 'Hello'

    def __init__(self, name, age):
        print(f'Object {self} created with {name=} and {age=}!')
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"{self._greetings_text} I'm {self.name}")


class CanFly:

    def start_plane_engine(self):
        ...

    def stop_plane_engine(self):
        ...

    def land_plane(self):
        ...


class CanDrive:

    def drive_to_somewhere(self):
        ...

    def start_car_engine(self):
        ...

    def stop_car_engine(self):
        ...


class UAPerson(Person, CanFly):
    pass


# tom = Person(name='Tom', age=30)
# tom.say_hello()
#
# bob = UAPerson('Bob', age=31)
# bob.start_plane_engine()
# tom.start_plane_engine()

# john = Person(name='John', age=40)


def say_hello(person_data):
    print(f"Hello I'm {person_data['name']}")


def some_func(person_data):
    pass


# tom = {'name': 'Tom', 'age': 30}
# bob = {'name': 'Bob', 'age': 31}
#
# say_hello(tom)


# print(f'{tom.planet=} {bob.planet=} {john.planet=}')


class A:

    def foo(self):
        print('A')


class G:

    def foo(self):
        print('G')


class B(G):

    def foo(self):
        print('B')


class C(A):

    def foo(self):
        print('C')


class D(C, B):
    pass


d = D()
d.foo()
print(D.__mro__)

