import matplotlib.pyplot as plt


def runge_kutta_system(x0, y0, x_end, h):
    x_values = []
    y1_values = []
    y2_values = []
    y3_values = []

    x = x0
    y1, y2, y3 = y0

    while x < x_end:
        x_values.append(x)
        y1_values.append(y1)
        y2_values.append(y2)
        y3_values.append(y3)

        k1 = h * f1(x, y1, y2, y3)
        l1 = h * f2(x, y1, y2, y3)
        m1 = h * f3(x, y1, y2, y3)

        k2 = h * f1(x + h / 2, y1 + k1 / 2, y2 + l1 / 2, y3 + m1 / 2)
        l2 = h * f2(x + h / 2, y1 + k1 / 2, y2 + l1 / 2, y3 + m1 / 2)
        m2 = h * f3(x + h / 2, y1 + k1 / 2, y2 + l1 / 2, y3 + m1 / 2)


        k3 = h * f1(x + h / 2, y1 + k2 / 2, y2 + l2 / 2, y3 + m2 / 2)
        l3 = h * f2(x + h / 2, y1 + k2 / 2, y2 + l2 / 2, y3 + m2 / 2)
        m3 = h * f3(x + h / 2, y1 + k2 / 2, y2 + l2 / 2, y3 + m2 / 2)

        k4 = h * f1(x + h, y1 + k3, y2 + k3, y3 + k3)
        l4 = h * f2(x + h, y1 + l3, y2 + l3, y3 + l3)
        m4 = h * f3(x + h, y1 + m3, y2 + m3, y3 + m3)

        y1 = y1 + (k1 + 2 * k2 + 2* k3 + k4) / 6
        y2 = y2 + (l1 + 2 * l2 + 2 * l3 + l4) / 6
        y3 = y3 + (m1 + 2 * m2 + 2 * m3 + m4) / 6

        x = x + h

    return x_values, y1_values, y2_values, y3_values


def u1(x):
    a = 0.003
    period = 6 * a
    x_shifted = x % period

    if x_shifted < 3 * a:
        return 10
    elif 3 * a <= x_shifted < 4 * a:
        return -10 / a * (x_shifted - 3 * a)
    elif 4 * a <= x_shifted < 5 * a:
        return -10
    else:
        return 10 / a * (x_shifted - 5 * a) - 10


def L2(y2):
    L_min = 7.2
    L_max = 72
    R1 = 10
    R2 = 20
    i_min = 1
    i_max = 2
    a0 = (L_min * i_max ** 2 - L_min * i_min ** 2 - L_max * i_max ** 2 + L_max * i_min ** 2) / (i_max ** 2 - i_min ** 2)
    a1 = a0 + R1 * i_min
    a2 = a0 + R1 * i_max
    a3 = a0 + R2 * i_max

    if abs(y2) <= 1:
        return 15
    elif abs(y2) <= 2:
        return a0 + a1 * (abs(y2)) + a2 * (abs(y2) ** 2) + a3 * (abs(y2) ** 3)
    else:
        return 1.5


def f1(x, y1, y2, y3):
    return ((u1(x) - y1 + y2 * 49 - y3) / (10 + 20)) / (28 * 10 **(-3))


def f2(x, y1, y2, y3):
    return (y3 - y2 * 49 - (((u1(x) - y1 + y2 * 49 - y3) / (10 + 20)) - y2) * 42) / L2(y2)


def f3(x, y1, y2, y3):
    return (((u1(x) - y1 + y2 * 49 - y3) / (10 + 20)) - y2) / (0.32 * 10 **(-3))


x0 = 0
y0 = [1, 0, 0]
x_end = 0.03
h = 0.000015

x_values, y1_values, y2_values, y3_values = runge_kutta_system(x0, y0, x_end, h)

with open("result.csv", "w") as file:
    file.write(f"Час,Напруга на конденсаторі С1,Напруга на конденсаторі С2,Індуктивність L2,Струм в індуктивності,Напруга на U1,Напруга на U2\n")
    for x, y1, y2, y3 in zip(x_values, y1_values, y2_values, y3_values):
        file.write(f"{x},{y1},{y3},{L2(y2)},{y2},{u1(x)},{50*y3}\n")

plt.figure(figsize=(12, 8))

plt.subplot(3, 2, 1)
plt.plot(x_values, y1_values)
plt.title("Напруга на конденсаторі C1 (y1)")
plt.xlabel("Час (s)")
plt.ylabel("Вольт (V)")

plt.subplot(3, 2, 3)
plt.plot(x_values, y3_values)
plt.title("Напруга на конденсаторі C2 (y3)")
plt.xlabel("Час (s)")
plt.ylabel("Вольт (V)")

plt.subplot(3, 2, 2)
plt.plot(x_values, y2_values)
plt.title("Струм в індуктивності L1 (y2)")
plt.xlabel("Час (s)")
plt.ylabel("Ампер (A)")

plt.subplot(3, 2, 5)
plt.plot(x_values, [u1(elem) for elem in x_values])
plt.title("Напруга  U1 (x)")
plt.xlabel("Час (s)")
plt.ylabel("Вольт (V)")
plt.tight_layout()

plt.subplot(3, 2, 4)
plt.plot(x_values, [elem * 50 for elem in y3_values])
plt.title("Напруга  U2 (50*y3)")
plt.xlabel("Час (s)")
plt.ylabel("Вольт (V)")

# plt.show()
plt.savefig('output_runge_kutta')

