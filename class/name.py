class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

identidades = []

for i in range(4):
  name = input("Digite o nome: ")
  age = int(input("Digite sua idade: "))
  identidades.append(Person(name,age))



for pessoa in identidades:
    print(f"Nome: {pessoa[2].name}, Idade: {pessoa[2].age}")

#print(f"Nome: {identidades[2].name}, Idade: {identidades[2].age}")
