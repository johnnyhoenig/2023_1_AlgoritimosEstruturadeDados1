class Veiculo:
    def __init__(self,marca=None,qtdrodas=None,modelo=None,) -> None:
        self.marca = marca
        self.qtdrodas = qtdrodas
        self.modelo = modelo
        self.velocidade = 0
    

    def __str__(self) -> str:
        print("Marca:",self.marca, "Numero de rodas: ",self.qtdrodas,"Modelo: ",self.modelo,"Velocidade: ",self.velocidade)

    def imprimir(self):
        print("Marca:",self.marca)
        print("Numero de Rodas: ",self.qtdrodas)
        print("Modelo: ",self.modelo)
        print("velocidade: ",self.velocidade)


    def acelerar(self,velocidadeDesejada=None):
        x=self.velocidade+velocidadeDesejada
        return f"velocidade",x


    def frear(self,velocidadeDesejada=None):
        y=self.velocidade-velocidadeDesejada
        return f"velocidade",y
    
    # def frear(self, valor = 0):
    #    self.velocidade -= valor if self.velocidade > 0 else 0