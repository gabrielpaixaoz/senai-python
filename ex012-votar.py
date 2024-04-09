import os

os.system("cls || clear")

idade = int(input("Digite a sua idade: "))

if(idade <= 17 or idade >= 66):
    print(f"Não é obrigado a votar")
else:
    print(f"Obrigado a votar")
