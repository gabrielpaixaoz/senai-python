import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Aluno:
    nome: str
    idade: int

QUANTIDADE_ALUNOS = 2

alunos = []

for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome = input("Digite seu nome: "),
        idade = int(input("Digite sua idade:"))
    )
    alunos.append(aluno)

    arquivo = "alunos.txt"

    with open(arquivo, "w") as arquivoDeAlunos:
        for aluno in alunos:
            arquivoDeAlunos.write(f"{aluno.nome}, {aluno.idade} \n")

    print("Dados salvos com sucesso")
