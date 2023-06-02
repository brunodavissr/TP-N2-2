import sqlite3

conexao = sqlite3.connect('biblioteca.db')

cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER,
        titulo TEXT,
        autor TEXT,
        genero TEXT,
        ano INTEGER
    )     
''')

def adicionar_livro(id, titulo, autor, genero, ano):
    cursor.execute("INSERT INTO livros (id, titulo, autor, genero, ano) VALUES (?,?,?,?,?)", (id, titulo, autor, genero, ano))
    conexao.commit()
    
def visualizar_livros():
    livros = cursor.execute("SELECT * FROM livros")
    for livro in livros:
        print(livro)
        
def atualizar_livro(id, titulo, autor, genero, ano):
    cursor.execute(f"UPDATE livros SET titulo = {titulo}, autor = {autor}, genero = {genero}, ano = {ano} WHERE id = {id}")
    conexao.commit()
        
def deletar_livro(id):
    cursor.execute(f"DELETE FROM livros WHERE id = {id}")
    conexao.commit()
    
print("Vou inserir O Codigo da Vinci")
adicionar_livro(1234, "O Codigo Da Vinci", "Dan Brown", "Suspense", 2003)

print("Livros que tem atualmente:")
visualizar_livros()

print("Vou inserir O Guia do Mochileiro das Galaxias")
adicionar_livro(5678, "O Guia do Mochileiro das Galaxias", "Douglas Adams", "Ficcao Cientifica", 1979)

print("Livros que tem atualmente:")
visualizar_livros()

print("Vou atualizar O Codigo da Vinci para 2023")
atualizar_livro(1234, "O Codigo Da Vinci", "Dan Brown", "Suspense", 2023)

print("Como ta agora:")
visualizar_livros()

conexao.close()