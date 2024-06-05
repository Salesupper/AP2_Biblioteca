import sys
from datetime import datetime, timedelta
from src.livros.livro_digital import Livro_digital, criar_tabela_livros_digitais, adicionar_livro_banco, deletar_livro_digital, alterar_status_livro, consultar_livro_por_id, consultar_todos_livros_digitais, devolver_livro_digital
from src.livros.livro_fisico import Livro_fisico, criar_tabela_livros_fisicos, adicionar_livro_banco as adicionar_livro_fisico, deletar_livro_fisico, consultar_livro_por_id as consultar_livro_fisico_por_id, consultar_todos_livros_fisicos, devolver_livro_fisico
from src.pessoas.funcionario import Funcionario, criar_tabela_funcionarios, adicionar_funcionario, deletar_funcionario, consultar_funcionario_por_id, consultar_todos_funcionarios
from src.pessoas.usuario import Usuario, criar_tabela_usuarios, adicionar_usuario, deletar_usuario, consultar_usuario_por_id, consultar_todos_usuarios
from src.servicos.emprestimo import registrar_emprestimo, consultar_todos_emprestimos, consultar_emprestimo_por_id, criar_tabela_emprestimos

nome_banco = "biblioteca.db"

def menu():
    while True:
        print("\nMenu Principal")
        print("1. Biblioteca")
        print("2. Funcionários")
        print("3. Usuários")
        print("4. Empréstimos")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            menu_biblioteca()
        elif escolha == "2":
            menu_funcionarios()
        elif escolha == "3":
            menu_usuarios()
        elif escolha == "4":
            menu_emprestimos()
        elif escolha == "5":
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
        print("5. Deletar Livro Digital")
        print("6. Deletar Livro Fisico")
        print("7. Voltar ao Menu Principal")
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
            deletar_livro_digital_menu()
        elif escolha == "6":
            deletar_livro_fisico_menu()
        elif escolha == "7":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_funcionarios():
    while True:
        print("\nMenu Funcionários")
        print("1. Cadastrar Funcionário")
        print("2. Excluir Funcionário")
        print("3. Listar Funcionários")
        print("4. Listar Todos os Funcionários")
        print("5. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_funcionario()
        elif escolha == "2":
            excluir_funcionario()
        elif escolha == "3":
            listar_funcionarios()
        elif escolha == "4":
            listar_todos_funcionarios()
        elif escolha == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_usuarios():
    while True:
        print("\nMenu Usuários")
        print("1. Cadastrar Usuário")
        print("2. Excluir Usuário")
        print("3. Listar Usuários")
        print("4. Listar Todos os Usuários")
        print("5. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_usuario()
        elif escolha == "2":
            excluir_usuario()
        elif escolha == "3":
            listar_usuarios()
        elif escolha == "4":
            listar_todos_usuarios()
        elif escolha == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_emprestimos():
    while True:
        print("\nMenu Empréstimos")
        print("1. Consultar Empréstimos Especifico")
        print("2. Listar Todos os Empréstimos")
        print("3. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            listar_emprestimos()
        elif escolha == "2":
            listar_todos_emprestimos()
        elif escolha == "3":
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

def deletar_livro_digital_menu():
    id_livro = input("ID do Livro Digital que deseja deletar: ")
    deletar_livro_digital(nome_banco, id_livro)

def deletar_livro_fisico_menu():
    id_livro = input("ID do Livro Fisico que deseja deletar: ")
    deletar_livro_fisico(nome_banco, id_livro)

def listar_livros():
    escolha = input("Deseja listar todos os livros? (s/n): ")
    if escolha.lower() == 's':
        tipo = input("Tipo de livro (1 para físico, 2 para digital): ")
        if tipo == '1':
            livros = consultar_todos_livros_fisicos(nome_banco)
            if livros:
                for livro in livros:
                    print(livro)
            else:
                print("Nenhum livro físico encontrado.")
        elif tipo == '2':
            livros = consultar_todos_livros_digitais(nome_banco)
            if livros:
                for livro in livros:
                    print(livro)
            else:
                print("Nenhum livro digital encontrado.")
        else:
            print("Tipo de livro inválido.")
    else:
        tipo = input("Tipo de livro (1 para físico, 2 para digital): ")
        id_livro = input("ID do Livro: ")
        if tipo == '1':
            livro = consultar_livro_fisico_por_id(nome_banco, id_livro)
            if livro:
                print(livro)
            else:
                print("Livro físico não encontrado.")
        elif tipo == '2':
            livro = consultar_livro_por_id(nome_banco, id_livro)
            if livro:
                print(livro)
            else:
                print("Livro digital não encontrado.")
        else:
            print("Tipo de livro inválido.")

def emprestar_livro():
    id_livro = input("ID do Livro: ")
    tipo = input("Tipo de livro (1 para físico, 2 para digital): ")
    id_usuario = input("ID do Usuário: ")
    
    usuario = consultar_usuario_por_id(nome_banco, id_usuario)
    if not usuario:
        print("Usuário não encontrado.")
        return
    
    funcionario_responsavel = input("ID do Funcionário responsável: ")
    funcionario = consultar_funcionario_por_id(nome_banco, funcionario_responsavel)
    if not funcionario:
        print("Funcionário não encontrado.")
        return
    
    data_emprestimo = datetime.now().strftime("%Y-%m-%d")
    prazo = int(input("Prazo do empréstimo (dias): "))
    data_devolucao = (datetime.now() + timedelta(days=prazo)).strftime("%Y-%m-%d")

    if tipo == "1":
        alterar_status_livro(nome_banco, id_livro, False)
    elif tipo == "2":
        alterar_status_livro(nome_banco, id_livro, False)
    else:
        print("Tipo de livro inválido.")
        return
    
    registrar_emprestimo(nome_banco, id_usuario, id_livro, data_emprestimo, data_devolucao)

def devolver_livro():
    tipo = input("Tipo de livro (1 para físico, 2 para digital): ")
    id_livro = input("ID do Livro: ")

    if tipo == "1":
        devolver_livro_fisico(nome_banco, id_livro)
    elif tipo == "2":
        devolver_livro_digital(nome_banco, id_livro)
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
    escolha = input("Deseja listar todos os funcionários? (s/n): ")
    if escolha.lower() == 's':
        funcionarios = consultar_todos_funcionarios(nome_banco)
        if funcionarios:
            for funcionario in funcionarios:
                print(funcionario)
        else:
            print("Nenhum funcionário encontrado.")
    else:
        id_funcionario = input("ID do Funcionário: ")
        funcionario = consultar_funcionario_por_id(nome_banco, id_funcionario)
        if funcionario:
            print(funcionario)
        else:
            print("Funcionário não encontrado.")

def listar_todos_funcionarios():
    funcionarios = consultar_todos_funcionarios(nome_banco)
    if funcionarios:
        for funcionario in funcionarios:
            print(funcionario)
    else:
        print("Nenhum funcionário encontrado.")

def cadastrar_usuario():
    id_usuario = input("ID do Usuário: ")
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    cpf = input("CPF: ")
    data_nascimento = input("Data de Nascimento: ")
    genero = input("Gênero: ")
    telefone = input("Telefone: ")

    usuario = Usuario(id_usuario, nome, endereco, cpf, data_nascimento, genero, telefone)
    adicionar_usuario(nome_banco, usuario)

def excluir_usuario():
    id_usuario = input("ID do Usuário: ")
    deletar_usuario(nome_banco, id_usuario)

def listar_usuarios():
    escolha = input("Deseja listar todos os usuários? (s/n): ")
    if escolha.lower() == 's':
        usuarios = consultar_todos_usuarios(nome_banco)
        if usuarios:
            for usuario in usuarios:
                print(usuario)
        else:
            print("Nenhum usuário encontrado.")
    else:
        id_usuario = input("ID do Usuário: ")
        usuario = consultar_usuario_por_id(nome_banco, id_usuario)
        if usuario:
            print(usuario)
        else:
            print("Usuário não encontrado.")

def listar_todos_usuarios():
    usuarios = consultar_todos_usuarios(nome_banco)
    if usuarios:
        for usuario in usuarios:
            print(usuario)
    else:
        print("Nenhum usuário encontrado.")

def listar_emprestimos():
    id_emprestimo = input("Digite o ID do empréstimo que deseja consultar: ")
    emprestimo = consultar_emprestimo_por_id(nome_banco, id_emprestimo)
    if emprestimo:
        print(emprestimo)
    else:
        print("Empréstimo não encontrado.")

def listar_todos_emprestimos():
    emprestimos = consultar_todos_emprestimos(nome_banco)
    if emprestimos:
        for emprestimo in emprestimos:
            print(emprestimo)
    else:
        print("Nenhum empréstimo encontrado.")

if __name__ == "__main__":
    
    criar_tabela_livros_digitais()
    criar_tabela_livros_fisicos()
    criar_tabela_funcionarios()
    criar_tabela_usuarios()
    criar_tabela_emprestimos()
    menu()