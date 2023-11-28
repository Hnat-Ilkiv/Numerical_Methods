import math

def f(x):
    return math.exp(x) + x

def df(x):
    return 1 + math.exp(x)

def stefensen_method(initial_guess, final_guess, tol, max_iter):
    x = initial_guess
    iter_count = 0

    while iter_count < max_iter:
        x_next = x - (f(x) ** 2) / (f(x + f(x)) - f(x))

        # Перевірка чи досі ми в заданому проміжку
        if x_next < initial_guess or x_next > final_guess:
            return None, iter_count

        # Перевірка на зупинку за критерієм збіжності
        if abs(x_next - x) < tol:
            return x_next, iter_count

        x = x_next
        iter_count += 1

    # Якщо досягнута максимальна кількість ітерацій
    return None, max_iter

# Вхідні дані
initial_guess = -9.0
final_guess = 3.0
tolerance = 1e-8
max_iterations = 1000

# Виклик методу Стефенсена
root, iterations = stefensen_method(initial_guess, final_guess, tolerance, max_iterations)

if root is not None:
    # Перевірка значення функції в знайденій точці
    function_value_at_root = f(root)

    print(f"Корінь рівняння: {root}")
    print(f"Значення функції в корені: {function_value_at_root}")
    print(f"Кількість ітерацій: {iterations}")
else:
    print("Метод не збігається до кореня за вказану кількість ітерацій.")
