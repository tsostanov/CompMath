import simple_optimizations as method
import sys

"""
Состанов Тимур Айратович
P3214 367550
Вариант 10
Метод простых итераций
"""

def matrix_printer(matrix):
    for line in matrix:
        print(' '.join(line))


accuracy = int(input('Введите точность:\n'))
mode = int(input('Выберите режим работы: 1 - ввод с клавиатуры, 2 - работа с файлом\n'))
matrix = []
if mode == 1:
    n = int(input('Введите количество строк матрицы:\n'))
    print('Вводите матрицу:')
    for i in range(n):
        new_line = list(map(int, input().split()))
        matrix.append(new_line)
elif mode == 2:
    file = input('Введите название файла с матрицей:\n')
    with open(file, 'r') as matrix_file:
        for lines in matrix_file.readlines():
            matrix.append(lines.split())



correct = method.correction_check(matrix)
print(correct)
if correct == 'Некорректная матрица':
    sys.exit(1)
else:
    matrix_printer(matrix)

diagonal = method.diagonal_form(matrix)
print(diagonal)
if diagonal == 'Матрицу нельзя привести к диагональному преобладанию':
    sys.exit(1)
else:
    matrix = diagonal
    print('Диагональная форма матрицы: \n')
    matrix_printer(matrix)

