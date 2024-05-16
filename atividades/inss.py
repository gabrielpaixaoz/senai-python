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
        desconto = salario * 0.09
        return salario - desconto
    elif salario >= 2203.49 and salario < 3305.22:
        desconto = salario * 0.12
        return salario - desconto
    elif salario >= 3305.23:
        desconto = salario * 0.14
        if desconto >= 854.36:
            desconto = 854.36    
        return salario - desconto

def IRRF(salario):
    if salario <= 2259.20:
        desconto = 0
        return salario - desconto
    elif salario >= 2259.20 and salario <= 2826.65:
        desconto = salario * 0.075
        return salario - desconto
    elif salario >= 2826.66 and salario <= 3751.05:
        desconto = salario * 0.15
        return salario - desconto
    elif salario >= 3751.06 and salario <= 4664.68:
        desconto = salario * 0.225
        return salario - desconto
    elif salario >= 4664.69:
        desconto = salario * 0.275
        return salario - desconto

def TRSS(salario,resposta):
    if resposta == 's':
        desconto = salario * 0.06
        return salario - desconto
        
    
def vale_refeicao(salario,beneficio):
    desconto = valor_beneficio * 0.20
    return salario - desconto 


if loginCorreto == loginUsuario and senhaUsuario == senhaCorreta:
    print("Login acessado!")
    salario_base = int(input("Digite seu salário: "))
    vale_tranposrte = input("Deseja vale transporte?(s/n): ")
    valor_beneficio = int(input("Digite o valor vale refeição fornecido pela empresa: "))
    desconto_inss = salario_base - INSS(salario_base)
    desconto_irrf = salario_base - IRRF(salario_base)
    desconto_transporte = salario_base - TRSS(salario_base,vale_tranposrte)
    desconto_beneficio = salario_base - vale_refeicao(salario_base,valor_beneficio)
    
    print(f"Salário base: {salario_base}")
    print(f"Desconto INSS: {desconto_inss}")
    print(f"Desconto IRFF: {desconto_irrf}")
    print(f"Desconto vale transporte: {desconto_transporte}")
    print(f"Desconto benefício: {desconto_beneficio}")
    
    
    
else:
    print("errado")
