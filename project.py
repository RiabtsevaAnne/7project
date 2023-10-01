import math

a = float(input("Введіть початок діапазону a: "))
b = float(input("Введіть кінець діапазону b: "))
h = float(input("Введіть крок h: "))

print("x\tf(x)")

for x in range(int(a * 100), int((b + h) * 100), int(h * 100)):
    x /= 100
    fx = 2 + 27 * math.log(x) + 3.97 * math.cos(x)
    print(f"{x:.2f}\t{fx:.2f}")

