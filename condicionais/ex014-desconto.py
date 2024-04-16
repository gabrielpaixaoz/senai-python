import os

os.system("clear || cls")

precoMorango = 2.50
precoMaca = 1.80

kgMorango = int(input("Quantos kilos de morango?: "))
kgMaca = int(input("Quantos kilos de maçã: "))

if kgMorango > 5:
    precoMorango = 2.20

if kgMaca > 5:
    precoMaca = 1.50

morangoPrecoTotal = precoMorango * kgMorango

macaPrecoTotal = precoMaca * kgMaca

KgTotal = kgMorango + kgMaca

Precototal = morangoPrecoTotal + macaPrecoTotal

Desconto = Precototal * 0.1

if KgTotal > 8 or Precototal > 25.00:
    Precototal = Precototal - Desconto


print(f"{KgTotal}")
print(f"{Precototal}")

