import math


def f(x):
    """Визначення функції"""
    return math.exp(x) + x

def df(x):
    """Визначення похідної функції"""
    return 1 + math.exp(x)

def secant_method(f, initial_guess, final_guess, tol, max_iter):
    if f(initial_guess) * f(final_guess) > 0:
        print("Не вдалося гарантувати наявність кореня в заданому інтервалі.")

    iter_count = 0

    while iter_count < max_iter:
        # Обчислення нового наближення за методом січних
        x_next = final_guess - f(final_guess) * (final_guess - initial_guess) / (f(final_guess) - f(initial_guess))

        # Перевірка на зупинку за критерієм збіжності
        if abs(x_next - final_guess) < tol:
            return x_next, iter_count

        # Оновлення наближень для наступної ітерації
        initial_guess, final_guess = final_guess, x_next
        iter_count += 1

    # Якщо досягнута максимальна кількість ітерацій
    print("Не вдалося знайти корінь за вказану кількість ітерацій.")
    return None, max_iter

if __name__ == "__main__":
    # Вхідні дані
    initial_guess = -9.0
    final_guess = 3.0
    tolerance = 1e-10
    max_iterations = 1000

    # Виклик Метод січних
    root, iterations = secant_method(f, initial_guess, final_guess, tolerance, max_iterations)

    if root is not None:
        # Перевірка значення функції в знайденій точці
        function_value_at_root = f(root)

        print(f"Корінь рівняння: {root}")
        print(f"Значення функції в корені: {function_value_at_root}")
        print(f"Кількість ітерацій: {iterations}")
    else:
        print("Метод не збігається до кореня за вказану кількість ітерацій.")
