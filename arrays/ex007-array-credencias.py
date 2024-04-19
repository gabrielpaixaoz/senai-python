import os
import random
from typing import List

os.system("clear")




numeros = []

for i in range(6):
    while True:
        numero = int(input(f"Digite o {i + 1}º Número: "))
        if numero > 0 and numero % 2 == 0:
            numeros.append(numero)
            break


numeros.reverse()

print(numeros)
