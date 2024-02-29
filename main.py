import simple_optimizations as method
import sys

"""
Состанов Тимур Айратович
P3214 367550
Вариант 10
Метод простых итераций
"""

def matrix_printer(matrix):
    max_width = max(len(str(elem)) for row in matrix for elem in row)
    for line in matrix:
        print(" ".join(str(elem).rjust(max_width) for elem in line))


accuracy = float(input('Введите точность:\n'))

matrix = []
while True:
    mode = int(input('Выберите режим работы: 1 - ввод с клавиатуры, 2 - работа с файлом\n'))
    if mode == 1:
        n = int(input('Введите количество строк матрицы:\n'))
        print('Вводите матрицу:')
        for i in range(n):
            new_line = list(map(float, input().split()))
            matrix.append(new_line)
        break
    elif mode == 2:
        file = input('Введите название файла с матрицей:\n')
        try:
            with open(file, 'r') as matrix_file:
                for line in matrix_file.readlines():
                    new_line = list(map(float, line.split()))
                    matrix.append(new_line)
            break
        except FileNotFoundError:
            print("Файл не найден. Пожалуйста, укажите существующий файл.")
    else:
        print("Некорректный режим. Пожалуйста, выберите 1 или 2.")


def diagonal_form(matrix):
    max_index = []
    for line in matrix:
        max_line = max(line[:-1])
        if max_line > (sum(line[:-1]) - max_line):
            index_line = line.index(max_line)
            if index_line not in max_index:
                max_index.append(index_line)
    if len(max_index) == len(matrix):
        diagonal_matrix = []
        for i in max_index:
            diagonal_matrix.append(matrix[i])
        return diagonal_matrix
    else:
        return 'Матрицу нельзя привести к диагональному преобладанию'


correct = method.correction_check(matrix)
print(correct)
if correct == 'Некорректная матрица':
    sys.exit(1)
else:
    matrix_printer(matrix)

diagonal = method.diagonal_form(matrix)
if diagonal == 'Матрицу нельзя привести к диагональному преобладанию':
    print(diagonal)
    sys.exit(1)
else:
    matrix = diagonal
    print('Диагональная форма матрицы:')
    matrix_printer(matrix)

equations = method.solve_diagonal_system(matrix)
print('Вектор неизвестных:')
matrix_printer(equations)
# for eq in equations:
#     print(eq)
