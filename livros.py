class Livro:

    def __init__(self, idlivro, nome_livro, autor_livro, categoria):
        self.idlivro = idlivro
        self.nome_livro = nome_livro
        self.autor_livro = autor_livro
        self.categoria = categoria

    def getCategoria(self):
        return self.categoria

    def getNome_livro(self):
        return self.nome_livro

    def getAutor_livro(self):
        return self.autor_livro

    def getIdlivro(self):
        return self.idlivro

