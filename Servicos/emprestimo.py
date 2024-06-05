import sqlite3
from Pessoas import usuario, funcionario
from Livros import livro_fisico
from datetime import datetime

class Emprestimo(usuario, funcionario, livro_fisico):
    def __init__(self,id_livro,id_usuario,id_funcionario,nome,edicao,isbn,prazo,entregue):
        super().__init__(id_livro,nome,edicao,isbn,id_usuario,id_funcionario)
        super().__init__(id_usuario)
        super().__init__(id_funcionario)
        self.prazo = prazo
        self.entregue = entregue

nome_banco = "biblioteca.db"

def criar_tabela_emprestimos():
    try:
        with sqlite3.connect(nome_banco) as conn:
            cursor = conn.cursor()
            comando_sql = ('''CREATE TABLE IF NOT EXISTS emprestimos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_usuario INTEGER NOT NULL,
                    id_livro INTEGER NOT NULL,
                    data_emprestimo DATE NOT NULL,
                    data_devolucao DATE NOT NULL,
                    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
                    FOREIGN KEY (id_livro) REFERENCES livros(id)
                )''')
        cursor.execute(comando_sql)

        print("Tabela empréstimo criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela empréstimo: {e}")

criar_tabela_emprestimos()