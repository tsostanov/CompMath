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


# Критерий по абсолютным отклонениям
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

equations, inition_approximation = method.solve_diagonal_system(matrix)
print('Матрица коэффициентов преобразованной системы:')
matrix_printer(equations)
print('Вектор правых частей преобразованной системы:')
matrix_printer(inition_approximation)

# За начальное приближение возьмем вектор правых частей
answer, delta_approximation = method.simple_optimizations(equations, inition_approximation, accuracy)

delta_matrix = [[] for i in range(len(matrix))]
for number, matrix_list in enumerate(matrix):
    factor_delta = method.calculate_factor_for_array(delta_approximation)
    factor_inition = method.calculate_factor_for_array(inition_approximation)
    factor = max(factor_delta, factor_inition)

    delta_matrix[number] = [(sum(int(delta_approximation[i][0] * factor) * int(matrix[number][i] * factor)
                                           for i in range(len(delta_approximation))) / (factor ** 2))]


print('Проверка')
matrix_printer(delta_matrix)
print('Невязка')
factor = method.calculate_factor_for_array(delta_approximation)
answer_matrix = [[(delta_matrix[i][0] * factor - matrix[i][-1] * factor) / factor] for i in range(len(delta_matrix))]
matrix_printer(answer_matrix)
