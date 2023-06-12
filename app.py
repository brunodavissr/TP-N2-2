import streamlit as st
import pandas as pd
from biblioteca import Livro, Biblioteca

# Nesta função, estaremos exibindo na tela do usuário os campos para que ele possa adicionar um livro à biblioteca
def adicionar_livro(biblioteca):
    st.subheader("Adicionar Livro")
    id = st.number_input("ID", step=1, min_value=0)
    titulo = st.text_input("Título")
    autor = st.text_input("Autor")
    genero = st.text_input("Gênero")
    ano = st.number_input("Ano", step=1, min_value=0)

    if st.button("Salvar"):
        if not titulo or not autor or not genero:
            st.error("Preencha todos os campos")
        elif biblioteca.livro_esta_na_biblioteca(id):
            st.error("Já há um livro com este ID na biblioteca. Escolha outro ID")
        else:
            livro = Livro(id, titulo, autor, genero, ano)
            biblioteca.adicionar_livro(livro)
            st.success("Livro adicionado com sucesso.")

def visualizar_livros(biblioteca):
    st.subheader("Livros")
    livros = biblioteca.visualizar_livros()
    livros_df = pd.DataFrame(livros, columns=["ID", "Título", "Autor", "Gênero", "Ano"])
    livros_df["ID"] = livros_df["ID"].astype(int)  # Converter a coluna ID para inteiros
    livros_df["Ano"] = livros_df["Ano"].astype(int)  # Converter a coluna Ano para inteiros
    st.dataframe(livros_df)

def atualizar_livro(biblioteca):
    st.subheader("Atualizar Livro")
    id = st.number_input("ID do livro a ser atualizado", format='%.0f')
    titulo = st.text_input("Novo Título")
    autor = st.text_input("Novo Autor")
    genero = st.text_input("Novo Gênero")
    ano = st.number_input("Novo Ano", format='%.0f')

    if st.button("Atualizar"):
        if not titulo or not autor or not genero:
            st.error("Preencha todos os campos")
        elif not biblioteca.livro_esta_na_biblioteca(id):
            st.error("Livro não está no acervo")
        else:
            livro = Livro(id, titulo, autor, genero, ano)
            biblioteca.atualizar_livro(livro)
            st.success("Livro atualizado com sucesso.")

def deletar_livro(biblioteca):
    st.subheader("Deletar Livro")
    id = st.number_input("ID do livro a ser deletado", format='%.0f')

    if st.button("Deletar"):
        if not biblioteca.livro_esta_na_biblioteca(id):
            st.error("Livro não está no acervo")
        else:
            biblioteca.deletar_livro(id)
            st.success("Livro deletado com sucesso.")

def main():
    st.title("Sistema de Gerenciamento de Biblioteca")
    biblioteca = Biblioteca('biblioteca.db')

    menu = ["Adicionar Livro", "Visualizar Livros", "Atualizar Livro", "Deletar Livro"]
    escolha = st.sidebar.selectbox("Menu", menu)

    if escolha == "Adicionar Livro":
        adicionar_livro(biblioteca)
    elif escolha == "Visualizar Livros":
        visualizar_livros(biblioteca)
    elif escolha == "Atualizar Livro":
        atualizar_livro(biblioteca)
    elif escolha == "Deletar Livro":
        deletar_livro(biblioteca)

if __name__ == "__main__":
    main()
