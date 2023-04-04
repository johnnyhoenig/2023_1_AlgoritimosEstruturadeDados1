from Pessoa import Pessoa
#from Juridica import Juridica
#from Cidade import Cidade


class Fisica( Pessoa ):
    def __init__(self, name=None, fone=None, cidade=None, cpf= None, empresa = None):
        super().__init__(name, fone, cidade)
        self.cpf = cpf
        self.empresa = empresa