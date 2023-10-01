import math

a = float(input("Введіть початок діапазону a: "))
b = float(input("Введіть кінець діапазону b: "))
h = float(input("Введіть крок h: "))

print("x\tf(x)")

x = a
while x <= b:
    fx = 0.9 * math.sin(math.pi + x) + 13 * math.exp(x)
    print(f"{x:.2f}\t{fx:.2f}")
    x += h
