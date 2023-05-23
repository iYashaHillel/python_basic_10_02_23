"""
Вірус пошкодив систему доступу до файлів.
Відомо, що над кожним файлом можна робити певні дії:
запис – W;
читання – R;
запуск - X.
На вхід програмі подається:
число n – кількість файлів;
n рядків з іменами файлів та допустимими операціями;
число m – кількість запитів до файлів;
m запитів виду "операція файл".
Для кожного припустимого запиту програма має повертати OK, для неприпустимого – Access denied.

Приклад введення:
3
python.exe X
book.txt R W
notebook.exe R W X
5
read python.exe
read book.txt
write notebook.exe
execute notebook.exe
write book.txt

Приклад виводу:
Access denied
OK
OK
OK
OK
"""

operations = {
    'read': 'r',
    'write': 'w',
    'execute': 'x',
}

files_count = int(input('File count: '))
files = {}

for i in range(files_count):
    file, *available_operations = input(f'File #{i}: ').lower().strip().split(' ')
    files[file] = available_operations

operations_count = int(input('Operation count: '))
output = ''

for i in range(operations_count):
    operation_type, file_name = input(f'Operation #{i}: ').lower().strip().split(' ')
    if operations[operation_type] in files[file_name]:
        output += 'OK\n'
    else:
        output += 'Access Denied\n'

print(output)
