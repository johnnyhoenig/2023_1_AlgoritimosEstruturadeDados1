from Cidade import Cidade
from Pessoa import Pessoa
from Produto import Produto
from Pedido import Pedido
from Categoria import Categoria

c1=Cidade("Porto Alegre")
p1 =Pessoa("joao", "5133224455", c1)
print("Nome da cidade do ", p1.nome, ":", p1.city.nome)
print("-------------------------------------")
p1.imprimir()
print("----------------------------")

"""Produto=[]

prod=input("digite o nome do produto: ")
while (prod):
    try:
        Produto.preco = input("digite o valor do produto:")
        Produto.categoria = input("digite a categoraia do produto:")
        Produto.nome = input("digite nome do produto")
    except:
        print("erro")
    prod=input("digite o nome do produto: ")

print(prod)"""