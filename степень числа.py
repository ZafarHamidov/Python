print("Программа возведения числа в квадрат")
n = int(input("Type a number: "))
for i in range(1, n+1):
    print(f"{i} x {i} = {i * i}")

print("Программа возведения числа в куб")
n = int(input("Type a number: "))
for i in range(1, n+1):
    print(f"{i} x {i} x {i} = {i * i * i}")

print("Программа возведения числа в любую степень")
while True:
    x = int(input("Число: "))
    n = int(input("Степень: "))
    print(x**n)

