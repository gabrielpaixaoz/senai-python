import os

os.system("clear")

nota : float = -1
soma : float = 0

for i in range(1,4):
    while True:
        nota = float(input("Digite a Nota: "))
        if nota < 0 or nota > 10:
            print("Nota inválida...") #true
        else:
            soma += nota #false
            break

media = soma / 2\

print(f"Média: {media}")

if media >= 7:
    print("Aprovado!")
elif media < 5:
    print("Reprovado!")   
elif media >= 5 and media <= 6.9:
    print("Recuperação") 

    