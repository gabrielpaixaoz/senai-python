import os
from dataclasses import dataclass


os.system("cls || clear")
QUANTIDADE_LIVROS = 1
livros = []
@dataclass
class Livro:
    nome:str
    autor:str
    categoria:str
    preco:float 

def salvar(lista):
    arquivo = 'T:\pythonclass\ex004\dados.txt'
    with open(arquivo, 'w') as arquivo:
        for livro in livros:
            arquivo.write(f"Nome:{livro.nome}, Autor:{livro.autor}, Categoria:{livro.categoria}, Preço:{livro.preco},")
            print(f"Dados gravados com sucesso.")


print("Solicitando dados: ")
for i in range(QUANTIDADE_LIVROS):
    livro = Livro(
        nome = input("Digite a nome do livro: "),
        autor = input("Digite o autor do livro:"),
        categoria = input("Digite a categoria do livro: "),
        preco = float(input("Digite o preço do livro: "))
    )
    livros.append(livro)
    print()

salvar(livros)