import uuid
import sqlite3
from Pessoas.funcionario import Funcionario
from Livros.livro_fisico import Livro_fisico



nome_banco = 'biblioteca.db'

# Conectar ao banco de dados ou criar um novo se não existir
conn = sqlite3.connect(nome_banco)
# Criar um cursor para executar comandos SQL
cursor = conn.cursor()
# Comando SQL para criar uma tabela de livros
comando_sql = '''
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY,
        id_carterinha TEXT NOT NULL,
        nome TEXT NOT NULL,
        endereco TEXT,
        cpf TEXT UNIQUE,
        data_nascimento DATE,
        genero TEXT,
        telefone TEXT
    )'''

# Executar o comando SQL para criar a tabela
cursor.execute(comando_sql)
# Commit para salvar as alterações no banco de dados
conn.commit()
# Comando SQL para inserir um livro na tabela
comando_sql_insercao = ''' 
    INSERT INTO funcionarios (nome, endereco, cpf, data_nascimento, genero, telefone, id_carterinha)
    VALUES (?, ?, ?, ?, ?, ?, ?)
'''

class Biblioteca:
    def __init__(self):
        self.estoque = []
        self.usuarios = []
        self.funcionarios = []
        self.livros_fisicos = []
        self.livros_digitais = []

    def criar_funcionario(self, nome, endereco, cpf, data_nascimento, genero, telefone):
        id_carterinha_funcionario = self.gerar_id_funcionario()
        novo_funcionario = Funcionario(nome, endereco, cpf, data_nascimento, genero, telefone, id_carterinha_funcionario)
        self.funcionarios.append(novo_funcionario)
        print(f"Funcionário {nome} criado com sucesso.")
        return (nome, endereco, cpf, data_nascimento, genero, telefone, id_carterinha_funcionario)

    def gerar_id_funcionario(self):
        return str(uuid.uuid4())

    def imprimir_funcionarios(self):
        for funcionario in self.funcionarios:
            print(funcionario)

biblioteca = Biblioteca()

# # Adicionar um novo funcionário
novo_funcionario = biblioteca.criar_funcionario("Maria", "Rua ABC", "123.456.789-01", "01/01/1980", "Feminino", "9999-8888")
biblioteca.imprimir_funcionarios()

# Executar o comando SQL de inserção para cada livro
cursor.execute(comando_sql_insercao, novo_funcionario)

# Commit para salvar as alterações no banco de dados
conn.commit()
conn.close()