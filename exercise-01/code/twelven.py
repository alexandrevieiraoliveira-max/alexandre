import os
os.system("clear")


a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = ((b ** 2) - (4 * a * c)) ** (1/2)


x1 = (-b + delta) / (2 * a)
x2 = (-b - delta) / (2 * a)


print(f"O resultado é: {x1} e o {x2}")