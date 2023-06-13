"""
ООП:
Наслідування
Інкапсуляція - Всі об'єкти в Python інкапсулюють у собі дані та методи роботи з ними, надаючи публічні інтерфейси для взаємодії.
1) Публічні методи (Public) - доступні з будь-якого місця програми
2) Захищені методи (Protected) - доступні лише всередині класу та його нащадків
3) Приватні методи (Private) - доступні лише всередині класу

Поліморфізм - Це означає, що дочірні класи можуть перевизначати методи батьківського класу і вирішувати одне
й те саме завдання різними шляхами, а конкретну реалізацію буде обрано лише під час виконання програми.

Абстракція - це виділення загальних характеристик об'єктів, їх властивостей та методів, при ігноруванні деталей реалізації.
"""
import abc

# a=4, b=2 -> res=8
# a=4, b=2 -> 8


def foo():
    data = {'hello': 'world'}
    return data


class Car:
    has_engine = True

    def __init__(self, model: str, brand: str, color: str, plate_number: str):
        self.model = model
        self.brand = brand
        self.color = color
        self._plate_number = self.__validate_plate_number(plate_number)

    @property
    def plate_number(self) -> str:
        return ''.join(map(lambda x: '*' if x.isdigit() else x, self._plate_number))

    @plate_number.setter
    def plate_number(self, plate_number: str):
        self._plate_number = self.__validate_plate_number(plate_number)

    # def set_plate_number(self, plate_number: str):
    #     self._plate_number = self.__validate_plate_number(plate_number)
    #
    # def get_plate_number(self) -> str:
    #     return ''.join(map(lambda x: '*' if x.isdigit() else x, self._plate_number))

    def drive(self):
        print(f'Car {self.model} is driving. Plate number: {self.plate_number}')

    def stop(self):
        print(f'Car {self.model} is stopped. Plate number: {self.plate_number}')

    @classmethod
    def some_class_method(cls):
        print(cls.has_engine)
        print('...')

    @staticmethod
    def __validate_plate_number(plate_number: str):
        if len(plate_number) != 8:
            raise ValueError('Plate number must be 8 symbols')
        if not plate_number[:2].isalpha():
            raise ValueError('First 2 symbols must be letters')
        if not plate_number[2:6].isdigit():
            raise ValueError('Symbols 3-6 must be digits')
        if not plate_number[6:].isalpha():
            raise ValueError('Last 2 symbols must be letters')
        return plate_number

    def __str__(self) -> str:
        return f'<{self.__class__} {self.brand=} {self.model=} {self.color=} {self.plate_number=}>'

    def __add__(self, other) -> str:
        if isinstance(other, int):
            return f'{self.plate_number}_{other}'
        return self.plate_number + ' ' + other.plate_number


class ElectroCar(Car):

    def __init__(self, model: str, brand: str, color: str, plate_number: str, battery_capacity: int):
        super().__init__(model, brand, color, plate_number)

        if not 0 <= battery_capacity <= 100:
            raise ValueError('Battery capacity must be between 0 and 100')
        self.battery_capacity = battery_capacity

    def drive(self):
        if self.battery_capacity <= 0:
            raise ValueError('Battery is empty')
        super().drive()
        self.battery_capacity -= 10

    def charge(self):
        print(f'Car {self.model} is charging. Plate number: {self.plate_number}')
        self.battery_capacity = 100


# bmw = Car(model='X5', brand='BMW', color='black', plate_number='AA0000AA')
# tesla = ElectroCar(model='X', brand='Tesla', color='black', plate_number='AA0000AB', battery_capacity=100)
#
# print(bmw + tesla)

#
# Car.some_class_method()

#
# print(tesla.plate_number)
#
# tesla.plate_number = 'AA00002C'


class Greetings(abc.ABC):

    def __init__(self, name: str):
        self.name = name

    @abc.abstractmethod
    def greetings(self):
        pass


class English(Greetings):

    def greetings(self):
        print(f'Hello {self.name}!')


class Ukraine(Greetings):

    def greetings(self):
        print(f'Вітаю {self.name}!')


# greetings_list = [
#     English('John'),
#     Ukraine('Bob'),
#     Ukraine('Mark'),
#     Car(model='X5', brand='BMW', color='black', plate_number='AA0000AA')
# ]
#
# for obj in greetings_list:
#     if isinstance(obj, Greetings):
#         obj.greetings()
