import os
from dataclasses import dataclass

os.system("cls || clear")
QUANTIDADE_DE_PESSOAS = 3
pessoas = []
@dataclass
class Pessoa:
    nome : str
    idade : int
    peso : float
    altura : float

def salvar(lista):
    arquivo = 'T:\pythonclass\ex002\dados.txt'
    with open(arquivo, 'w') as arquivo:
        for pessoa in pessoas:
            arquivo.write(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}, Peso: {pessoa.peso}, Altura: {pessoa.altura}\n")
            print(f"Dados gravados com sucesso.")

print("Solicitando dados: ")
for i in range(QUANTIDADE_DE_PESSOAS):
    pessoa = Pessoa(
        nome = input("Digite seu nome: "),
        idade = int(input("Digite sua idade: ")),
        peso = float(input("Digite seu peso: ")),
        altura = float(input("Digite sua altura: "))
    )
    pessoas.append(pessoa)
    print()

    salvar(pessoas)




