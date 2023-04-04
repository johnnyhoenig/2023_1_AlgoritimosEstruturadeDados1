from Aluno import Aluno
class AlunoEnsinoMedio(Aluno):
    def __init__(self, cod, nome, matricula,ano):
        super().__init__(cod, nome, matricula)
        self.ano=None

    def imprimir(self):
        super.imprimir(Aluno)
        print("ano Ensino Medio: ", self.ano)
