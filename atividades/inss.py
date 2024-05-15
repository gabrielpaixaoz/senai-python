import os

os.system("clear || cls")

loginCorreto : str = 'gabriel'
senhaCorreta : str = '123'

loginUsuario = input("Digite o seu login: ")
senhaUsuario = input('Digite a senha: ')


if loginCorreto == loginUsuario and senhaUsuario == senhaCorreta:
    print("Login acessado!")
    salario_base = int(input("Digite seu salário: "))
    
else:
    print("errado")
