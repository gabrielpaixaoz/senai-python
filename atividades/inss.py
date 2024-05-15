import os

os.system("clear || cls")

loginCorreto : str = 'gabriel'
senhaCorreta : str = '123'

loginUsuario = input("Digite o seu login: ")
senhaUsuario = input('Digite a senha: ')

def INSS(salario):
    if salario >= 0 and salario < 1101:
        desconto = salario * 0.075
        return salario - desconto
    elif salario >= 1101 and salario < 2203.48:
        desconto = salario * 0.9
        return salario - desconto
    elif salario >= 2203.49 and salario < 3305.22:
        desconto = salario * 0.12
        return salario - desconto
    elif salario >= 3305.23 and salario < 6433.57:
        desconto = salario * 0.14
        return salario - desconto
        
        
    

if loginCorreto == loginUsuario and senhaUsuario == senhaCorreta:
    print("Login acessado!")
    salario_base = int(input("Digite seu salário: "))
    salario_inss = INSS(salario_base)
    print(salario_base)
    print(salario_inss)
    
else:
    print("errado")
