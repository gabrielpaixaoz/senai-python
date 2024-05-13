class Reserva:
    def __init__(self, numero_aviao, nome_passageiro):
        self.numero_aviao = numero_aviao
        self.nome_passageiro = nome_passageiro

# Inicialização dos vetores
avioes = [0] * 4
assentos_disponiveis = [0] * 4
reservas = []

def registrar_avioes():
    print("Informe o número de cada avião:")
    for i in range(4):
        avioes[i] = input(f"Avião {i+1}: ")

def registrar_assentos_disponiveis():
    print("Informe a quantidade de assentos disponíveis para cada avião:")
    for i in range(4):
        assentos_disponiveis[i] = int(input(f"Assentos disponíveis para o avião {avioes[i]}: "))

def realizar_reserva():
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
    print("Aviões disponíveis: ")
    for i in range(4):
        print(f"Avião nº {avioes[i]}")
    numero = input("Informe o número do avião: ")
    indice_aviao = avioes.index(numero)
    indice_aviao + 1
    
    def filtrar_aviao(reservas, numero):
        return [obj.nome_passageiro for obj in reservas if obj.numero_aviao == numero]

    nomes_filtrados = filtrar_aviao(reservas,reservas[indice_aviao].numero_aviao)

    print(f"Reservas no avião {numero}: ")
    for i in range(len(nomes_filtrados)):
        print(f"{i + 1}º Passageiro: {nomes_filtrados[i]}")
    

def verificar_passageiro():
    passageiro = str(input("Digite o nome do passageiro: "))
    def filtrar_passageiro(reservas, passageiro):
        return [obj for obj in reservas if obj.nome_passageiro == passageiro]
    aviao_filtrados = filtrar_passageiro(reservas,passageiro)

    print(aviao_filtrados)

    for pessoa in aviao_filtrados:
     print(f"Nome: {pessoa.nome_passageiro}, Idade: {pessoa.numero_aviao}")




def menu():
    print("\nMenu:")
    print("1. Registrar número de cada avião")
    print("2. Registrar quantitativo de assentos disponíveis em cada avião")
    print("3. Reservar passagem aérea")
    print("4. Encerrar")
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
