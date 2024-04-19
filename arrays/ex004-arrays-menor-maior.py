import os 

os.system("clear")

numeros = []
maiorNumero = 0
menorNumero = 99999

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º Número: "))
    numeros.append(numero)
    if numero > maiorNumero:
        maiorNumero = numero
    if numero < menorNumero:
        menorNumero = numero


print(f"Números informados: {numeros}")
print(f"Maior número: {maiorNumero}")
print(f"Menor número: {menorNumero}")