import os

os.system("cls || clear")

loginCorreto : str
senhaCorreta : str

loginCorreto = "Zodan"
senhaCorreta = "123"

nome = str(input("Digite o usuário: "))
senha = str(input("Digite a senha: "))

if(nome == loginCorreto and senha == senhaCorreta):
    print(f"Bem-vindo!")    
else:
    print(f"Login ou senha inválidos.")