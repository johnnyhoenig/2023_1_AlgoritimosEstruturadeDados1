class Pessoa():
    def __init__(self, nome, idadePessoa):
        print("Objeto instanciado")
        self.nome = nome
        self.idade = idadePessoa
        self.fone = input("digite o Telefone:")

    def imprimir(self):
        print("Nome: " , self.nome)
        print("idade: ", self.idade)
        print("Telefone: ", self.fone)
