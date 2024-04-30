import os 

def logoSenai():
    os.system("cls || clear")
    print("=== SENAI ===")

def somar(n1, n2):
    resultado = n1 + n2
    return resultado

def mediar(soma,qtd):
    resultado = soma /  qtd
    return resultado

logoSenai()
primeiroNumero = int(input("Digite o primeiro número: "))
logoSenai()
segundoNumero = int(input("Digite o segundo número: "))

soma = somar(primeiroNumero, segundoNumero)

media = mediar(soma,2)

print(media)
