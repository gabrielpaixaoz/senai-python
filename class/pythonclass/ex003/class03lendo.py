import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Aluno:
    nome : str
    idade : int

arquivoOrigem = 'T:\pythonclass\ex003\dados.txt'

listaAlunos = []

with open(arquivoOrigem, 'r') as arquivo:
    for linha in arquivo:
        nome, idade = linha.strip().split(',')
        listaAlunos.append(Aluno(nome=nome, idade=int(idade)))


print("\n Exibindo dados")
for i in listaAlunos:
    print(f"Nome: {i.nome}")
    print(f"Idade: {i.idade}")
    print()