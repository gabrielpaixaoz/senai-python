import os

os.system("clear || cls")


soma : float
media : float
produto : float

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma = numero1 + numero2
media = soma/2
produto = numero1 * numero2


print(f"Soma: {soma}")
print(f"Media: {media}")
print(f"Produto: {produto}")







if(numero1 > numero2):
    print(f"Maior número: {numero1}")
else:
    print(f"Maior número: {numero2}")

if(numero1 < numero2):
    print(f"Menor número: {numero1}")
else:
    print(f"Menor número: {numero2}")
