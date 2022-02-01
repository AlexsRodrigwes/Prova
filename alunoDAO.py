from optparse import Values
from Database import Database

class alunoDAO:

    def __init__(self):
        pass


    def cadastrar(self, aluno): 
        bd  = Database().conectar()
        cursor = bd.cursor()
        script = "insert into aluno (nome_aluno,telefone) values ('"+aluno.getNome_aluno()+"', '"+aluno.getTelefone()+"')"
        cursor.execute(script)
        bd.commit()
        print("Aluno cadastrado com sucesso!")

    def excluir(self, id):
        bd = Database().conectar()
        cursor = bd.cursor()
        script = ("delete from aluno where id="+id)
        cursor.execute()
        bd.commit()
        print("Aluno excluido!")