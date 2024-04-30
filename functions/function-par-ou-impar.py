import os 
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")


def checarParOuImpar(numero):
    if numero % 2 == 0:
        print("Par")
    else:
        print("Impar")

logoSenai()
numero = int(input("Digite um número: "))


logoSenai()
checarParOuImpar(numero)
