# number = int(input('Enter your number: '))


# if number == 1:
#     print('One')
# elif number == 2:
#     print('Two')
# elif number == 3:
#     print('Third')
# elif number == 4:
#     print('Four')
# elif number == 5:
#     print('Five')
# else:
#     print('Error')

# a = True
# b = False
# c = True
# d = ''
# e = 0
# a_more_then_5 = a > 5

# if a > 5 or e is not None and e >= 0:
#     print('+')
# else:
#     print('-')
#
# if a:
#     print('a is True')
#     if b:
#         print('b also is true')
#         if c:
#             print('c is true')


# if ...:
#     pass


# if number % 2 == 0:
#     print('Even')
# else:
#     print('Odd')


# if False:
#     print('+')
# else:
#     print('Default')
#
# if True:
#     print('....')
# else:
#     ...

# if number % 2 != 0:
#     print('Odd')


"""
Овен (21.03 – 20.04)
Телець (21.04 – 21.05)
Близнята (22.05 – 21.06)
Рак (22.06 – 22.07)
Лев (23.07 – 21.08)
Діва (22.08 – 23.09)
Терези (24.09 – 23.10)
Скорпіон (24.10 – 22.11)
Стрілець (23.11 – 21.12)
Козеріг (22.12 – 20.01)
Водолій (21.01 – 18.02)
Риби (19.02 – 20.03)
"""

day = 31
month = 1

if (21 <= day <= 31 and month == 1) or (1 <= day <= 18 and month == 2):
    print('Водолій')

import calendar
import datetime

day = int(input('Введіть день вашого народження: '))
month = int(input('Введіть місяць вашого народження: '))
max_day = calendar.monthrange(2023, month)[1]

if not (1 <= day <= max_day and 1 <= month <= 12):
    print('Помилка, день або місяць неправильний!')
    exit()

user_date = datetime.date(2023, month, day)
if datetime.date(2023, 1, 21) <= user_date <= datetime.date(2023, 2, 18):
    print('Ти Водолій')
    print(
        'Пом’якшити гостроту щоденних викликів можуть допомогти прості та зрозумілі речі, як-от хобі. Одне з них — випікання, традиційне для українців ремесло, яке не тільки демонструє глибокий зв’язок між минулим і сьогоденням, а й сприяє віднайденню душевного спокою та фокусуванню на важливому тут і зараз.'
    )
elif datetime.date(2023, 2, 19) <= user_date <= datetime.date(2023, 3, 20):
    print('Ти Риби')
    print(
        'Представникам знаків Води — Рака, Скорпіона, Риб — рік нагадуватиме контрастний душ: то підноситиме догори і спонукатиме до відкритості та творчості, то занурюватиме на звичні глибини, даруючи опору та спокій. Цього року ви — завбачливі ентузіасти. Ваші уява та інтуїція будуть на висоті. Якщо у вас є заповітна мрія або ціль, саме ці здібності допоможуть швидше наблизитися до неї.'
    )
print('Все ок')

user_choice = 'y'

while user_choice == 'y':
    print('+1 Push-up')
    user_choice = input('y/n: ')

print('End')
