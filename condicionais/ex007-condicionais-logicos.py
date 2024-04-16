import os

os.system("cls || clear")

idade : int

idade = int(input("Digite sua idade: "))


if idade < 18 or idade >= 65:
    print("Não votar")
else:
    print("Pode votar.")