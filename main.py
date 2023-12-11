import math

import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import fsolve

# Модифікований метод Ейлера
def modified_euler_method(f, x0, t0, tn, h):
    num_steps = int((tn - t0) / h)
    t_values = np.linspace(t0, tn, num_steps + 1)
    x_values = np.zeros((len(t_values), len(x0)))
    x_values[0] = x0

    for i in range(num_steps):
        x = x_values[i]
        t = t_values[i]
        x_star = x + h * f(x, t)
        f_star = f(x_star, t + h)
        x_next = x + 0.5 * h * (f(x, t) + f_star)
        x_values[i + 1] = x_next

    return t_values, x_values

# Неявний метод Ейлера
def implicit_euler_method(f, x0, t0, tn, h):
    num_steps = int((tn - t0) / h)
    t_values = np.linspace(t0, tn, num_steps + 1)
    x_values = np.zeros((len(t_values), len(x0)))
    x_values[0] = x0

    for i in range(num_steps):
        x_prev = x_values[i]
        t = t_values[i]

        def equation(x_next):
            return x_prev + h * f(x_next, t + h) - x_next

        x_next_guess = x_prev + h * f(x_prev, t)
        x_next_solution = fsolve(equation, x_next_guess)
        x_values[i + 1] = x_next_solution

    return t_values, x_values

# Явний метод Ейлера
def plicit_euler_method(f, x0, t0, tn, h):
    num_steps = int((tn - t0) / h)
    t_values = np.linspace(t0, tn, num_steps + 1)
    x_values = np.zeros((len(t_values), len(x0)))
    x_values[0] = x0

    for i in range(num_steps):
        x = x_values[i]
        t = t_values[i]
        x_next = x + h * f(x, t)
        x_values[i + 1] = x_next

    return t_values, x_values

Umax = 100
f = 50
U1 = lambda t: Umax * math.sin(2 * math.pi * f * t)
R1 = 5
R2 = 4
L2 = 0.02
L3 = 0.015
C1 = 300e-6
t0 = 0
tn = 0.2
x0 = np.array([0, 0, 0])
h = 10e-5

def F(x, t):
    dxdt = (x[1] + x[2]) / C1
    dydt = (U1(t) - x[0] - R1*x[1] - R1*x[2] - R2*x[1]) / L3
    dzdt = (U1(t) - x[0] - R1*x[1] - R1*x[2]) / L2
    return np.array([dxdt, dydt, dzdt])



# Модифікований метод Ейлера
t_values, x_values = modified_euler_method(F, x0, t0, tn, h)

u2_values = [4*elem for elem in  x_values[:, 2]]
u1_values = [Umax * math.sin(2 * math.pi * f * t) for t in t_values]

plt.figure(figsize=(10, 6))
plt.plot(t_values, u1_values, label='U1')
plt.plot(t_values, u2_values, label='U2')

plt.xlabel('Time (t)')
plt.ylabel('Volts')
plt.legend()
plt.title('System of Differential Equations (Modified Euler method)')
plt.grid(True)
plt.savefig('output_modified_euler_method.png')

# Неявний метод Ейлера
t_values, x_values = implicit_euler_method(F, x0, t0, tn, h)

u2_values = [4*elem for elem in  x_values[:, 2]]
u1_values = [Umax * math.sin(2 * math.pi * f * t) for t in t_values]

plt.figure(figsize=(10, 6))
plt.plot(t_values, u1_values, label='U1')
plt.plot(t_values, u2_values, label='U2')

plt.xlabel('Time (t)')
plt.ylabel('Volts')
plt.legend()
plt.title('System of Differential Equations (Implicit Euler method)')
plt.grid(True)
plt.savefig('output_implicit_euler_method.png')

# Явний метод Ейлера
t_values, x_values = plicit_euler_method(F, x0, t0, tn, h)

u2_values = [4*elem for elem in  x_values[:, 2]]
u1_values = [Umax * math.sin(2 * math.pi * f * t) for t in t_values]

plt.figure(figsize=(10, 6))
plt.plot(t_values, u1_values, label='U1')
plt.plot(t_values, u2_values, label='U2')


plt.xlabel('Time (t)')
plt.ylabel('Volts')
plt.legend()
plt.title('System of Differential Equations (Plicit Euler method)')
plt.grid(True)
plt.savefig('output_plicit_euler_method.png')
