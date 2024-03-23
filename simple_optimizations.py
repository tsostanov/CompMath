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
    initial_approximation = []
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
        initial_approximation.append([line[-1] / factor])
        equations.append(equation)
    return equations, initial_approximation


def calculate_factor_for_array(arr):
    factor = 0
    for row in arr:
        for number_str in row:
            if '.' in str(number_str):
                decimal_digits = len(str(number_str)) - str(number_str).index('.') - 1
                factor = max(factor, decimal_digits)
    return 10 ** factor


def simple_optimizations(transformed_matrix, start_approximation, accuracy):
    answer = 1

    print(" Метод простых итераций")
    print(" | ".join(["k ", *(f"x{i}                " for i in range(1, len(start_approximation) + 1)),
                      "difference"]))
    print(" | ".join(
        ["0 "] + [str(item) + (" " * (18 - len(str(item)))) for sublist in start_approximation for item in sublist] + [
            "---"]))

    vector_of_right_parts = start_approximation[:]
    delta_approximation = [[] for _ in range(len(start_approximation))]
    factor_start = calculate_factor_for_array(start_approximation)

    for number, coefficients in enumerate(transformed_matrix):
        factor = max([10 ** max(
            (len(str(number_str)) - str(number_str).index('.') - 1) if '.' in str(number_str) else 0 for number_str in
            coefficients), factor_start])

        delta_approximation[number] = [
            (sum(int(start_approximation[i][0] * factor) * int(transformed_matrix[number][i] * factor)
                 for i in range(len(start_approximation))) + int(vector_of_right_parts[number][0] * (factor ** 2))) / (
                    factor ** 2)]

    factor_delta = calculate_factor_for_array(delta_approximation)
    factor_result = max([factor_delta, factor_start])
    accuracy_check = (max(
        abs(int(delta_approximation[i][0] * factor_result) - int(start_approximation[i][0] * factor_result)) for i in
        range(len(delta_approximation))) / factor_result)
    print(" | ".join(
        [str(answer) + " "] + [str(item) + (" " * (18 - len(str(item)))) for sublist in delta_approximation for item in
                               sublist] + [str(accuracy_check)]))
    while accuracy_check >= accuracy:
        start_approximation = delta_approximation
        answer += 1

        delta_approximation = [[] for _ in range(len(start_approximation))]
        factor_start = calculate_factor_for_array(start_approximation)

        for number, coefficients in enumerate(transformed_matrix):
            factor = max([10 ** max(
                (len(str(number_str)) - str(number_str).index('.') - 1) if '.' in str(number_str) else 0 for number_str
                in
                coefficients), factor_start])
            delta_approximation[number] = [
                (sum(int(start_approximation[i][0] * factor) * int(transformed_matrix[number][i] * factor)
                     for i in range(len(start_approximation))) +
                 int(vector_of_right_parts[number][0] * (factor ** 2))) / (factor ** 2)]
        factor_delta = calculate_factor_for_array(delta_approximation)
        factor_result = max([factor_delta, factor_start])
        accuracy_check = (max(
            abs(int(delta_approximation[i][0] * factor_result) - int(start_approximation[i][0] * factor_result)) for i
            in range(len(delta_approximation))) / factor_result)
        print(" | ".join(
            [str(answer) + " "] + [str(item) + (" " * (18 - len(str(item)))) for sublist in delta_approximation for item
                                   in sublist] + [str(accuracy_check)]))

    return answer, delta_approximation
