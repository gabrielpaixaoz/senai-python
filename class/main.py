import os
os.system("cls || clear")
class Reserva:
    def __init__(self, numero_aviao, nome_passageiro):
        self.numero_aviao = numero_aviao
        self.nome_passageiro = nome_passageiro

# Inicialização dos vetores
avioes = [0] * 4
assentos_disponiveis = [0] * 4
reservas = []

def registrar_avioes():
    os.system("cls || clear")
    print("Informe o número de cada avião:")
    for i in range(4):
        avioes[i] = input(f"Avião {i+1}: ")

def registrar_assentos_disponiveis():
    os.system("cls || clear")
    print("Informe a quantidade de assentos disponíveis para cada avião:")
    for i in range(4):
        assentos_disponiveis[i] = int(input(f"Assentos disponíveis para o avião {avioes[i]}: "))

def realizar_reserva():
    os.system("cls || clear")
    if len(reservas) >= 10:
        print("Limite de reservas atingido!")
        return
    
    numero_aviao = input("Informe o número do avião: ")
    if numero_aviao not in avioes:
        print("Este avião não existe!")
        return
    
    indice_aviao = avioes.index(numero_aviao)
    if assentos_disponiveis[indice_aviao] == 0:
        print("Não há assentos disponíveis para este avião!")
        return
    
    nome_passageiro = input("Informe o nome do passageiro: ")
    reservas.append(Reserva(numero_aviao, nome_passageiro))
    assentos_disponiveis[indice_aviao] -= 1
    print("Reserva realizada com sucesso!")


def verificar_aviao():
    os.system("cls || clear")
    def filtrar_aviao(reservas, numero):
        return [obj.nome_passageiro for obj in reservas if obj.numero_aviao == numero]
    print("Aviões disponíveis: ")
    for i in range(4):
        print(f"Avião nº {avioes[i]}")
    numero = input("Informe o número do avião: ")
    if numero not in avioes:
        print("Este avião não existe!")
        return
    indice_aviao = avioes.index(numero)
    


    

    if 0 <= indice_aviao < len(reservas):

        nomes_filtrados = filtrar_aviao(reservas,reservas[indice_aviao].numero_aviao)
        for i in range(len(nomes_filtrados)):
            print(f"{i + 1}º Passageiro: {nomes_filtrados[i]}")
    else:
        print("Não há reservas realizadas para este avião!")

    

    
    
    
    

def verificar_passageiro():
    os.system("cls || clear")
    passageiro = str(input("Digite o nome do passageiro: "))
    def filtrar_passageiro(reservas, passageiro):
        return [obj for obj in reservas if obj.nome_passageiro == passageiro]
    aviao_filtrados = filtrar_passageiro(reservas,passageiro)

    if len(aviao_filtrados) <= 0:
        print("Não há reservas realizadas para este passageiro!")
    else:
        print("=== Reservas realizadas ===")
        for pessoa in aviao_filtrados:
            print(f"Reserva para o avião nº: {pessoa.numero_aviao}")




def menu():
    print("\nMenu:")
    print("1. Registrar número de cada avião")
    print("2. Registrar quantitativo de assentos disponíveis em cada avião")
    print("3. Reservar passagem aérea")
    print("4. Verificar avião")
    print("5. Verificar passageiro")
    print("6. Encerrar")

    print(avioes)
    print(assentos_disponiveis)

# Programa principal
while True:
    menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        registrar_avioes()
    elif opcao == 2:
        registrar_assentos_disponiveis()
    elif opcao == 3:
        realizar_reserva()
    elif opcao == 4:
        verificar_aviao()
    elif opcao == 5:
        verificar_passageiro()
    elif opcao == 6:
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")
