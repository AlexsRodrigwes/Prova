class Aluno:

    def __init__(self, idaluno, nome_aluno, telefone):
        self.idaluno = idaluno
        self.nome_aluno = nome_aluno
        self.telefone = telefone

    def getNome_aluno(self):
        return self.nome_aluno

    def getTelefone(self):
        return self.telefone

    def getIdaluno(self):
        return self.idaluno