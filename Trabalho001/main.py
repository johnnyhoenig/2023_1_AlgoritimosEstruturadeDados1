from Notebook import Notebook
from PC_mesa import PC_mesa

modelo=input("digite o modelo do desktop: ")
cor=input("digite a cor do desktop: ")
preco=input("digite o valor do desktop: ")
pfonte=input("digite a potencia da fonte:")
PC1=PC_mesa(modelo,cor,preco,pfonte)
PC2=PC_mesa("dell","vermelho",5999,500)
PC_mesa.getInformacoes(PC2)
PC_mesa.getInformacoes(PC1)
Note1=Notebook("lenovo","preto",800,3)
Notebook.getInformacoes(Note1)

modelo=input("digite o modelo do Notebook: ")
cor=input("digite a cor do Notebook: ")
preco=input("digite o valor do Notebook: ")
Tbateria=input("Digite o tempo de duraçao da bateria: ")
Note2=Notebook(modelo,cor,preco,Tbateria)
Notebook.getInformacoes(Note2)
