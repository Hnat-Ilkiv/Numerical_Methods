def subtract_vectors(v1, v2):
    return [a - b for a, b in zip(v1, v2)]

def multiply_matrix_vector(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]

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

