import math

from steffensen_method import steffensen_method
from combined_method import combined_method
from secant_method import secant_method

def f(x):
    return math.exp(x) + x

def df(x):
    return 1 + math.exp(x)

if __name__ == "__main__":
    # Вхідні дані
    initial_guess = -9.0
    final_guess = 3.0
    tolerance = 1e-10
    max_iterations = 1000

    # Виклик методу Стефенсена
    root, iterations = steffensen_method(f, initial_guess, final_guess, tolerance, max_iterations)

    if root is not None:
        # Перевірка значення функції в знайденій точці
        function_value_at_root = f(root)

        print("Метод Стеффенсуна:")
        print(f"\tКорінь рівняння: {root}")
        print(f"\tЗначення функції в корені: {function_value_at_root}")
        print(f"\tКількість ітерацій: {iterations}")
    else:
        print("\tМетод не збігається до кореня за вказану кількість ітерацій.")

    # Виклик Комбінований методу хорд та дотичних
    root, iterations = combined_method(f, df, initial_guess, final_guess, tolerance, max_iterations)

    if root is not None:
        # Перевірка значення функції в знайденій точці
        function_value_at_root = f(root)

        print("Комбінований метод хорд та дотичних:")
        print(f"\tКорінь рівняння: {root}")
        print(f"\tЗначення функції в корені: {function_value_at_root}")
        print(f"\tКількість ітерацій: {iterations}")
    else:
        print("\tМетод не збігається до кореня за вказану кількість ітерацій.")

    # Виклик Методу січних
    root, iterations = secant_method(f, initial_guess, final_guess, tolerance, max_iterations)

    if root is not None:
        # Перевірка значення функції в знайденій точці
        function_value_at_root = f(root)

        print("Метод січних:")
        print(f"\tКорінь рівняння: {root}")
        print(f"\tЗначення функції в корені: {function_value_at_root}")
        print(f"\tКількість ітерацій: {iterations}")
    else:
        print("\tМетод не збігається до кореня за вказану кількість ітерацій.")
