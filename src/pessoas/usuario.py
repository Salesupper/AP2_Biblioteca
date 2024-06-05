import sqlite3
from src.pessoas.pessoa import Pessoa

class Usuario(Pessoa):
    def __init__(self, id_usuario, nome, endereco, cpf, data_nascimento, genero, telefone):
        super().__init__(nome, endereco, cpf, data_nascimento, genero, telefone)
        self._id_usuario = id_usuario
        
    # Get
    @property
    def id_usuario(self):
        return self._id_usuario

    # Set
    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

    def __str__(self):
        return f'''Nome: {self.nome}, CPF: {self._cpf},Endereço: {self._endereco},
        Data de Nascimento: {self.data_nascimento}, 
        Gênero: {self.genero}, Telefone: {self._telefone}, 
        ID Carteirinha: {self._id_usuario}'''

nome_banco = "biblioteca.db"
def criar_tabela_usuarios():
    try:
        with sqlite3.connect(nome_banco) as conn:
            cursor = conn.cursor()

            comando_sql = '''
            CREATE TABLE IF NOT EXISTS usuarios (
            id_usuario TEXT PRIMARY KEY,
            nome TEXT NOT NULL,
            endereco TEXT,
            cpf VARCHAR(11) NOT NULL UNIQUE,
            data_nascimento DATE,
            genero VARCHAR(1),
            telefone VARCHAR(15) NOT NULL
            )
            '''
            cursor.execute(comando_sql)

        print("Tabela usuários criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela usuários: {e}")

def adicionar_usuario(nome_banco, usuario):
    try:
        with sqlite3.connect(nome_banco) as conn:
            cursor = conn.cursor()

            comando_sql = '''
            INSERT INTO usuarios (id_usuario, nome, endereco, cpf, data_nascimento, genero, telefone)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            '''
            valores = (usuario.id_usuario, usuario.nome, usuario.endereco, usuario.cpf, usuario.data_nascimento, usuario.genero, usuario.telefone)

            cursor.execute(comando_sql, valores)

        print("Usuário adicionado ao banco de dados com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao adicionar usuário ao banco de dados: {e}")

def deletar_usuario(nome_banco, id_usuario):
    try:
        with sqlite3.connect(nome_banco) as conn:
            cursor = conn.cursor()

            comando_sql = '''
            DELETE FROM usuarios WHERE id_usuario = ?
            '''
            cursor.execute(comando_sql, (id_usuario,))

            if cursor.rowcount > 0:
                print("Usuário deletado do banco de dados com sucesso.")
            else:
                print("Nenhum usuário encontrado com o ID fornecido.")
    except sqlite3.Error as e:
        print(f"Erro ao deletar usuário do banco de dados: {e}")

def consultar_usuario_por_id(nome_banco, id_usuario):
    try:
        with sqlite3.connect(nome_banco) as conn:
            cursor = conn.cursor()

            comando_sql = '''
            SELECT * FROM usuarios WHERE id_usuario = ?
            '''
            cursor.execute(comando_sql, (id_usuario,))
            usuario = cursor.fetchone()

            if usuario:
                return usuario
            else:
                print("Nenhum usuário encontrado com o ID fornecido.")
                return None
    except sqlite3.Error as e:
        print(f"Erro ao consultar usuário no banco de dados: {e}")
        return None
    
def consultar_todos_usuarios(nome_banco):
    try:
        conn = sqlite3.connect(nome_banco)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        conn.close()
        return usuarios
    except sqlite3.Error as e:
        print(f"Erro ao consultar todos os usuários: {e}")
        return None