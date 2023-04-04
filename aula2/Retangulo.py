class Retangulo():
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura


    def Calculo_area(self):
        return self.largura * self.altura


    def imprimir(self):
        print("largura:",self.largura)
        print("altura",self.altura)
        print("Área:",self.Calculo_area())

