import os
os.system("clear")

x = str(input("Digite o seu nick: "))

x = x.lower()
quite = (len(x) - 1) // 2

x = x[:quite] + x[:quite].upper() + x[quite + 1:]

xX = "Xx_" + x + "_xX"

print(xX)