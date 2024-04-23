import os

os.system("cls")


numeros = []
qtdPar = 0
qtdImpar = 0
qtdPositivo = 0
qtdNegativo = 0
qtd = 0

for i in range(5):
    while True:
        numero = int(input(f"Digite {i + 1}º Número"))
        qtd = qtd + 1 
        if numero % 2 == 0:
            qtdPar = qtdPar + 1
        else:
            qtdImpar = qtdImpar + 1
        if numero > 0:
            qtdPositivo = qtdPositivo + 1
        else:
            qtdNegativo = qtdNegativo + 1
        break


print(qtdPar)
print(qtdImpar)
print(qtdPositivo)
print(qtdNegativo)
print(qtd)
        