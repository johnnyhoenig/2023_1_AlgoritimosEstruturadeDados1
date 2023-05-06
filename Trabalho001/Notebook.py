from Computador import Computador
class Notebook(Computador):
    def __init__(self, modelo, cor, preco,tempoDeBateria=None) -> str:
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria 


    def getInformacoes(self):
        print(super().__str__())
        print(f"Duraçao de bateria: {self.__tempoDeBateria}")
    
    def cadastrar(self,modelo,cor,preco,Tbateria):
        super().cadastrar(modelo,cor,preco)
        self.__tempoDeBateria=Tbateria
        
