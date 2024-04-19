import os

os.system("clear")

nota : float = -1
soma : float =  0
contador = 0

while True:
    soma += nota 
    contador += 1
    nota = float(input("Digite a Nota: "))

    resposta = (input("Deseja inserir mais uma nota?"))
    
    if resposta == 'S':
           teste = 0
    elif resposta == 'N':
          break
    elif resposta == 'P':
          print(f"Quantidade de notas: {contador}")


media = soma / contador

print(f"Média: {media}")
print(contador)
print(soma)

    