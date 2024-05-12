from Pessoas.funcionario import Funcionario

import uuid


class Biblioteca:
    def __init__(self):
        self.estoque = []
        self.usuarios = []
        self.funcionarios = []
        self.livros_fisicos = []
        self.livros_digitais = []

    def criar_funcionario(self, nome, endereco, cpf, data_nascimento, genero, telefone):
        id_carterina_funcionario = self.gerar_id_funcionario()
        novo_funcionario = Funcionario(nome, endereco, cpf, data_nascimento, genero, telefone, id_carterina_funcionario)
        self.funcionarios.append(novo_funcionario)
        print(f"Funcionário {nome} criado com sucesso.")

    def gerar_id_funcionario(self):
        return str(uuid.uuid4())

    def imprimir_funcionarios(self):
        for funcionario in self.funcionarios:
            print(funcionario)


biblioteca = Biblioteca()

# Adicionar um novo funcionário
biblioteca.criar_funcionario("Maria", "Rua ABC", "123.456.789-00", "01/01/1980", "Feminino", "9999-8888")
biblioteca.imprimir_funcionarios()
