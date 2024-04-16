import os


os.system("clear")

nota : float = -1

while (nota < 0 or nota > 10):
    nota = float(input("Digite a nota: "))    

print(f"Sua nota: {nota}")