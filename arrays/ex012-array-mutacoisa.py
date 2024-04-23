import os

os.system("cls")


numeros = []
qtdPar = 0
qtdImpar = 0
qtdPositivo = 0
qtdNegativo = 0
qtd = 0
maiorNumero = 0
menorNumero = 999999999
somaImpar = 0
somaPar = 0
soma = 0

for i in range(5):
    while True:
        numero = int(input(f"Digite {qtd + 1}º Número: "))
        qtd = qtd + 1
        soma = soma + numero 
        if numero % 2 == 0:
            qtdPar = qtdPar + 1
            somaPar = somaPar + numero
        else:
            qtdImpar = qtdImpar + 1
            somaImpar = somaImpar + numero
        if numero > 0:
            qtdPositivo = qtdPositivo + 1
        else:
            qtdNegativo = qtdNegativo + 1
        if numero > maiorNumero:
            maiorNumero  = numero
        if numero < menorNumero:
            menorNumero = numero
        break

mediaPar = somaPar / qtdPar
mediaImpar = somaImpar / qtdImpar
media = soma / qtd



print(f"Quantidade de números pares :{qtdPar}")
print(f"Quantidade de números impares:{qtdImpar}")
print(f"Quantidade de números positivos: {qtdPositivo}")
print(f"Quantidade de números negativos: :{qtdNegativo}")
print(f"Quantidade de números inseridos:{qtd}")
print(f"Média de números pares:{mediaPar}")
print(f"Média de números impares:{mediaImpar}")
print(f"Média dos numeros inseridos:{media}")


numeros.reverse()

print(numeros)