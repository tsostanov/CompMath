def correction_check(matrix):
    matrix_length = (len(matrix[0]) - 1)
    matrix_lines = len(matrix)
    if matrix_lines == matrix_length:
        for i in range(1, len(matrix)):
            if (len(matrix[i]) - 1) != matrix_length:
                return 'Некорректная матрица'
        return 'Введеная матрица:'
    else:
        return 'Некорректная матрица'


def diagonal_form(matrix):
    max_index = []
    for line in matrix:
        max_line = max(line[:-1])
        if max_line > (sum(line[:-1]) - max_line):
            index_line = line.index(max_line)
            if index_line not in max_index:
                max_index.append(index_line)
    if len(max_index) == len(matrix):
        diagonal_matrix = [[] for _ in range(len(matrix))]
        for number, line in enumerate(max_index):
            diagonal_matrix[line] = matrix[number]
        return diagonal_matrix
    else:
        return 'Матрицу нельзя привести к диагональному преобладанию'


def solve_diagonal_system(matrix):
    equations = []
    for i, line in enumerate(matrix):
        factor = line[i]
        if factor == 0:
            break
        equation = []
        for j, coefficient in enumerate(line[:-1]):
            if j != i:
                equation.append((-1) * coefficient / factor)
            else:
                equation.append(0)
        equation.append(line[-1] / factor)
        equations.append(equation)
    return equations
