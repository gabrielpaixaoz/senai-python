import os

os.system("clear || cls")

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))


print("\n ===Exibindo resultados=== ")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso:.3f}")