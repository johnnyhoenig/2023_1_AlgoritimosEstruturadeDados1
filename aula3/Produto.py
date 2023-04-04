class Produto:
    def __init__(self,nome, preco, cat ):
        self.id = None
        self.nome = nome
        self.preco = preco
        self.categoria = cat
        
    
    def imprimir(self):
        print("nome: ",self.nome)
        print("preço: ", self.preco)
        print("categoria: ", self.categoria.nome)