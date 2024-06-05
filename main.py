import sys
from Livros.livro_digital import Livro_digital, criar_tabela_livros_digitais, adicionar_livro_banco, deletar_livro_digital, alterar_status_livro, consultar_livro_por_id
from Livros.livro_fisico import Livro_fisico, criar_tabela_livros_fisicos, adicionar_livro_banco as adicionar_livro_fisico, deletar_livro_fisico, consultar_livro_por_id as consultar_livro_fisico_por_id
from Pessoas.funcionario import Funcionario, criar_tabela_funcionarios, adicionar_funcionario, deletar_funcionario, consultar_funcionario_por_id

nome_banco = "biblioteca.db"

def menu():
    while True:
        print("\nMenu Principal")
        print("1. Biblioteca")
        print("2. Funcionários")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            menu_biblioteca()
        elif escolha == "2":
            menu_funcionarios()
        elif escolha == "3":
            sys.exit()
        else:
            print("Opção inválida. Tente novamente.")

def menu_biblioteca():
    while True:
        print("\nMenu Biblioteca")
        print("1. Cadastrar Livro")
        print("2. Listar Livros")
        print("3. Emprestar Livro")
        print("4. Devolver Livro")
        print("5. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_livro()
        elif escolha == "2":
            listar_livros()
        elif escolha == "3":
            emprestar_livro()
        elif escolha == "4":
            devolver_livro()
        elif escolha == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_funcionarios():
    while True:
        print("\nMenu Funcionários")
        print("1. Cadastrar Funcionário")
        print("2. Excluir Funcionário")
        print("3. Listar Funcionários")
        print("4. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_funcionario()
        elif escolha == "2":
            excluir_funcionario()
        elif escolha == "3":
            listar_funcionarios()
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

def cadastrar_livro():
    tipo = input("Tipo de livro (1 para físico, 2 para digital): ")
    id_livro = input("ID do Livro: ")
    nome = input("Nome: ")
    isbn = input("ISBN: ")
    editora = input("Editora: ")
    autor = input("Autor: ")
    qtd_paginas = int(input("Quantidade de páginas: "))
    nmr_edicao = int(input("Número da edição: "))
    genero = input("Gênero: ")
    faixa_etaria = int(input("Faixa etária: "))

    if tipo == "1":
        tipo_capa = input("Tipo de capa: ")
        livro = Livro_fisico(id_livro, nome, isbn, editora, autor, qtd_paginas, nmr_edicao, genero, faixa_etaria, tipo_capa)
        adicionar_livro_fisico(nome_banco, livro)
    elif tipo == "2":
        tamanho_mb = float(input("Tamanho em MB: "))
        livro = Livro_digital(id_livro, nome, isbn, editora, autor, qtd_paginas, nmr_edicao, genero, faixa_etaria, tamanho_mb)
        adicionar_livro_banco(nome_banco, livro)
    else:
        print("Tipo de livro inválido.")

def listar_livros():
    tipo = input("Tipo de livro (1 para físico, 2 para digital): ")
    id_livro = input("ID do Livro: ")

    if tipo == "1":
        livro = consultar_livro_fisico_por_id(nome_banco, id_livro)
    elif tipo == "2":
        livro = consultar_livro_por_id(nome_banco, id_livro)
    else:
        print("Tipo de livro inválido.")
        return

    if livro:
        print(livro)
    else:
        print("Livro não encontrado.")

def emprestar_livro():
    id_livro = input("ID do Livro: ")
    tipo = input("Tipo de livro (1 para físico, 2 para digital): ")
    if tipo == "1":
        alterar_status_livro(nome_banco, id_livro, False)
    elif tipo == "2":
        alterar_status_livro(nome_banco, id_livro, False)
    else:
        print("Tipo de livro inválido.")

def devolver_livro():
    id_livro = input("ID do Livro: ")
    tipo = input("Tipo de livro (1 para físico, 2 para digital): ")
    if tipo == "1":
        alterar_status_livro(nome_banco, id_livro, True)
    elif tipo == "2":
        alterar_status_livro(nome_banco, id_livro, True)
    else:
        print("Tipo de livro inválido.")

def cadastrar_funcionario():
    id_funcionario = input("ID do Funcionário: ")
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    cpf = input("CPF: ")
    data_nascimento = input("Data de Nascimento: ")
    genero = input("Gênero: ")
    telefone = input("Telefone: ")

    funcionario = Funcionario(id_funcionario, nome, endereco, cpf, data_nascimento, genero, telefone)
    adicionar_funcionario(nome_banco, funcionario)

def excluir_funcionario():
    id_funcionario = input("ID do Funcionário: ")
    deletar_funcionario(nome_banco, id_funcionario)

def listar_funcionarios():
    id_funcionario = input("ID do Funcionário: ")
    funcionario = consultar_funcionario_por_id(nome_banco, id_funcionario)
    if funcionario:
        print(funcionario)
    else:
        print("Funcionário não encontrado.")

if __name__ == "__main__":
    criar_tabela_livros_digitais()
    criar_tabela_livros_fisicos()
    criar_tabela_funcionarios()
    menu()
