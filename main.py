def subtract_vectors(v1, v2):
    return [a - b for a, b in zip(v1, v2)]

def multiply_matrix_vector(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


#
# Метод Ньютона з кінцево-різницевою матрицею Якобі
#

def newton_method(x0, epsilon, max_iter=100):
    x = x0[:]
    identity_matrix = [[1 if i == j else 0 for j in range(len(x))] for i in range(len(x))]

    for _ in range(max_iter):
        # Обчислення значень функцій та матриці Якобі
        f = [
            x[0]**2 - x[1]**2 + 0.1 - x[0],
            2*x[0]*x[1] - 0.1 - x[1]
        ]
        
        J = [
            [2*x[0] - 1, -2*x[1]],
            [2*x[1], 2*x[0] - 1]
        ]
        
        # Обертання матриці Якобі
        J_inv = [[J[1][1], -J[0][1]], [-J[1][0], J[0][0]]]
        determinant = J[0][0] * J[1][1] - J[0][1] * J[1][0]
        J_inv = [[elem / determinant for elem in row] for row in J_inv]
        
        # Ітераційна формула
        delta_x = multiply_matrix_vector(J_inv, f)
        x = subtract_vectors(x, delta_x)
        
        # Перевірка умови збіжності
        if max(abs(elem) for elem in f) < epsilon:
            break
    
    return x

# Виклик функції для заданого початкового наближення та відносної похибки
x0 = [1, 1]
epsilon = 5e-10
result = newton_method(x0, epsilon)
print("Результат методу Ньютона:", result)

#
# 𝜀-алгоритм
#
def epsilon_algorithm(x0, epsilon, max_iter=100):
    m = len(x0)
    q = m
    n = 2 * q + 1
    p = 2
    x = x0[:]
    Sn = [0] * n
    E = [[1 if i == j else 0 for j in range(m)] for i in range(m)]

    for _ in range(max_iter):
        # Встановлення нулів у 𝜀-матриці
        epsilon_matrix = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(p):
            # Обчислення значень функцій та матриці Якобі
            f = [
                x[0] ** 2 - x[1] ** 2 + 0.1 - x[0],
                2 * x[0] * x[1] - 0.1 - x[1]
            ]

            J = [
                [2 * x[0] - 1, -2 * x[1]],
                [2 * x[1], 2 * x[0] - 1]
            ]

            # Обертання матриці Якобі
            J_inv = [[J[1][1], -J[0][1]], [-J[1][0], J[0][0]]]
            determinant = J[0][0] * J[1][1] - J[0][1] * J[1][0]
            J_inv = [[elem / determinant for elem in row] for row in J_inv]

            # Ітераційна формула
            delta_x = multiply_matrix_vector(J_inv, f)
            x = subtract_vectors(x, delta_x)

            # Заповнення 𝜀-матриці
            for j in range(m):
                epsilon_matrix[i][j] = x[j] - x0[j]
                epsilon_matrix[i + q][j] = epsilon_matrix[i][j] - Sn[j]

            # Перевірка умови збіжності
            if max(abs(elem) for elem in f) < epsilon:
                break

        # Обчислення елементу матриці n
        e_matrix_element = multiply_matrix_vector(epsilon_matrix, [elem[0] for elem in epsilon_matrix])
        Sn = [elem / (2 * epsilon) for elem in e_matrix_element]

        # Перевірка умови завершення ітераційного процесу
        if all(isinstance(elem, (int, float)) and elem < epsilon for elem in Sn):
            break

    return x

# Виклик функції для заданого початкового наближення та відносної похибки
x0 = [1, 1]
epsilon = 5e-10
result_epsilon = epsilon_algorithm(x0, epsilon)
print("Результат 𝜀-алгоритму:", result_epsilon)

#
# Спрощений метод Ньютона
#
def simplified_newton_method(x0, epsilon, max_iter=100):
    m = len(x0)
    n = 2 * m + 1
    E = [[1 if i == j else 0 for j in range(m)] for i in range(m)]
    x = x0[:]

    for _ in range(max_iter):
        # Обчислення значень функцій та матриці Якобі
        f = [
            x[0] ** 2 - x[1] ** 2 + 0.1 - x[0],
            2 * x[0] * x[1] - 0.1 - x[1]
        ]

        J = [
            [2 * x[0] - 1, -2 * x[1]],
            [2 * x[1], 2 * x[0] - 1]
        ]

        # Обертання матриці Якобі
        J_inv = [[J[1][1], -J[0][1]], [-J[1][0], J[0][0]]]
        determinant = J[0][0] * J[1][1] - J[0][1] * J[1][0]
        J_inv = [[elem / determinant for elem in row] for row in J_inv]

        # Ітераційна формула
        delta_x = multiply_matrix_vector(J_inv, f)
        x = subtract_vectors(x, delta_x)

        # Перевірка умови збіжності
        if max(abs(elem) for elem in f) < epsilon:
            break

    return x

# Виклик функції для заданого початкового наближення та відносної похибки
x0 = [1, 1]
epsilon = 5e-10
result_simplified_newton = simplified_newton_method(x0, epsilon)
print("Результат спрощеного методу Ньютона:", result_simplified_newton)
