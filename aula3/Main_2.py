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
cat1 = Categoria("Bebidas")
cat2 = Categoria("alimentos")
prod1 = Produto("coca-cola",7.99,cat1)
prod2 = Produto("Fanta", 6.95 ,cat1)
prod3 = Produto("Arroz",3.95 ,cat2)

ped1 = Pedido ("27/03/2023", "Rua a,100", p1)
print("Total: ", ped1.addProduto(prod1))
print("Total: ", ped1.addProduto(prod2))
ped1.imprimir()