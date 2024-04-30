import os

def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

def conversor(metro):
    centimentro = metro * 100
    return centimentro

logoSenai()

metro = float(input("Digite seu número em metros para conversão: "))


convertido = conversor(metro)

logoSenai()
print(f"{metro} Metros em centimetros: {convertido}")
