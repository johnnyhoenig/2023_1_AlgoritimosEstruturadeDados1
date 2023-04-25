from Veiculo import Veiculo
class Bicicleta(Veiculo):
    def __init__(self,marca,qtdrodas,modelo,numMarchas=None,bagageiro=None) :
        super().__init__(marca,qtdrodas,modelo,)
        self.numMarchas=numMarchas
        self.bagageiro=bagageiro
    

    def __str__(self) -> str:
        return super().__str__() + f"Numero de Marchas:",self.numMarchas,"Tamanho Bagageiro:",self.bagageiro

    def imprimir(self):
        super().imprimir()
        print("Numero de Marchas: ",self.numMarchas)
        print("Tamanho Bagageiro: ",self.bagageiro)





#b1 = Bicicleta(ffhfh, gfgf)

#print( b1 )

