import sqlite3

# Esta classe terá apenas os dados de um livro
class Livro:
    def __init__(self, id, titulo, autor, genero, ano):
        self.id = id  # ID do livro
        self.titulo = titulo  # Título do livro
        self.autor = autor  # Autor do livro
        self.genero = genero  # Gênero do livro
        self.ano = ano  # Ano de publicação do livro

# Esta classe poderá interagir com a biblioteca. Terá ações como adicionar um livro, visualizar os livros da biblioteca, atualizar um livro ou retirar um livro do acervo da biblioteca
class Biblioteca:
    def __init__(self, db_file):
        self.conexao = sqlite3.connect(db_file)  # Conexão com o banco de dados SQLite
        self.cursor = self.conexao.cursor()  # Cursor para executar comandos SQL no banco de dados
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS livros (
                id INTEGER,
                titulo TEXT,
                autor TEXT,
                genero TEXT,
                ano INTEGER
            )
        ''')  # Cria a tabela 'livros' se ela não existir

    def livro_esta_na_biblioteca(self, id):
        livro = self.cursor.execute("SELECT * FROM livros WHERE id = ?", [id]).fetchone()
        return livro is not None  # Verifica se um livro com o ID fornecido está na biblioteca

    def adicionar_livro(self, livro):
        self.cursor.execute("INSERT INTO livros (id, titulo, autor, genero, ano) VALUES (?,?,?,?,?)",
                            (livro.id, livro.titulo, livro.autor, livro.genero, livro.ano))
        self.conexao.commit()  # Adiciona um livro à biblioteca

    def visualizar_livros(self):
        livros = self.cursor.execute("SELECT * FROM livros")
        return livros  # Retorna os livros presentes na biblioteca

    def atualizar_livro(self, livro):
        self.cursor.execute("UPDATE livros SET titulo = ?, autor = ?, genero = ?, ano = ? WHERE id = ?",
                            (livro.titulo, livro.autor, livro.genero, livro.ano, livro.id))
        self.conexao.commit()  # Atualiza as informações de um livro na biblioteca

    def deletar_livro(self, id):
        self.cursor.execute("DELETE FROM livros WHERE id = ?", [id])
        self.conexao.commit()  # Remove um livro da biblioteca

    def fechar_conexao(self):
        self.conexao.close()  # Fecha a conexão com o banco de dados
