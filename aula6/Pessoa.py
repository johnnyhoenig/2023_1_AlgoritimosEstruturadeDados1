from Cidade import Cidade

class Pessoa:
    def __init__(self, name=None, fone=None , cidade=None):
        self.id = None
        self.nome = name
        self.fone = fone
        self.city = cidade
    

    def __str__(self) -> str:
        texto = "Nome:"+self.nome
        texto += "\n Fone: "+self.fone
        return texto


    def imprimir(self):
        print("nome: ",self.nome)
        print("Telefone: ", self.fone)
        print("Cidade: ", self.city.nome)