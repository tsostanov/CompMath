"""
Состанов Тимур Айратович
P3214 367550
Вариант 10
Метод простых итераций
"""


mode = int(input('Выберите режим работы: 1 - ввод с клавиатуры, 2 - работа с файлом\n'))
accuracy = int(input('Введите точность:\n'))
matrix = []
n = int(input('Введите количество строк матрицы:\n'))
print('Вводите матрицу:')
for i in range(n):
    new_line = list(map(int, input().split()))
    matrix.append(new_line)

print(matrix)


