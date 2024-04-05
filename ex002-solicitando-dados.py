import os

os.system("clear")

#Solicitando dados para o usuário.
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso  = float(input("Digite seu peso: "))


# Exibindo dados inseridos pelo usuário.
print("\n=== Exibindo resultados ===")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso}")