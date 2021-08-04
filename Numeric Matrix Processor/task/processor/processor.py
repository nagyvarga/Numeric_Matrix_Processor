MENU = ('1. Add matrices', '2. Multiply matrix by a constant', '3. Multiply matrices', '4. Transpose matrix',
        '5. Calculate a determinant', '6. Inverse matrix', '0. Exit')
TRANSPOSE_MENU = ('1. Main diagonal', '2. Side diagonal', '3. Vertical line', '4. Horizontal line')
TRANSPOSE_OPTION = [str(num) for num in range(5)]
OPTIONS = [str(num) for num in range(7)]


def ask_matrix_size(plus_word=''):
    while True:
        try:
            plus_word += '' if plus_word == '' else ' '
            print(f'Enter size of {plus_word}matrix: ', end='')
            size = [int(num) for num in input().split()]
        except (ValueError, TypeError):
            continue
        else:
            if len(size) == 2 and size[0] > 0 and size[1] > 0:
                return size


def add_matrices(matrix_1, matrix_2):
    new_matrix = [[] for _ in matrix_1]
    row_counter = -1
    if size_comparison(matrix_1, matrix_2):
        for m_row_1, m_row_2 in zip(matrix_1, matrix_2):
            row_counter += 1
            for m_column_1, m_column_2 in zip(m_row_1, m_row_2):
                new_matrix[row_counter].append(m_column_1 + m_column_2)
    else:
        return None
    return new_matrix


def transpose_diagonal(matrix, main_diagonal):
    new_matrix_column, new_matrix_row = matrix_size(matrix)
    new_matrix = [[] for _ in range(new_matrix_row)]
    for i in range(new_matrix_row):
        for j in range(new_matrix_column):
            if main_diagonal:
                new_matrix[i].append(matrix[j][i])
            else:
                new_matrix[i].append(matrix[new_matrix_column - 1 - j][new_matrix_row - 1 - i])
    return new_matrix


def transpose_line(matrix, vertical_line):
    new_matrix = [[] for _ in matrix]
    matrix_row, matrix_column = matrix_size(matrix)
    for i in range(matrix_row):
        for j in range(matrix_column):
            if vertical_line:
                new_matrix[i].append(matrix[i][matrix_column - 1 - j])
            else:
                new_matrix[i].append(matrix[matrix_row - 1 - i][j])
    return new_matrix


def cofactor(matrix):
    matrix_row, matrix_column = matrix_size(matrix)
    new_matrix = [[] for _ in matrix]
    for i in range(matrix_row):
        for j in range(matrix_column):
            sign = (-1) ** (i + j)
            new_matrix[i].append(sign * determinant(minor(matrix, j, i)))
    return new_matrix


def determinant(matrix):
    matrix_row, matrix_column = matrix_size(matrix)
    if matrix_column == 1:
        return matrix[0][0]
    elif matrix_column == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    sum_det = 0
    for i in range(matrix_column):
        sum_det += matrix[0][i] * ((-1) ** i) * determinant(minor(matrix, i))
    return sum_det


def minor(matrix, column, row=0):
    matrix_row, matrix_column = matrix_size(matrix)
    new_matrix = [[] for _ in range(matrix_row - 1)]
    row_increment = -1
    for r in range(matrix_row):
        if r != row:
            row_increment += 1
        for c in range(matrix_column):
            if r != row and c != column:
                new_matrix[row_increment].append(matrix[r][c])
    return new_matrix


def print_det(det):
    print('The result is:')
    print(det)


def multiply_by_constant(matrix, const):
    matrix_row, matrix_column = matrix_size(matrix)
    for i in range(matrix_row):
        for j in range(matrix_column):
            matrix[i][j] = float_or_int(matrix[i][j] * const)
    return matrix


def multiply_matrices(matrix_1, matrix_2):
    matrix_1_row, matrix_1_column = matrix_size(matrix_1)
    matrix_2_row, matrix_2_column = matrix_size(matrix_2)
    if matrix_1_column == matrix_2_row:
        new_matrix = [[] for _ in range(matrix_1_row)]
        for row in range(matrix_1_row):
            for column in range(matrix_2_column):
                cells_value = 0
                for cell in range(matrix_2_row):
                    cells_value += matrix_1[row][cell] * matrix_2[cell][column]
                new_matrix[row].append(cells_value)
    else:
        return None
    return new_matrix


def print_matrix(matrix):
    if matrix is not None:
        print('The result is:')
        for matrix_row in matrix:
            print(*[num for num in matrix_row])
    else:
        print('The operation cannot be performed.')


def matrix_size(matrix):
    matrix_row = len(matrix)
    matrix_column = len(matrix[0])
    return [matrix_row, matrix_column]


def size_comparison(matrix_1, matrix_2):
    size_1 = matrix_size(matrix_1)
    size_2 = matrix_size(matrix_2)
    if size_1[0] == size_2[0] and size_1[1] == size_2[1]:
        return True
    return False


def input_matrix(size, plus_word=''):
    matrix_row, matrix_column = size
    new_matrix = [[] for _ in range(matrix_row)]
    plus_word += '' if plus_word == '' else ' '
    print(f'Enter {plus_word}matrix:')
    for r in range(matrix_row):
        while True:
            try:
                new_matrix[r] = [float_or_int(float(item)) for item in input().split()]
            except (ValueError, TypeError):
                continue
            else:
                break
    return new_matrix


def user_choice(list_of_menu, options):
    while True:
        print('', *list_of_menu, sep='\n')
        choice = input('Your choice: ')
        if choice in options:
            break
    return choice


def float_or_int(number):
    if float(int(number)) == number:
        return int(number)
    return number


while True:
    option = user_choice(MENU, OPTIONS)
    if option == '0':
        break
    elif option == '1':
        matrix_one = input_matrix(ask_matrix_size('first'), 'first')
        matrix_two = input_matrix(ask_matrix_size('second'), 'second')
        print_matrix(add_matrices(matrix_one, matrix_two))
    elif option == '2':
        matrix_one = input_matrix(ask_matrix_size())
        constant = float_or_int(float(input('Enter constant: ')))
        print_matrix(multiply_by_constant(matrix_one, constant))
    elif option == '3':
        matrix_one = input_matrix(ask_matrix_size('first'), 'first')
        matrix_two = input_matrix(ask_matrix_size('second'), 'second')
        print_matrix(multiply_matrices(matrix_one, matrix_two))
    elif option == '4':
        transpose_option = user_choice(TRANSPOSE_MENU, TRANSPOSE_OPTION)
        if transpose_option == '1':
            matrix_one = input_matrix(ask_matrix_size())
            print_matrix(transpose_diagonal(matrix_one, True))
        elif transpose_option == '2':
            matrix_one = input_matrix(ask_matrix_size())
            print_matrix(transpose_diagonal(matrix_one, False))
        elif transpose_option == '3':
            matrix_one = input_matrix(ask_matrix_size())
            print_matrix(transpose_line(matrix_one, True))
        elif transpose_option == '4':
            matrix_one = input_matrix(ask_matrix_size())
            print_matrix(transpose_line(matrix_one, False))
    elif option == '5':
        matrix_one = input_matrix(ask_matrix_size())
        print_det(determinant(matrix_one))
    elif option == '6':
        matrix_one = input_matrix(ask_matrix_size())
        det_of_matrix = determinant(matrix_one)
        if det_of_matrix != 0:
            print_matrix(multiply_by_constant(transpose_diagonal(cofactor(matrix_one), True), 1 / det_of_matrix))
        else:
            print("This matrix doesn't have an inverse.")
