import os

def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")


def mostrarTabuada(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")



while True:
    logoSenai()
    numero = int(input("Digite um número de 1 a 10: "))

    if numero > 1 and numero < 10:
        break


mostrarTabuada(numero)
    


