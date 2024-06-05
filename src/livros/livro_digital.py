import sqlite3
from livros.livro import Livro

class Livro_digital(Livro):
    def __init__(self, id_livro, nome, isbn, editora, autor, qtd_paginas, nmr_edicao, genero, faixa_etaria, tamanho_mb, disponivel=True):
        super().__init__(id_livro,nome,isbn,editora,autor,qtd_paginas,nmr_edicao,genero,faixa_etaria)
        self.id_livro = id_livro
        self.tamanho_mb = tamanho_mb
        self.disponivel = disponivel

    def __str__(self):
        return f"ID: {self.id_livro}, Nome: {self.nome}, ISBN: {self.isbn}, Editora: {self.editora}, Autor: {self.autor}, Páginas: {self.qtd_paginas}, Edição: {self.nmr_edicao}, Gênero: {self.genero}, Faixa Etária: {self.faixa_etaria}, tamanho em MB: {self.tamanho_mb}"

nome_banco = "biblioteca.db"

def criar_tabela_livros_digitais():
    try:
        with sqlite3.connect(nome_banco) as conn:
            cursor = conn.cursor()

            comando_sql = '''
            CREATE TABLE IF NOT EXISTS livros_digitais (
                id_livro TEXT PRIMARY KEY,
                nome TEXT,
                isbn TEXT,
                editora TEXT,
                autor TEXT,
                qtd_paginas INTEGER,
                nmr_edicao INTEGER,
                genero TEXT,
                faixa_etaria INTEGER,
                tamanho_mb REAL,
                disponivel INTEGER DEFAULT 1
            )
            '''
            cursor.execute(comando_sql)

        print("Tabela livros_digitais criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela livros_digital: {e}")

def adicionar_livro_banco(nome_banco, livro):
    try:
        with sqlite3.connect(nome_banco) as conn:
            cursor = conn.cursor()

            comando_sql = '''
            INSERT INTO livros_digitais (id_livro, nome, isbn, editora, autor, qtd_paginas, nmr_edicao, genero, faixa_etaria, tamanho_mb, disponivel)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            '''
            valores = (livro.id_livro, livro.nome, livro.isbn, livro.editora, livro.autor, livro.qtd_paginas, livro.nmr_edicao, livro.genero, livro.faixa_etaria, livro.tamanho_mb, livro.disponivel)

            cursor.execute(comando_sql, valores)

        print("Livro adicionado ao banco de dados com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao adicionar livro ao banco de dados: {e}")

def deletar_livro_digital(nome_banco, id_livro):
    try:
        with sqlite3.connect(nome_banco) as conn:
            cursor = conn.cursor()

            comando_sql = '''
            DELETE FROM livros_digitais WHERE id_livro = ?
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
            UPDATE livros_digitais SET disponivel = ? WHERE id_livro = ?
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
            SELECT * FROM livros_digitais WHERE id_livro = ?
            '''
            cursor.execute(comando_sql, (id_livro,))
            livro = cursor.fetchone()

            if livro:
                return Livro_digital(*livro)
            else:
                print("Nenhum livro encontrado com o ID fornecido.")
                return None
    except sqlite3.Error as e:
        print(f"Erro ao consultar livro no banco de dados: {e}")
        return None

criar_tabela_livros_digitais()

novo_livro = Livro_digital(
    id_livro = 0,
    nome="1984",
    isbn="77722-2",
    editora="São Carlos",
    autor="George",
    qtd_paginas=271,
    nmr_edicao=3,
    genero="ficção",
    faixa_etaria=18,
    tamanho_mb = 800,
    disponivel = True
)

#adicionar_livro_banco(nome_banco, novo_livro)
#deletar_livro_digital(nome_banco, "0")
#alterar_status_livro(nome_banco, "0", False)
livro_consultado = consultar_livro_por_id(nome_banco, 0)
if livro_consultado:
    print(livro_consultado)