import sqlite3

#Esta classe terá apenas os dados de um livro
class Livro:
    def __init__(self, id, titulo, autor, genero, ano):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ano = ano

#Esta classe poderá interagir com a biblioteca. Terá ações como adicionar um livro, visualizar os livros da bibioteca, atualizar um livro ou retirar um livro do acervo da biblioteca
class Biblioteca:
    def __init__(self, db_file):
        self.conexao = sqlite3.connect(db_file)
        self.cursor = self.conexao.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS livros (
                id INTEGER,
                titulo TEXT,
                autor TEXT,
                genero TEXT,
                ano INTEGER
            )
        ''')

    def adicionar_livro(self, livro):
        self.cursor.execute("INSERT INTO livros (id, titulo, autor, genero, ano) VALUES (?,?,?,?,?)",
                            (livro.id, livro.titulo, livro.autor, livro.genero, livro.ano))
        self.conexao.commit()

    def visualizar_livros(self):
        livros = self.cursor.execute("SELECT * FROM livros")
        return livros

    def atualizar_livro(self, livro):
        self.cursor.execute("UPDATE livros SET titulo = ?, autor = ?, genero = ?, ano = ? WHERE id = ?",
                            (livro.titulo, livro.autor, livro.genero, livro.ano, livro.id))
        self.conexao.commit()

    def deletar_livro(self, id):
        self.cursor.execute("DELETE FROM livros WHERE id = ?", [id])
        self.conexao.commit()

    def fechar_conexao(self):
        self.conexao.close()
