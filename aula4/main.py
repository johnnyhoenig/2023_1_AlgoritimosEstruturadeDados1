from Fisica import Fisica
from Cidade import Cidade
from Juridica import Juridica

c1=Cidade("POA",1)
c2=Cidade("Capão da Canoa",2)

pf1 = Fisica("joao","3322-5500", c1 , "000.538.447-35")
pf2 = Fisica("maria","3322-5450", c2 , "361.558.447-35")
pf3 = Fisica("carlos","3322-7777", c1 , "666.538.442-35")

pj1 = Juridica("Mercado do zé","987654321",c2,"00.111.222/0001-02")


pj1.imprimir()
pj1.addfuncionario(pf1)
pj1.addfuncionario(pf2)
pj1.imprimir()