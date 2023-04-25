from Autormovel import Automovel
class Carro(Automovel):
    def __init__(self,marca,qtdrodas,modelo,potencidaDoMotor,qtdPortas=None):
        super().__init__(marca,qtdrodas,modelo,potencidaDoMotor)
        self.qtdPortas=qtdPortas
    
    def __str__(self) -> str:
        print("Numero de Portas:",self.qtdPortas)
    
    def imprimir(self):
        super().imprimir()
        print("Numero de portas: ",self.qtdPortas)