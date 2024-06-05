import sqlite3
from datetime import datetime
from src.livros.livro import Livro
from src.pessoas.funcionario import Funcionario
from src.pessoas.usuario import Usuario
from src.livros.livro_digital import alterar_status_livro

class Emprestimo(Livro, Usuario, Funcionario):
    def __init__(self, id_livro, id_usuario, id_funcionario, nome, edicao, isbn, prazo, entregue):
        Livro.__init__(self, id_livro, nome, edicao, isbn)
        Usuario.__init__(self, id_usuario)
        Funcionario.__init__(self, id_funcionario)
        self.prazo = prazo
        self.entregue = entregue

    def get_id_livro(self):
        return self.id_livro
    
    def get_id_usuario(self):
        return self.id_usuario
    
    def get_id_funcionario(self):
        return self.id_funcionario
    
    def get_nome(self):
        return self.nome
    
    def get_edicao(self):
        return self.edicao
    
    def get_isbn(self):
        return self.isbn
    
    def get_prazo(self):
        return self.prazo
    
    def get_entregue(self):
        return self.entregue


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

def registrar_emprestimo(nome_banco, id_usuario, id_livro, data_emprestimo, data_devolucao):
    try:
        with sqlite3.connect(nome_banco) as conn:
            cursor = conn.cursor()
            comando_sql = '''
            INSERT INTO emprestimos (id_usuario, id_livro, data_emprestimo, data_devolucao)
            VALUES (?, ?, ?, ?)
            '''
            valores = (id_usuario, id_livro, data_emprestimo, data_devolucao)
            cursor.execute(comando_sql, valores)
            
            # Alterar o status do livro para indisponível (0)
            alterar_status_livro(nome_banco, id_livro, 0)
            
            print("Empréstimo registrado com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao registrar empréstimo: {e}")

def consultar_todos_emprestimos(nome_banco):
    try:
        conn = sqlite3.connect(nome_banco)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM emprestimos")
        emprestimos = cursor.fetchall()
        conn.close()
        return emprestimos
    except sqlite3.Error as e:
        print(f"Erro ao consultar todos os empréstimos: {e}")
        return None

def consultar_emprestimo_por_id(nome_banco, id_emprestimo):
    conn = sqlite3.connect(nome_banco)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM emprestimos WHERE id = ?", (id_emprestimo,))
    emprestimo = cursor.fetchone()
    conn.close()
    return emprestimo