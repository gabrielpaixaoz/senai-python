import os

os.system("cls")


numeros = []



for i in range(6): 
    while True:
        numero = int(input(f"Digite o {i + 1} número: "))
        if numero > 0 and numero % 2 == 0:
            numeros.append(numero)
            break



numeros.reverse()

print(numeros)

for i in range(6):
    print(f"{i + 1}º Número: {numeros[i]}")