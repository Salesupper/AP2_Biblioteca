import sqlite3
from src.pessoas.pessoa import Pessoa

class Funcionario (Pessoa):
    def __init__(self, id_funcionario, nome, endereco, cpf, data_nascimento, genero, telefone):
        super().__init__(nome, endereco, cpf, data_nascimento, genero, telefone)
        self._id_funcionario = id_funcionario
        
    # Get
    def get_id_funcionario(self):
        return self._id_carterina_funcionario
    
    # Set
    def set_id_funcionario(self, id_funcionario):
        self._id_funcionario = id_funcionario

    #Getters
    @property
    def endereco(self):
        return self._endereco
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def telefone(self):
        return self._telefone

    #setters
    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone
        
    def __str__(self):
        return f'''Nome: {self.nome}, CPF: {self._cpf},Endereço: {self._endereco},
        Data de Nascimento: {self.data_nascimento}, 
        Gênero: {self.genero}, Telefone: {self._telefone}, 
        ID Carteirinha: {self._id_funcionario}'''

nome_banco = "biblioteca.db"

def criar_tabela_funcionarios():
    try:
        with sqlite3.connect(nome_banco) as conn:
            cursor = conn.cursor()

            comando_sql = '''
            CREATE TABLE IF NOT EXISTS funcionarios (
            id_funcionario TEXT PRIMARY KEY,
            nome TEXT NOT NULL,
            endereco TEXT,
            cpf VARCHAR(11) NOT NULL UNIQUE,
            data_nascimento DATE,
            genero VARCHAR(1),
            telefone VARCHAR(15) NOT NULL
            )
            '''
            cursor.execute(comando_sql)
        # Deletando a tabela
        drop_table_query = 'DROP TABLE IF EXISTS funcionários'
        cursor.execute(drop_table_query)
        conn.commit()


        print("Tabela funcionários criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela funcionários: {e}")

def adicionar_funcionario(nome_banco, funcionario):
    try:
        with sqlite3.connect(nome_banco) as conn:
            cursor = conn.cursor()

            comando_sql = '''
            INSERT INTO funcionarios (id_funcionario, nome, endereco, cpf, data_nascimento, genero, telefone)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            '''
            valores = (funcionario._id_funcionario, funcionario.nome, funcionario.endereco, funcionario.cpf, funcionario.data_nascimento, funcionario.genero, funcionario.telefone)

            cursor.execute(comando_sql, valores)

        print("Funcionário adicionado ao banco de dados com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao adicionar funcionário ao banco de dados: {e}")

def deletar_funcionario(nome_banco, id_funcionario):
    try:
        with sqlite3.connect(nome_banco) as conn:
            cursor = conn.cursor()

            comando_sql = '''
            DELETE FROM funcionarios WHERE id_funcionario = ?
            '''
            cursor.execute(comando_sql, (id_funcionario,))

            if cursor.rowcount > 0:
                print("Funcionário deletado do banco de dados com sucesso.")
            else:
                print("Nenhum funcionário encontrado com o ID fornecido.")
    except sqlite3.Error as e:
        print(f"Erro ao deletar funcionário do banco de dados: {e}")

def consultar_funcionario_por_id(nome_banco, id_funcionario):
    try:
        with sqlite3.connect(nome_banco) as conn:
            cursor = conn.cursor()

            comando_sql = '''
            SELECT * FROM funcionarios WHERE id_funcionario = ?
            '''
            cursor.execute(comando_sql, (id_funcionario,))
            Funcionario = cursor.fetchone()

            if Funcionario:
                return Funcionario
            else:
                print("Nenhum funcionário encontrado com o ID fornecido.")
                return None
    except sqlite3.Error as e:
        print(f"Erro ao consultar funcionário no banco de dados: {e}")
        return None

def consultar_todos_funcionarios(nome_banco):
    try:
        conn = sqlite3.connect(nome_banco)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM funcionarios")
        funcionarios = cursor.fetchall()
        conn.close()
        return funcionarios
    except sqlite3.Error as e:
        print(f"Erro ao consultar todos os funcionários: {e}")
        return None