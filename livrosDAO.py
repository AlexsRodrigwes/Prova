from optparse import Values
from Database import Database

class livrosDAO:

    def __init__(self):
        pass


    def cadastrar(self, livro): 
        bd  = Database().conectar()
        cursor = bd.cursor()
        script = "insert into livro (nome_livro,nome_autor, categoria) values ('"+livro.getNome_livro()+"', '"+livro.getAutor_livro()+"', '"+livro.getCategoria()+"')"
        cursor.execute(script)
        bd.commit()
        print("Livro cadastrado com sucesso!")

    def excluir(self, id):
        bd = Database().conectar()
        cursor = bd.cursor()
        script = ("delete from livro where id="+id)
        cursor.execute(script)
        bd.commit()
        print("Livro excluido!")

