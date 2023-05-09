"""
Програма запитує користувача пароль і записує в змінну password.
Необхідно порахувати складність пароля,
де за кожну пройдену перевірку пароль отримує +1 бал до підсумкової оцінки, максимальна кількість балів – 5

Перевірки:
* Довжина пароля більша або дорівнює 8 символам.
* У паролі є хоча б одна цифра
* У паролі є хоча б одна велика
* У паролі є хоча б одна маленька буква
* У паролі є хоча б один спеціальний символ (+, -, /, _, % і т.д. P.S. їх насправді більше)
Після всіх перевірок потрібно вивести користувачеві кількість - кількість балів за пароль, а також рекомендації щодо поліпшення пароля.

INPUT 1:
Enter your password: admin123

OUTPUT 1:
Password score: 3
Recommendation:
Use capital letters
Use special characters

INPUT 2:
Enter your password: P@ssword1

OUTPUT 2:
Password score: 5

INPUT 3:
Enter your password: admin

OUTPUT 3:
Password score: 1
Use capital letters
The minimum password length is 8
Use digits
Use special characters
"""

password = input('Enter your password:')

recommendation = ''
score = 0
has_upper = False
has_lower = False
has_digit = False
has_spec = False

if len(password) >= 8:
    score += 1
else:
    recommendation += 'The minimum password length is 8\n'

for char in password:
    if char.isupper():
        has_upper = True
    if char.islower():
        has_lower = True
    if char.isdigit():
        has_digit = True
    if not char.isdigit() and not char.isalpha():
        has_spec = True

score += has_upper + has_lower + has_digit + has_spec

if not has_upper:
    recommendation += 'Use capital letters\n'
if not has_lower:
    recommendation += 'Use lower letters\n'
if not has_digit:
    recommendation += 'Use digits\n'
if not has_spec:
    recommendation += 'Use special characters\n'

print(f'Password score: {score}')
if recommendation:
    print('Recommendation:')
    print(recommendation)


