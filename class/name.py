class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

identidades = []

for i in range(3):
  name = input("Digite o nome: ")
  age = int(input("Digite sua idade: "))
  identidades.append(Person(name,age))



for pessoa in identidades:
   print(f"Nome: {pessoa.name}, Idade: {pessoa.age}")


escolha = int(input("Escolha a idade desejada: "))



if escolha == identidades[0].age:
  print(identidades[0].age)

elif escolha == identidades[1].age:
  print(identidades[1].age)

elif escolha == identidades[2].age:
  print(identidades[2].age)



# if identidades[1].age == 20:
 # print("Este número é 20!")
# else:
 # print("Este número não é 20!")
