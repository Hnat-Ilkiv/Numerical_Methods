import math

# Функція, яку інтегруємо
def f(x):
    return x * math.sqrt((x**2 - 4)**3)

def F(x):
    return math.sqrt((x**2 - 4)**5) / 5

# Метод правих прямокутників
def right_rectangle_method(a, b, n):
    h = (b - a) / n
    result = 0
    for i in range(1, n + 1):
        result += f(a + i * h)
    result *= h
    return result

# Метод лівих прямокутників
def left_rectangle_method(a, b, n):
    h = (b - a) / n
    result = 0
    for i in range(n):
        result += f(a + i * h)
    result *= h
    return result

# Метод трапецій
def trapezoidal_method(a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    result *= h
    return result

# Значення інтегралу за допомогою методів
a = 2
b = 3
n = 30

true_result = F(b) - F(a)
integral_right_rectangle = right_rectangle_method(a, b, n)
integral_left_rectangle = left_rectangle_method(a, b, n)
integral_trapezoidal = trapezoidal_method(a, b, n)

# Result ~11.18034
print(f"|           Метод               |  Результат  |Відносна похибка|")
print(f"|За методом правих прямокутників|{integral_right_rectangle:.10f}|   {(true_result - integral_right_rectangle):.10f}|")
print(f"|За методом лівих прямокутників |{integral_left_rectangle:.10f}|    {(true_result - integral_left_rectangle):.10f}|")
print(f"|За методом трапецій            |{integral_trapezoidal:.10f}|   {(true_result - integral_trapezoidal):.10f}|")
print(f"|Очікуваний результат           |{true_result:.10f}|    {(true_result - true_result):.10f}|")

