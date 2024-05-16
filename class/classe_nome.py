class Cliente:
    def __init__(self, nome,idade,sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

print("Solicitando dados ao usuário")


clientes = []
for i in range(3):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo: ")
    clientes.append(Cliente(nome,idade,sexo))

for cliente in clientes:
    print(f"Nome: {cliente.nome}")
    print(f"Idade: {cliente.idade}")
    print(f"Sexo: {cliente.sexo}")
