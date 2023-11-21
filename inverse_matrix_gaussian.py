def generate_matrix(task_number):
    k = task_number
    s = 0.02 * k

    matrix = [
        [8.3, 2.62 + s, 4.1, 1.9],
        [3.92, 8.45, 7.78 - s, 2.46],
        [3.77, 7.21 + s, 8.04, 2.28],
        [2.21, 3.65 - s, 1.69, 6.69]
    ]

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(lambda x: f" {x:.2f}" if x >= 0 else f"{x:.2f}", row)))

def inverse_matrix_gaussian(matrix):
    n = len(matrix)
    # Створюємо розширену матрицю, що містить одиничну матрицю
    augmented_matrix = [row + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(matrix)]

    for i in range(n):
        # Ділимо поточний рядок на елемент на головній діагоналі, щоб отримати 1
        pivot = augmented_matrix[i][i]
        for j in range(2 * n):
            augmented_matrix[i][j] /= pivot

        # Нулюємо елементи в інших рядках стовпця, використовуючи елементарні операції
        for k in range(n):
            if i != k:
                factor = augmented_matrix[k][i]
                for j in range(2 * n):
                    augmented_matrix[k][j] -= factor * augmented_matrix[i][j]

    # Вибираємо праву частину (обернену матрицю)
    inverse_matrix = [row[n:] for row in augmented_matrix]

    return inverse_matrix

def gaussian_elimination_with_pivoting(matrix):
    n = len(matrix)
    # Створюємо розширену матрицю, що містить одиничну матрицю
    augmented_matrix = [row + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(matrix)]

    for i in range(n):
        # Вибір головного елемента
        pivot_row = max(range(i, n), key=lambda j: abs(augmented_matrix[j][i]))
        augmented_matrix[i], augmented_matrix[pivot_row] = augmented_matrix[pivot_row], augmented_matrix[i]

        # Ділимо поточний рядок на елемент на головній діагоналі, щоб отримати 1
        pivot = augmented_matrix[i][i]
        for j in range(2 * n):
            augmented_matrix[i][j] /= pivot

        # Нулюємо елементи в інших рядках стовпця, використовуючи елементарні операції
        for k in range(n):
            if i != k:
                factor = augmented_matrix[k][i]
                for j in range(2 * n):
                    augmented_matrix[k][j] -= factor * augmented_matrix[i][j]

    inverse_matrix = [row[n:] for row in augmented_matrix]

    return inverse_matrix

if __name__ == "__main__":
    # Генерації матриці для завдання №9
    task_number = 9
    matrix_for_task = generate_matrix(task_number)

    # Знаходимо обернену матрицю за допомогою простого методу Гауса
    inverse_matrix1 = inverse_matrix_gaussian(matrix_for_task)

    # Знаходимо обернену матрицю за допомогою методу Гауса з вибором головного елемента
    inverse_matrix2 = gaussian_elimination_with_pivoting(matrix_for_task)

    # Виводимо результат
    print("Матриця №1:")
    print_matrix(matrix_for_task)
    print("\nОбернена матриця №1:")
    print_matrix(inverse_matrix1)
    print("\nОбернена матриця №2:")
    print_matrix(inverse_matrix2)
    print(f"\nОбернена матриця №1 == Обернена матриця №2 >> {inverse_matrix1 == inverse_matrix2}")
