from Pessoa import Pessoa
#from Fisica import Fisica
#from Cidade import Cidade
class Juridica(Pessoa):
    def __init__(self, name=None, fone=None, cidade=None, cnpj=None):
        super().__init__(name, fone, cidade)
        self.cnpj = cnpj
        self.funcionario = []
    

    def addfuncionario( self, pFisica ):
        self.funcionario.append (pFisica)

    def imprimir(self):
        print("Empresa", self.nome)
        print("Fone", self.fone)
        print("Cidade", self.city.nome)
        print("Funcionarios: /n-------------------")
        if len(self.funcionario) == 0:
            print("Nao possui funcionarios.")
        else:
            for pFisica in self.funcionario:
                print("Nome Func.:", pFisica.nome)
                print("Telefone:", pFisica.fone)
                print("Cidade:", pFisica.city.nome)
                print("||||||||||||||||||||||||||||||")
