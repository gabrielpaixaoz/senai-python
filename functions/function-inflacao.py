import os

def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")



def inflacionar(preco):
    desconto10 = preco * 0.1
    desconto20 = preco * 0.2
    if preco <= 99:
        inflacao = preco - desconto10
        return inflacao

    else:
        inflacao = preco - desconto20
        return inflacao
    

logoSenai()
preco = float(input("Digite o preço: "))

inflacao = inflacionar(preco)

print(inflacao)
