from Computador import Computador
class PC_mesa(Computador):
    def __init__(self, modelo, cor, preco,potenciaDaFonte=None):
        self._potenciaDaFonte = potenciaDaFonte
        super().__init__(modelo, cor, preco)
    

    def __str__(self) -> str:
       return f"Modelo: {self.__modelo}, Cor: {self.__cor}, Preço: {self.__preco}, Potencia da fonte: {self._potenciaDaFonte}."
    
    
    def getInformacoes(self):
        print(super().__str__())
        print("potencia da Fonte:" ,self._potenciaDaFonte)
    

    def cadastrar(self,modelo,cor,preco,potenciaDaFonte):
        super().cadastrar(modelo,cor,preco)
        self._potenciaDaFonte = potenciaDaFonte