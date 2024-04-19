from os import system

system("clear")

notas = []
qtd = 0
soma = 0

for i in range(3):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)
    soma = soma + nota

qtd = len(notas)


media = soma/qtd

mediaFormatada = round(media,2)


for i in range(len(notas)):
    print(f"{i + 1}ª Nota: {notas[i]}")

print(mediaFormatada)