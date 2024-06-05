from src.servicos import emprestimo

emprestimo.Emprestimo()

emprestimo = emprestimo.Emprestimo(1, 101, 201, "Livro Exemplo", "1ª Edição", "123456789", "2024-06-15", False)
print(emprestimo.get_nome())