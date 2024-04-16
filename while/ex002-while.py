import os

os.system("clear")


nota1 : float = -1

while(nota1 < 0 or nota1 > 10):
    nota1 = float(input("Digite a primeira nota: "))

nota2 : float = -1

while(nota2 < 0 or nota2 > 10):
    nota2 = float(input("Digite a segunda nota: "))

soma = nota1 + nota2

media = soma/2

print(f"A média: {media}")