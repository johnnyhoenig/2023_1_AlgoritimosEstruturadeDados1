from Veiculo import Veiculo
class Automovel(Veiculo):
    def __init__(self,marca,qtdrodas,modelo,potencidaDoMotor=None):
        super().__init__(marca,qtdrodas,modelo,)
        self.potenciaDoMotor=potencidaDoMotor
    
    
    def __str__(self) -> str:
        return super().__str__() + f"Potencia do motor: ",self.potenciaDoMotor
    

    def imprimir(self):
        super().imprimir()
        print("Potencia Motor: ",self.potenciaDoMotor)