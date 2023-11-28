import math

def f(x):
    return math.exp(x) + x

def df(x):
    return 1 + math.exp(x)

def combined_method(initial_guess, final_guess, tol, max_iter):
    if f(initial_guess) * f(final_guess) > 0:
        print("Не вдалося гарантувати наявність кореня в заданому інтервалі.")

    # Початкова апроксимація кореня
    x = (initial_guess + final_guess) / 2
    iter_count = 0

    while iter_count < max_iter:
        # Обчислення нової апроксимації за комбінованим методом
        x_next = x - f(x) / df(x) # iter_count 5

        # Перевірка на зупинку за критерієм збіжності
        if abs(x_next - x) < tol:
            return x_next, iter_count

        x = x_next
        iter_count += 1

    # Якщо досягнута максимальна кількість ітерацій
    print("Не вдалося знайти корінь за вказану кількість ітерацій.")
    return None, max_iter


if __name__ == "__main__":
    # Вхідні дані
    initial_guess = -9.0
    final_guess = 3.0
    tolerance = 1e-8
    max_iterations = 1000

    # Виклик Комбінований метод хорд та дотичних
    root, iterations = combined_method(initial_guess, final_guess, tolerance, max_iterations)

    if root is not None:
        # Перевірка значення функції в знайденій точці
        function_value_at_root = f(root)

        print(f"Корінь рівняння: {root}")
        print(f"Значення функції в корені: {function_value_at_root}")
        print(f"Кількість ітерацій: {iterations}")
    else:
        print("Метод не збігається до кореня за вказану кількість ітерацій.")
