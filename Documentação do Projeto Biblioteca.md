# Documentação do Projeto "Biblioteca"

## Visão Geral

O projeto "Biblioteca" é um sistema de gerenciamento de biblioteca desenvolvido em Python. Ele permite que os usuários cadastrem livros físicos e digitais, realizem empréstimos, cadastrem e gerenciem funcionários e usuários da biblioteca.

## Requisitos

O projeto requer Python 3.x e as seguintes bibliotecas:

- `datetime`
- `sqlite3`
- `sys`

## Estrutura do Projeto

O projeto está estruturado da seguinte forma:

- `main.py`: Arquivo principal contendo o código do sistema.
- `biblioteca.db`: Arquivo de banco de dados SQLite onde são armazenados os dados do sistema.
- `src/`: Diretório contendo os módulos do sistema organizados em subdiretórios:
  - `livros/`: Módulos relacionados a livros.
  - `pessoas/`: Módulos relacionados a funcionários e usuários.
  - `servicos/`: Módulos relacionados a empréstimos.

Cada subdiretório possui os seguintes arquivos:

- `<nome_modulo>.py`: Arquivo contendo a definição das classes e funções relacionadas ao módulo.
- `criar_tabela_<nome_modulo>.py`: Arquivo contendo a função para criar a tabela no banco de dados, se ainda não existir.

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

1. **Cadastro de Livros:**
   - Permite cadastrar livros físicos e digitais na biblioteca.
   - Os livros físicos podem incluir informações como título, autor, editora, número de páginas, tipo de capa, entre outros.
   - Os livros digitais podem incluir informações como título, autor, editora, número de páginas e tamanho em MB.

2. **Listagem de Livros:**
   - Permite listar todos os livros cadastrados na biblioteca, filtrando por tipo (físico ou digital) e/ou ID do livro.
   
3. **Empréstimos:**
   - Permite que os usuários realizem empréstimos de livros cadastrados na biblioteca.
   - Ao realizar um empréstimo, é necessário informar o ID do livro, o ID do usuário e o prazo de devolução.
   - Após o empréstimo, o sistema atualiza o status do livro para indisponível.

4. **Devolução de Livros:**
   - Permite que os usuários realizem a devolução de livros emprestados.
   - Ao realizar a devolução, o sistema atualiza o status do livro para disponível.

5. **Cadastro de Funcionários:**
   - Permite cadastrar novos funcionários da biblioteca.
   - Os funcionários podem ser cadastrados com informações como nome, endereço, CPF, data de nascimento, gênero e telefone.

6. **Exclusão de Funcionários:**
   - Permite excluir funcionários cadastrados na biblioteca.

7. **Listagem de Funcionários:**
   - Permite listar todos os funcionários cadastrados na biblioteca.

8. **Cadastro de Usuários:**
   - Permite cadastrar novos usuários da biblioteca.
   - Os usuários podem ser cadastrados com informações como nome, endereço, CPF, data de nascimento, gênero e telefone.

9. **Exclusão de Usuários:**
   - Permite excluir usuários cadastrados na biblioteca.

10. **Listagem de Usuários:**
    - Permite listar todos os usuários cadastrados na biblioteca.

11. **Consulta de Empréstimos:**
    - Permite consultar empréstimos específicos pelo ID do empréstimo.

12. **Listagem de Todos os Empréstimos:**
    - Permite listar todos os empréstimos realizados na biblioteca.

## Execução

Para executar o sistema, navegue até o diretório `AP2_Biblioteca` no terminal e execute o seguinte comando:

    - python main.py

Certifique-se de ter as dependências instaladas e que o arquivo `biblioteca.db` esteja presente no mesmo diretório do código.

## Contribuição

Este projeto é de código aberto e as contribuições são bem-vindas. Sinta-se à vontade para reportar problemas, enviar solicitações de recursos ou enviar pull requests para melhorias.

## Autores

Este projeto foi desenvolvido por [Yarlei Cruz, Jullyen Soares, Caio Haritov e Gabriel Sales].