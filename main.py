from alunoDAO import alunoDAO
from livros import Livro
from aluno import Aluno
from livrosDAO import livrosDAO
from Database import Database


#Inicinaod livroDAO
livroD = livrosDAO()
alunoD = alunoDAO()
#Criando livro para adiconar

livro = Livro(idlivro=None, nome_livro='Minha vida fora de série', autor_livro='Paula Pimenta', categoria= 'romance')
aluno = Aluno(idaluno=None, nome_aluno='Sabrina', telefone= '981212425')
livro = Livro(idlivro=None, nome_livro='A seleção', autor_livro='Kiera Cass', categoria= 'romance')
aluno = Aluno(idaluno=None, nome_aluno='Alexia', telefone= '984168173')
livro = Livro(idlivro=None, nome_livro='Anne de Green Gables', autor_livro='Lucy Maud Montgomery', categoria= 'fantasia')
aluno = Aluno(idaluno=None, nome_aluno='Vicktor Emannuel', telefone= '982565953')
livroD.cadastrar(livro)
alunoD.cadastrar(aluno)