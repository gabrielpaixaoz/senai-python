import os

os.system("clear")

numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º Número: "))
    if numero < 0:
        numero = 0
    numeros.append(numero)

print(numeros)