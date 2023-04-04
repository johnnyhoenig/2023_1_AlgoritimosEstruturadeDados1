class Aluno:
    def __init__(self, cod, nome, matricula):
        self.cod = None
        self.nome = None
        self.matricula = None
    
    
    def imprimir(self):
        print("Nome do Aluno: ",self.nome) 
        print("Codigo: ",self.cod) 
        print("Matricula: ",self.matricula) 