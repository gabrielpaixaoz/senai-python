import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Aluno:
    nome : str
    idade : int

QUANTIDADE_ALUNOS = 2

alunos = []

for i in range(QUANTIDADE_ALUNOS):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    alunos.append(Aluno(nome = nome,idade = idade))

for aluno in alunos:
    print(f"Nome: {aluno.nome}")
    print(f"Idade: {aluno.idade}")
