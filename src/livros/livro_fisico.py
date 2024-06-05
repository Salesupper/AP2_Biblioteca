import sqlite3
from src.livros.livro import Livro

class Livro_fisico(Livro):
    def __init__(self, id_livro, nome, isbn, editora, autor, qtd_paginas, nmr_edicao, genero, faixa_etaria, tipo_capa, disponivel=True):
        super().__init__(id_livro,nome, isbn, editora, autor, qtd_paginas, nmr_edicao, genero, faixa_etaria)
        self.id_livro = id_livro
        self.tipo_capa = tipo_capa
        self.disponivel = disponivel
    
    def __str__(self):
        return f"ID: {self.id_livro}, Nome: {self.nome}, ISBN: {self.isbn}, Editora: {self.editora}, Autor: {self.autor}, Páginas: {self.qtd_paginas}, Edição: {self.nmr_edicao}, Gênero: {self.genero}, Faixa Etária: {self.faixa_etaria}, Tipo de Capa: {self.tipo_capa}"

nome_banco = "biblioteca.db"

def criar_tabela_livros_fisicos():
    try:
        with sqlite3.connect(nome_banco) as conn:
            cursor = conn.cursor()

            comando_sql = '''
            CREATE TABLE IF NOT EXISTS livros_fisicos (
                id_livro TEXT PRIMARY KEY,
                nome TEXT,
                isbn TEXT,
                editora TEXT,
                autor TEXT,
                qtd_paginas INTEGER,
                nmr_edicao INTEGER,
                genero TEXT,
                faixa_etaria INTEGER,
                tipo_capa TEXT,
                disponivel INTEGER DEFAULT 1
            )
            '''
            cursor.execute(comando_sql)

        print("Tabela livros_fisicos criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela livros_fisicos: {e}")

def adicionar_livro_banco(nome_banco, livro):
    try:
        with sqlite3.connect(nome_banco) as conn:
            cursor = conn.cursor()

            comando_sql = '''
            INSERT INTO livros_fisicos (id_livro, nome, isbn, editora, autor, qtd_paginas, nmr_edicao, genero, faixa_etaria, tipo_capa, disponivel)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            '''
            valores = (livro.id_livro, livro.nome, livro.isbn, livro.editora, livro.autor, livro.qtd_paginas, livro.nmr_edicao, livro.genero, livro.faixa_etaria, livro.tipo_capa, livro.disponivel)

            cursor.execute(comando_sql, valores)

        print("Livro adicionado ao banco de dados com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao adicionar livro ao banco de dados: {e}")

def deletar_livro_fisico(nome_banco, id_livro):
    try:
        with sqlite3.connect(nome_banco) as conn:
            cursor = conn.cursor()

            comando_sql = '''
            DELETE FROM livros_fisicos WHERE id_livro = ?
            '''
            cursor.execute(comando_sql, (id_livro,))

            if cursor.rowcount > 0:
                print("Livro deletado do banco de dados com sucesso.")
            else:
                print("Nenhum livro encontrado com o ID fornecido.")
    except sqlite3.Error as e:
        print(f"Erro ao deletar livro do banco de dados: {e}")

def alterar_status_livro(nome_banco, id_livro, disponivel):
    try:
        with sqlite3.connect(nome_banco) as conn:
            cursor = conn.cursor()

            comando_sql = '''
            UPDATE livros_fisicos SET disponivel = ? WHERE id_livro = ?
            '''
            cursor.execute(comando_sql, (disponivel, id_livro))

            if cursor.rowcount > 0:
                print("Status do livro alterado com sucesso.")
            else:
                print("Nenhum livro encontrado com o ID fornecido.")
    except sqlite3.Error as e:
        print(f"Erro ao alterar o status do livro no banco de dados: {e}")

def consultar_livro_por_id(nome_banco, id_livro):
    try:
        with sqlite3.connect(nome_banco) as conn:
            cursor = conn.cursor()

            comando_sql = '''
            SELECT * FROM livros_fisicos WHERE id_livro = ?
            '''
            cursor.execute(comando_sql, (id_livro,))
            livro = cursor.fetchone()

            if livro:
                return Livro_fisico(*livro)
            else:
                print("Nenhum livro encontrado com o ID fornecido.")
                return None
    except sqlite3.Error as e:
        print(f"Erro ao consultar livro no banco de dados: {e}")
        return None
    
def consultar_todos_livros_fisicos(nome_banco):
    try:
        conn = sqlite3.connect(nome_banco)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM livros_fisicos")
        livros = cursor.fetchall()
        conn.close()
        return livros
    except sqlite3.Error as e:
        print(f"Erro ao consultar todos os livros físicos: {e}")
        return None

def devolver_livro_fisico(nome_banco, id_livro):
    try:
        with sqlite3.connect(nome_banco) as conn:
            cursor = conn.cursor()

            # Verifica se o livro está disponível para devolução
            livro = consultar_livro_por_id(nome_banco, id_livro)
            if not livro:
                print("Livro não encontrado.")
                return
            if livro.disponivel:
                print("O livro já está disponível.")
                return

            # Atualiza o status do livro para disponível (1)
            alterar_status_livro(nome_banco, id_livro, True)
            print("Livro devolvido com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao devolver o livro: {e}")