import os
from dataclasses import dataclass

os.system("cls || clear")
QUANTIDADE_ALUNOS = 2


alunos = []
arquivo = 'T:\pythonclass\ex001\dlunos.txt'

@dataclass
class Aluno:
    nome: str
    idade: int
def salvar(lista):
    with open(arquivo, 'w') as arquivo:
        for aluno in alunos:
            arquivo.write(f"{aluno.nome},{aluno.idade}\n")
            print(f"Dados gravados com sucesso.")


print("Solicitando dados: ")
for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome = input("Digite seu nome: "),
        idade = int(input("Digite sua idade: "))
    )
    alunos.append(aluno)
    print()

salvar(alunos)

