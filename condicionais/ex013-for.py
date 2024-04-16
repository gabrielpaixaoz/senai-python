import os 

os.system

qtdPar : int
qtdImpar : int

qtdPar = 0
qtdImpar = 0

n1 = int(input("Digite o primeiro número: "))
if n1 % 2 == 0:
    qtdPar = qtdPar + 1
else:
    qtdImpar = qtdImpar + 1 

n2 = int(input("Digite o segundo número: "))
if n2 % 2 == 0:
    qtdPar = qtdPar + 1
else:
    qtdImpar = qtdImpar + 1

n3 = int(input("Digite o terceiro número: "))
if n3 % 2 == 0:
    qtdPar = qtdPar + 1
else:
    qtdImpar = qtdImpar + 1

n4 = int(input("Digite o quarto número: "))
if n4 % 2 == 0:
    qtdPar = qtdPar + 1
else:
    qtdImpar = qtdImpar + 1

n5 = int(input("Digite o quinto número: "))
if n5 % 2 == 0:
    qtdPar = qtdPar + 1
else:
    qtdImpar = qtdImpar + 1

soma : int

soma = n1 + n2 + n3 + n4 + n5

print(f"Soma: {soma}")
print(f"Quantidade de pares: {qtdPar}")
print(f"Quantidade de ímpares: {qtdImpar}")




soma = n1 + n2 + n3 + n4 + n5