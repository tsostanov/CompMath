def correction_check(matrix):
    matrix_length = len(matrix[0])
    for i in range(1, len(matrix)):
        if len(matrix[i]) != matrix_length:
            return 'Некорректная матрица'
    return 'Введеная матрица: \n'



def diagonal_form(matrix):
    max_index = []
    for line in matrix:
        max_line = int(max(line))
        if max_line >= (sum(line) - max_line):
            index_line = line.index(max_line)
            if index_line not in max_index:
                max_index.append(index_line)
    if len(max_index) == len(matrix):
        diagonal_matrix = [[]]
        for i in max_index:
            diagonal_matrix.append(matrix[i])
            return diagonal_matrix
    else:
        return 'Матрицу нельзя привести к диагональному преобладанию'