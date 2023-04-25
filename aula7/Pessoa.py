class Pessoa:
    def __init__(self, name=None, fone=None ,Endereco=None):
        self.id = None
        self.nome = name
        self._fone = fone
        self.__Endereco = Endereco


    def __str__(self) -> str:
        return print("nome: ",self.nome,"Telefone: ", self.fone,"Endereço: ", self.Endereco)

    def imprimir(self):
        print("nome: ",self.nome)
        print("Telefone: ", self._fone)
        print("Endereço:", self.__Endereco)
        