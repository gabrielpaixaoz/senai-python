import os

os.system("clear")

notas = []
soma = 0

for i in range(4):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)
    soma = soma + nota

contador = len(notas)

media = soma/contador

for i in range(len(notas)):
    print(f"{i + 1}ª Nota:{notas[i]}")

print(f"Média: {media}")
if media >= 7:
    print("APROVADO!")
elif media >= 5 and media <= 6.9:
    print("RECUPERAÇÃO")
else:
    print("REPROVADO!")