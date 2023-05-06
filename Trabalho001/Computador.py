from abc import ABC, abstractmethod
class Computador(ABC):
    def __init__(self,modelo=None,cor=None,preco=None) -> str:
        self.__modelo=modelo
        self.__cor=cor
        self.__preco=preco
    

    def __str__(self) -> str:
       return f"Modelo: {self.__modelo}, Cor: {self.__cor}, Preço: {self.__preco}."
    
    def getInformacoes(self):
       print(super().__str__())
    
    @abstractmethod
    def cadastrar(self,modelo,cor,preco):
        self.__modelo=modelo   
        self.__cor=cor  
        self.__preco=preco