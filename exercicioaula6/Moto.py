from Autormovel import Automovel
class Moto(Automovel):
    def __init__(self,marca,qtdrodas,modelo,potencidaDoMotor,partidaEletrica=None):
        super().__init__(marca,qtdrodas,modelo,potencidaDoMotor)
        self.partidaEletrica = partidaEletrica
    
    def __str__(self) -> str:
        return super().__str__() + f"Partida eletrica: ",self.partidaEletrica
    
    def imprimir(self):
        super().imprimir()
        print("Partida Eletrica: ",self.partidaEletrica)
    


    
