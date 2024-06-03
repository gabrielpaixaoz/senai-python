import os
from dataclasses import dataclass

os.system("cls || clear")

QUANTIDADE_USUARIOS = 1
usuarios = []
@dataclass

class Usuarios:
    nome:str
    data_de_nascimento:str
    rg:str
    cpf:str

def salvar(lista):
    arquivo = 'T:\python class\ex001\dados.txt'