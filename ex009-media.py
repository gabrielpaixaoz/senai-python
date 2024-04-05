import os

os.system("clear || cls")

nome : str
idade : int
nota1 : float
nota2 : float
nota3 : float
nota4 : float
media : float

nome = str(input("Digite seu nome: "))

idade = int(input("Digite sua idade"))

nota1 = float(input("Digite a 1 nota: "))

nota2 = float(input("Digite a 2 nota: "))

nota3 = float(input("Digite a 3 nota: "))

nota4 = float(input("Digite a 4 nota: "))

media = (nota1 + nota2 + nota3 + nota4)/4

print(f"Média: {media}")
