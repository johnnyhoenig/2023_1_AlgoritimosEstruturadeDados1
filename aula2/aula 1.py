'''class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = pessoa("maria", 25)
print('nome:', p1.nome)
print('idade:', p1.idade)
'''
from Pessoa import Pessoa
#name = input("digite seu nome: ")
#posso criar um name antes ou imprimir tudo numa linha pessoa recebe paremetros imprimidos direto em linha:
p1 = Pessoa((str(input("digite o nome: "))), (int(input("digite idade: "))))
#print("Idade:", p1.idade)
p1.imprimir()

