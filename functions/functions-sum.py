import os

def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

def somar(n1, n2):
    resultado = n1 + n2
    return resultado


logoSenai()
primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))

soma = somar(primeiroNumero, segundoNumero)

print(f"Soma: {soma}")
