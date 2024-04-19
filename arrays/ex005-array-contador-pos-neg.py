import os

os.system("clear")

numeros = []

qtdPositivo = 0
qtdNegativo = 0
soma = 0

for i in range(10):
    numero = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)
    if numero > 0:
        qtdPositivo = qtdPositivo +  1
        soma = soma + numero
    else:
        qtdNegativo = qtdNegativo + 1

 
print(f"Quantidade de números Positivos: {qtdPositivo}")
print(f"Soma dos positivos: {soma}")
print(f"Quantidade de números Negativos: {qtdNegativo}")
